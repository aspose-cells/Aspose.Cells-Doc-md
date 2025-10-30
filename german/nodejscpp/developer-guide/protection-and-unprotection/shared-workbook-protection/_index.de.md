---
title: Kennwortschutz oder Schutz des freigegebenen Arbeitsbuchs mit Node.js über C++
linktitle: Arbeitsmappe mit Kennwort schützen oder entschützen
type: docs
weight: 10
url: /de/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Mögliche Verwendungsszenarien**

Sie können das freigegebene Arbeitsbuch mit Microsoft Excel schützen oder un保护, wie im folgenden Screenshot gezeigt. Aspose.Cells for Node.js via C++ unterstützt diese Funktion ebenfalls mit den Methoden [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) und [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Freigegebenes Arbeitsblatt passwortgeschützt oder nicht passwortgeschützt machen**

Der folgende Beispielcode erstellt eine Arbeitsmappe, schützt sie und ermöglicht die Freigabe und speichert sie als [Ausgabedatei Excel](55541777.xlsx). Im Screenshot ist zu sehen, dass beim Versuch, den Schutz aufzuheben, Microsoft Excel Sie auffordert, das Passwort zum Aufheben des Schutzes einzugeben.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Beispielcode**

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
