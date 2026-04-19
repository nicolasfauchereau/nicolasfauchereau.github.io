import sys
import datetime
from pathlib import Path
import re

def create_post(title):
    # 1. Prep the naming
    date_str = datetime.date.today().isoformat()
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    folder_name = f"{date_str}-{slug}"
    post_dir = Path("posts") / folder_name

    # 2. Build the directory
    post_dir.mkdir(parents=True, exist_ok=True)

    # 3. Create a template index.qmd (or .ipynb)
    template = f"""---
title: "{title}"
date: "{date_str}"
categories: []
image: ""
---

## Introduction
"""
    (post_dir / "index.qmd").write_text(template)
    print(f"Successfully created: {post_dir}/index.qmd")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_post(" ".join(sys.argv[1:]))
    else:
        print("Usage: python new_post.py 'My New S2S Research'")

