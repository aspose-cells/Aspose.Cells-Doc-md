---
title: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal with Python.NET
linktitle: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal
description: Learn how to handle localized Excel formulas using Aspose.Cells for Python via .NET API.
type: docs
weight: 30
url: /python-net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
---

## **Possible Usage Scenarios**

Microsoft Excel Formulas may have different names in different locales or regions or languages. For example, **SUM** function is called **SUMME** in German. Aspose.Cells for Python via .NET requires specific implementation to work with localized function names. Similar to Excel VBA's **Range.FormulaLocal**, Aspose.Cells provides [**Cell.formula_local**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula_local/) property which requires implementing [**GlobalizationSettings.get_local_function_name(str)**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/get_local_function_name/) method.

## **Implement Cell.FormulaLocal using Python.NET**

This implementation demonstrates how to override [**get_local_function_name**](https://reference.aspose.com/cells/python-net/aspose.cells/globalizationsettings/get_local_function_name/) to return localized function names. The example appends "UserFormulaLocal_" prefix to standard names. Adapt this logic to return locale-specific names like German "SUMME" for "SUM".

```python
import aspose.cells as ac

class UserDefinedGlobalizationSettings(ac.GlobalizationSettings):
    def get_local_function_name(self, standard_name):
        return f"UserFormulaLocal_{standard_name}"

# Initialize workbook with custom globalization settings
workbook = ac.Workbook()
gs = UserDefinedGlobalizationSettings()
workbook.settings.globalization_settings = gs

# Set formulas and display localized versions
worksheet = workbook.worksheets[0]
cell = worksheet.cells.get("A3")
cell.formula = "=SUM(A1:A2)"
print(f"Formula Local: {cell.formula_local}")

cell = worksheet.cells.get("A4")
cell.formula = "=AVERAGE(B1:B2,B5)"
print(f"Formula Local: {cell.formula_local}")
```

## **Console Output**

{{< highlight python >}}
Formula Local: =UserFormulaLocal_SUM(A1:A2)
Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)
{{< /highlight >}}

```python
from aspose.cells import Workbook, GlobalizationSettings

class GS(GlobalizationSettings):
    def get_local_function_name(self, standard_name):
        if standard_name == "SUM":
            return "UserFormulaLocal_SUM"
        if standard_name == "AVERAGE":
            return "UserFormulaLocal_AVERAGE"
        return ""

def run():
    # Create workbook
    wb = Workbook()
    
    # Assign GlobalizationSettings implementation
    wb.settings.globalization_settings = GS()
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Access cell C4
    cell = ws.cells.get("C4")
    
    # Assign SUM formula and print FormulaLocal
    cell.formula = "SUM(A1:A2)"
    print("Formula Local:", cell.formula_local)
    
    # Assign AVERAGE formula and print FormulaLocal
    cell.formula = "=AVERAGE(B1:B2, B5)"
    print("Formula Local:", cell.formula_local)
```