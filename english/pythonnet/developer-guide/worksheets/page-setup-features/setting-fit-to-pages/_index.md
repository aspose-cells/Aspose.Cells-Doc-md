---
title: How to Print Excel as Fitted Pages Wide and Tall with Python.NET
linktitle: How to Print Excel as Fitted Pages Wide and Tall
type: docs
weight: 200
url: /python-net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Learn to set fit_to_pages_wide and fit_to_pages_tall properties for Excel printing using Aspose.Cells for Python via .NET API.
keywords: Python Excel Printing, Python Fit to Page Settings, Python FitToPagesWide, Python FitToPagesTall, Python Print Worksheet as One Page, Python Print All Columns in One Page
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

The fit_to_pages_wide and fit_to_pages_tall settings control spreadsheet scaling during printing. These settings ensure printed output fits within specified page dimensions:

1. **fit_to_pages_wide**: Specifies horizontal page count for printing
1. **fit_to_pages_tall**: Specifies vertical page count for printing

## **Why Use FitToPagesWide and FitToPagesTall**
Key benefits include:
1. Precise print layout control
1. Consistent multi-sheet formatting
1. Professional document presentation

## **How to Print File as Fitted Pages Wide and Tall in Excel**
To configure in Microsoft Excel:
1. Open workbook and select worksheet
1. Navigate to **Page Layout** → **Page Setup** dialog
1. In **Page** tab under **Scaling**:
   - Select "Fit to"
   - Specify pages wide (horizontal) and tall (vertical)

<br>
<img src="2.png" width=60% />

## **How to Print Excel as Fitted Pages Wide and Tall Using Aspose.Cells**
To configure programmatically:
1. Load [sample file](input.xlsx)
1. Access worksheet's [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) object
1. Set [**fit_to_pages_tall**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_tall/) and [**fit_to_pages_wide**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/fit_to_pages_wide/) properties

```python
from aspose.cells import Workbook

# Instantiating a Workbook object
workbook = Workbook("input.xlsx")

# Accessing the first worksheet in the Excel file
worksheet = workbook.worksheets[0]

# Setting the number of pages to which the length of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_tall = 1

# Setting the number of pages to which the width of the worksheet will be spanned
worksheet.page_setup.fit_to_pages_wide = 1

# Save the workbook
workbook.save("out_net.pdf")
```

Output result:
<br>
<img src="1.png" width=60% />

## **How to Print Worksheet as One Page**
To force single-page output:
1. Use [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Set [**one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/one_page_per_sheet/) property

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting OnePagePerSheet option
options.one_page_per_sheet = True

# Save the workbook with options
workbook.save("OnePagePerSheet.pdf", options)
```

Output result:
<br>
<img src="3.png" width=60% />

## **How to Print All Columns in One Page**
To consolidate columns horizontally:
1. Configure [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
1. Enable [**all_columns_in_one_page_per_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/all_columns_in_one_page_per_sheet/) property

```python
from aspose.cells import Workbook, PdfSaveOptions

# Instantiating a Workbook object
workbook = Workbook("sample.xlsx")

options = PdfSaveOptions()

# Setting all columns in one page per sheet
options.all_columns_in_one_page_per_sheet = True

# Save the workbook
workbook.save("AllColumnsInOnePagePerSheet.pdf", options)
```

Output result:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="python-net" >}}
