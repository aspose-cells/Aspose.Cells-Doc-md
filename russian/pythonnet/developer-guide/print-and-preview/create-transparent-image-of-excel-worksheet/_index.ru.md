---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ru/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Иногда нужно генерировать изображение листа с прозрачностью. Необходимо применить прозрачность ко всем ячейкам, у которых нет заливки. API Aspose.Cells for Python via .NET предоставляет свойство [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) для применения прозрачности к изображению листа. Если это свойство установлено в **false**, ячейки без заливки будут отображены белым цветом, а если в **true**, ячейки без заливки будут прозрачными.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
