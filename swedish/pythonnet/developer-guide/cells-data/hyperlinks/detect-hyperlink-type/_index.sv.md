---
title: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/python-net/detect-hyperlink-type/
description: Lär dig hur man upptäcker hyperlänktyp genom Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Upptäck hyperlänktyp i Python, Upptäck hyperlänktypen, Hämta hyperlänktypen.
---

## **Upptäck hyperlänktyp**

En Excel-fil kan ha olika typer av hyperlänkar som externa, cellreferenser, filvägar, osv. Aspose.Cells för Python via .NET stöder funktionen att upptäcka hyperlänkens typ. Typerna av hyperlänkar representeras av [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype)-utskottsmedlemmar. Utskottsmedlemmar

- EXTERN: Extern länk
- FILVÄG: Lokal och fullständig sökväg till filer/mappar.
- E-POST: E-post
- CELLREFERENS: Länk till cell eller namngivet område.

För att kontrollera hyperlänkens typ, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink)-klassen en [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/)-egenskap med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). Följande kodsnutt visar användningen av [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/)-egenskapen med hjälp av denna [källa excel-fil](94896195.xlsx).

### Källkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
