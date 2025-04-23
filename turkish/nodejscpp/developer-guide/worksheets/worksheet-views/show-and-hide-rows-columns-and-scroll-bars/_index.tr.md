---  
title: Yüksek ve Kaydırma Çubuklarını Node.js ile C++ kullanarak Göster ve Gizle  
linktitle: Satırları Sütunları ve Kaydırma Çubuklarını Göster ve Gizle  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/show-and-hide-rows-columns-and-scroll-bars/  
description: Bu makale, Node.js kullanarak C++ aracılığıyla Excel çalışma sayfası satırlarını ve sütunlarını programatik olarak gösterme ve gizleme yöntemini göstermektedir. Kaydırma çubuklarının görünürlüğünü kontrol edin ve birden çok satır, sütunu etkili şekilde gizleyin.  
---  

{{% alert color="primary" %}}  
Aspose.Cells, bir çalışma sayfasının Satırların, Sütunların ve Kaydırma Çubuklarının görünürlüğünü kontrol etmenin yollarını sağlar.  
{{% /alert %}}  

## **Satır ve Sütunları Göster ve Gizle**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her çalışma sayfasına erişmesine olanak tanıyan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu, çalışma sayfasındaki satır veya sütunları yönetmek için birkaç yöntem sunar. Bunlardan bazıları aşağıda tartışılmıştır.  

### **Satır ve Sütunları Göster**  

Geliştiriciler, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunun [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) ve [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) metodlarını sırasıyla çağırarak herhangi bir gizli satır veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:  

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.  
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Gizli bir sütunu görünür yapmak için, önce daha önce atanan genişliğine veya orijinal genişliğine geri yüklemeniz gerekirse, lütfen negatif genişlik değeri ile sütunu gizlemeyi açın. Örneğin: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **Satır ve Sütunları Gizle**  

Geliştiriciler, belirli bir satır veya sütunu gizlemek için sırasıyla [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) ve [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenmek istenen satır ve sütun indekslerini parametre olarak alır.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileBuffer = fs.readFileSync(filePath);

const workbook = new AsposeCells.Workbook(fileBuffer);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().hideRow(2);

worksheet.getCells().hideColumn(1);

workbook.save(path.join(dataDir, "output.out.xls"));
```  

{{% alert color="primary" %}}  
Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.  
{{% /alert %}}  

### **Birden Fazla Satır ve Sütunu Gizleme**  

Geliştiriciler, aynı anda birden fazla satır veya sütunu gizlemek için sırasıyla [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) ve [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenecek başlangıç satırı veya sütunu indeksi ve satır veya sütun sayısı parametreleri olarak alır.  

```javascript
const fs = require('fs');
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

// Hiding 3, 4 and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));

// No explicit close needed for file stream as we're working with in-memory data
```  

## **Kaydırma Çubuklarını Göster ve Gizle**  

Kaydırma çubukları, herhangi bir dosyanın içeriğini gezinmek için kullanılır. Genellikle iki tür kaydırma çubuğu bulunur:  

- Dikey kaydırma çubukları  
- Yatay kaydırma çubukları  

Microsoft Excel ayrıca yatay ve dikey kaydırma çubukları sağlar böylece kullanıcılar çalışma sayfası içeriğinde kaydırma yapabilirler. Aspose.Cells kullanarak geliştiriciler Excel dosyalarında her iki türde de kaydırma çubuklarının görünürlüğünü kontrol edebilirler.  

### **Kaydırma Çubuklarının Görünürlüğünü Kontrol Etmek**  

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasını yönetmek için geniş özellikler ve yöntemler içerir. Kaydırma çubuklarının görünürlüğünü kontrol etmek için [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) ve [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) özelliklerini kullanın. [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) ve [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) Boolean özellikleridir, bu da bu özelliklerin yalnızca **doğru** veya **yanlış** değerleri depolayabileceği anlamına gelir.  

#### **Kaydırma Çubuklarını Görünür Yapma**  

Kaydırma çubuklarını görünür hale getirmek için [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) veya [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) özelliğini **true** olarak ayarlayın.  

#### **Kaydırma çubuklarını gizleme**  

Kaydırma çubuklarını gizlemek için [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isVScrollBarVisible--) veya [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#isHScrollBarVisible--) özelliğini **false** olarak ayarlayın.  

**Örnek Kod**  

Aşağıda, bir Excel dosyasını, book1.xls'yi açan, her iki kaydırma çubuğunu gizleyen ve ardından değiştirilmiş dosyayı output.xls olarak kaydeden tam bir kod bulunmaktadır.  

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

// Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setIsVScrollBarVisible(false);

// Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setIsHScrollBarVisible(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

