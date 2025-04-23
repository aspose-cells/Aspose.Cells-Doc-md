---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 430
url: /ru/go-cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

Вы можете указать размер бумаги принтера при загрузке книги, используя метод [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Обратите внимание, что при создании нового файла в MS Excel установленный размер бумаги совпадает с настройками вашего принтера по умолчанию.

{{% /alert %}}

Следующий пример кода демонстрирует использование метода [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/go-cpp/loadoptions/setpapersize/). Он сначала создаёт рабочую книгу, сохраняет её в поток памяти в формате XLSX, затем загружает её с размером бумаги A5 и сохраняет в PDF, затем снова загружает с размером A3 и сохраняет в PDF. Открыв полученные PDF, вы увидите, что размеры бумаги различаются: один A5, другой A3. Скачать пример PDF с A5 [здесь](PrinterSize-a5_out.pdf) и с A3 [здесь](PrinterSize-a3_out.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookWithPrinterSize.go" >}}
