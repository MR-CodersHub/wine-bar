import os
import re

root_dir = r"d:\MR CodersHub\Front-end Projects\May Day\wine-bar-main\wine-bar-main"

html_files = []
for dirpath, _, filenames in os.walk(root_dir):
    for f in filenames:
        if f.endswith(".html"):
            html_files.append(os.path.join(dirpath, f))

print(f"Found {len(html_files)} HTML files to scan.")

# Styles, regexes, and replacements
for file_path in html_files:
    rel_path = os.path.relpath(file_path, root_dir)
    filename = os.path.basename(file_path)
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    # 1. Update padding responsive classes from px-6 to px-4 sm:px-6
    new_content = new_content.replace("px-6 lg:px-10", "px-4 sm:px-6 lg:px-10")

    # 2. Make hero section heights and padding responsive
    new_content = new_content.replace("min-h-[85vh]", "min-h-[60vh] sm:min-h-[75vh] md:min-h-[85vh]")
    new_content = new_content.replace("min-h-screen", "min-h-[80vh] md:min-h-screen")
    new_content = new_content.replace("min-h-[75vh]", "min-h-[60vh] sm:min-h-[70vh] md:min-h-[75vh]")
    new_content = new_content.replace("min-h-[60vh]", "min-h-[50vh] sm:min-h-[55vh] md:min-h-[60vh]")

    # 3. Add responsive padding to the content container inside the hero
    new_content = re.sub(
        r'(class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-10 w-full[^"]*)(mt-10|mt-12|pt-20|pt-24)',
        r'\1pt-28 pb-12 sm:pt-32 sm:pb-20 md:py-32',
        new_content
    )

    # 4. Make hero headings responsive
    new_content = new_content.replace(
        "text-7xl md:text-8xl text-white leading-[0.9]",
        "text-4xl sm:text-6xl md:text-8xl text-white leading-[1.1] sm:leading-[0.95] md:leading-[0.9]"
    )
    new_content = new_content.replace(
        "text-6xl md:text-8xl leading-[0.95]",
        "text-4xl sm:text-6xl md:text-8xl leading-[1.1] sm:leading-[0.95] md:leading-[0.95]"
    )
    new_content = new_content.replace(
        "text-7xl md:text-8xl text-white leading-[0.9] mt-8",
        "text-4xl sm:text-6xl md:text-8xl text-white leading-[1.1] sm:leading-[0.95] md:leading-[0.9] mt-8"
    )

    # 5. Make absolute float cards responsive (hide on small screen to prevent horizontal scroll breaking)
    new_content = new_content.replace("absolute -bottom-10 -right-10", "hidden sm:block absolute -bottom-10 -right-10")

    # 6. Stats section grid cols responsiveness
    new_content = new_content.replace("grid-cols-2 lg:grid-cols-4 gap-8", "grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6")

    # 7. Check if file has changed and save
    if new_content != content:
        print(f"Fixed responsiveness in {rel_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"No changes for {rel_path}")
