import customtkinter as ctk
import subprocess
import threading
import os
import platform

try:
    import psutil
except ImportError:
    psutil = None

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue") 

class SryFootprintApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sry Footprint")
        self.geometry("1000x700")

        self.color_accent = "#8A2BE2"
        self.color_hover = "#7B68EE"
        self.color_sidebar = "#18181b"
        self.color_card = "#27272a"

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color=self.color_sidebar)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Sry Footprint", 
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color=self.color_accent
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 30))

        self.btn_dashboard = self.create_nav_button("Dashboard", self.show_dashboard, 1)
        self.btn_network = self.create_nav_button("Network Tools", self.show_network, 2)
        self.btn_cleanup = self.create_nav_button("Cleanup", self.show_cleanup, 3)

        self.dashboard_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.network_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.cleanup_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.init_dashboard()
        self.init_network_tools()
        self.init_cleanup_tools()

        self.show_dashboard()

        if psutil:
            self.update_analytics()

    def create_nav_button(self, text, command, row):
        btn = ctk.CTkButton(
            self.sidebar_frame,
            text=text,
            command=command,
            height=50,
            corner_radius=10,
            fg_color="transparent",
            hover_color=self.color_hover,
            font=ctk.CTkFont(size=15, weight="bold"),
            anchor="w"
        )
        btn.grid(row=row, column=0, padx=15, pady=5, sticky="ew")
        return btn

    def show_dashboard(self):
        self.network_frame.grid_forget()
        self.cleanup_frame.grid_forget()
        self.dashboard_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.btn_dashboard.configure(fg_color=self.color_accent)
        self.btn_network.configure(fg_color="transparent")
        self.btn_cleanup.configure(fg_color="transparent")

    def show_network(self):
        self.dashboard_frame.grid_forget()
        self.cleanup_frame.grid_forget()
        self.network_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.btn_network.configure(fg_color=self.color_accent)
        self.btn_dashboard.configure(fg_color="transparent")
        self.btn_cleanup.configure(fg_color="transparent")

    def show_cleanup(self):
        self.dashboard_frame.grid_forget()
        self.network_frame.grid_forget()
        self.cleanup_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.btn_cleanup.configure(fg_color=self.color_accent)
        self.btn_dashboard.configure(fg_color="transparent")
        self.btn_network.configure(fg_color="transparent")

    def init_dashboard(self):
        self.dashboard_frame.grid_columnconfigure((0, 1), weight=1)

        cat_art = "      /\\_/\\\n     ( o.o )\n      > ^ <"
        cat_label = ctk.CTkLabel(
            self.dashboard_frame,
            text=cat_art,
            font=ctk.CTkFont(family="Consolas", size=28, weight="bold"),
            text_color=self.color_accent
        )
        cat_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))

        sys_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
        try:
            gpu_info = subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode().split('\n')[1].strip()
        except:
            gpu_info = "Unknown GPU"

        info_label = ctk.CTkLabel(
            self.dashboard_frame, 
            text=f"System: {sys_info}\nGPU: {gpu_info}", 
            font=ctk.CTkFont(size=16),
            justify="left",
            anchor="w"
        )
        info_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 20))

        self.cpu_card = self.create_stat_card(self.dashboard_frame, "CPU Usage", 2, 0)
        self.ram_card = self.create_stat_card(self.dashboard_frame, "RAM Usage", 2, 1)
        
        if not psutil:
            err = ctk.CTkLabel(self.dashboard_frame, text="Install 'psutil' to see live analytics.", text_color="gray")
            err.grid(row=3, column=0, columnspan=2, pady=20)

    def create_stat_card(self, parent, title, row, col):
        card = ctk.CTkFrame(parent, fg_color=self.color_card, corner_radius=15)
        card.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)
        
        lbl = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=14, weight="bold"), text_color="gray")
        lbl.pack(pady=(15, 5), padx=20, anchor="w")
        
        progress = ctk.CTkProgressBar(card, orientation="horizontal", height=15, corner_radius=8)
        progress.pack(pady=(5, 10), padx=20, fill="x")
        progress.set(0)
        progress.configure(progress_color=self.color_accent)
        
        val_lbl = ctk.CTkLabel(card, text="0%", font=ctk.CTkFont(size=24, weight="bold"))
        val_lbl.pack(pady=(0, 15), padx=20, anchor="e")
        
        return {"progress": progress, "label": val_lbl}

    def update_analytics(self):
        if not psutil: return
        
        cpu = psutil.cpu_percent()
        self.cpu_card["progress"].set(cpu / 100)
        self.cpu_card["label"].configure(text=f"{cpu}%")
        
        ram = psutil.virtual_memory().percent
        self.ram_card["progress"].set(ram / 100)
        self.ram_card["label"].configure(text=f"{ram}%")
        
        self.after(1000, self.update_analytics)

    def init_network_tools(self):
        self.network_frame.grid_columnconfigure(0, weight=1)
        self.network_frame.grid_rowconfigure(1, weight=1)

        btn_frame = ctk.CTkFrame(self.network_frame, fg_color="transparent")
        btn_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        def create_net_btn(text, cmd, col):
            ctk.CTkButton(
                btn_frame, 
                text=text, 
                command=cmd,
                fg_color=self.color_card,
                hover_color=self.color_hover,
                height=40
            ).grid(row=0, column=col, padx=5, sticky="ew")

        create_net_btn("List DNS Cache", self.list_dns, 0)
        create_net_btn("Flush DNS", self.flush_dns, 1)
        create_net_btn("Ping Google", self.ping_google, 2)
        create_net_btn("IP Config (All)", self.ip_config_all, 3)

        self.output_textbox = ctk.CTkTextbox(
            self.network_frame, 
            font=ctk.CTkFont(family="Consolas", size=12),
            activate_scrollbars=True,
            fg_color="#1e1e1e"
        )
        self.output_textbox.grid(row=1, column=0, sticky="nsew")
        self.output_textbox.insert("0.0", "Network Tools Ready.\n")

    def init_cleanup_tools(self):
        self.cleanup_frame.grid_columnconfigure(0, weight=1)
        self.cleanup_frame.grid_rowconfigure(1, weight=1)

        btn_frame = ctk.CTkFrame(self.cleanup_frame, fg_color="transparent")
        btn_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

        btn_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        def create_clean_btn(text, cmd, col):
            ctk.CTkButton(
                btn_frame, 
                text=text, 
                command=cmd,
                fg_color=self.color_card,
                hover_color=self.color_hover,
                height=40
            ).grid(row=0, column=col, padx=5, sticky="ew")

        create_clean_btn("Clean Temp", self.clean_temp, 0)
        create_clean_btn("Clean Recent", self.clean_recent, 1)
        create_clean_btn("Empty Bin", self.empty_recycle_bin, 2)
        create_clean_btn("Clear Events", self.clear_event_logs, 3)
        create_clean_btn("Clear Prefetch", self.clear_prefetch, 4)

        self.cleanup_textbox = ctk.CTkTextbox(
            self.cleanup_frame, 
            font=ctk.CTkFont(family="Consolas", size=12),
            activate_scrollbars=True,
            fg_color="#1e1e1e"
        )
        self.cleanup_textbox.grid(row=1, column=0, sticky="nsew")
        self.cleanup_textbox.insert("0.0", "Cleanup Tools Ready.\n")

    def run_command(self, command, target_textbox=None):
        """Runs a system command in a background thread to keep UI responsive."""
        if target_textbox is None:
            target_textbox = self.output_textbox
            
        target_textbox.insert("end", f"\n> Executing: {command}...\n")
        target_textbox.see("end")
        
        def _thread_target():
            try:
                startupinfo = None
                if os.name == 'nt':
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, startupinfo=startupinfo)
                stdout, stderr = process.communicate()
                result = stdout + stderr
            except Exception as e:
                result = f"Error executing command: {e}"
            
            self.after(0, lambda: self.update_output(result, target_textbox))

        threading.Thread(target=_thread_target, daemon=True).start()

    def update_output(self, text, target_textbox):
        target_textbox.insert("end", text + "\n" + "-"*40 + "\n")
        target_textbox.see("end")

    def list_dns(self):
        self.run_command("ipconfig /displaydns")

    def flush_dns(self):
        self.run_command("ipconfig /flushdns")

    def ping_google(self):
        self.run_command("ping 8.8.8.8")

    def ip_config_all(self):
        self.run_command("ipconfig /all")

    def clean_temp(self):
        self.run_command('del /q /f /s "%TEMP%\\*"', self.cleanup_textbox)

    def clean_recent(self):
        self.run_command('del /q /f /s "%APPDATA%\\Microsoft\\Windows\\Recent\\*"', self.cleanup_textbox)

    def empty_recycle_bin(self):
        self.run_command('powershell.exe -NoProfile -Command "Clear-RecycleBin -Force"', self.cleanup_textbox)

    def clear_event_logs(self):
        self.run_command('powershell.exe -Command "Get-EventLog -LogName * | ForEach { Clear-EventLog $_.Log }"', self.cleanup_textbox)

    def clear_prefetch(self):
        self.run_command('del /q /f /s C:\\Windows\\Prefetch\\*', self.cleanup_textbox)

if __name__ == "__main__":
    app = SryFootprintApp()
    app.mainloop()