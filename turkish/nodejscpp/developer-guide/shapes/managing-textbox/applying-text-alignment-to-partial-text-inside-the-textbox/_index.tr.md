---
title: Metin hizalamasını Textbox a nasıl uygularsınız/ayarlarsınız Node.js ile C++ kullanarak
linktitle: Metin hizalamasını metin kutusuna uygulama/ayarlama
type: docs
weight: 20
url: /tr/nodejs-cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Aspose.Cells for Node.js via C++ kullanarak Textbox a metin hizalamasını nasıl uygularsınız/ayarlarsınız.
keywords: metin hizalamasını uygula/ayarla TextBox Worksheet Excel Aspose Node.js ile C++ kullanarak
---

TextBox'lar, belgelerimizin ve diyagramlarımızın anlatım gücünü artırabilir ve farklı bölümlere farklı hizalamalar uygulamak, okuyucuların dikkatini çekmeye yardımcı olabilir. Ancak, TextBox'un varsayılan hizalaması tüm ihtiyaçlarımıza uymayabilir. Bunun için, her TextBox'u hedef gereksinimlerinizi karşılayacak şekilde ayarlamanız gerekebilir. Çok sayıda TextBox nesnesi ayarlayacaksanız, şanslısınız. Eğer çok sayıda TextBox ayarlamak zorundaysanız, sorun yaşayabilirsiniz. Endişelenmeyin, [Aspose.Cells](https://products.aspose.com/cells/) böyle bir API arayüzü sunar ve işinizi görür.

Aşağıdaki örnek kod bir metin kutusuna metin hizalaması uygular.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();
const shapes = workbook.getWorksheets().get(0).getShapes();

// add a TextBox
const shape = shapes.addTextBox(2, 0, 2, 0, 50, 120);
shape.setText("This is a test.");

// set alignment
shape.setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
shape.setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Save the excel file.
workbook.save(path.join(dataDir, "result.xlsx"));
```

Bir TextBox şeklinin içindeki bazı metinlerin metin hizalamasını uygun HTML metni ile değiştirebilirsiniz. Aşağıdaki örnek kod, TextBox içindeki kısmi metne hizalama uygular.

[kaynak dosyası](SampleTextboxExcel2016.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "SampleTextboxExcel2016.xlsx");

// Initialize an object of the Workbook class to load the template file
const sourceWb = new AsposeCells.Workbook(sourceFilePath);

// Access the target textbox whose text is to be aligned
const sourceTextBox = sourceWb.getWorksheets().get(0).getShapes().get(0);

// Create an object of the target workbook
const destWb = new AsposeCells.Workbook();

// Access the first worksheet from the collection
const _sheet = destWb.getWorksheets().get(0);

// Create new textbox
const _textBox = _sheet.getShapes().addShape(AsposeCells.MsoDrawingType.TextBox, 1, 0, 1, 0, 200, 200);

// Alternatively text box can be added using the following line as well
// const _textBox = _sheet.getShapes().addTextBox(1, 0, 1, 0, 200, 200);

// Use Html string from a template file textbox
_textBox.setHtmlText(sourceTextBox.getHtmlText());

// Save the workbook on disk
destWb.save("Output.xlsx");
```
