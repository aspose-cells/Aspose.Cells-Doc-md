---
title: Setting Formula for Named Range
type: docs
weight: 20
url: /python-net/setting-formula-for-named-range/
---

## **Setting Formula for Named Range**
Like Excel application, Aspose.Cells for Python via .NET APIs provide the ability to specify a formula for a named range while using its [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to) property. There could be numerous usability scenarios for this feature, a few of which are detailed as follow.
### **Setting a Simple Formula for Named Range**
A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Setting a Complex Formula for Named Range**
A complex formula could be anything such as a dynamic range or a formula spanning over multiple cells in different worksheets. The following example creates a dynamic range using the INDEX function to get the value from a list based on its location.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Here is another example that uses a named range to sum values from 2 cells in different worksheets.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
