---
title: Modifier la police uniquement pour certains caractères Unicode lors de la sauvegarde en PDF avec Node.js via C++
linktitle: Modifier la police uniquement des caractères Unicode spécifiques lors de l enregistrement en PDF
type: docs
weight: 260
url: /fr/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Apprenez comment changer la police de certains caractères Unicode lors de la sauvegarde en PDF en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Certains caractères Unicode ne sont pas affichables par la police spécifiée par l'utilisateur. Un de ces caractères Unicode est **Non-breaking Hyphen** (U+2011) et son numéro Unicode est 8209. Ce caractère ne peut pas être affiché avec **Times New Roman**, mais il peut être affiché avec d'autres polices comme **Arial Unicode MS**.

 Lorsqu'un tel caractère apparaît à l'intérieur d'un mot ou d'une phrase en police spécifique comme Times New Roman, Aspose.Cells change la police de tout le mot ou de la phrase en une police pouvant afficher ce caractère, comme Arial Unicode ou MS.

 Cependant, ce comportement est indésirable pour certains utilisateurs qui souhaitent uniquement que la police de ce caractère spécifique soit modifiée plutôt que toute la phrase ou le mot.

 Pour traiter ce problème, Aspose.Cells fournit la propriété `PdfSaveOptions.isFontSubstitutionCharGranularity` qui doit être définie sur vrai afin que seule la police des caractères non affichables soit modifiée pour une police affichable, tandis que le reste du mot ou de la phrase reste dans la police d'origine.

{{% /alert %}} 

## **Exemple**
La capture d'écran suivante compare les deux fichiers PDF générés par le code d'exemple ci-dessous.

 L'un est généré sans définir la propriété `PdfSaveOptions.isFontSubstitutionCharGranularity` et l'autre après avoir défini cette propriété sur vrai.

 Comme vous pouvez le voir dans le premier PDF, la police de la phrase entière a changé de Times New Roman à Arial Unicode MS à cause du tiret non sécable. Dans le second PDF, seule la police du tiret non sécable a changé.

|**Premier fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Deuxième fichier PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Code d'exemple**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



{{< app/cells/assistant language="nodejs-cpp" >}}
