---
title: Définir en têtes et pieds de page avec Node.js via C++
linktitle: Définir des en têtes et des pieds de page
type: docs
weight: 30
url: /fr/nodejs-cpp/setting-headers-and-footers/
description: Cet article explique comment insérer automatiquement une image dans l en tête et le pied de page des feuilles Excel en utilisant Aspose.Cells for Node.js via C++. 
keywords: insérer une image dans l en tête et le pied de page d Excel via Node.js avec C++, exécuter des commandes de script pour l en tête et le pied de page dans Node.js avec C++
---

{{% alert color="primary" %}}

Les en-têtes et les pieds de page sont les lignes de texte affichées en dessous de la marge supérieure ou au-dessus de la marge inférieure respectivement. Il est possible d'ajouter des en-têtes et des pieds de page aux feuilles de calcul également. Les en-têtes et les pieds de page peuvent être utilisés pour afficher des informations utiles comme le numéro de page, le nom de l'auteur, le nom du sujet ou la date et l'heure. Les en-têtes et les pieds de page sont gérés à l'aide des paramètres de configuration de la page.

{{% /alert %}}

## **Définition des en-têtes et des pieds de page**

Aspose.Cells for Node.js via C++ permet d'ajouter des en-têtes et pieds de page aux feuilles de calcul en temps réel, mais nous recommandons de définir manuellement ces éléments dans un fichier préconçu pour l'impression. Vous pouvez utiliser Microsoft Excel comme outil GUI pour définir les en-têtes et pieds de page afin d'économiser du temps et des efforts de développement. Aspose.Cells peut importer le fichier et enregistrer ces paramètres.

Pour ajouter des en-têtes et des pieds de page à l'exécution, Aspose.Cells fournit des appels d'API spéciaux et des commandes de script pour formater les en-têtes et les pieds de page.

### **Commandes de script**

Les commandes de script sont des commandes spéciales qui vous permettent de définir le formatage des en-têtes et des pieds de page.

|**Commandes de script**|**Description**|
| :- | :- |
|&P| Le numéro de la page actuelle
|&G| Une image
|&N| Le nombre total de pages
|&D| La date actuelle
|&T| L'heure actuelle
|&A| Le nom de la feuille de calcul
|&F| Le nom du fichier sans son chemin d'accès
|&&Text|Montre &Text. Par exemple : &&WO sera affiché comme &WO|
|&"\<FontName>"| Représente un nom de police. Par exemple : &"Arial"
|&"\<FontName>, \<FontStyle>"| Représente un nom de police avec un style. Par exemple : &"Arial, Gras"
|&\<FontSize>| Représente la taille de la police. Par exemple : "&14abc". Mais, si cette commande est suivie d'un nombre ordinaire à imprimer dans l'en-tête, cela doit être séparé d'un caractère d'espace de la taille de la police. Par exemple : "&14 123".

### **Définir les en-têtes et les pieds de page**

La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) fournit deux méthodes, [**setHeader(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeader-number-string-) et [**setFooter(number, string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooter-number-string-), utilisées pour ajouter un en-tête et un pied de page à une feuille de calcul. Ces méthodes prennent uniquement deux paramètres :

- **Section** – la section où l'en-tête ou le pied de page doit être placé. Il existe trois sections : gauche, centre et droite, représentées respectivement par 0, 1 et 2.
- **Script** – le script à utiliser pour l'en-tête ou le pied de page. Ce script contient des commandes de script pour formater les en-têtes ou les pieds de page.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const excel = new AsposeCells.Workbook();

// Obtaining the reference of the PageSetup of the worksheet
const pageSetup = excel.getWorksheets().get(0).getPageSetup();

// Setting worksheet name at the left section of the header
pageSetup.setHeader(0, "&A");

// Setting current date and current time at the central section of the header
// and changing the font of the header
pageSetup.setHeader(1, "&\"Times New Roman,Bold\"&D-&T");

// Setting current file name at the right section of the header and changing the
// font of the header
pageSetup.setHeader(2, "&\"Times New Roman,Bold\"&12&F");

// Setting a string at the left section of the footer and changing the font
// of a part of this string ("123")
pageSetup.setFooter(0, "Hello World! &\"Courier New\"&14 123");

// Setting the current page number at the central section of the footer
pageSetup.setFooter(1, "&P");

// Setting page count at the right section of footer
pageSetup.setFooter(2, "&N");

// Save the Workbook.
excel.save("SetHeadersAndFooters_out.xls");
```

### **Insérer une image dans un en-tête ou un pied de page**

 La classe [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup) possède deux méthodes supplémentaires, [**setHeaderPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setHeaderPicture-number-numberarray-) et [**setFooterPicture(number, number[])**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#setFooterPicture-number-numberarray-), utilisées pour ajouter des images dans l'en-tête et le pied de page. Ces méthodes prennent comme paramètres :

- **Section** – la section d'en-tête ou de pied de page où l'image sera placée. Il existe trois sections, left, center et right, représentées respectivement par les valeurs 0, 1 et 2.
- **Tableau de bytes** – les données graphiques (les données binaires doivent être écrites dans le buffer d'un tableau de bytes).

Après l'exécution du code ci-dessous et l'ouverture du fichier, vérifiez l'en-tête de la feuille de calcul en :

1. Dans le menu **Fichier**, sélectionnez **Mise en page**. Une boîte de dialogue s'affichera.
1. Sélectionnez l'onglet **En-tête/Pied de page**.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a Workbook object
const workbook = new AsposeCells.Workbook();

// Creating a string variable to store the url of the logo/picture
const logoUrl = path.join(dataDir, "aspose-logo.jpg");

// Declaring a byte array
const binaryData = fs.readFileSync(logoUrl);

// Creating a PageSetup object to get the page settings of the first worksheet of the workbook
const pageSetup = workbook.getWorksheets().get(0).getPageSetup();

// Setting the logo/picture in the central section of the page header
pageSetup.setHeaderPicture(1, binaryData);

// Setting the script for the logo/picture
pageSetup.setHeader(1, "&G");

// Setting the Sheet's name in the right section of the page header with the script
pageSetup.setHeader(2, "&A");

// Saving the workbook
workbook.save(path.join(dataDir, "InsertImageInHeaderFooter_out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
