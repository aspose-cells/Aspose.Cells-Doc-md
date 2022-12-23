---
title: Подогнать все столбцы рабочего листа на одной странице PDF
type: docs
weight: 160
url: /ru/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

 Иногда вам нужно создать файл PDF, который умещает все столбцы рабочего листа на одной странице.[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) свойство предоставляет эту функцию очень простым в использовании способом. Сложные вычисления, такие как высота и ширина вывода PDF, обрабатываются внутри и основаны на данных на листе.

{{% /alert %}}

## **Подгонка столбцов рабочего листа на одной странице PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)гарантирует, что все столбцы на листе отображаются на одной странице PDF, хотя строки могут расширяться до нескольких страниц в зависимости от данных на листе.

Пример кода ниже показывает, как использовать[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)свойство для отображения большого рабочего листа из 100 столбцов.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Если на заданном листе много столбцов, отображаемый файл PDF может отображать содержимое очень маленького размера. Он по-прежнему читается при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваша электронная таблица содержит формулы, лучше всего вызвать[**Рабочая книга.ВычислитьФормулу()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)непосредственно перед рендерингом электронной таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
