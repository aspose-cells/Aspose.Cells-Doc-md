---
title: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 250
url: /ru/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

Иногда пользователю нужно скопировать высоты строк исходного диапазона в целевой диапазон. Aspose.Cells предоставляет enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) для этой цели. При установке свойства [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) в значение [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS), высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

{{% /alert %}} 
## **Копировать высоты строк исходного диапазона в целевой диапазон**
Следующий пример кода демонстрирует, как использовать enum [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) для копирования высот строк исходного диапазона в целевой. Открывая сгенерированный этим кодом файл Excel в Microsoft Excel, вы увидите, что высоты строк целевого диапазона точно совпадают с высотами исходного диапазона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
