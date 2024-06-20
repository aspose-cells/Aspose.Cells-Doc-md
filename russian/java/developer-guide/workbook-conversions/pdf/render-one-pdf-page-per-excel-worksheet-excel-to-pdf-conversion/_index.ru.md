---
title: Рендеринг одной страницы PDF на один лист Excel – Преобразование Excel в PDF
type: docs
weight: 40
url: /ru/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

При работе с большими файлами Microsoft Excel (например, книгой, содержащей много листов, каждый из которых имеет 50 столбцов и 300 или более строк данных), возможно, вы захотите, чтобы выходной PDF показывал одну страницу на лист, независимо от размера листа. Это означает, что каждая страница скорее всего будет иметь радикально отличный размер страницы. Это может быть достигнуто с использованием Aspose.Cells for Java.

{{% /alert %}}

Пожалуйста, ознакомьтесь с следующим образцом кода, который преобразует файл Excel с несколькими листами в PDF.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Если опция [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) установлена в **true**, весь контент листа рендерится на одну страницу PDF. Установленный [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) формат бумаги является недействительным, но другие настройки, установленные через [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup), также вступают в силу.

{{% /alert %}} {{% alert color="primary" %}}

Если ваша таблица содержит формулы, лучше всего вызвать метод [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) прямо перед отображением таблицы в формате PDF. Это гарантирует пересчет значений, зависящих от формулы, и правильные значения будут отображены в PDF.

{{% /alert %}}
