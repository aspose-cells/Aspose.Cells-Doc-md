##Calculation of Excel 2016 MINIFS and MAXIFS functions with Python.NET
Learn how to calculate Excel 2016 MINIFS and MAXIFS functions using Aspose.Cells for Python via .NET API with code examples.
## **Possible Usage Scenarios**
Microsoft Excel 2016 supports MINIFS and MAXIFS functions. These functions are not supported in Excel 2013 or earlier versions. Aspose.Cells also supports the calculation of these functions. The following screenshot illustrates the usage of these functions. Please read the red comments inside the screenshot to understand how these functions work.
![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)
## **Calculation of Excel 2016 MINIFS and MAXIFS functions**
The following sample code loads the [sample excel file](5115149.xlsx) and calls the [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) method to perform the formula calculation via Aspose.Cells, then saves the results in the [output PDF](5115154.pdf).
```python
import os
from aspose.cells import Workbook, PdfSaveOptions
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")
# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))
# Perform Aspose.Cells formula calculation
workbook.calculate_formula()
# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True
if not os.path.exists(output_dir):
os.makedirs(output_dir)
workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
