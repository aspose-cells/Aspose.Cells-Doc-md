---
title: Passwort zum Schutz des Arbeitsblatts mit Node.js über C++ verifizieren
linktitle: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 370
url: /de/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Erfahren Sie, wie Sie das Passwort überprüfen, das zum Schutz eines Arbeitsblatts verwendet wurde, mit Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells APIs haben die [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection)-Klasse durch die Einführung nützlicher Eigenschaften & Methoden verbessert. Eine davon ist die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)-Methode, mit der Sie ein Passwort als *string*-Instanz angeben und überprüfen können, ob dieses Passwort zum Schutz des [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) verwendet wurde.

{{% /alert %}}

Die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)-Methode gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des Arbeitsblatts verwendeten Passwort übereinstimmt, und **false**, wenn das Passwort nicht übereinstimmt. Der folgende Code verwendet die [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-)-Methode in Verbindung mit der [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)-Eigenschaft, um die Passwortsicherung zu erkennen und das Passwort zu überprüfen.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = workbook.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
// Verify the password used to protect the Worksheet
if (sheet.getProtection().verifyPassword("1234")) {
console.log("Specified password has matched");
} else {
console.log("Specified password has not matched");
}
}
```
