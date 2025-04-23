---  
title: Sauvegarder le classeur au format Excel Open XML strict avec Node.js via C++  
linktitle: Enregistrer le classeur au format de feuille de calcul strict Open XML  
type: docs  
weight: 150  
url: /fr/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/  
description: Apprenez comment sauvegarder un classeur au format Excel Open XML strict en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells for Node.js via C++ vous permet de sauvegarder le classeur au format *Strict Open XML Spreadsheet*. À cette fin, il fournit la propriété [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--). Si vous définissez sa valeur à [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), le fichier Excel de sortie sera sauvegardé au format Strict Open XML Spreadsheet.  

## **Enregistrer le classeur au format strict Open XML Spreadsheet**  

Le code d'exemple suivant crée un classeur et définit la valeur de la propriété [**WorkbookSettings.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getCompliance--) à [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/nodejs-cpp/ooxmlcompliance), puis l'enregistre en tant que [fichier Excel de sortie](67338272.xlsx). Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue Enregistrer sous..., vous verrez son format comme *Strict Open XML Spreadsheet* comme indiqué dans cette capture d'écran.  

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook.
const wb = new AsposeCells.Workbook();

// Specify - Strict Open XML Spreadsheet - Format.
wb.getSettings().setCompliance(AsposeCells.OoxmlCompliance.Iso29500_2008_Strict);

// Add message in cell B4 of first worksheet.
const b4 = wb.getWorksheets().get(0).getCells().get("B4");
b4.putValue("This Excel file has Strict Open XML Spreadsheet format.");

// Save to output Excel file.
wb.save("outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

