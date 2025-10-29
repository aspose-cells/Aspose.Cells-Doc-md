---
title: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 590
url: /ru/python-net/copy-row-heights-of-source-range-to-destination-range/
description: В этой статье описано, как скопировать высоту строк исходного диапазона в целевой диапазон с помощью Aspose.Cells для Python via .NET библиотеки.
keywords: Библиотека Python для Excel, Как скопировать высоту строк исходного диапазона в целевой диапазон с помощью Python Excel Library, Как скопировать высоту строк исходного диапазона только с помощью библиотеки Python для Excel.
---

{{% alert color="primary" %}}

Иногда пользователю нужно скопировать высоту строк исходного диапазона в целевой диапазон. Aspose.Cells для Python via .NET предоставляет перечисление [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) для этой цели. Когда вы установите свойство [**PasteOptions.paste_type**](https://reference.aspose.com/cells/python-net/aspose.cells/pasteoptions/paste_type/) с перечислением [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype), то высота всех строк внутри исходного диапазона будет скопирована в целевой диапазон.

{{% /alert %}}

В приведенном ниже примере кода объясняется, как использовать перечисление [**PasteType.ROW_HEIGHTS**](https://reference.aspose.com/cells/python-net/aspose.cells/pastetype) для копирования высот строк исходного диапазона в целевой диапазон. После того, как вы откроете созданный этим кодом выходной файл Excel в Microsoft Excel, вы увидите, что высоты строк в целевом диапазоне точно такие же, как исходного диапазона.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-GetRowHeightsOfSourceRangeToDestinationRange.py" >}}
{{< app/cells/assistant language="python-net" >}}
