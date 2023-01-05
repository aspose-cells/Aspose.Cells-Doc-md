---
title: Загрузить рабочую книгу с указанным размером бумаги для принтера
type: docs
weight: 430
url: /ru/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 Вы можете указать размер бумаги для принтера по вашему выбору при загрузке книги с помощью[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) метод. Обратите внимание: если вы создадите новый файл в MS Excel, вы обнаружите, что размер бумаги совпадает с настройкой принтера по умолчанию на вашем устройстве.

{{% /alert %}}

 Следующий пример кода иллюстрирует использование[**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) метод. Сначала он создает книгу, а затем сохраняет ее в потоке памяти в формате XLSX. Затем он загружает его с размером бумаги A5 и сохраняет в формате PDF. Затем он снова загружает его с размером бумаги A3 и снова сохраняет в формате PDF. Если вы откроете выходные PDF-файлы и проверите их размер бумаги, вы увидите, что они разные. Один А5, второй А3. Пожалуйста, загрузите[Выход А5 PDF](5115234.pdf) и[Выход A3 PDF](5115233.pdf) сгенерированный кодом для вашей справки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
