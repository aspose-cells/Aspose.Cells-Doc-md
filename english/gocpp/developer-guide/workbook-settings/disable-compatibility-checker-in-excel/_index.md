---
title: Disable Compatibility Checker in Excel with Golang via C++
linktitle: Disable Compatibility Checker
type: docs
weight: 170
url: /go-cpp/disable-compatibility-checker-in-excel/
description: This article shows how to disable compatibility checker through the Aspose.Cells for C++ API.
keywords: C++ Disable Compatibility Checker, Excel Disable Compatibility Checker in C++, Disable Compatibility Checker in Workbook. 
---

## Disable Compatibility Checker in Excel Worksheets in C++

{{% alert color="primary" %}}

Microsoft Excel's Compatibility Checker flags that saving a file in an earlier file format might cause functionality issues or loss of fidelity. The Compatibility Checker is a feature of Microsoft Office Excel 2007 and Microsoft Excel 2010.

When you save a workbook in a previous version, Excel 97 through Excel 2003, from Excel 2007 or Excel 2010, the Compatibility Checker scans the workbook to see if it contains features that are not supported by the earlier version. To help you make decisions about how to handle compatibility issues, the Compatibility Checker displays dialog boxes with options. It can also be used to create a report on any issues in the workbook, or disable the feature.

Sometimes, you need to disable the Compatibility Checker for a particular spreadsheet. With Aspose.Cells APIs you can do this programmatically so that users don't get frustrated or confused by the Compatibility Checker dialog box popping up when they re‑save the file in Microsoft Excel manually.

{{% /alert %}}

## **How to Disable Compatibility Checker using Microsoft Excel**

To disable the Compatibility Checker in Microsoft Excel (for example Microsoft Excel 2007/2010):

- (Excel 2007) On the Office button, click **Prepare**, then **Run Compatibility Checker**, and then clear the **Check compatibility when you save this workbook** option.
- (Excel 2010) On the File tab, click **Info**, then **Check for issues**, click **Check Compatibility**, and, finally, clear the **Check compatibility when you save this workbook** option.

## **How to Disable Compatibility Checker using Aspose.Cells APIs**

Set the [**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcheckcompatibility/) property to **False** to disable Microsoft Excel's Compatibility Checker.

### **Code Examples**

The code examples that follow show how to disable the Compatibility Checker with Aspose.Cells for C++.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCompatibilityCheckerInExcel.go" >}}