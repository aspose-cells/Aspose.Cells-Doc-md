---
title: Upptäck hyperlänkstyp
type: docs
weight: 180
url: /sv/java/detect-hyperlink-type/
---
## **Upptäck hyperlänkstyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferens, filsökväg, etc. Aspose.Cells stöder funktionen för att upptäcka typen av hyperlänk. Typerna av hyperlänkar representeras av[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Uppräkning. De[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Uppräkning har följande medlemmar.

- [**EXTERN**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Extern länk
- [**SÖKVÄG**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Lokal och fullständig sökväg till filer\mappar.
- [**E-POST**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-post
- [**CELL_REFERENS**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Länk till cell eller namngivet område.

För att kontrollera typen av hyperlänk,[**Hyperlänk**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) klass ger en[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) fastighet med en returtyp av[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Följande kodavsnitt visar användningen av[**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)egendom genom att använda denna[source excel-fil](LinkTypes.xlsx).

## Källkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Följande är utdata som genereras av kodavsnittet ovan.

## Konsolutgång
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
