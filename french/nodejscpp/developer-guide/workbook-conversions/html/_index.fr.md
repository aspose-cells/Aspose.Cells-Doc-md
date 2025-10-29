---
title: HTML avec Node.js via C++
linktitle: HTML
type: docs
weight: 230
url: /fr/nodejs-cpp/convert-excel-to-html/
---

## **Conversion de Classeur Excel en HTML**
L’API Aspose.Cells offre un support pour l’exportation de feuilles de calcul au format HTML. À cette fin, Aspose.Cells utilise la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) pour offrir la flexibilité de contrôler plusieurs aspects du HTML de sortie.

L'exemple de code ci-dessous montre comment enregistrer un classeur en tant que fichier HTML avec Node.js :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **Conversion de Classeur Excel en Fichiers MHTML**
MHTML combine le HTML normal avec des ressources externes (c'est-à-dire le contenu généralement lié, comme les images, animations, audio, etc.) en un seul fichier. Il est utilisé pour les courriels avec l'extension de fichier .mht. Aspose.Cells prend en charge la lecture et l'écriture des fichiers MHTML.

L'exemple de code ci-dessous montre comment enregistrer un classeur en tant que fichier MHTML avec Node.js :

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **Sujets avancés**
- [Ajuster automatiquement les colonnes et les lignes lors du chargement du HTML dans le classeur](/cells/fr/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Évitez la notation exponentielle des grands nombres lors de l'importation depuis HTML](/cells/fr/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Changer le type de cible de lien HTML](/cells/fr/nodejs-cpp/change-the-html-link-target-type/)
- [Convertir Excel en HTML avec info-bulle](/cells/fr/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/fr/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Supprimer les espaces redondants après un saut de ligne lors de l'importation d'HTML](/cells/fr/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML](/cells/fr/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Désactiver l'exportation des scripts de trame et des propriétés de document](/cells/fr/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel vers HTML - Utiliser l'option PresentationPreference pour une meilleure mise en page](/cells/fr/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Exclure les styles inutilisés lors de la conversion d'Excel en HTML](/cells/fr/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expansion du texte de droite à gauche lors de l'exportation d'un fichier Excel vers HTML](/cells/fr/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exporter les formatages conditionnels DataBar, ColorScale et IconSet lors de la conversion d'Excel en HTML](/cells/fr/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exporter les commentaires lors de l'enregistrement d'un fichier Excel en HTML](/cells/fr/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Exporter les propriétés du classeur de document et de la feuille de calcul lors de la conversion d'Excel en HTML](/cells/fr/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exporter Excel au format HTML avec des lignes de grille](/cells/fr/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Exporter la plage de la zone d'impression en HTML](/cells/fr/nodejs-cpp/export-print-area-range-to/)
- [Exporter un style de bordure similaire lorsque le style de bordure n'est pas pris en charge par les navigateurs Web](/cells/fr/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exporter la feuille de calcul CSS séparément dans le HTML de sortie](/cells/fr/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Masquer le contenu superposé avec CrossHideRight lors de l'enregistrement au format HTML](/cells/fr/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Préfixer les styles des éléments de table avec la propriété HtmlSaveOptions.TableCssId](/cells/fr/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Empêcher l'exportation du contenu masqué de la feuille de calcul lors de l'enregistrement au format HTML](/cells/fr/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Fournir le chemin du fichier html de la feuille exportée via l'interface IFilePathProvider](/cells/fr/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Reconnaître les balises auto-fermantes](/cells/fr/nodejs-cpp/recognise-self-closing-tags/)
- [Rendre le remplissage dégradé pour WordArt lors de la conversion des feuilles de calcul en HTML](/cells/fr/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Définir la largeur de colonne sur une unité extensible comme em ou pourcentage](/cells/fr/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Définir la police par défaut lors du rendu de la feuille de calcul en HTML](/cells/fr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Spécifier comment croiser la chaîne dans le HTML de sortie en utilisant HtmlCrossType](/cells/fr/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Prise en charge de la mise en page des balises DIV lors du chargement d'HTML dans le classeur Excel](/cells/fr/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML](/cells/fr/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
