---
title: Конвертировать Excel в JSON
type: docs
weight: 300
url: /ru/net/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в формат JSON с помощью Aspose.Cells.
keywords: Экспорт рабочей книги в формат JSON без использования office 2013, office 2016, office 2019 и office 365
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию рабочей книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

Не нужно задумываться, как конвертировать книгу Excel в JSON, потому что библиотека Apose.Cells для .NET имеет лучшее решение. API Aspose.Cells поддерживает конвертацию электронных таблиц в формат JSON. Для экспорта книги в JSON передайте [**SaveFormat.Json**](https://reference.aspose.com/cells/net/aspose.cells/saveformat) как второй параметр метода [**Workbook.Save**](https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/3). Отправьте класс [**JsonSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/JsonSaveoptions), чтобы задать дополнительные настройки для экспорта листа в JSON.

Приведенный ниже код демонстрирует экспорт книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в файл Json, сгенерированный кодом, для ознакомления.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New.cs" >}}

Приведенный ниже пример кода, который использует класс JsonSaveOptions для указания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Excel-to-JSON-New2.cs" >}}

