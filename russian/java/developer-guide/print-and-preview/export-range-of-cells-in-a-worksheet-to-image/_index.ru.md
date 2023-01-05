---
title: Экспорт диапазона Cells на листе в изображение
type: docs
weight: 130
url: /ru/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Вы можете создать изображение рабочего листа, используя Aspose.Cells. Однако иногда вам нужно экспортировать в изображение только диапазон ячеек рабочего листа. В этой статье объясняется, как этого добиться.

{{% /alert %}}

 Чтобы сделать изображение диапазона, установите область печати на желаемый диапазон, а затем установите все поля на 0. Также установите[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) к**истинный**.

Следующий код берет изображение диапазона E8:H10. Ниже приведен скриншот исходной книги, используемой в коде. Вы можете попробовать код с любой книгой.

**Входной файл**

![дело:изображение_альтернативный_текст](export-range-of-cells-in-a-worksheet-to-image_1.png)

При выполнении кода создается изображение только диапазона E8:H10.

**Выходное изображение**

![дело:изображение_альтернативный_текст](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 Вы также можете найти статью[Преобразование рабочего листа в различные форматы изображений](/cells/ru/java/converting-worksheet-to-different-image-formats/) полезный.
