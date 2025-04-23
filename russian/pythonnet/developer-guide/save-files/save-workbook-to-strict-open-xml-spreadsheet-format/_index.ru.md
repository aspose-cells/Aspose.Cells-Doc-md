---
title: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 150
url: /ru/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET позволяет сохранять рабочую книгу в формате *Strict Open XML Spreadsheet*. Для этого предназначено свойство [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Если установить его значение как [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance), то выходной файл Excel будет сохранен в формате Strict Open XML Spreadsheet.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

В следующем образце кода создается книга и устанавливается значение свойства [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) как [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) и сохраняется в [выходной Excel-файл](67338272.xlsx). Если вы откроете выходной Excel-файл в Microsoft Excel и откроете диалоговое окно Сохранить как..., то увидите его формат как *Strict Open XML Spreadsheet*, как показано на этом скриншоте.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

