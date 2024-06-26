import yaml
import os

def generate_redirect_html(url):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; URL={url}">
</head>
<body>
    <p>If you are not redirected automatically, follow this <a href="{url}">link</a>.</p>
</body>
</html>
    """.strip()

# Load the configuration
with open('redirects.yml', 'r') as file:
    config = yaml.safe_load(file)

# Create the public directory if it doesn't exist
os.makedirs('public', exist_ok=True)

# Generate redirect pages
for redirect in config['redirects']:
    from_path = redirect['from'].lstrip('/')
    to_url = redirect['to']
    
    # Create full path for the new file
    full_path = os.path.join('public', from_path)
    
    # Create all necessary directories
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Generate the HTML file
    with open(os.path.join(full_path, 'index.html'), 'w') as file:
        file.write(generate_redirect_html(to_url))

print("Redirect pages generated successfully!")