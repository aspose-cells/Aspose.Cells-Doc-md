---
title: Setting Formula for Named Range
type: docs
weight: 20
url: /python-net/setting-formula-for-named-range/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Setting Formula for Named Range**
Like the Excel application, Aspose.Cells for Python via .NET APIs provides the ability to specify a formula for a named range by using its [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to) property. There could be numerous use cases for this feature, a few of which are detailed as follows.

### **Setting a Simple Formula for Named Range**
A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}

### **Setting a Complex Formula for Named Range**
A complex formula could be anything, such as a dynamic range or a formula spanning over multiple cells in different worksheets. The following example creates a dynamic range using the INDEX function to get the value from a list based on its location.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}

Here is another example that uses a named range to sum values from two cells in different worksheets.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
