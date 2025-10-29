---
title: Configuration des propriétés ScaleCrop et LinksUpToDate des propriétés intégrées du document avec Node.js via C++
linktitle: Définir les propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.
type: docs
weight: 320
url: /fr/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Apprenez à définir les propriétés ScaleCrop et LinksUpToDate des propriétés intégrées du document en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**
[BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) et [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) sont deux propriétés intégrées étendues définies dans le format OpenXml. Leur objectif est le suivant.

## **1) ScaleCrop**
Cet élément indique le mode d'affichage de la vignette du document. Définissez cet élément sur **TRUE** pour activer le redimensionnement de la vignette du document à l'affichage. Définissez cet élément sur **FALSE** pour activer le rognage de la vignette du document afin de montrer uniquement les sections qui s'adaptent à l'affichage.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **2) LinksUpToDate**
Cet élément indique si les hyperliens dans un document sont à jour. Définissez cet élément sur **TRUE** pour indiquer que les hyperliens sont mis à jour. Définissez cet élément sur **FALSE** pour indiquer que les hyperliens sont obsolètes.

Les valeurs possibles pour cet élément sont définies par le type de données booléen du schéma XML W3C.

## **Capture d'écran montrant ces propriétés dans le fichier app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Définition des propriétés ScaleCrop et LinksUpToDate des propriétés de document intégrées.**
Le code d'exemple suivant définit les propriétés intégrées étendues [BuiltInDocumentPropertyCollection.getScaleCrop()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getScaleCrop--) et [BuiltInDocumentPropertyCollection.getLinksUpToDate()](https://reference.aspose.com/cells/nodejs-cpp/builtindocumentpropertycollection/#getLinksUpToDate--) du classeur. Veuillez vérifier le fichier excel de sortie généré avec ce code, changer son extension en .zip, extraire son contenu et consulter app.xml comme montré dans la capture d'écran ci-dessus.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object.
const workbook = new AsposeCells.Workbook();

// Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
workbook.getBuiltInDocumentProperties().getScaleCrop(true);
workbook.getBuiltInDocumentProperties().setLinksUpToDate(true);

// Saving the Excel file.
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Auto);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
