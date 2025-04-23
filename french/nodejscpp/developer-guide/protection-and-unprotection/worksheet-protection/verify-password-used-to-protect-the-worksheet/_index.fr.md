---
title: Vérifier le mot de passe utilisé pour protéger la feuille de calcul avec Node.js via C++
linktitle: Vérifiez le mot de passe utilisé pour protéger la feuille de calcul
type: docs
weight: 370
url: /fr/nodejs-cpp/verify-password-used-to-protect-the-worksheet/
description: Apprenez comment vérifier le mot de passe utilisé pour protéger une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Les API Aspose.Cells ont amélioré la classe [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) en introduisant certaines propriétés et méthodes utiles. L'une de ces méthodes est [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) qui permet de spécifier un mot de passe sous forme d'instance de *string* et de vérifier si le même mot de passe a été utilisé pour protéger le [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

{{% /alert %}}

La méthode [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) retourne **true** si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée et **false** dans le cas contraire. Le code suivant utilise la méthode [**Protection.verifyPassword(string)**](https://reference.aspose.com/cells/nodejs-cpp/protection/#verifyPassword-string-) en conjonction avec la propriété [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) pour détecter la protection par mot de passe et vérifier ce dernier.

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
