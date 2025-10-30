---
title: Lösenordsskydda eller avsäkra delad arbetsbok med Node.js via C++
linktitle: Lösenordsskydda eller upphäva skyddet för delad arbetsbok
type: docs
weight: 10
url: /sv/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Möjliga användningsscenario**

Du kan skydda eller oförhindra den delade arbetsboken med Microsoft Excel som visas i skärmbilder nedan. Aspose.Cells for Node.js via C++ stöder också denna funktion med metoderna [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) och [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Lösenordsskydda eller upplåsa den delade arbetsboken**

Följande exempelkod skapar en arbetsbok och skyddar den medan du aktiverar delning och sparar den som [utdata Excelfil](55541777.xlsx). På skärmbilden visas det att när du försöker avskydda den, ber Microsoft Excel dig att ange lösenordet för att avskydda den.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
