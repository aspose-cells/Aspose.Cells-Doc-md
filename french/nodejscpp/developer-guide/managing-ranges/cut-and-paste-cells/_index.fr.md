---  
title: Couper et coller une plage avec Node.js via C++  
linktitle: Couper et coller la plage  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/cut-and-paste-cells/  
description: Apprenez comment couper et coller des cellules dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Couper et coller des cellules**  

Aspose.Cells for Node.js via C++ vous permet de couper et coller des cellules dans une feuille de calcul en utilisant la méthode [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) de la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/). La méthode [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) accepte les paramètres suivants.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/) : La plage de cellules à couper.  
- Index de ligne : L'index de la ligne pour insérer les cellules.  
- Index de colonne : L'index de la colonne pour insèrer les cellules.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/) : La direction du décalage des colonnes.  

L'exemple suivant montre comment couper et coller des cellules dans une feuille de calcul.  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 2).setValue(1);
worksheet.getCells().get(1, 2).setValue(2);
worksheet.getCells().get(2, 2).setValue(3);
worksheet.getCells().get(2, 3).setValue(4);
worksheet.getCells().createRange(0, 2, 3, 1).setName("NamedRange");

const cut = worksheet.getCells().createRange("C:C");
worksheet.getCells().insertCutCells(cut, 0, 1, AsposeCells.ShiftType.Right);
workbook.save(path.join(outDir, "CutAndPasteCells.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
