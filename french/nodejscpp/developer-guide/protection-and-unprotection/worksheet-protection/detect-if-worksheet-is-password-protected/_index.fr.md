---
title: Détecter si une feuille de calcul est protégée par mot de passe avec Node.js via C++
linktitle: Détecter si la feuille de calcul est protégée par mot de passe
type: docs
weight: 360
url: /fr/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Découvrez comment détecter si une feuille de calcul est protégée par mot de passe en utilisant Aspose.Cells for Node.js via C++. 
keywords: Détecter la protection par mot de passe de la feuille de calcul Node.js via C++, Vérifier si la feuille de calcul est protégée par mot de passe Node.js via C++, Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

Il est possible de protéger séparément les classeurs et les feuilles de calcul. Par exemple, un tableau peut contenir une ou plusieurs feuilles protégées par mot de passe, cependant, le classeur lui-même peut ou non être protégé. Les API Aspose.Cells fournissent les moyens de détecter si une feuille donnée est protégée par mot de passe ou non. Cet article montre comment utiliser l'API Aspose.Cells for Node.js via C++ pour réaliser cela.

{{% /alert %}}

Aspose.Cells for Node.js via C++ a exposé la propriété [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) pour détecter si une feuille de calcul est protégée par mot de passe ou non. La propriété de type booléen [**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--) retourne **true** si [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) est protégé par mot de passe et **false** sinon.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
