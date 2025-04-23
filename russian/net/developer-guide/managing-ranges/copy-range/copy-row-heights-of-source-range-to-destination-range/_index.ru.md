---
title: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 590
url: /ru/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

Иногда пользователю требуется скопировать высоты строк исходного диапазона в целевой диапазон. Aspose.Cells предоставляет перечисление [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) для этой цели. Когда вы установите свойство [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) с перечислением [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype), то высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

{{% /alert %}}

В приведенном ниже примере кода объясняется, как использовать перечисление [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype) для копирования высот строк исходного диапазона в целевой диапазон. После того, как вы откроете созданный этим кодом выходной файл Excel в Microsoft Excel, вы увидите, что высоты строк в целевом диапазоне точно такие же, как исходного диапазона.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
