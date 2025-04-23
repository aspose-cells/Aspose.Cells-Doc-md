---
title: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 150
url: /ru/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет сохранить книгу в формате *Strict Open XML Spreadsheet*. Для этого предоставляется свойство [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance). Если установить его значение как [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance), то выходной файл Excel будет сохранен в формате Strict Open XML Spreadsheet.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

В следующем образце кода создается книга и устанавливается значение свойства [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) как [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance) и сохраняется в [выходной Excel-файл](67338272.xlsx). Если вы откроете выходной Excel-файл в Microsoft Excel и откроете диалоговое окно Сохранить как..., то увидите его формат как *Strict Open XML Spreadsheet*, как показано на этом скриншоте.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
{{< app/cells/assistant language="csharp" >}}
