---
title: Конвертировать Excel в JSON
type: docs
weight: 300
url: /ru/python-net/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с помощью Aspose.Cells for Python via .NET API.
keywords: Python Преобразование Excel в json, Преобразование Excel в json Pyton via NET, Экспорт рабочей книги в json, Преобразование файла Excel в json
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает преобразование рабочей книги в файл Json (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

Не нужно задумываться, как преобразовать рабочую книгу Excel в JSON, потому что у библиотеки Aspose.Cells для Python via .NET есть лучшее решение. API Aspose.Cells предоставляет поддержку преобразования электронных таблиц в формат JSON. Для экспорта рабочей книги в JSON передайте [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) вторым параметром метода [**Workbook.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions). Также можно использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions), чтобы указать дополнительные настройки для экспорта листа в JSON.

Приведенный ниже код демонстрирует экспорт книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в файл Json, сгенерированный кодом, для ознакомления.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

Приведенный ниже пример кода, который использует класс JsonSaveOptions для указания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}

{{< app/cells/assistant language="python-net" >}}
