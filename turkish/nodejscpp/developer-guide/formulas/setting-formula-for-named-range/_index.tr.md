---
title: Node.js ile C++ kullanarak Tanımlı Aralık için Formül Ayarlama
linktitle: Adlandırılmış Aralık için Formül Ayarlama
type: docs
weight: 20
url: /tr/nodejs-cpp/setting-formula-for-named-range/
description: Aspose.Cells for Node.js via C++ kullanarak elektronik tablolar için tanımlı aralıklara formüller ayarlamayı öğrenin.
---

## **Adlandırılmış Aralık için Formül Ayarlama**
Excel uygulaması gibi, Aspose.Cells API'leri de [Range.getRefersTo()](https://reference.aspose.com/cells/nodejs-cpp/range/#getRefersTo--) özelliği kullanılırken bir tanımlı aralık için formül belirleme imkanı sağlar. Bu özellik için birçok kullanılabilirlik senaryosu olabilir, bunlardan bazıları aşağıda detaylandırılmıştır.

### **Basit Formül Ayarlama Adlandırılmış Aralık için**
Basit bir formül, aynı (veya farklı) çalışma sayfasındaki başka bir hücreye bir referans olabilir. Aşağıdaki örnek, yeni bir elektronik tablo oluşturur ve referansını başka bir hücreye ayarlar.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "NewNamedRange"
const index = worksheets.getNames().add("NewNamedRange");

// Access the newly created Named Range
const name = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
name.setRefersTo("=Sheet1!$A$3");

// Set the formula in the cell A1 to the newly created Named Range
worksheets.get(0).getCells().get("A1").setFormula("NewNamedRange");

// Insert the value in cell A3 which is being referenced in the Named Range
worksheets.get(0).getCells().get("A3").putValue("This is the value of A3");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```

### **Karmaşık Formül Ayarlama Adlandırılmış Aralık için**
Karmaşık bir formül, bir dinamik aralık veya farklı çalışma sayfalarındaki birden çok hücreye yayılan bir formül olabilir. Aşağıdaki örnek, bir değerin konumuna bağlı olarak INDEX işlevini kullanarak dinamik bir aralık oluşturur.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Add a new Named Range with name "data"
let index = worksheets.getNames().getCount();
worksheets.getNames().add("data");

// Access the newly created Named Range from the collection
const data = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a cell range in same worksheet
data.setRefersTo("=Sheet1!$A$1:$A$10");

// Add another Named Range with name "range"
index = worksheets.getNames().getCount();
worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property to a formula using the Named Range data
range.setRefersTo("=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

// Save the workbook
book.save(path.join(dataDir, "output_out.xlsx"));
```

Aşağıda, farklı çalışma sayfalarındaki 2 hücreden değerleri toplamak için adlandırılmış bir aralık kullanan başka bir örnek bulunmaktadır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook
const book = new AsposeCells.Workbook();

// Get the WorksheetCollection
const worksheets = book.getWorksheets();

// Insert some data in cell A1 of Sheet1
worksheets.get("Sheet1").getCells().get("A1").putValue(10);

// Add a new Worksheet and insert a value to cell A1
worksheets.get(worksheets.add()).getCells().get("A1").putValue(10);

// Add a new Named Range with name "range"
const index = worksheets.getNames().add("range");

// Access the newly created Named Range from the collection
const range = worksheets.getNames().get(index);

// Set RefersTo property of the Named Range to a SUM function
range.setRefersTo("=SUM(Sheet1!$A$1,Sheet2!$A$1)");

// Insert the Named Range as formula to 3rd worksheet
worksheets.get(worksheets.add()).getCells().get("A1").setFormula("range");

// Calculate formulas
book.calculateFormula();

// Save the result in XLSX format
book.save(path.join(dataDir, "output_out.xlsx"));
```
