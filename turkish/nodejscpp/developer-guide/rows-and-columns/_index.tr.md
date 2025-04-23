---  
title: Node.js ve C++ aracılığıyla Satır ve Sütunları Biçimlendirin  
linktitle: Satır ve Sütunlar  
type: docs  
weight: 100  
url: /tr/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++, satır yüksekliği veya sütun genişliği değiştirmenin yanı sıra, satırlar veya sütunlar üzerinde biçimlendirme uygulamayı destekler.  
keywords: Satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliği ve sütun genişliği ayarlı, satır yüksekliğini veya sütun genişliğini değiştirme, satır ve sütunları biçimlendirme, satır yüksekliği ve sütun genişliği ayarlama hakkında bilgi.  
---  

{{% alert color="primary" %}}  
Tablolar ve sütunlar ile çalışırken, satırların yüksekliğini veya sütunların genişliğini değiştirmek gerekebilir. Bazen, satır veya sütun üzerinde biçimlendirme uygulamak, verileri göstermek için mevcut yüksekliği veya genişliği değiştirmeyi gerektirir. Normalde kullanıcılar, Microsoft Excel kullanarak satır yüksekliği ve sütun genişliklerini WYSIWYG ortamında ayarlar. Ancak, Aspose.Cells ile geliştiriciler bu işlemleri çalışma zamanında gerçekleştirebilir.  
{{% /alert %}}  

## **Satırlarla Çalışmak**  

### **Satır Yüksekliğini Ayarlamak**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) adlı bir özelliğe sahiptir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu sağlar.  

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu, bir çalışma sayfasında satır veya sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda daha ayrıntılı olarak tartışılmıştır.  

### **Bir Satırın Yüksekliğini Ayarlama**  

Yalnızca bir satırın yüksekliğini [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) yöntemi çağrılarak ayarlamak mümkündür. [**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Satır dizini**, yüksekliği değiştirdiğiniz satırın dizini.  
- **Satır yüksekliği**, satıra uygulanan satır yüksekliği.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **Bir Çalışma Sayfasındaki Tüm Satırların Yüksekliğini Ayarlama**  

Eğer geliştiriciler, çalışma sayfasındaki tüm satırlar için aynı satır yüksekliğini ayarlamak isterse, bunu [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--) özelliğini kullanarak yapabilirler.  

**Örnek:**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **Sütunlarla Çalışmak**  

### **Bir Sütunun Genişliğini Ayarlama**  

Bir sütunun genişliğini [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) yöntemi çağrılarak ayarlayın. [**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-) yöntemi aşağıdaki parametreleri alır:  

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.  
- **Sütun genişliği**, istenen sütun genişliği.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **Piksel cinsinden Sütun Genişliğini Ayarlama**  

Bir sütunun genişliğini [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) yöntemi çağrılarak ayarlayın. [**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-) yöntemi aşağıdaki parametreleri alır:  

- **Sütun dizini**, genişliği değiştirdiğiniz sütunun dizini.  
- **Sütun genişliği**, pikseller cinsinden istenen sütun genişliği.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **Bir Çalışma Sayfasındaki Tüm Sütunların Genişliğini Ayarlama**  

Tüm sütunlar için aynı sütun genişliğini ayarlamak için, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--) özelliğini kullanın.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **Gelişmiş Konular**  
- [Satır ve Sütunları Otomatik Sığdır](/cells/tr/nodejs-cpp/autofit-rows-and-columns/)  
- [Aspose.Cells Kullanarak Metni Sütunlara Dönüştürme](/cells/tr/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [Satırları ve Sütunları Kopyalama](/cells/tr/nodejs-cpp/copying-rows-and-columns/)  
- [Çalışma Sayfasındaki Boş Satırları ve Sütunları Silme](/cells/tr/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [Satır ve Sütunları Gruplama ve Grubu Kaldırma](/cells/tr/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [Satır ve Sütunları Gizleme ve Gösterme](/cells/tr/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Excel Çalışma Sayfasına Satır Eklemek veya Silmek](/cells/tr/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Excel dosyasının Satır ve Sütunlarını Eklemek ve Silmek](/cells/tr/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [Çalışma Sayfasındaki Yinelemeli Satırları Kaldırma](/cells/tr/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [Çalışma sayfasında boş sütunları ve satırları silerken diğer çalışma sayfalarındaki referansları güncelle](/cells/tr/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

