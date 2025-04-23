---
title: Obtenir des en têtes ou pieds de page avec Node.js via C++
linktitle: Obtenir les en têtes ou pieds de page
type: docs
weight: 30
url: /fr/nodejs-cpp/get-headers-or-footers/
description: Cet article explique comment obtenir de manière programmatique les en têtes et pieds de page des fichiers Excel ou OpenOffice en utilisant l’API ou la bibliothèque Node.js via C++.
---

{{% alert color="primary" %}}

Les en-têtes et pieds de page ne s'affichent qu'en mode Mise en page, Aperçu avant impression et sur les pages imprimées. 

Vous pouvez également utiliser la boîte de dialogue Mise en page si vous souhaitez afficher les en-têtes ou pieds de page pour plus d'une feuille de calcul à la fois. 

Pour d'autres types de feuilles, tels que les feuilles de graphique ou les graphiques, vous pouvez insérer des en-têtes et pieds de page uniquement en utilisant la boîte de dialogue Mise en page.

{{% /alert %}}

## **Obtenir des en-têtes et des pieds de page dans MS Excel**
1. Cliquez sur la feuille de calcul où vous souhaitez afficher ou modifier les en-têtes ou les pieds de page.
2. Dans l’onglet Affichage, dans le groupe Vues du classeur, cliquez sur Mise en page.
   Excel affiche la feuille de calcul en mode Mise en page.
3. Pour afficher ou modifier un en-tête ou un pied de page, cliquez sur la zone de texte de l'en-tête ou du pied de page de gauche, du centre ou de droite en haut ou en bas de la page de la feuille de calcul (sous En-tête ou au-dessus de Pied de page).


## **Obtention d’en-têtes et pieds de page avec Aspose.Cells for Node.js via C++**
Avec les méthodes [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) et [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-), les développeurs Node.js peuvent simplement obtenir les en-têtes ou pieds de page du fichier.

1. Construisez un classeur pour ouvrir le fichier.
2. Obtenez la feuille de calcul où vous souhaitez obtenir les en-têtes ou pied de page.
3. Obtenez l’en-tête ou le pied de page avec un ID de section spécifique.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **Analyser les en-têtes et les pieds de page en liste de commandes**
Le texte dans l'en-tête ou le pied de page peut contenir des commandes spéciales, par exemple un espace réservé pour le numéro de page, la date actuelle ou les attributs de mise en forme du texte.

Les commandes spéciales sont représentées par une seule lettre précédée d'un esperluette ("&").

Les chaînes d'en-tête et de pied de page sont construites en utilisant la grammaire ABNF. Il n'est pas facile de comprendre sans un visualiseur.

Aspose.Cells for Node.js via C++ fournit la méthode [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) pour analyser les en-têtes et pieds de page en tant que liste de commandes.

Les codes suivants montrent comment analyser l'en-tête ou le pied de page en tant que liste de commandes et traiter les commandes :

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
