---
title: Upptäck hyperlink typ med Golang via C++
linktitle: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/go-cpp/detect-hyperlink-type/
description: Lär dig hur du upptäcker hyperlänktstyp via API n Aspose.Cells for C++.
keywords: Upptäck hyperlänkstyp, Upptäck typen av hyperlänk, Få typen av hyperlänk
---

## **Identifiera hyperlänkstyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filsökväg osv. Aspose.Cells stöder funktionen att upptäcka hyperlänkstypen. Hyperlänkstyperna representeras av [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)-uppräkningen. [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/)-uppräkningen har följande medlemmar.

- Extern: Extern länk
- Filsökväg: Lokal och full sökväg till filer/mappar.
- E-post: E-post
- Cellreferens: Länk till cell eller namnområde.

För att kontrollera hyperlänkens typ, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/)-klassen en [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/)-egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). Följande kodsnutt visar användningen av [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/)-egenskapen med hjälp av denna [källa excel-fil](94896195.xlsx).

### Källkod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
Följande är utdatan som genereras av den tidigare givna kodsnutten.

### Konsolutfall
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
