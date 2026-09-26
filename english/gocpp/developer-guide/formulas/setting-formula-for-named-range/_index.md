---
title: Setting Formula for Named Range with Golang via C++
linktitle: Setting Formula for Named Range
type: docs
weight: 20
url: /go-cpp/setting-formula-for-named-range/
description: Learn how to set formulas for named ranges in Excel files using Aspose.Cells with Golang via C++.
---

## **Setting Formula for Named Range**
Like the Excel application, Aspose.Cells APIs provide the ability to specify a formula for a named range using its [GetRefersTo()](https://reference.aspose.com/cells/go-cpp/range/getrefersto/) property. There could be numerous usability scenarios for this feature, a few of which are detailed as follows.

### **Setting a Simple Formula for Named Range**
A simple formula could be a reference to another cell in the same (or different) worksheet. The following example creates a named range in a new spreadsheet and sets its reference to another cell.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaForNamedRange.go" >}}

### **Setting a Complex Formula for Named Range**
A complex formula could be a dynamic range or a formula spanning multiple cells in different worksheets. The following example creates a dynamic range using the `INDEX` function to get a value from a list based on its location.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaForNamedRange-1.go" >}}

Here is another example that uses a named range to sum values from two cells in different worksheets.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingFormulaForNamedRange-2.go" >}}
{{< app/cells/assistant language="go" >}}
