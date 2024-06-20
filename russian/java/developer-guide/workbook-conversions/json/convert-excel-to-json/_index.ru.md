---
title: Конвертировать Excel в JSON
type: docs
weight: 20
url: /ru/java/convert-excel-to-json/
description: Узнайте, как конвертировать файл Excel в JSON с помощью Aspose.Cells for Java API.
keywords: Экспорт рабочей книги в формате JSON с помощью Java, конвертирование Excel в JSON с использованием Java, сохранение Excel в JSON в Java, конвертирование рабочей книги в JSON с использованием Java, сохранение рабочей книги в JSON в Java, экспорт Excel в JSON via Java.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает конвертацию рабочей книги в файл JSON (JavaScript Object Notation).

{{% /alert %}}

## **Как конвертировать рабочую книгу Excel в JSON**

Нет необходимости задаваться вопросом, как преобразовать книгу Excel в формат JSON, потому что у библиотеки Aspose.Cells Java есть лучшее решение. API Aspose.Cells Java поддерживает преобразование электронных таблиц в формат JSON. Чтобы экспортировать книгу в формат JSON, передайте [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) вторым параметром метода [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). Вы также можете использовать класс [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) для указания дополнительных параметров экспорта листа в JSON.

Приведенный ниже пример кода демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

Приведенный ниже пример кода, который использует класс JsonSaveOptions для указания дополнительных настроек, демонстрирует экспорт рабочей книги Excel в Json. Пожалуйста, ознакомьтесь с кодом для конвертации [исходного файла](sample.xlsx) в Json-файл, сгенерированный кодом, для справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
