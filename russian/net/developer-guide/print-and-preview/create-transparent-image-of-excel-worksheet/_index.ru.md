---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ru/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться создать изображение вашего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам без цвета заливки. Aspose.Cells предоставляет свойство [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) для применения прозрачности к изображению листа. Когда это свойство имеет значение **false**, то ячейки без цвета заливки рисуются белым цветом, а когда оно имеет значение **true**, то ячейки без цвета заливки рисуются прозрачными.

{{% /alert %}} 

На следующем изображении листа прозрачность не была применена. Ячейки без цвета заливки рисуются белым цветом.

|**Вывод без прозрачности: фон ячейки белый**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Тогда как на следующем изображении листа прозрачность была применена. Ячейки без цвета заливки рисуются прозрачными.

|**Вывод со включенной прозрачностью**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Следующий образец кода генерирует прозрачное изображение из листа Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
