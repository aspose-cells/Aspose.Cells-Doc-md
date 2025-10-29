---
title: Сохранение рабочей книги в формат строго открытого XML таблицы с помощью Golang через C++
linktitle: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 150
url: /ru/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Узнайте, как сохранить рабочую книгу в формате Strict Open XML Spreadsheet с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет сохранять рабочую книгу в формате *Strict Open XML Spreadsheet*. Для этого предоставляется свойство [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/). Если установить его значение в [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), то выходной файл Excel сохранится в формате Strict Open XML Spreadsheet.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

Следующий пример кода создает рабочую книгу и устанавливает значение свойства [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) как [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), затем сохраняет ее как [выходной файл Excel](67338272.xlsx). Если открыть выходной файл Excel в Microsoft Excel и выбрать «Сохранить как…», вы увидите его формат как *Strict Open XML Spreadsheet*, что показано на этом скриншоте.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
