# QR Code Generator - Day 13 Project
# Learning: Image generation, qrcode module, GUI with tkinter

import qrcode
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self, root):
        """Initialize the QR Code Generator GUI"""
        self.root = root
        self.root.title("QR Code Generator - Day 13")
        self.root.geometry("600x700")
        self.root.configure(bg='#f0f0f0')
        
        # Store the generated QR code
        self.qr_image = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Set up the user interface"""
        # Main title
        title_label = tk.Label(
            self.root, 
            text="🔗 QR Code Generator", 
            font=("Arial", 20, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # QR Type selection
        tk.Label(input_frame, text="QR Code Type:", font=("Arial", 12), bg='#f0f0f0').pack(anchor='w')
        self.qr_type = tk.StringVar(value="text")
        type_frame = tk.Frame(input_frame, bg='#f0f0f0')
        type_frame.pack(fill='x', pady=5)
        
        # Radio buttons for QR type
        tk.Radiobutton(type_frame, text="Text", variable=self.qr_type, value="text", bg='#f0f0f0').pack(side='left', padx=10)
        tk.Radiobutton(type_frame, text="URL", variable=self.qr_type, value="url", bg='#f0f0f0').pack(side='left', padx=10)
        tk.Radiobutton(type_frame, text="WiFi", variable=self.qr_type, value="wifi", bg='#f0f0f0').pack(side='left', padx=10)
        tk.Radiobutton(type_frame, text="Email", variable=self.qr_type, value="email", bg='#f0f0f0').pack(side='left', padx=10)
        
        # Input text area
        tk.Label(input_frame, text="Content:", font=("Arial", 12), bg='#f0f0f0').pack(anchor='w', pady=(20, 5))
        self.text_area = tk.Text(input_frame, height=5, width=50, font=("Arial", 10))
        self.text_area.pack(fill='x', pady=5)
        
        # QR Code customization
        custom_frame = tk.Frame(self.root, bg='#f0f0f0')
        custom_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(custom_frame, text="Customization:", font=("Arial", 12, "bold"), bg='#f0f0f0').pack(anchor='w')
        
        # Size and colors
        size_frame = tk.Frame(custom_frame, bg='#f0f0f0')
        size_frame.pack(fill='x', pady=5)
        
        tk.Label(size_frame, text="Size:", bg='#f0f0f0').pack(side='left')
        self.size_var = tk.StringVar(value="10")
        size_spinbox = tk.Spinbox(size_frame, from_=1, to=20, textvariable=self.size_var, width=5)
        size_spinbox.pack(side='left', padx=5)
        
        tk.Label(size_frame, text="Border:", bg='#f0f0f0').pack(side='left', padx=(20, 5))
        self.border_var = tk.StringVar(value="4")
        border_spinbox = tk.Spinbox(size_frame, from_=1, to=10, textvariable=self.border_var, width=5)
        border_spinbox.pack(side='left', padx=5)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(
            button_frame,
            text="🎯 Generate QR Code",
            command=self.generate_qr,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        generate_btn.pack(side='left', padx=10)
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="💾 Save QR Code",
            command=self.save_qr,
            bg='#2196F3',
            fg='white',
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        save_btn.pack(side='left', padx=10)
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_all,
            bg='#f44336',
            fg='white',
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        )
        clear_btn.pack(side='left', padx=10)
        
        # QR Code display frame
        self.display_frame = tk.Frame(self.root, bg='white', relief='sunken', bd=2)
        self.display_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Label to show QR code
        self.qr_label = tk.Label(
            self.display_frame, 
            text="Generated QR Code will appear here",
            bg='white',
            fg='gray',
            font=("Arial", 12)
        )
        self.qr_label.pack(expand=True)
        
        # Status bar
        self.status_label = tk.Label(
            self.root,
            text="Ready to generate QR codes",
            bg='#e0e0e0',
            fg='#333333',
            font=("Arial", 10),
            anchor='w'
        )
        self.status_label.pack(fill='x', side='bottom')
    
    def format_content(self, content, qr_type):
        """Format content based on QR type"""
        if qr_type == "url":
            # Add http:// if not present
            if not content.startswith(('http://', 'https://')):
                content = 'https://' + content
        elif qr_type == "email":
            # Format as mailto link
            if not content.startswith('mailto:'):
                content = 'mailto:' + content
        elif qr_type == "wifi":
            # Format WiFi credentials (expecting format: SSID:PASSWORD:WPA)
            parts = content.split(':')
            if len(parts) >= 2:
                ssid = parts[0]
                password = parts[1]
                security = parts[2] if len(parts) > 2 else "WPA"
                content = f"WIFI:T:{security};S:{ssid};P:{password};;"
        
        return content
    
    def generate_qr(self):
        """Generate QR code from input text"""
        try:
            # Get input content
            content = self.text_area.get("1.0", tk.END).strip()
            
            if not content:
                messagebox.showwarning("Warning", "Please enter some content!")
                return
            
            # Format content based on type
            qr_type = self.qr_type.get()
            formatted_content = self.format_content(content, qr_type)
            
            # Create QR code instance with customization
            qr = qrcode.QRCode(
                version=1,  # Controls size (1-40)
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
                box_size=int(self.size_var.get()),  # Size of each box
                border=int(self.border_var.get()),  # Border size
            )
            
            # Add data to QR code
            qr.add_data(formatted_content)
            qr.make(fit=True)
            
            # Create image with colors
            self.qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Display QR code in GUI
            self.display_qr_code()
            
            # Update status
            self.status_label.config(text=f"QR Code generated for {qr_type}: {content[:50]}...")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")
            self.status_label.config(text="Error generating QR code")
    
    def display_qr_code(self):
        """Display the generated QR code in the GUI"""
        if self.qr_image:
            # Resize image for display (max 300x300)
            display_image = self.qr_image.copy()
            display_image.thumbnail((300, 300), Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage for tkinter
            photo = ImageTk.PhotoImage(display_image)
            
            # Update label with image
            self.qr_label.config(image=photo, text="")
            self.qr_label.image = photo  # Keep a reference
    
    def save_qr(self):
        """Save the generated QR code to file"""
        if not self.qr_image:
            messagebox.showwarning("Warning", "Please generate a QR code first!")
            return
        
        try:
            # Ask user for save location
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*")
                ],
                title="Save QR Code"
            )
            
            if file_path:
                # Save the QR code
                self.qr_image.save(file_path)
                messagebox.showinfo("Success", f"QR Code saved to:\n{file_path}")
                self.status_label.config(text=f"QR Code saved to {os.path.basename(file_path)}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save QR code: {str(e)}")
            self.status_label.config(text="Error saving QR code")
    
    def clear_all(self):
        """Clear all inputs and display"""
        self.text_area.delete("1.0", tk.END)
        self.qr_label.config(image="", text="Generated QR Code will appear here")
        self.qr_label.image = None
        self.qr_image = None
        self.status_label.config(text="Ready to generate QR codes")

def main():
    """Main function to run the QR Code Generator"""
    # Create the main window
    root = tk.Tk()
    
    # Create and run the application
    app = QRCodeGenerator(root)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    # First, let's create some example usage in terminal
    print("🔗 QR Code Generator - Day 13")
    print("=" * 40)
    
    # Example 1: Simple text QR code
    print("\n1. Creating a simple text QR code...")
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("Hello, World! This is my first QR code in Python!")
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("example_text_qr.png")
    print("✅ Text QR code saved as 'example_text_qr.png'")
    
    # Example 2: URL QR code
    print("\n2. Creating a URL QR code...")
    qr_url = qrcode.QRCode(version=1, box_size=10, border=4)
    qr_url.add_data("https://github.com")
    qr_url.make(fit=True)
    
    img_url = qr_url.make_image(fill_color="navy", back_color="white")
    img_url.save("example_url_qr.png")
    print("✅ URL QR code saved as 'example_url_qr.png'")
    
    # Example 3: WiFi QR code
    print("\n3. Creating a WiFi QR code...")
    wifi_data = "WIFI:T:WPA;S:MyWiFiNetwork;P:mypassword123;;"
    qr_wifi = qrcode.QRCode(version=1, box_size=8, border=4)
    qr_wifi.add_data(wifi_data)
    qr_wifi.make(fit=True)
    
    img_wifi = qr_wifi.make_image(fill_color="green", back_color="white")
    img_wifi.save("example_wifi_qr.png")
    print("✅ WiFi QR code saved as 'example_wifi_qr.png'")
    
    print("\n🎯 Examples created! Now launching GUI...")
    print("📱 Try different QR types: Text, URL, WiFi, Email")
    print("🎨 Customize size, border, and colors")
    print("💾 Save your QR codes as PNG or JPG files")
    
    # Launch the GUI
    main()