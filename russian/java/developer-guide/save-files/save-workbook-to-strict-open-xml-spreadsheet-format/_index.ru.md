---
title: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 100
url: /ru/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Возможные сценарии использования**

Aspose.Cells позволяет сохранять книгу в формате *Strict Open XML Spreadsheet*. Для этой цели предоставляется свойство [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance). Если установить его значение как [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT), то выходной файл Excel будет сохранен в формате *Strict Open XML Spreadsheet*.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

Следующий пример создает книгу и устанавливает значение свойства [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance) как [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO_29500_2008_STRICT), и сохраняет его как [выходной файл Excel](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Если открыть выходной файл Excel в Microsoft Excel и открыть диалоговое окно *Сохранить как...*, вы увидите его формат как *Strict Open XML Spreadsheet*, как показано на этом снимке экрана.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
