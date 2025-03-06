import os

# Get the current working directory
current_directory = os.getcwd()

# Create HTML content
html_content = f"""
<!doctype html>

<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1.0">
        <link rel="stylesheet" href="https://pyscript.net/releases/2023.05.1/pyscript.css">
        <script type="module" src="https://pyscript.net/releases/2023.05.1/pyscript.js"></script>

        <py-config>
            packages=["matplotlib"]
        </py-config>

    </head>

    <body>
        <py-repl>   
            import matplotlib.pyplot as plt
            
            x = [87,91,97,95]
            
            plt.hist(x)
            
            plt.show() 
        </py-repl>
    </body>

</html>

"""

# Write the HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
