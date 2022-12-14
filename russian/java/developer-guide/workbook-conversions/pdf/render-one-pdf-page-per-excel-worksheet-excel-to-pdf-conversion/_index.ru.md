---
title: Рендеринг одной страницы PDF на лист Excel - Преобразование Excel в PDF
type: docs
weight: 40
url: /ru/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

При работе с большими Microsoft файлами Excel (например, рабочей книгой с большим количеством листов, каждый из которых содержит 50 столбцов и 300 или более строк данных), может потребоваться, чтобы вывод PDF отображал одну страницу на листе независимо от размера рабочего листа. . Это будет означать, что каждая страница, вероятно, будет иметь совершенно разный размер страницы. Этого можно добиться, позвонив по номеру Aspose.Cells for Java.

{{% /alert %}}

См. следующий пример кода, который преобразует файл Excel с несколькими листами в PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Если[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) опция установлена на**истинный** , все содержимое листа отображается на одной странице PDF. Размер бумаги, установленный[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) недействителен, но другие настройки, заданные с помощью[**Настройка страницы**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)все равно вступят в силу.

{{% /alert %}} {{% alert color="primary" %}}

Если ваша электронная таблица содержит формулы, лучше вызвать[**Рабочая книга.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) непосредственно перед преобразованием электронной таблицы в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}
