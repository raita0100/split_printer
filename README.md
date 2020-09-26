# split_printer
helper tool to print on both sides for single side printer.

## How to use
1. Install python (This is a python program).
2. install pip.
3. install dependencies from [requirements.txt]() file.
   ```cmd
   pip install -r requirements.txt
   ```
4. ### Run program
   ```cmd
   python pdf_process_v0.py -f Assignment.pdf -m 1
   ```
  now we get three files 
  * odd_pages.pdf (odd pages from original document)
  * even_pages.pdf (Even pages from original document)
  * reverse.pdf (revered pages of even_pages.pdf)
  
### How to print on single side printing printer
1. First print __*odd_pages.pdf*__. (Do not take away the pages leve there in the pile only).
2. After completion, put the pile in reverse as obtained from printer with head as inwards.
3. Then print __*reverse.pdf*__.
  
