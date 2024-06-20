---
title: Конвертировать Excel в JSON
type: docs
weight: 300
url: /ru/python-java/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с помощью Aspose.Cells для Python via Java.
keywords: Экспорт рабочей книги в формат JSON без использования office 2013, office 2016, office 2019 и office 365
---

{{% alert color="primary" %}}

Aspose.Cells для Python via Java поддерживает преобразование Книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

Нет необходимости думать, как преобразовать книгу Excel в формат JSON, потому что библиотека Aspose.Cells для Python via Java предлагает лучшее решение. API Aspose.Cells для Python via Java поддерживает преобразование электронных таблиц в формат JSON. Чтобы экспортировать книгу в формат JSON, передайте [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) в качестве второго параметра метода [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). Вы также можете использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) для указания дополнительных настроек экспорта листа в формат JSON.

Приведенный ниже пример кода демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

Приведенный ниже пример кода, который использует класс JsonSaveOptions для указания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
