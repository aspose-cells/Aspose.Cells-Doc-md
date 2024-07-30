---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 430
url: /ru/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Вы можете указать размер бумаги принтера по вашему выбору при загрузке вашей книги с помощью метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Пожалуйста, обратите внимание, что если создать новый файл в MS Excel, вы обнаружите, что размер бумаги такой же, как установка выбранного принтера по умолчанию на вашем компьютере.

{{% /alert %}}

Следующий пример кода иллюстрирует использование метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Сначала он создает рабочую книгу, затем сохраняет ее в потоке памяти в формате XLSX. Затем он загружает его с размером бумаги A5 и сохраняет в формате PDF. Затем снова загружает с размером бумаги A3 и снова сохраняет в формате PDF. Если вы откроете выходные файлы PDF и проверите их размер бумаги, вы увидите, что они разные. Один - A5, а другой - A3. Пожалуйста, скачайте [выходной PDF с размером A5](PrinterSize-a5_out.pdf) и [выходной PDF с размером A3](PrinterSize-a3_out.pdf), сгенерированные кодом, для вашего ознакомления.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
