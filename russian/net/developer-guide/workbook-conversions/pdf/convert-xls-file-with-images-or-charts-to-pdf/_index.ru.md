---
title: Конвертировать файл XLS с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/net/convert-xls-file-with-images-or-charts-to-pdf/
---
{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование XLS файлов, содержащих изображения и диаграммы, в PDF документов. Aspose.Cells for .NET может работать самостоятельно, чтобы преобразовать электронную таблицу в PDF: Aspose.PDF for .NET не требуется для преобразования. Этот процесс может выполняться в памяти, поскольку он не зависит от временных или промежуточных XML-файлов. Это означает, что большие файлы Excel, например, содержащие изображения, диаграммы и другие объекты рисования, могут быть преобразованы быстро и эффективно.

{{% /alert %}} 
## **Образец кода**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

 Если электронная таблица содержит формулы, лучше вызвать[Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) непосредственно перед рендерингом в PDF. Это гарантирует, что значения, зависящие от формулы, пересчитываются, а правильные значения отображаются в PDF.

{{% /alert %}}
