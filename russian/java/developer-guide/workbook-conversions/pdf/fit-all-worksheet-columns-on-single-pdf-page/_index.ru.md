---
title: Вписать все столбцы листа в одну страницу PDF
type: docs
weight: 70
url: /ru/java/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Иногда вы хотите создать файл PDF, который помещает все столбцы листа на одну страницу. Свойство [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) предоставляет эту функцию очень простым способом. Сложные расчеты, такие как высота и ширина выходной страницы PDF, обрабатываются внутренне и основаны на данных на листе.

{{% /alert %}}

## **Вписать столбцы листа на одну страницу PDF**

 [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) гарантирует, что все столбцы листа будут отображены на одной странице PDF, хотя строки могут занимать несколько страниц в зависимости от данных на листе.

{{% alert color="primary" %}}

Если на листе много столбцов, то созданный PDF-файл может отображать содержимое в очень малом масштабе. Оно все равно читаемо при увеличении в приложении для просмотра, таком как Acrobat Reader.

{{% /alert %}}

Приведенный ниже образец кода показывает, как использовать свойство [**PdfSaveOptions.setAllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#AllColumnsInOnePagePerSheet) для отображения большого листа из 100 столбцов.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FitAllWorksheetColumns-FitAllWorksheetColumns.java" >}}

{{% alert color="primary" %}}

Если ваша таблица содержит формулы, лучше всего вызвать метод [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед отображением таблицы в формате PDF. Таким образом будет обеспечено пересчет значений, зависящих от формулы, и правильные значения будут отображены в PDF.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
