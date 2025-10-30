---
title: Kopiera datat i ett område med stil i C++
linktitle: Kopiera dataområde med stil
type: docs
weight: 610
url: /sv/go-cpp/copy-range-data-with-style/
description: Kopiera data i ett område inklusive cellstilar i Excel filer med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Kopiera endast data i område](/cells/sv/cpp/copy-range-data-only/) förklarar hur man kopierar celldata mellan områden. Denna artikel visar hur man kopierar cellområden samtidigt som man bevarar deras formateringsstilar med hjälp av Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells tillhandahåller klasser och metoder för att arbeta med områden inklusive [**CreateRange()**](https://reference.aspose.com/cells/go-cpp/cells/createrange_string_string/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), och [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Detta exempel visar hur man:

1. Skapa en arbetsbok
1. Fyll celler med data
1. Skapa en [**Range**](https://reference.aspose.com/cells/go-cpp/range/)
1. Skapa och konfigurera ett [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objekt
1. Applicera stilar på området
1. Skapa ett andra område
1. Kopiera formaterad data mellan områden

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataWithStyle.go" >}}
