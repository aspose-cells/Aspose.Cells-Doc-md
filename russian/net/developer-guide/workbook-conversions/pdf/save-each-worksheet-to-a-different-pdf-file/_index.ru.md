---
title: Сохраните каждый рабочий лист в другой файл PDF
type: docs
weight: 130
url: /ru/net/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование файлов XLS (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for .NET может работать независимо, чтобы преобразовать электронную таблицу в PDF, и вам не нужно использовать Aspose.PDF for .NET для преобразования. Преобразование не требует, чтобы программное обеспечение создавало или использовало какие-либо временные файлы, поскольку весь процесс может выполняться в памяти.

{{% /alert %}} 
##  **Сохраните каждый рабочий лист в другой файл PDF**
 Если вам нужно сохранить каждый рабочий лист в файле Excel шаблона для создания разных файлов PDF, вы можете легко это сделать. Вы можете попробовать установить один индекс листа на**[`PdfSaveOptions.SheetSet`] (https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/)** вариант за раз для рендеринга на PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[Рабочая книга.ВычислитьФормулу()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) непосредственно перед рендерингом электронной таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
