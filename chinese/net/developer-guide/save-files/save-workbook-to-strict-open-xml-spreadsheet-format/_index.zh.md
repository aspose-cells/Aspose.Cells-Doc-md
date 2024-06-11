---
title: 将工作簿保存为严格的 Open XML 电子表格格式
type: docs
weight: 150
url: /zh/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **可能的使用场景**

Aspose.Cells允许您将工作簿保存为*严格的Open XML电子表格*格式。为此，它提供了**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**属性。如果将其值设置为**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**，则输出的Excel文件将以严格的Open XML电子表格格式保存。

## **将工作簿保存为严格的 Open XML 电子表格格式**

以下示例代码创建一个工作簿，并将**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**属性的值设置为**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**，并将其保存为[输出的Excel文件](67338272.xlsx)。如果您在Microsoft Excel中打开输出的Excel文件并打开“另存为...”对话框，您将看到其格式为*严格的Open XML电子表格*，如此屏幕截图所示。

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
