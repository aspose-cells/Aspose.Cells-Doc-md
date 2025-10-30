---
title: Avfrys rader eller kolumner med Node.js via C++
linktitle: Avfrys fönster
type: docs
weight: 190
url: /sv/nodejs-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: I denna artikel lär du dig hur man programatiskt avfryser rader, kolumner eller paneler i Excel arbetsblad med Node.js API och C++.
keywords: Avfrys paneler, Avfrys rader, Avfrys kolumner, avfri fönstret med Node.js via C++.
---

## **Introduktion**

I denna artikel lär vi oss hur man avfryser rader, kolumner och paneler. Om arbetsbladen i Excel-filer är frysta, vill vi ibland avfrysa arbetsbladet eller justera frysta rader, kolumner eller paneler.


## **I Excel**

1. Klicka på fliken Visa > Frys fönster > Avfrys fönster.

**![avfrysta fönster i Excel](Avfrys-Fönster.png)**




## **Avfrys rader, kolumner eller paneler med Aspose.Cells for Node.js via C++**
Det är enkelt att avfrysa paneler med Aspose.Cells for Node.js via C++. Använd [**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unFreezePanes--)-metoden för att avfrysa paneler.

1. Konstruera arbetsboken för att öppna den frysta filen.
2. Avfrys paneler med Worksheet.unfreezePanes()-metoden.
3. Spara filen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const frozenFilePath = path.join(dataDir, "Frozen.xlsx");

const workbook = new AsposeCells.Workbook(frozenFilePath); 
workbook.getWorksheets().get(0).unFreezePanes();
workbook.save("Unfrozen.xlsx");
```

Bifogad [provkälla för Excel-filen](Fryst.xlsx).
{{< app/cells/assistant language="nodejs-cpp" >}}
