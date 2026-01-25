# Sry Footprint

**Sry Footprint** is a modern, clean, and lightweight system utility application designed for Windows. It provides a unified interface for monitoring system performance, managing network configurations, and cleaning digital footprints to maintain privacy and disk space.

Built with Python and CustomTkinter, it features a dark, purple-themed aesthetic ("Sry Style") that is easy on the eyes and simple to navigate.

## 🚀 Features

### 1. Dashboard & Analytics
*   **Real-time Monitoring**: Visual progress bars for CPU and RAM usage.
*   **System Information**: Displays current OS version, Architecture, and GPU model.
*   **Aesthetic**: Includes a custom ASCII art logo and a clean layout.

### 2. Network Tools
Manage your network connection and DNS settings without opening the command prompt.
*   **List DNS Cache**: View the current contents of the Windows DNS resolver cache.
*   **Flush DNS**: Clear the DNS cache to resolve connection issues or update outdated records.
*   **Ping Test**: Quickly check internet connectivity by pinging Google servers.
*   **IP Configuration**: View detailed network adapter information (IP, MAC, DHCP).

### 3. Cleanup Tools (Digital Footprint)
Tools to remove temporary files and usage history.
*   **Clean Temp Files**: Deletes temporary files from the `%TEMP%` directory.
*   **Clean Recent Docs**: Clears the history of recently opened documents.
*   **Empty Recycle Bin**: Force-empties the recycle bin.
*   **Clear Event Logs**: Wipes Windows Event Logs (Requires Admin).
*   **Clear Prefetch**: Removes prefetch files to reset application launch history (Requires Admin).

## 🎯 Who is this for?
*   **Privacy-Conscious Users**: People who want to quickly wipe traces of their activity (recent docs, logs) with a single click.
*   **Gamers & Power Users**: Users who need to quickly flush DNS or check system stats without navigating through complex Windows settings.
*   **Minimalists**: Anyone who prefers a clean, dark-mode GUI over typing commands into a terminal.

## ⚡ How Effective Is It?
**Sry Footprint** is highly effective because it acts as a direct wrapper around native Windows system commands.
*   **Reliability**: It executes standard commands like `ipconfig`, `powershell`, and `del`, ensuring the same level of effectiveness as an IT professional working in the terminal.
*   **Speed**: Operations are performed instantly in background threads, keeping the interface responsive.
*   **Limitations**: Some cleanup functions (like clearing Event Logs or Prefetch) require the application to be run as **Administrator** to function due to Windows security permissions.

## 🛠️ Technical Details
*   **Language**: Python 3
*   **GUI Framework**: CustomTkinter (Modern wrapper for Tkinter)
*   **System Interaction**: Uses the `subprocess` module to execute shell commands and `psutil` for hardware monitoring.

## 📦 Installation & Usage

1.  **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    ```bash
    python sry_footprint.py
    ```

    *Note: For full cleanup functionality, right-click your terminal or the script and select "Run as Administrator".*