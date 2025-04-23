---  
title: Convertir un fichier Excel en format PDF compatible avec PDF/A 1a avec Node.js via C++  
linktitle: Convertir un fichier Excel en format PDF compatible avec PDF/A 1a  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Apprenez comment convertir des fichiers Excel en fichiers PDF conformes à PDF/A en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

 PDF/A est une version spécifique du PDF conçue pour la conservation à long terme des documents. PDF/A est une version standardisée ISO du format Portable Document Format (PDF) qui est un format d'archivage du PDF intégrant toutes les polices utilisées dans le document dans le fichier PDF. PDF/A diffère du PDF en interdisant des fonctionnalités telles que le lien de police (opposé à l'intégration de police) et le chiffrement. Aspose.Cells for Node.js via C++ permet de sauvegarder les fichiers Excel en fichiers PDF conformes à PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab et PDF/A-3u sont supportés). Ce sujet décrit comment sauvegarder le classeur Excel en fichier PDF conforme à PDF/A (PDF/A-1a).  

## **Convertir le fichier Excel au format PDF Compatible avec PDF/A-1a**  

Les développeurs peuvent utiliser la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) pour définir différents attributs pour la conversion. La définition de différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) vous donne le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le PDF de sortie. La propriété la plus importante est [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) qui vous permet d'enregistrer les fichiers Excel au format PDF/A conforme.  

 Le code d'exemple suivant explique comment convertir un fichier Excel en format PDF compatible avec PDF/A-1a. Veuillez voir le [PDF de sortie](outputCompliancePdfA1a.pdf) ainsi que la capture d'écran pour référence.  

## **Capture d'écran**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

