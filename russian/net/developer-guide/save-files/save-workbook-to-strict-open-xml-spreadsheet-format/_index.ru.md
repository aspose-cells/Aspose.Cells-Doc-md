---
title: Сохранить книгу в строгом формате электронной таблицы Open XML
type: docs
weight: 150
url: /ru/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---
## **Возможные сценарии использования**

Aspose.Cells позволяет сохранить книгу в*Строгая электронная таблица Open XML*формат. С этой целью он обеспечивает**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**имущество. Если вы установите его значение как**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**, то выходной файл Excel будет сохранен в формате электронной таблицы Strict Open XML.

## **Сохранить книгу в строгом формате электронной таблицы Open XML**

В следующем примере кода создается рабочая книга и задается значение**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)** собственность как**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)** и сохраняет его как[выходной файл Excel](67338272.xlsx) . Если вы откроете выходной файл Excel в Microsoft Excel и откроете диалоговое окно «Сохранить как...», вы увидите его формат как*Строгая электронная таблица Open XML*как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
