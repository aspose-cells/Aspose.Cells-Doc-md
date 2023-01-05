---
title: 将工作簿保存为严格的 Open XML 电子表格格式
type: docs
weight: 150
url: /zh/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---
## **可能的使用场景**

Aspose.Cells 允许您将工作簿保存在*严格的 Open XML 电子表格*格式。为此，它提供了**[工作簿.设置.合规性](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**财产。如果将其值设置为**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**, 然后输出的 Excel 文件将以 Strict Open XML Spreadsheet 格式保存。

## **将工作簿保存为严格的 Open XML 电子表格格式**

下面的示例代码创建一个工作簿并设置**[工作簿.设置.合规性](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**财产作为**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**并将其另存为[输出Excel文件](67338272.xlsx) .如果您在 Microsoft Excel 中打开输出 Excel 文件并打开“另存为...”对话框，您将看到其格式为*严格的 Open XML 电子表格*如这个屏幕截图所示。

![待办事项：图片_替代_文本](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
