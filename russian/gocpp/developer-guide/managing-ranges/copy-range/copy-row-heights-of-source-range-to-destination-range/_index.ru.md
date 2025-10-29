---
title: Копировать высоту строк исходного диапазона в целевой диапазон с помощью Golang через C++
linktitle: Копировать высоту строк исходного диапазона в целевой диапазон
type: docs
weight: 590
url: /ru/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Узнайте, как копировать высоту строк из исходного диапазона в целевой с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

 Иногда пользователи нуждаются в копировании высоты строк из исходного диапазона в целевой. Aspose.Cells предлагает перечисление [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) для этой задачи. Когда вы установите свойство [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) с этим перечислением [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/), высоты всех строк внутри исходного диапазона будут скопированы в целевой диапазон.

{{% /alert %}}

 Следующий пример кода объясняет, как использовать перечисление [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) для копирования высот строк из исходного диапазона в целевой. После открытия полученного файла Excel в Microsoft Excel, вы увидите, что высоты строк целевого диапазона точно такие же, как и у исходного.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
