---
title: Upptäck hyperlänkstyp
type: docs
weight: 160
url: /sv/net/detect-hyperlink-type/
---
## **Upptäck hyperlänkstyp**

 En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filsökväg, etc. Aspose.Cells stöder funktionen för att upptäcka typen av hyperlänk. Typerna av hyperlänkar representeras av[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Uppräkning. De[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype)Uppräkning har följande medlemmar.

- Extern: Extern länk
- FilePath: Lokal och fullständig sökväg till filer\mappar.
- E-post: E-post
- CellReference: Länk till cell eller namngett område.

 För att kontrollera typen av hyperlänk,[**Hyperlänk**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) klass ger en[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) fastighet med en returtyp av[**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). Följande kodavsnitt visar användningen av[**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype)egendom genom att använda denna[källkod excel-fil](94896195.xlsx).

### Källkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

Följande är utdata som genereras av kodavsnittet ovan.

### Konsolutgång
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
