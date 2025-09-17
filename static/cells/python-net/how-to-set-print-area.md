##How to Set Print Area with Python.NET
Learn how to set and clear print areas in Excel files using Aspose.Cells for Python via .NET.
## **Possible Usage Scenarios**
Setting a print area in a document helps control printed content. Key reasons include:
1. Focus on Specific Data: Print only relevant sections
1. Improved Layout: Organize content neatly across pages
1. Save Resources: Reduce paper/ink consumption
1. Professional Presentation: Ensure polished output
1. Consistency: Maintain uniform print outputs
## **How to Set Print Area in Excel**
To set a print area programmatically:
1. Access worksheet's page setup properties
1. Define print area using cell range notation
1. Save modified workbook
```python
# Sample image reference remains unchanged
```
## **How to Clear Print Area in Excel**
To remove print area constraints:
1. Access page setup properties
1. Reset print area to empty string
1. Save changes
```python
# Sample image reference remains unchanged
```
## **What Happens After Clearing the Print Area**
Clearing the print area results in:
1. Default printing of entire worksheet
1. Removal of previous range constraints
1. Inclusion of all formatted cells
## **How to Set Print Area Using Aspose.Cells**
Set print area through worksheet's page setup:
```python
import aspose.cells as ac
# Load sample workbook
workbook = ac.Workbook("input.xlsx")
# Access first worksheet
worksheet = workbook.worksheets[0]
# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"
# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```
```python
# Output image reference
```
## **How to Clear Print Area Using Aspose.Cells**
Remove existing print area definition:
```python
import aspose.cells as ac
# Load sample workbook
workbook = ac.Workbook("input.xlsx")
# Access first worksheet
worksheet = workbook.worksheets[0]
# Clear print area
worksheet.page_setup.print_area = ""
# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```
```python
# Output image reference
```
```python
from aspose.cells import Workbook
# Load the workbook
workbook = Workbook("input.xlsx")
# Access the desired worksheet
worksheet = workbook.worksheets[0]
# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"
# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook
# Load the workbook
workbook = Workbook("input.xlsx")
# Access the desired worksheet
worksheet = workbook.worksheets[0]
# Clear the print area
worksheet.page_setup.print_area = ""
# Save the workbook
workbook.save("clear_print_area.pdf")
```
