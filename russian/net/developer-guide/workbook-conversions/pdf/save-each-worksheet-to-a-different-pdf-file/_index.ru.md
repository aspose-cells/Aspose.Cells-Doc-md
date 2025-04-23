---
title: Сохраните каждый рабочий лист в отдельный файл PDF
type: docs
weight: 130
url: /ru/net/save-each-worksheet-to-a-different-pdf-file/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование файлов XLS (с изображениями, диаграммами и т. д.) в документы PDF. Aspose.Cells for .NET может быть использован для независимого преобразования электронной таблицы в PDF, и для этого не требуется использовать Aspose.PDF для .NET для преобразования. Преобразование не требует создания или использования каких-либо временных файлов, так как весь процесс может быть выполнен в памяти.

{{% /alert %}} 
## **Сохранить каждый лист в отдельный файл PDF**
Если вам необходимо сохранить каждый лист в вашем исходном файле Excel в различные файлы PDF, вы можете легко это сделать. Вы можете попробовать установить один индекс листа на [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/sheetset/) опцию за раз для рендеринга в PDF.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SaveEachWorksheetToDifferentPDF-1.cs" >}}

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше всего вызвать [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед преобразованием таблицы в формат PDF. Таким образом будет гарантирован пересчет значений, зависящих от формул, и в PDF файл будут выведены правильные значения.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
