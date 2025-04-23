---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /ru/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображение вашего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам, которые не имеют цвета заливки. Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) для применения прозрачности к изображению листа. Когда это свойство установлено на **false**, то ячейки без цвета заливки рисуются белым цветом, а когда оно установлено на **true**, ячейки без цвета заливки рисуются прозрачно.

{{% /alert %}}

На следующем изображении листа прозрачность не была применена. Ячейки без цвета заливки рисуются белым цветом.

**Изображение листа без применения прозрачности**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Тогда как на следующем изображении листа прозрачность была применена. Ячейки без цвета заливки рисуются прозрачными.

**Изображение листа после применения прозрачности**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Вы можете использовать следующий образец кода для создания прозрачного изображения вашего листа Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
