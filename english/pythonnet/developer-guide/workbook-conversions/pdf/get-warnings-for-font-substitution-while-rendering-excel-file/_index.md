---
title: Get Warnings for Font Substitution while Rendering Excel File with Python.NET
linktitle: Get Warnings for Font Substitution while Rendering Excel File
type: docs
weight: 230
url: /python-net/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Learn how to detect font substitutions during Excel to PDF conversion using Aspose.Cells for Python.NET with code examples and warnings handling.
---

{{% alert color="primary" %}} 

When rendering a Microsoft Excel file to PDF using Aspose.Cells for Python via .NET, font substitution warnings can help identify formatting discrepancies. This article shows how to implement font substitution warnings to understand differences between original and rendered documents.

{{% /alert %}} 

To receive font substitution warnings during Excel to PDF conversion in Python.NET:

1. Implement the `IWarningCallback` interface
2. Set the `warning_callback` property in `PdfSaveOptions`
3. Handle warnings in your callback implementation

The following images demonstrate font substitution in action:

|**Original document with missing fonts**|**Result after font substitution**|
| :- | :- |
|![Font substitution source](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|![Font substitution result](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Implementation Steps**
### **1. Required Imports**
```python
import aspose.cells as cells
from aspose.cells import IWarningCallback, WarningInfo, WarningType
```

### **2. Implement Warning Callback**
```python
class FontSubstitutionWarningCallback(IWarningCallback):
    def warning(self, warning_info):
        if warning_info.warning_type == WarningType.FONT_SUBSTITUTION:
            print(f"Font substitution: {warning_info.description}")
```

### **3. Configure Conversion Options**
```python
def convert_with_warnings():
    # Load source workbook
    workbook = cells.Workbook("source.xlsx")
    
    # Configure PDF save options
    options = cells.PdfSaveOptions()
    options.warning_callback = FontSubstitutionWarningCallback()
    
    # Save with warnings handling
    workbook.save("output.pdf", options)
```

## **Sample Output**
When running this code with missing fonts, you'll see console warnings like:
```python
Font substitution: Font [ Athene Logos; Regular ] substituted in Cell [ A6 ] in Sheet [ Sheet1 ]
Font substitution: Font [ B Traffic; Regular ] substituted in Cell [ A7 ] in Sheet [ Sheet1 ]
```

{{% alert color="primary" %}} 
Always call `workbook.calculate_formula()` before rendering if your spreadsheet contains formulas. This ensures correct calculation results in the output PDF.
{{% /alert %}}

## **Download Resources**
- [Source Excel File](5112611.xlsx)
- [Output PDF Example](5112616.pdf)

```python
import os
from aspose.cells import IWarningCallback, WarningType, Workbook, PdfSaveOptions

class GetWarningsForFontSubstitution(IWarningCallback):
    def warning(self, info):
        if info.warning_type == WarningType.FONT_SUBSTITUTION:
            print(f"WARNING INFO: {info.description}")

def run():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    
    workbook = Workbook(os.path.join(data_dir, "source.xlsx"))
    
    options = PdfSaveOptions()
    options.warning_callback = GetWarningsForFontSubstitution()
    
    output_path = os.path.join(data_dir, "output_out.pdf")
    workbook.save(output_path, options)
```

**Key API References:**
- [IWarningCallback](https://reference.aspose.com/cells/python-net/aspose.cells/iwarningcallback/)
- [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/)
- [WarningInfo](https://reference.aspose.com/cells/python-net/aspose.cells/warninginfo/)