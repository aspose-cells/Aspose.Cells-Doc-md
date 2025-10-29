---
title: Copier la hauteur des lignes de la plage source vers la plage de destination avec Golang via C++
linktitle: Copier la hauteur des lignes de la plage source vers la plage de destination
type: docs
weight: 590
url: /fr/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Apprenez comment copier la hauteur des lignes d une plage source vers une plage de destination en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Parfois, les utilisateurs doivent copier la hauteur des lignes d'une plage source vers une plage de destination. Aspose.Cells fournit l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) à cet effet. Lorsque vous définissez la propriété [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) avec l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/), les hauteurs de toutes les lignes à l'intérieur de la plage source seront copiées dans la plage de destination.

{{% /alert %}}

Le code d'exemple suivant explique comment utiliser l'énumération [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/) pour copier la hauteur des lignes d'une plage source vers une plage de destination. Une fois que vous ouvrez le fichier Excel généré par ce code dans Microsoft Excel, vous verrez que les hauteurs des lignes de la plage de destination sont exactement identiques à celles de la plage source.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
