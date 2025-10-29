---  
title: Spécifier le nombre significatif de chiffres à stocker dans un fichier Excel avec Node.js via C++  
linktitle: Spécification des chiffres significatifs à stocker dans le fichier Excel  
type: docs  
weight: 30  
url: /fr/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Apprenez à spécifier le nombre de chiffres significatifs à stocker dans un fichier Excel en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Par défaut, Aspose.Cells for Node.js via C++ stocke 17 chiffres significatifs des valeurs double dans le fichier Excel, contrairement à MS-Excel qui ne stocke que 15 chiffres significatifs. Vous pouvez modifier le comportement par défaut de Aspose.Cells de 17 chiffres significatifs à 15 chiffres significatifs en utilisant la propriété [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**  

Le code suivant force Aspose.Cells à utiliser 15 chiffres significatifs lors de la stockage des valeurs double dans le fichier Excel. Veuillez vérifier le [fichier Excel de sortie](22774105.xlsx). Changez son extension en .zip, dézippez-le et vous verrez que seuls 15 chiffres significatifs sont stockés dans le fichier Excel. La capture d'écran suivante illustre l'effet de la propriété [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) sur le fichier Excel de sortie.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
