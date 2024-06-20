---
title: Экспорт диапазона ячеек листа в изображение
type: docs
weight: 130
url: /ru/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Вы можете создать изображение листа с помощью Aspose.Cells. Однако иногда вам может потребоваться экспортировать только диапазон ячеек листа в изображение. В этой статье объясняется, как это сделать.

{{% /alert %}}

Чтобы сделать изображение диапазона, установите область печати в нужный диапазон, а затем установите все поля на 0. Также установите [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) ​​на **true**.

Приведённый ниже код делает изображение диапазона E8:H10. Ниже приведен снимок экрана используемой в коде исходной книги. Вы можете попробовать код с любой книгой.

**Входной файл**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Выполнение кода создает изображение только диапазона E8:H10.

**Изображение на выходе**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Вы также можете найти статью [Преобразование листа в другие форматы изображений](/cells/ru/java/converting-worksheet-to-different-image-formats/) полезной.
