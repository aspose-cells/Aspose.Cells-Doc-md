---
title: Protection des feuilles avec Node.js via C++
linktitle: Protéger les feuilles de calcul
type: docs
weight: 10
url: /fr/nodejs-cpp/protecting-worksheets/
description: Découvrez comment protéger les feuilles dans Excel en utilisant Aspose.Cells for Node.js via C++, y compris la protection des lignes, colonnes, et cellules spécifiques.
---


{{% alert color="primary" %}}

Lorsqu'une feuille est protégée, les actions qu'un utilisateur peut effectuer sont restreintes. Par exemple, ils ne peuvent pas saisir de données, insérer ou supprimer des lignes ou colonnes, etc.

{{% /alert %}}

## **Protéger les feuilles de calcul**

### **Introduction**

Les options de protection générales dans Microsoft Excel sont :

- Contenu
- Objets
- Scénarios

Les feuilles de calcul protégées ne cachent ni ne protègent les données sensibles, donc c'est différent du chiffrement de fichier. Généralement, la protection de feuille de calcul est adaptée à des fins de présentation. Elle empêche l'utilisateur final de modifier les données, le contenu et la mise en forme dans la feuille de calcul.

### **Protéger une feuille de calcul**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul d'un fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) fournit la méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) qui est utilisée pour appliquer une protection sur la feuille. La méthode [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) accepte les paramètres suivants :

- Type de protection, le type de protection à appliquer sur la feuille de calcul. Le type de protection est appliqué à l'aide de l'énumération [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype).
- Nouveau mot de passe, le nouveau mot de passe utilisé pour protéger la feuille de calcul.
- Ancien mot de passe, l'ancien mot de passe, si la feuille de calcul est déjà protégée par mot de passe. Si la feuille de calcul n'est pas déjà protégée, passez simplement null.

L'énumération [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) contient les types de protection prédéfinis suivants :

|**Types de protection**|**Description**|
| :- | :- |
|All|L'utilisateur ne peut rien modifier sur cette feuille de calcul|
|Contents|L'utilisateur ne peut pas saisir de données dans cette feuille de calcul|
|Objects|L'utilisateur ne peut pas modifier les objets de dessin|
|Scenarios|L'utilisateur ne peut pas modifier les scénarios sauvegardés|
|Structure|L'utilisateur ne peut pas modifier la structure|
|Windows|La protection est appliquée aux fenêtres|
|None|Aucune protection n'est appliquée|

L'exemple ci-dessous montre comment protéger une feuille de calcul avec un mot de passe.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Après le code ci-dessus est utilisé pour protéger la feuille de calcul, vous pouvez vérifier la protection sur la feuille de calcul en l'ouvrant. Une fois que vous ouvrez le fichier et essayez d'ajouter des données à la feuille de calcul, vous verrez le dialogue suivant:

|**Un avertissement de dialogue indiquant qu'un utilisateur ne peut pas modifier la feuille de calcul**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Pour travailler sur la feuille de calcul, protégez la feuille de calcul en sélectionnant la **Protection**, puis **Désactiver la protection de la feuille** dans le menu **Outils**.

Après avoir sélectionné l'élément de menu Désactiver la protection de la feuille, un dialogue s'ouvrira qui vous invitera à saisir le mot de passe afin que vous puissiez travailler sur la feuille de calcul comme indiqué ci-dessous:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Protéger quelques cellules dans la feuille de calcul à l'aide de Microsoft Excel**

Il peut y avoir certains scénarios où vous devez verrouiller uniquement quelques cellules dans la feuille. Si vous souhaitez verrouiller certaines cellules spécifiques, vous devez déverrouiller toutes les autres cellules. Toutes les cellules d'une feuille sont déjà initialisées pour le verrouillage ; vous pouvez le vérifier en ouvrant un fichier Excel dans MS Excel et en cliquant sur **Format | Cellules...** pour ouvrir la boîte de dialogue **Format Cells** et en cliquant sur l'onglet **Protection** pour voir si la case **Verrouillé** est cochée par défaut.

Les points suivants décrivent comment verrouiller quelques cellules en utilisant MS Excel. Cette méthode s'applique à Microsoft Office Excel 97, 2000, 2002, 2003, et les versions supérieures.

1. Sélectionnez l'ensemble de la feuille de calcul en cliquant sur le bouton **Sélectionner tout** (le rectangle gris directement au-dessus du numéro de ligne pour la ligne 1 et à gauche de la lettre de colonne A).
2. Cliquez sur **Cellules** dans le menu **Format**, cliquez sur l'onglet **Protection**, puis décochez la case **Verrouillé**.
   Cela déverrouille toutes les cellules de la feuille.
   Si la commande **Cellules** n'est pas disponible, certaines parties de la feuille de calcul peuvent déjà être verrouillées. Dans le menu **Outils**, pointez sur **Protection**, puis cliquez sur **Désactiver la protection de la feuille**.
3. Sélectionnez simplement les cellules que vous souhaitez verrouiller et répétez l'étape 2, mais cette fois cochez la case **Verrouillé**.
4. Dans le menu **Outils**, pointez sur **Protection**, cliquez sur **Protéger la feuille** puis sur **OK**.
5. Dans la boîte de dialogue **Protéger la feuille**, vous avez la possibilité de spécifier un mot de passe et de sélectionner les éléments que vous souhaitez permettre aux utilisateurs de modifier.

### **Protéger quelques cellules dans la feuille de calcul en utilisant Aspose.Cells**

Dans cette méthode, nous utilisons l'API Aspose.Cells uniquement pour effectuer la tâche.

Exemple : L'exemple suivant montre comment protéger quelques cellules dans la feuille de calcul. Il débloque d'abord toutes les cellules de la feuille, puis verrouille 3 cellules (A1, B1, C1). Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) sur true ou false et appliquer la méthode *Column/Row.applyStyle()* pour verrouiller ou déverrouiller la ligne/colonne avec vos attributs souhaités.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Protéger une ligne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle ligne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) de la classe [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row) pour appliquer [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) à une ligne spécifique de la feuille de calcul. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) qui possède tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une ligne dans la feuille de calcul. Il débloque d'abord toutes les cellules, puis verrouille la première ligne. Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) sur true ou false pour verrouiller ou déverrouiller la ligne/colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Protéger une colonne dans la feuille de calcul**

Aspose.Cells vous permet de verrouiller facilement n'importe quelle colonne dans la feuille de calcul. Ici, nous pouvons utiliser la méthode [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-) de la classe [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column) pour appliquer [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) à une colonne spécifique. Cette méthode prend deux arguments : un objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) et un objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) qui contient tous les membres liés à la mise en forme appliquée.

L'exemple suivant montre comment protéger une colonne dans la feuille de calcul. Il débloque toutes les cellules, puis verrouille la première colonne. Enfin, il protège la feuille. L'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) contient une propriété booléenne, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Vous pouvez définir la propriété [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) sur true ou false pour verrouiller ou déverrouiller la colonne en utilisant l'objet [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Autoriser les utilisateurs à modifier les plages**

L'exemple suivant montre comment autoriser les utilisateurs à modifier une plage dans une feuille de calcul protégée.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
