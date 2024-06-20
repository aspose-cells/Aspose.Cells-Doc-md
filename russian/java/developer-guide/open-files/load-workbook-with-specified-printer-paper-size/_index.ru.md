---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 790
url: /ru/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Вы можете указать размер бумаги принтера на ваш выбор при загрузке книги с помощью метода [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Обратите внимание, что если вы создаете новый файл в MS Excel, вы увидите, что размер бумаги такой же, как установка внешего принтера в вашем устройстве.

{{% /alert %}} 
## **Загружать книгу с указанным размером бумаги принтера**
Ниже приведен пример кода, иллюстрирующий использование метода [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Сначала создается книга, затем она сохраняется в поток байтов в формате XLSX. Затем она загружается с размером бумаги A5 и снова сохраняется в формате PDF. Затем она снова загружается с размером бумаги A3 и снова сохраняется в формате PDF. Если открыть выходные PDF и проверить их размер бумаги, вы увидите, что они отличаются. Один - A5, а другой - A3. Скачайте [PDF с A5 размером](5473435.pdf) и [PDF с A3 размером](5473436.pdf), сгенерированные кодом для вашего справочника.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
