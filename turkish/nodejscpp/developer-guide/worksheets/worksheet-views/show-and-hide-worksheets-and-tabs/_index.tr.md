---  
title: Sayfaları ve Sekmeleri Göster ve Gizle ile Node.js kullanarak C++  
linktitle: Sayfaları ve Tabları Gösterme ve Gizleme  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: Bu makale, Node.js API veya Node.js Kütüphanesini kullanarak Excel çalışma sayfasını programatik olarak gösterme ve gizleme için örnek kod sağlar. Ayrıca, Excel çalışma kitabı sekmelerini gösterip gizleme nasıl yapılır anlatılmıştır.  
---  

{{% alert color="primary" %}}  
Aspose.Cells kullanıcının çalışma sayfalarını ve sekmelerini gösterebilmesine ve gizleyebilmesine olanak tanır.  
{{% /alert %}}  

## **Bir Çalışma Sayfasını Gösterme ve Gizleme**  

Bir Excel dosyasında bir veya birden fazla çalışma sayfası olabilir. Excel dosyası oluşturduğumuzda, içinde çalıştığımız Excel dosyasına çalışma sayfaları ekleriz. Bir Excel dosyasındaki her çalışma sayfası kendi veri ve biçimlendirme ayarları gibi diğer çalışma sayfalarından bağımsızdır. Bazı durumlarda, geliştiriciler kendi ilgileri için Excel dosyalarındaki birkaç çalışma sayfasını gizlemek ve diğerlerini göstermek isteyebilirler. **Aspose.Cells** bu nedenle geliştiricilere Excel dosyalarında çalışma sayfalarının görünürlüğünü kontrol etme imkanı sunar.  

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.  

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş özellikler ve yöntemler sunar. Bir çalışma sayfasının görünürlüğünü kontrol etmek için, [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) özelliğini [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının kullanın. [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) bir Boolean özelliğidir, bu da yalnızca **doğru** veya **yanlış** değerleri depolayabilir.  

### **Bir Çalışma Sayfasını Görünür Yapma**  

Bir çalışma sayfasını görünür yapmak için [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) özelliğini **true** olarak ayarlayın.  

### **Bir Çalışsayıyı Gizleme**  

Bir çalışma sayfasını gizlemek için [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**Worksheet.isVisible()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible--) özelliğini **false** olarak ayarlayın.  

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(chunks)); // Fixed from stream to Blob

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Tabları Gösterme ve Gizleme**  

Microsoft Excel dosyasının alt kısmına dikkatlice baktığınızda, bir dizi kontrolü göreceksiniz. Bunlar şunları içerir:  

- Sayfa sekmeleri.  
- Sekme kaydırma düğmeleri.  

Sayfa sekmeleri, Excel dosyasındaki çalışma sayfalarını temsil eder. Herhangi bir sekmeye tıklayarak o çalışma sayfasına geçebilirsiniz. Çalışma kitabında daha fazla çalışma sayfası olduğunda, daha fazla sayfa sekmesi olacaktır. İyi bir sayıda çalışma sayfasının olduğu Excel dosyasında bunları dolaşmak için düğmeler kullanmanız gerekebilir. Bu nedenle, Microsoft Excel, sayfa sekmeleri ve sekmeler arasında kaydırmak için düğmeler sağlar.  

Aspose.Cells kullanarak geliştiriciler Excel dosyalarında sayfa sekmelerinin ve sekmelerin kaydırma düğmelerinin görünürlüğünü kontrol edebilirler.  

Aspose.Cells, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için geliştiriciler [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) özelliğini kullanabilirler. [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) Boolean bir özelliktir, bu da sadece **true** veya **false** değeri depolayabileceği anlamına gelir.  

### **Sekmeleri Görünür Yapma**  

Sekmeleri görünür yapmak için [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) özelliğini **true** yapın.  

### **Sekmeleri Gizleme**  

Bir Excel dosyasında sekmeleri gizlemek için [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**WorkbookSettings.getShowTabs()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShowTabs--) özelliğini **false** yapın.  

Aşağıda, bir Excel dosyasını (book1.xls) açan, sekmelerini gizleyen ve değiştirilmiş dosyayı output.xls olarak kaydeden tam bir örnek bulunmaktadır. Kodun çalıştırılmasından sonra çalışma kitabının sekmelerinin gizlendiğini göreceksiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Sekme Çubuğu Genişliğini Kontrol Etme**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

