---  
title: Kırp ve Yapıştır Aralığı Node.js ile C++ kullanarak  
linktitle: Aralığı Kırparak ve Yapıştırarak  
type: docs  
weight: 130  
url: /tr/nodejs-cpp/cut-and-paste-cells/  
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma sayfası içinde hücreleri kesip yapıştırmayı nasıl yapacağınızı öğrenin.  
---  

## **Hücreleri Kırp ve Yapıştır**  

Aspose.Cells for Node.js via C++, [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) yöntemi ve [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/) koleksiyonu metodu kullanılarak hücreleri kesip yapıştırma özelliği sağlar. [**InsertCutCells**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertCutCells-Range-number-number-ShiftType-) aşağıdaki parametreleri kabul eder.  

- [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/): Kesilecek hücrelerin aralığı.  
- Satır Dizini: Hücreleri eklemek için satırın dizini.  
- Sütun Dizini: Hücreleri eklemek için sütunun dizini.  
- [**ShiftType**](https://reference.aspose.com/cells/nodejs-cpp/shifttype/): Sütunların kaydırma yönü.  

Aşağıdaki örnek, çalışma sayfası üzerinde hücreleri kesip yapıştırmayı gösterir.  

## **Örnek Kod**  

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

