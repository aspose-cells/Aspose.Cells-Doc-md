---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 430
url: /ru/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Вы можете указать размер бумаги принтера по вашему выбору при загрузке вашей книги с помощью метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Пожалуйста, обратите внимание, что если создать новый файл в MS Excel, вы обнаружите, что размер бумаги такой же, как установка выбранного принтера по умолчанию на вашем компьютере.

{{% /alert %}}

Следующий пример кода показывает использование метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). Он сначала создает рабочую книгу, затем сохраняет ее в памяти в формате XLSX, после чего загружает с размером бумаги A5 и сохраняет в PDF. Затем загружает снова с размером бумаги A3 и снова сохраняет как PDF. Открыв выходные PDF-файлы и проверив их размер бумаги, вы увидите, что они разные. Один — A5, другой — A3. Для ознакомления скачайте [PDF с размером A5](PrinterSize-a5_out.pdf) и [PDF с размером A3](PrinterSize-a3_out.pdf), созданные кодом.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
