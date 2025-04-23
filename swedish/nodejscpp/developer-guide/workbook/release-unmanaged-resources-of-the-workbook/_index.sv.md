---
title: Släpp oanvända resurser för arbetsboken med Node.js via C++
linktitle: Frigör ohanterade resurser i arbetsboken
type: docs
weight: 310
url: /sv/nodejs-cpp/release-unmanaged-resources-of-the-workbook/
description: Lär dig hur du frigör oanvända resurser för Workbook objektet med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Aspose.Cells tillhandahåller [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)-metoden för att frigöra de oanvände resurserna för [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-objektet. Disposeringsmönstret används endast för objekt som tillgång till oanvänt resurser, som fil- och rörhandtag, registretaggar, väntande handtag eller pekare till block av oanvänt minne. Detta beror på att garbage collection är mycket effektiv på att återvinna oanvända hanterade objekt, men kan inte återvinna oanvänt minne.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-objekt implementerar nu *System.IDisposable*-gränssnittet som har en metod [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--). Du kan antingen kalla [**Workbook.dispose()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#dispose--)-metoden direkt eller använda *Using*-satsen för att automatiskt kalla denna metod.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create workbook object
const wb1 = new AsposeCells.Workbook();

// Call Dispose method
wb1.dispose();

// Call Dispose method via a scoped approach
(async () => {
const wb2 = new AsposeCells.Workbook();
// Any other code goes here
wb2.dispose();
})();
```
