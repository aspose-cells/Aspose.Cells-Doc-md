---
title: Node.js ile C++ kullanarak çalışma sayfasını görüntüye dönüştürürken varsayılan yazı tipini ayarlama
linktitle: Yaygın Olarak Kullanılan Yazı tipini Resimlere Dönüştürürken Belirleme
type: docs
weight: 360
url: /tr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma sayfalarını görüntüye dönüştürürken varsayılan yazı tipini nasıl ayarlayacağınızı öğrenin. 
---

{{% alert color="primary" %}}

Yayımlama sırasında elektronik tabloları görüntü olarak oluşturmak için [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliğini kullanın. Bu özellik, elektronik tablonun varsayılan yazı tipi karakterlerinizi oluşturamadığında yalnızca etkilidir. [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliği ile belirtilen varsayılan yazı tipi, geçersiz veya var olmayan yazı tiplerine sahip tüm hücreler için kullanılır.

{{% /alert %}}

## Yayımlama Sırasında Varsayılan Yazı Tipini Ayarlayın

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, ilk çalışma sayfasındaki A4 hücresine bazı metinler ekler ve yazı tipini geçersiz veya olmayan bir yazı tipine ayarlar. Sonra, çalışma sayfasının iki görselini alır. Birinci görsel, [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliğini *Courier New* olarak ayarlayarak alınır, ikinci görsel ise [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliğini *Times New Roman* yaparak alınır.

Bu, [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliği *Courier New* olarak ayarlandıktan sonra çıkan görseldir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Bu, [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliği *Times New Roman* olarak ayarlandıktan sonra çıkan görseldir.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Örnek Kod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
