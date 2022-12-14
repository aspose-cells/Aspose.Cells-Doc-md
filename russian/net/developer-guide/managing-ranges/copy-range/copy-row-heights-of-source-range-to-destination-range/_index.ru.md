---
title: Копировать высоты строк исходного диапазона в целевой диапазон
type: docs
weight: 590
url: /ru/net/copy-row-heights-of-source-range-to-destination-range/
---
{{% alert color="primary" %}}

 Иногда пользователю необходимо скопировать высоту строки исходного диапазона в целевой диапазон. Aspose.Cells предоставляет[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) enum для этой цели. Когда вы установите[**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) имущество с[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) enum, то высота всех строк внутри исходного диапазона будет скопирована в целевой диапазон.

{{% /alert %}}

 В следующем примере кода объясняется, как использовать[**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)enum для копирования высоты строк исходного диапазона в целевой диапазон. Как только вы откроете выходной файл Excel, сгенерированный этим кодом, в Microsoft Excel, вы увидите, что высота строки целевого диапазона точно такая же, как высота строки исходного диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
