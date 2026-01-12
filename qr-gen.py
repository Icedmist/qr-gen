import qrcode
import sys

def create_qr():
    print("---  Custom QR Code Generator ---")
    
    # 1. Ask for the content
    data = input("Enter the URL or text to encode: ").strip()
    
    # Simple validation: Stop if user typed nothing
    if not data:
        print(" Error: You didn't enter any text!")
        sys.exit()

    # 2. Ask for a filename
    filename = input("Name your file (e.g., 'portfolio'): ").strip()
    
    # Logic: Ensure it ends with .png
    if not filename.endswith(".png"):
        filename += ".png"

    # 3. Ask for color preference
    print("\nChoose a color:")
    print("1. Standard Black")
    print("2. Navy Blue")
    print("3. Deep Red")
    
    color_choice = input("Enter 1, 2, or 3: ").strip()
    
    # Logic: Map numbers to color names
    colors = {
        '1': 'black',
        '2': 'navy',
        '3': 'darkred'
    }
    # Default to black if you type something random
    chosen_color = colors.get(color_choice, 'black')

    print(f"\nGenerating {chosen_color} QR code...")

    # 4. Generate the QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # this creates the image with the chosen color
    img = qr.make_image(fill_color=chosen_color, back_color="white")
    
    # 5. Save and Finish
    img.save(filename)
    print(f" Done! Open '{filename}' in your file explorer to see it.")

if __name__ == "__main__":
    create_qr()