---
title: Generera bilder av villkorliga formateringsdatabars med Golang via C++
linktitle: Generera bilder för betingad formatering DataBars
description: Aspose.Cells är ett C++ bibliotek för hantering av kalkylbladsfiler. Det stöder generation av villkorsformaterade datastavar och bilder, vilket gör att användare kan anpassa visningen av kalkylbladet baserat på cellvärden. Denna artikel introducerar hur man använder Aspose.Cells biblioteket för att generera villkorsformat datastavar och bilder.
keywords: Aspose.Cells, Betingad formatering, Databalkar, Bilder, Kalkylblad
type: docs
weight: 40
url: /sv/go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder på DataBars för betingad formatering. Du kan använda Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/)-metod för att generera dessa bilder. Denna artikel visar hur man genererar en DataBar-bild med hjälp av Aspose.Cells.

{{% /alert %}}

Följande exempel genererar Datastapeln för cell C1. Först accessar den formateringsvillkoret för cellen, och därefter från detta objekt accessar den [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/)-objektet och använder dess [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/)-metod för att generera bilden av cellen. Slutligen sparas bilden på disken.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}
