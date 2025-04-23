---
title: Загружать книгу с указанным размером бумаги принтера
type: docs
weight: 790
url: /ru/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Вы можете указать размер бумаги вашего принтера при загрузке рабочей книги, используя метод [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Обратите внимание, что при создании нового файла в MS Excel размер бумаги по умолчанию совпадает с настройками вашего принтера.

{{% /alert %}} 
## **Загружать книгу с указанным размером бумаги принтера**
Следующий пример иллюстрирует использование метода [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). Он сначала создает рабочую книгу, сохраняет в поток байтов в формате XLSX, затем загружает ее с размером бумаги A5 и сохраняет в PDF, затем снова загружает с размером A3 и сохраняет еще раз в PDF. Открыв итоговые PDF, вы увидите, что размеры бумаги разные: один — A5, другой — A3. Для ознакомления скачайте сгенерированные примеру файлы [A5 PDF](5473435.pdf) и [A3 PDF](5473436.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
