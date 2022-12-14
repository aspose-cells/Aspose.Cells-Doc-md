---
title: Рендеринг одной страницы PDF на лист Excel - Преобразование Excel в PDF
type: docs
weight: 100
url: /ru/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

При работе с большими Microsoft файлами Excel (например, рабочей книгой с большим количеством листов, каждый из которых содержит 50 столбцов и 300 или более строк данных), может потребоваться, чтобы вывод PDF отображал одну страницу на листе независимо от размера рабочего листа. . Это будет означать, что каждая страница, вероятно, будет иметь совершенно разный размер страницы. Этого можно добиться, позвонив по номеру Aspose.Cells for .NET.

{{% /alert %}} 

См. следующий пример кода, который преобразует файл Excel с несколькими листами в PDF.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Если[Одна страница на листе](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) опция установлена на**истинный**, все содержимое листа будет отображено на одной странице PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Если ваша электронная таблица содержит формулы, лучше всего вызвать[Рабочая книга.ВычислитьФормулу()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)непосредственно перед рендерингом электронной таблицы в PDF. Это гарантирует, что значения, зависящие от формулы, будут пересчитаны, а в PDF-файле отобразятся правильные значения.

{{% /alert %}}
