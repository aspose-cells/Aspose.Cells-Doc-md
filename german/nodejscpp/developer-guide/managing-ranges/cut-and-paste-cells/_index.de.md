---  
title: Bereich schneiden und mit Node.js über C++ einfügen  
linktitle: Bereich ausschneiden und einfügen  
type: docs  
weight: 130  
url: /de/nodejs-cpp/cut-and-paste-cells/  
description: Erfahren Sie, wie man Zellen innerhalb eines Arbeitsblatts mit Aspose.Cells for Node.js via C++ schneidet und einfügt.  
---  

## **Zellen ausschneiden und einfügen**  

Aspose.Cells for Node.js via C++ bietet die Möglichkeit, Zellen innerhalb eines Arbeitsblatts mit der Methode [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) der Sammlung [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/) zu schneiden und einzufügen. Der [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) akzeptiert die folgenden Parameter.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): Der Bereich von Zellen, die ausgeschnitten werden sollen.  
- Zeilenindex: Der Index der Zeile zum Einfügen von Zellen.  
- Spaltenindex: Der Index der Spalte zum Einfügen von Zellen.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): Die Verschiebungsrichtung der Spalten.  

Das folgende Beispiel zeigt, wie man Zellen innerhalb eines Arbeitsblatts ausschneiden und einfügen kann.  

## **Beispielcode**  

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
