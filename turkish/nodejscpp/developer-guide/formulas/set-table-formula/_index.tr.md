---
title: Yeni satırlara veri girerken, formüllerde otomatik olarak tablo veya liste nesnesinde formüllerdeki formülleri yaymak
linktitle: Tablo Formülünü Ayarlar
type: docs
weight: 260
url: /tr/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Yeni satırlarda veri girerken tablolar veya liste nesnelerinde otomatik olarak formüller yayılmasını öğrenin Aspose.Cells for Node.js via C++ kullanarak.
---

## **Olası Kullanım Senaryoları**
Bazen, Tablo veya Liste Nesnesindeki formülünüzün yeni veri girerken otomatik olarak yeni satırlara yayılmasını istersiniz. Bu, Microsoft Excel'in varsayılan davranışıdır. Aynı işlevselliği Aspose.Cells for Node.js via C++ ile sağlamak için lütfen [ListColumn.getFormula()](https://reference.aspose.com/cells/nodejs-cpp/listcolumn/#getFormula--) özelliğini kullanın.

## **Formülü Otomatik Yayma - Yeni Satırlara Veri Girerken Tablo veya Liste Nesnesinde Otomatik Yayılım**
Aşağıdaki örnek kod, B sütunundaki formülün yeni veriler girildiğinde otomatik olarak yeni satırlara yayılacak şekilde bir Tablo veya Liste Nesnesi oluşturur. Bu kodla üretilen [çıktı excel dosyasını](5115469.xlsx) kontrol edin. A3 hücresine herhangi bir sayı girerseniz, B2 hücresindeki formülün otomatik olarak B3 hücresine yayıldığını göreceksiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const book = new AsposeCells.Workbook();

// Access first worksheet
const sheet = book.getWorksheets().get(0);

// Add column headings in cell A1 and B1
sheet.getCells().get(0, 0).putValue("Column A");
sheet.getCells().get(0, 1).putValue("Column B");

// Add list object, set its name and style
const listObject = sheet.getListObjects().get(sheet.getListObjects().add(0, 0, 1, sheet.getCells().getMaxColumn(), true));
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium2);
listObject.setDisplayName("Table");

// Set the formula of second column so that it propagates to new rows automatically while entering data
listObject.getListColumns().get(1).setFormula("=[Column A] + 1");

// Save the workbook in xlsx format
book.save(path.join(dataDir, "output_out.xlsx"));
```
