---
title: Подогнать все столбцы рабочего листа на одной странице PDF
type: docs
weight: 70
url: /ru/java/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Иногда вам нужно создать файл PDF, который умещает все столбцы рабочего листа на одной странице.[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)свойство предоставляет эту функцию очень простым в использовании способом. Сложные вычисления, такие как высота и ширина выходной страницы PDF, обрабатываются внутри и основаны на данных на листе.

{{% /alert %}}

## **Подгонка столбцов рабочего листа на одной странице PDF**

[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)гарантирует, что все столбцы рабочего листа отображаются на одной странице PDF, хотя строки могут расширяться до нескольких страниц в зависимости от данных в рабочем листе.

{{% alert color="primary" %}}

Если на заданном листе много столбцов, отображаемый файл PDF может отображать содержимое очень маленького размера. Он по-прежнему читается при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}}

 Пример кода ниже показывает, как использовать[**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet)свойство для отображения большого рабочего листа из 100 столбцов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) непосредственно перед преобразованием электронной таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
