---
title: Déprotéger une feuille de calcul avec Node.js via C++
linktitle: Déprotéger une feuille de calcul
type: docs
weight: 20
url: /fr/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Si un développeur doit supprimer la protection d'une feuille de calcul protégée pendant l'exécution pour pouvoir apporter des modifications au fichier? Cela peut être facilement fait avec Aspose.Cells.

{{% /alert %}}

## **Déprotéger une feuille de calcul**

### **Utilisation de Microsoft Excel**

Pour supprimer la protection d'une feuille de calcul:

Dans le menu **Outils**, sélectionnez **Protection** puis **Déprotéger la feuille**. La protection sera levée sauf si la feuille est protégée par un mot de passe. Dans ce cas, une fenêtre de dialogue demande le mot de passe. Saisissez-le et la feuille sera déprotégée.

### **Déprotéger une feuille de calcul simplement protégée en utilisant Aspose.Cells**

Une feuille de calcul peut être déprotégée en appelant la méthode [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Une feuille simplement protégée n'est pas protégée par un mot de passe. Ces feuilles peuvent être déprotégées en appelant la méthode [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) sans passer de paramètre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Déprotéger une feuille de calcul protégée par mot de passe à l'aide d'Aspose.Cells**

Une feuille protégée par mot de passe est une feuille qui est protégée avec un mot de passe. Ces feuilles peuvent être déprotégées en appelant une version surchargée de la méthode [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) qui prend le mot de passe en paramètre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
