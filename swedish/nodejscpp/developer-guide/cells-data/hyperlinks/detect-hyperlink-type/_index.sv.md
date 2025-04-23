---
title: Upptäck hyperlänktyp
type: docs
weight: 160
url: /sv/nodejs-cpp/detect-hyperlink-type/
description: Lär dig hur du upptäcker hyperlänktstyp via API et Aspose.Cells for Node.js via C++.
keywords: Upptäck hyperlänktstyp Node.js via C++, upptäck typen av hyperlänk Node.js via C++, Hämta typen av hyperlänk Node.js via C++
---

## **Identifiera hyperlänkstyp**

En Excelfil kan ha olika typer av hyperlänkar som extern, cellreferens, filväg, etc. Aspose.Cells for Node.js via C++ stödjer funktionen att upptäcka typen av hyperlänk. Typerna av hyperlänkar representeras av [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeration. [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeration har följande medlemmar.

- Extern: Extern länk
- Filväg: Lokal och fullständig sökväg till filer/mappar.
- E-post: E-post
- Cellreferens: Länk till cell eller namngiven intervall.

För att kontrollera typen av hyperlänk, tillhandahåller [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink)-klassen en [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--)-metod med en returtyp av [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Följande kodexempel visar användningen av [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--)-metoden med hjälp av denna [källa Excel-fil](94896195.xlsx).

### Källkod

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


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
