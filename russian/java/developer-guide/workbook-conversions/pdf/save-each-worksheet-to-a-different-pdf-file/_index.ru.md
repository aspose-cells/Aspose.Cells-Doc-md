---
title: Сохраните каждый рабочий лист в другой файл PDF
type: docs
weight: 50
url: /ru/java/save-each-worksheet-to-a-different-pdf-file/
---
{{% alert color="primary" %}}

Aspose.Cells поддерживает преобразование файлов электронных таблиц (содержащих изображения, диаграммы и т. д.) в документы PDF. Aspose.Cells for Java может работать независимо для преобразования электронной таблицы в документ PDF, и вам больше не нужно использовать Aspose.PDF for Java для преобразования. Преобразование также не требует создания/использования каких-либо временных файлов, так как весь процесс может выполняться в памяти.

{{% /alert %}}

Если вам нужно сохранить каждый рабочий лист в файле Excel шаблона для создания разных файлов PDF. Этого можно легко добиться. Вы можете попытаться скрыть листы в файле и сделать видимым один лист за раз, в зависимости от того, как вы будете отображать PDF-файлы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SaveEachWorksheettoDifferentPDF-SaveEachWorksheettoDifferentPDF.java" >}}

{{% alert color="primary" %}}

 Если электронная таблица содержит формулы, лучше вызвать[**Рабочая книга.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()непосредственно перед визуализацией электронной таблицы в PDF. Это гарантирует, что значения, зависящие от формулы, пересчитываются, а правильные значения отображаются в формате PDF.

{{% /alert %}}
