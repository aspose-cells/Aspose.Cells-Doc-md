---
title: Disable Compatibility Checker in Excel
type: docs
weight: 270
url: /java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excel's Compatibility Checker flags when saving a file in an earlier file format that saving the file might cause functionality issues or loss of fidelity. The Compatibility Checker is a feature of Microsoft Office Excel 2007, 2010 & 2013.

When you save a workbook in a previous version, Excel 97 through Excel 2003, from Excel 2007 or Excel 2010, the Compatibility Checker scans the workbook to see if it contains features that are not supported by the earlier version. To help you make decisions about how to handle compatibility issues, the Compatibility Checker displays dialog boxes with options. It can also be used to create a report on any issues in the workbook, or disable the feature.

Sometimes, you need to disable the Compatibility Checker for a particular spreadsheet. With Aspose.Cells' APIs you can do this dynamically so that the users don't get frustrated or confused by the Compatibility Checker dialog box popping up when they re-save the file in Microsoft Excel manually.

{{% /alert %}}

## **Using Microsoft Excel**

To disable the Compatibility Checker in Microsoft Excel (for example Microsoft Excel 2007/2010):

- (Excel 2007) On the Office button, click **Prepare**, then **Run Compatibility Checker**, and then clear the **Check compatibility when you save this workbook** option.
- (Excel 2010 & 2013) On the File tab, click **Info**, then **Check for issues**, click **Check Compatibility**, and, finally, clear the **Check compatibility when you save this workbook** option.

## **Using Aspose.Cells APIs**

Set the [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) property to **False** to disable Microsoft Excel's Compatibility Checker.

Suppose we have a template XLS file. When a user saves or re-saves it in MS Excel 2007/2010/2013, the Compatibility Checker dialog box is displayed, as shown in the screenshot below.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

The following code shows how to disable the Compatibility Checker with Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
{{< app/cells/assistant language="java" >}}