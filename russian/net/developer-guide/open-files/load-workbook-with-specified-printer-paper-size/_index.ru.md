---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 430
url: /ru/net/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Вы можете указать размер бумаги принтера по вашему выбору при загрузке вашей книги с помощью метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize). Пожалуйста, обратите внимание, что если создать новый файл в MS Excel, вы обнаружите, что размер бумаги такой же, как установка выбранного принтера по умолчанию на вашем компьютере.

{{% /alert %}}

В следующем примере кода показано использование метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize). Сначала он создает рабочую книгу, затем сохраняет ее в памяти в формате XLSX. Затем он загружает ее с размером бумаги A5 и снова сохраняет ее в формате PDF. Затем он снова загружает его с размером бумаги A3 и снова сохраняет его в формате PDF. Если вы откроете выходные PDF-файлы и проверите их размер бумаги, вы увидите, что они отличаются. Один A5, а другой A3. Пожалуйста, загрузите [A5 выходной PDF](5115234.pdf) и [A3 выходной PDF](5115233.pdf), сгенерированный кодом для вашего ориентира.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
