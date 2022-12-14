---
title: Преобразование Excel в JSON
type: docs
weight: 300
url: /ru/python-java/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с Aspose.Cells для Python через Java.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells для Python через Java поддерживает преобразование рабочей книги в файл Json (нотация объектов JavaScript).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

 Не нужно задаваться вопросом, как преобразовать книгу Excel в JSON, потому что Aspose.Cells для Python через библиотеку Java имеет лучшее решение. Aspose.Cells для Python через Java API обеспечивает поддержку преобразования электронных таблиц в формат JSON. Чтобы экспортировать книгу в JSON, передайте[**СохранитьФормат.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) в качестве второго параметра[**Книга.сохранить**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ) метод. Вы также можете использовать[**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) класс, чтобы указать дополнительные параметры для экспорта рабочего листа в JSON.

 В следующем примере кода демонстрируется экспорт книги Excel в формат Json. Пожалуйста, посмотрите код для преобразования[исходный файл](sample.xlsx) в файл Json, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

 В следующем примере кода, который использует класс JsonSaveOptions для указания дополнительных параметров, демонстрируется экспорт книги Excel в Json. Пожалуйста, посмотрите код для преобразования[исходный файл](sample.xlsx) в файл Json, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
