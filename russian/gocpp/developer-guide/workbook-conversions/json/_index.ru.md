---
title: Преобразуйте рабочую книгу в JSON с помощью Golang через C++
linktitle: Преобразовать рабочую книгу в JSON
type: docs
weight: 300
url: /ru/go-cpp/convert-workbook-to-json/
description: Узнайте, как преобразовать рабочие книги Excel в формат JSON с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование рабочей книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

API Aspose.Cells поддерживает преобразование таблиц в формат JSON. Чтобы экспортировать рабочую книгу в JSON, передайте [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) в качестве второго параметра метода [**Workbook::Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/), чтобы задать дополнительные настройки для экспорта листа в JSON.

Следующий пример демонстрирует экспорт активного листа в JSON, используя член перечисления [**SaveFormat::Json**](https://reference.aspose.com/cells/go-cpp/saveformat/). Ознакомьтесь с примером кода для преобразования [исходного файла](book1.xlsx) в [выходной JSON файл](book1.json), созданный этим кодом.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Json.go" >}}
## **Расширенные темы**
- [Преобразовать CSV в JSON](/cells/ru/cpp/convert-csv-to-json/)
- [Преобразование Excel в JSON](/cells/ru/cpp/convert-excel-to-json/)
- [Преобразовать JSON в CSV](/cells/ru/cpp/convert-json-to-csv/)
- [Преобразовать JSON в Excel](/cells/ru/cpp/convert-json-to-excel/)
