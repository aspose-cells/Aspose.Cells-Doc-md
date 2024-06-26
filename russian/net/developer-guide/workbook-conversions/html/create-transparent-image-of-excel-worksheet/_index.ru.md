﻿---
title: Создать прозрачное изображение рабочего листа Excel
type: docs
weight: 170
url: /ru/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Иногда вам нужно создать изображение вашего рабочего листа как прозрачное изображение. Вы хотите применить прозрачность ко всем ячейкам, которые не имеют цветов заливки. Aspose.Cells обеспечивает[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)свойство, чтобы применить прозрачность к изображению рабочего листа. Когда это свойство**ЛОЖЬ** , то ячейки без цветов заливки рисуются белым цветом, а когда он**истинный**, ячейки без цветов заливки отображаются прозрачными.

{{% /alert %}} 

На следующем изображении рабочего листа прозрачность не применялась. Ячейки без заливки окрашены в белый цвет.

|**Вывод без прозрачности: фон ячейки белый**|
|:- |
|![дело:изображение_альтернативный_текст](create-transparent-image-of-excel-worksheet_1.png)|

В то время как на следующем изображении рабочего листа была применена прозрачность. Ячейки без цветов заливки прозрачны.

|**Вывод с включенной прозрачностью**|
|:- |
|![дело:изображение_альтернативный_текст](create-transparent-image-of-excel-worksheet_2.png)|

Следующий пример кода создает прозрачное изображение из листа Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
