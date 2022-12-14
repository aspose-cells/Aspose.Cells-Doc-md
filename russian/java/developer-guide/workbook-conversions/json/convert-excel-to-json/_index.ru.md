---
title: Преобразование Excel в JSON
type: docs
weight: 20
url: /ru/java/convert-excel-to-json/
description: Узнайте, как преобразовать файл Excel в JSON с помощью Aspose.Cells.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование рабочей книги в файл Json (нотация объекта JavaScript).

{{% /alert %}}

## **Конвертировать книгу Excel в JSON**

 Не нужно задаваться вопросом, как преобразовать книгу Excel в JSON, потому что библиотека Aspose.Cells Java имеет лучшее решение. Aspose.Cells Java API обеспечивает поддержку преобразования электронных таблиц в формат JSON. Чтобы экспортировать книгу в JSON, передайте[**СохранитьФормат.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) в качестве второго параметра[**Книга.сохранить**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) метод. Вы также можете использовать[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) класс, чтобы указать дополнительные параметры для экспорта рабочего листа в JSON.

 В следующем примере кода демонстрируется экспорт книги Excel в формат Json. Пожалуйста, посмотрите код для преобразования[исходный файл](sample.xlsx) в файл Json, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 В следующем примере кода, который использует класс JsonSaveOptions для указания дополнительных параметров, демонстрируется экспорт книги Excel в Json. Пожалуйста, посмотрите код для преобразования[исходный файл](sample.xlsx) в файл Json, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
