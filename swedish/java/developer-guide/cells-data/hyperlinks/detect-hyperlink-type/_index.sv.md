---
title: Upptäck hyperlänktyp
type: docs
weight: 180
url: /sv/java/detect-hyperlink-type/
---

## **Upptäck hyperlänktyp**

En Excelfil kan ha olika typer av hyperlänkar som externa, cellreferenser, filvägar, etc. Aspose.Cells stöder funktionen att upptäcka hyperlänkens typ. Hyperlänkstyperna representeras av [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)-uppräkningen. [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)-uppräkningen har följande medlemmar.

- [**EXTERNAL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Extern länk
- [**FILE_PATH**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Lokal och full filväg till filer\mappar
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): E-post
- [**CELL_REFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Länk till cell eller namngivet område.

För att kontrollera typen av hyperlänk tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink)-klassen en [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)-egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). Följande kodsnutt demonstrerar användningen av [**LinkType**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)-egenskapen genom att använda detta [käll-excel-fil](LinkTypes.xlsx).

## Källkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

Följande är utdatan som genereras av den tidigare givna kodsnutten.

## Konsoloutput
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
