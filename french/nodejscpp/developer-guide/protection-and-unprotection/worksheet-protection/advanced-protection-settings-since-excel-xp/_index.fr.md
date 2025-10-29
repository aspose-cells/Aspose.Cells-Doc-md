---
title: Paramètres de protection avancée depuis Excel XP avec Node.js via C++
linktitle: Paramètres de protection avancée depuis Excel XP
type: docs
weight: 30
url: /fr/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

Depuis la publication d'Excel 2002 ou XP, Microsoft a ajouté de nombreux paramètres de protection avancés.

{{% /alert %}}


## **Introduction**

Ces paramètres de protection restreignent ou permettent aux utilisateurs de:

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, lignes ou colonnes.
- Insérer des lignes, colonnes ou hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells for Node.js via C++ supporte toutes les fonctionnalités de protection avancée offertes par Excel XP ou versions ultérieures.

### **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** puis **Protéger la feuille**. Une boîte de dialogue s'affiche.

Pour voir les paramètres de protection disponibles dans Excel 2016 :

1. Dans le menu **Fichier**, sélectionnez **Protéger le classeur** puis **Protéger la feuille en cours**.
1. Sélectionnez **Protéger la feuille** dans le menu **Révision**.

Les étapes mentionnées ci-dessus afficheront une boîte de dialogue où vous pourrez autoriser ou restreindre les fonctionnalités de la feuille de calcul ou appliquer un mot de passe à la feuille.

### **Paramètres de protection avancée utilisant Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ supporte tous les paramètres de protection avancée.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit la propriété [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) utilisée pour appliquer ces paramètres de protection avancés. La propriété [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer les restrictions.

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Veuillez ne pas appeler la méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) de la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) lors de l'utilisation de la propriété [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--). Enregistrez également le fichier au format Excel97To2003 ou Xlsx car les paramètres de protection avancée ne sont pris en charge que par Excel XP et versions ultérieures.

{{% /alert %}}

### **Problème de verrouillage de cellules**

Si vous souhaitez restreindre la modification des cellules par les utilisateurs, celles-ci doivent être verrouillées avant l'application des paramètres de protection. Sinon, les cellules peuvent être modifiées même si la feuille est protégée. Dans Microsoft Excel XP, les cellules peuvent être verrouillées via la boîte de dialogue suivante :

|**Boîte de dialogue pour verrouiller les cellules dans Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Il est également possible de verrouiller des cellules en utilisant l'API Aspose.Cells. Chaque cellule peut recevoir un format [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contenant une propriété booléenne [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Définissez la propriété [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) sur **true** ou **false** pour verrouiller ou déverrouiller la cellule.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
