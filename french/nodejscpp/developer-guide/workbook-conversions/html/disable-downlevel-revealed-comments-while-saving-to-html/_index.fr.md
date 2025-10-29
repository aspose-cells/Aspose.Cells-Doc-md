---
title: Désactiver les commentaires révélés en dessous lors de l enregistrement en HTML avec Node.js via C++
linktitle: Désactiver les commentaires révélés de niveau inférieur lors de l enregistrement en HTML
type: docs
weight: 20
url: /fr/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Apprenez comment désactiver les commentaires révélés en dessous lors de l enregistrement d un fichier Excel en HTML en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, Aspose.Cells révèle les commentaires conditionnels en dessous. Ces commentaires conditionnels concernent principalement les anciennes versions d'Internet Explorer et sont inutiles pour les navigateurs modernes. Vous pouvez en savoir plus à leur sujet via le lien suivant.

- [Commentaire conditionnel - Commentaire conditionnel révélé de niveau inférieur](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Node.js via C++ permet d'éliminer ces commentaires révélés en dessous en réglant la propriété [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--) sur **true**.

## **Désactiver les commentaires révélés de niveau inférieur lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.getDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getDisableDownlevelRevealedComments--). La capture d'écran montre l'effet de cette propriété lorsqu'elle n'est pas réglée sur true. Veuillez télécharger le [fichier Excel d'exemple](50528257.xlsx) utilisé dans ce code et le [HTML de sortie](50528258.zip) généré par celui-ci pour référence.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample workbook
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleDisableDownlevelRevealedComments.xlsx"));

// Disable DisableDownlevelRevealedComments
const opts = new AsposeCells.HtmlSaveOptions();
opts.setDisableDownlevelRevealedComments(true);

// Save the workbook in html
workbook.save(path.join(outputDir, "outputDisableDownlevelRevealedComments_true.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
