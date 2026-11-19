# news-image-20261118: the entry image is the entry.png beside this file,
# and the program copies it to /output/entry.png. The image sums up the
# world news of Wednesday 18 November 2026: the date is named at the top,
# then the day's seven biggest stories across regions and fields. Standard
# library only; no network; deterministic: the same bytes are written on
# every run. The image is a whole 1024 by 1024 PNG of under 1 MiB.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
dst = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copyfile(src, dst)
