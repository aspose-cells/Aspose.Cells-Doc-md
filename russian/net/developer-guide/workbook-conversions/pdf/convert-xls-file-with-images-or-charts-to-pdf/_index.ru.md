---
title: Преобразование XLS файла с изображениями или диаграммами в PDF
type: docs
weight: 50
url: /ru/net/convert-xls-file-with-images-or-charts-to-pdf/
---

{{% alert color="primary" %}} 

Aspose.Cells поддерживает преобразование файлов XLS, содержащих изображения и диаграммы, в документы PDF. Aspose.Cells for .NET может работать независимо для преобразования электронной таблицы в PDF: для этого не требуется Aspose.PDF for .NET. Процесс может быть выполнен в памяти, так как он не зависит от временных или промежуточных XML-файлов. Это означает, что большие файлы Excel, например, содержащие изображения, диаграммы и другие объекты рисования, могут быть быстро и эффективно преобразованы.

{{% /alert %}} 
## **Образец кода**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertXLSFileToPDF-1.cs" >}}

{{% alert color="primary" %}} 

Если электронная таблица содержит формулы, лучше вызвать метод [Workbook.CalculateFormula](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) прямо перед рендерингом в PDF. Это гарантирует, что зависимые от формулы значения будут пересчитаны, и правильные значения будут отображены в PDF.

{{% /alert %}}
