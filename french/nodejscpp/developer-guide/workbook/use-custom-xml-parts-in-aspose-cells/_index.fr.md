---
title: Utilisez les parties XML personnalisées dans Aspose.Cells avec Node.js via C++
linktitle: Utilisez des parties XML personnalisées dans Aspose.Cells
type: docs
weight: 390
url: /fr/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Apprenez comment utiliser les parties XML personnalisées dans Aspose.Cells for Node.js via C++. Intégrez des données XML externes dans les fichiers Excel sans problème.
--- 

## Utilisation de parties XML personnalisées dans Aspose.Cells

Les parties XML personnalisées sont les données XML stockées par différentes applications comme SharePoint, etc. à l'intérieur du fichier Excel. Ces données sont utilisées par différentes applications qui en ont besoin. Microsoft Excel n'utilise pas ces données, il n'y a donc pas d'interface graphique pour les ajouter. Vous pouvez visualiser ces données en changeant l’extension de **.xlsx** à **.zip** puis en l’ouvrant avec **WinZip**. Vous pouvez également ouvrir le fichier ZIP avec n'importe quel utilitaire de compression Windows tiers tel que WinRAR ou WinZip. Les données se trouvent dans le dossier **customXml**.

Vous pouvez ajouter des parties XML personnalisées en utilisant Aspose.Cells via la méthode [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/).

Le code d'exemple ci-dessous utilise la méthode [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) et ajoute le **Book Catalog XML** dont le nom est **BookStore**. L'image suivante montre le résultat de ce code. Comme vous pouvez le voir, le Book Catalog XML est ajouté dans le nœud BookStore, qui est le nom de cette propriété.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Code Node.js pour utiliser les parties XML personnalisées

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## Article connexe

- [Ajout de propriétés personnalisées visibles dans le volet Informations sur le document](/cells/fr/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
