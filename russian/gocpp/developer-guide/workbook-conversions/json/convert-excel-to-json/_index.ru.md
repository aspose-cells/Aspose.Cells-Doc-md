---
title: Конвертация Excel в JSON с помощью Golang через C++
linktitle: Преобразование Excel в JSON
type: docs
weight: 300
url: /ru/go-cpp/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с помощью Aspose.Cells и C++.
keywords: Экспорт рабочей книги в формат JSON без использования office 2013, office 2016, office 2019 и office 365
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию рабочей книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

Не нужно гадать, как преобразовать рабочую книгу Excel в JSON, потому что библиотека Aspose.Cells for C++ предоставляет лучшее решение. API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Чтобы экспортировать рабочую книгу в JSON, передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) как второй параметр метода [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) для задания дополнительных настроек при экспорте листа в JSON.

Следующий пример показывает экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON, созданный этим кодом.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
Следующий пример, использующий класс JsonSaveOptions для задания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в JSON. Ознакомьтесь с кодом для преобразования [исходного файла](sample.xlsx) в JSON, созданный этим кодом.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
