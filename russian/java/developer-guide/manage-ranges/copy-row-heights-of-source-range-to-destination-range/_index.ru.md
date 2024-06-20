---
title: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 250
url: /ru/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Иногда пользователю нужно скопировать высоту строк исходного диапазона в целевой диапазон. Aspose.Cells предоставляет перечисление [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) для этой цели. Когда вы установите свойство [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) с перечислением [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS), то высота всех строк внутри исходного диапазона будет скопирована в целевой диапазон.

{{% /alert %}} 
## **Копировать высоты строк исходного диапазона в целевой диапазон**
В следующем образце кода объясняется, как использовать перечисление [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) для копирования высоты строк исходного диапазона в целевой диапазон. После открытия сгенерированного этим кодом файла Excel в Microsoft Excel вы увидите, что высоты строк целевого диапазона точно такие же, как у исходного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
