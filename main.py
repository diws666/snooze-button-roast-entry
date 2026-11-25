import os

# Verified count: 139 characters, exactly 1 line, no trailing newline.
LINE = "I hit snooze at 6 a.m. on a Saturday. The alarm laughed, reset itself for 6:05, and whispered: you have nowhere to be, and yet here we are."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)

with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
