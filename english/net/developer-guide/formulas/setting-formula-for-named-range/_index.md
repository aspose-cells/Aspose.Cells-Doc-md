---
title: Setting Formula for Named Range
type: docs
weight: 20
url: /net/setting-formula-for-named-range/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Setting Formula for Named Range**
Like the Excel application, Aspose.Cells APIs provide the ability to specify a formula for a named range using its [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto) property. There could be numerous usability scenarios for this feature, a few of which are detailed as follows.

### **Setting a Simple Formula for Named Range**
A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}

### **Setting a Complex Formula for Named Range**
A complex formula could be anything such as a dynamic range or a formula that spans multiple cells across different worksheets. The following example creates a dynamic range using the INDEX function to get the value from a list based on its location.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}

Here is another example that uses a named range to sum values from two cells in different worksheets.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
