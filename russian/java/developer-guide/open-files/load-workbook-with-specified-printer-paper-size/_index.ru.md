---
title: Загрузить рабочую книгу с указанным размером бумаги для принтера
type: docs
weight: 790
url: /ru/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 Вы можете указать размер бумаги для принтера по вашему выбору при загрузке книги с помощью[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) метод. Обратите внимание: если вы создадите новый файл в MS Excel, вы обнаружите, что размер бумаги совпадает с настройкой принтера по умолчанию на вашем устройстве.

{{% /alert %}} 
## **Загрузить рабочую книгу с указанным размером бумаги для принтера**
 Следующий пример кода иллюстрирует использование[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) метод. Сначала он создает книгу, а затем сохраняет ее в потоке массива байтов в формате XLSX. Затем он загружает его с размером бумаги A5 и сохраняет в формате PDF. Затем он снова загружает его с размером бумаги A3 и снова сохраняет в формате PDF. Если вы откроете выходные PDF-файлы и проверите их размер бумаги, вы увидите, что они разные. Один А5, второй А3. Пожалуйста, загрузите[Выход А5 PDF](5473435.pdf) и[Выход A3 PDF](5473436.pdf) сгенерированный кодом для вашей справки.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
