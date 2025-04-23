---
title: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 160
url: /ru/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Иногда требуется создать PDF-файл, в который поместятся все столбцы листа на одну страницу. Cвойство [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) предоставляет эту функцию в очень удобной форме использования. Сложные вычисления, такие как высота и ширина выходного PDF, обрабатываются внутри и основаны на данных в листе.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) обеспечивает отображение всех столбцов на одной странице PDF, хотя строки могут занимать несколько страниц в зависимости от данных в листе.

Приведенный ниже образец кода показывает, как использовать свойство [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) для отображения большого листа с 100 столбцами.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Когда у какого-либо листа много столбцов, сгенерированный PDF-файл может отображать содержимое очень маленького размера. Оно все еще читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}} {{% alert color="primary" %}}

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
