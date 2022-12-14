---
title: Копировать высоты строк исходного диапазона в целевой диапазон
type: docs
weight: 250
url: /ru/java/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}} 

 Иногда пользователю необходимо скопировать высоту строки исходного диапазона в целевой диапазон. Aspose.Cells предоставляет[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum для этой цели. Когда вы установите[PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) имущество с[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) enum, то высота всех строк внутри исходного диапазона будет скопирована в целевой диапазон.

{{% /alert %}} 
## **Копировать высоты строк исходного диапазона в целевой диапазон**
 В следующем примере кода объясняется, как использовать[PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)enum для копирования высоты строк исходного диапазона в целевой диапазон. Как только вы откроете выходной файл Excel, сгенерированный этим кодом, в Microsoft Excel, вы увидите, что высота строки целевого диапазона точно такая же, как высота строки исходного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
