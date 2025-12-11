---
title: How to set AutoRecover property of Workbook with Golang via C++
linktitle: How to set AutoRecover property of Workbook
type: docs
weight: 220
url: /go-cpp/how-to-set-autorecover-property-of-workbook/
description: Learn how to enable or disable the AutoRecover property of a workbook using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

You can use Aspose.Cells to set the AutoRecover property of a workbook. The default value of this property is **true**. When you set it to **false** for a workbook, Microsoft Excel disables AutoRecover (Autosave) on that Excel file.

Aspose.Cells provides the [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) property to enable or disable this option.

{{% /alert %}}

The following code demonstrates how to use the [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) property of the workbook. The code first reads the default value of this property, which is **true**, then sets it to **false** and saves the workbook. It then reads the workbook again and obtains the value of this property, which is **false** at this time.

## C++ code to set the AutoRecover property of Workbook

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Output**

Here is the console output of the above sample code.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}