---
title: Kopiera endast områdeformat med Golang via C++
linktitle: Kopiera endast stilområde
type: docs
weight: 620
url: /sv/go-cpp/copy-range-style-only/
description: Lär dig att kopiera enbart stilen för ett område i Excel med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

[Kopiera endast data i område](/cells/sv/cpp/copy-range-data-only/) och [Kopiera data med stil](/cells/sv/cpp/copy-range-data-with-style/) förklarar hur man kopierar data från ett område till ett annat på egen hand eller komplett med formatering. Det är också möjligt att kopiera enbart formateringen. Denna artikel visar hur.

{{% /alert %}} 

Detta exempel skapar en arbetsbok, fyller den med data och kopierar endast stil från ett intervall.

1. Skapa ett område.
1. Skapa ett [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en andra cellintervall.
1. Kopiera det första områdets formatering till det andra området.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeStyleOnly.go" >}}
