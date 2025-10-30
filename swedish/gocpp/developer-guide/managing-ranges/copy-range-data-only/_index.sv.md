---
title: Kopiera endast område data med Golang via C++
linktitle: Kopiera endast dataområde
type: docs
weight: 600
url: /sv/go-cpp/copy-range-data-only/
description: Lär dig att kopiera endast data utan formatering med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Ibland behöver du kopiera data från en cellintervall till en annan, kopiera bara datan, inte formateringen. Aspose.Cells erbjuder den här funktionen.

Den här artikeln ger en exempelkod som använder Aspose.Cells för att kopiera ett datintervall.

{{% /alert %}}

Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Skapa en [**Range**](https://reference.aspose.com/cells/go-cpp/range/).
1. Skapa ett [**Style**](https://reference.aspose.com/cells/go-cpp/style/)-objekt med specificerade formateringsattribut.
1. Tillämpa stilformatering på området.
1. Skapa en annan cellintervall.
1. Kopiera data från det första området till det andra området.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeDataOnly.go" >}}
