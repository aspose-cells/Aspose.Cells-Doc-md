---
title: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/net/detect-hyperlink-type/
description: Lär dig hur du upptäcker hyperlänkstyp genom Aspose.Cells for .NET API.
keywords: Upptäck hyperlänkstyp, Upptäck typen av hyperlänk, Få typen av hyperlänk
---

## **Upptäck hyperlänktyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filsökväg osv. Aspose.Cells stöder funktionen att upptäcka hyperlänkstypen. Hyperlänkstyperna representeras av [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)-uppräkningen. [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)-uppräkningen har följande medlemmar.

- Extern: Extern länk
- Filsökväg: Lokal och full sökväg till filer/mappar.
- E-post: E-post
- Cellreferens: Länk till cell eller namnområde.

För att kontrollera hyperlänkens typ, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink)-klassen en [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)-egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Följande kodsnutt visar användningen av [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)-egenskapen med hjälp av denna [källa excel-fil](94896195.xlsx).

### Källkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Följande är utdatan som genereras av den tidigare givna kodsnutten.

### Konsolutfall
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
