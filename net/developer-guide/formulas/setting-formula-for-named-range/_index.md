---
title: Setting Formula for Named Range
type: docs
weight: 220
url: /net/setting-formula-for-named-range/
---

## **Setting Formula for Named Range**
Like Excel application, Aspose.Cells APIs provide the ability to specify a formula for a named range while using its [RefersTo](https://apireference.aspose.com/cells/net/aspose.cells/range/properties/refersto) property. There could be numerous usability scenarios for this feature, a few of which are detailed as follow.
### **Setting a Simple Formula for Named Range**
A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Setting a Complex Formula for Named Range**
A complex formula could be anything such as a dynamic range or a formula spanning over multiple cells in different worksheets. The following example creates a dynamic range using the INDEX function to get the value from a list based on its location.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Here is another example that uses a named range to sum values from 2 cells in different worksheets.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
