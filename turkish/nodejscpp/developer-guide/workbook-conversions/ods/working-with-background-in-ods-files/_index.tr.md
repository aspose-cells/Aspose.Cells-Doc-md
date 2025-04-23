---  
title: Node.js ile C++ kullanarak ODS Dosyalarında Arka Plan ile Çalışmak  
linktitle: ODS Dosyalarında Arka Planla Çalışma  
type: docs  
weight: 150  
url: /tr/nodejs-cpp/working-with-background-in-ods-files/  
description: Aspose.Cells for Node.js via C++ kullanarak ODS dosyalarında arka planları nasıl yöneteceğinizi öğrenin.  
---  

## **ODS Dosyalarında Arka Plan**  

Arka plan, ODS dosyalarındaki sayfalara eklenebilir. Arka plan ya renkli bir arka plan ya da grafik arka plan olabilir. Arka plan, dosya açıldığında görünmez ancak dosya PDF olarak yazdırılırsa, arka plan, oluşturulan PDF'de görünür. Arka plan ayrıca yazdırma önizleme ile de görüntülenir.  

Aspose.Cells for Node.js via C++, arka plan bilgilerini okumak ve ODS dosyalarına arka plan eklemek için yetenek sağlar.  

## **ODS dosyalarına arka plan ekleme yeteneği sağlamak için Aspose.Cells, arka plan ile ilgili bilgileri yönetmek için {0} sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS](90112030.ods) dosyasını yükleyerek arka plan bilgilerini okuma yeteneğini gösterir.**  

Aspose.Cells for Node.js via C++, ODS Dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) sınıfını sağlar. Aşağıdaki kod örneği, [kaynak ODS](90112030.ods) dosyasını yükleyerek ve arka plan bilgisini okuyarak [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) sınıfının kullanımını gösterir. Lütfen kod tarafından oluşturulan Konsol Çıktısına bakın.  

### **Örnek Kod**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load source Excel file
const filePath = path.join(sourceDir, "GraphicBackground.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

const background = worksheet.getPageSetup().getODSPageBackground();

console.log("Background Type: " + background.getType().toString());
console.log("Background Position: " + background.getGraphicPositionType().toString());

// Save background image
const imagePath = outputDir + "background.jpg";
fs.writeFileSync(imagePath, Buffer.from(background.getGraphicData()));
```  

### **Konsol Çıktısı**  

{{< highlight javascript >}}  
Background Type: Graphic  
Background Position: CenterCenter  
{{< /highlight >}}  

## **ODS dosyasına Renkli Arka Plan Ekleme**  

Aspose.Cells for Node.js via C++, ODS Dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) sınıfını sağlar. Aşağıdaki kod örneği, [**OdsPageBackground.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getColor--) özelliğinin kullanımını gösterir ve ODS dosyasına renkli bir arka plan ekler. Lütfen kod tarafından oluşturulan [çıktı ODS](90112031.ods) dosyasına bakın.  

### **Örnek Kod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setColor(AsposeCells.Color.Azure);
background.setType(AsposeCells.OdsPageBackgroundType.Color);

workbook.save(outputDir + "ColoredBackground.ods", AsposeCells.SaveFormat.Ods);
```  

## **ODS dosyasına Grafik Arka Plan Ekleme**  

Aspose.Cells for Node.js via C++, ODS Dosyalarında arka planı yönetmek için [**OdsPageBackground**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground) sınıfını sağlar. Aşağıdaki kod örneği, [**OdsPageBackground.getGraphicData()**](https://reference.aspose.com/cells/nodejs-cpp/odspagebackground/#getGraphicData--) özelliğinin kullanımını gösterir ve ODS dosyasına grafiksel bir arka plan ekler. Lütfen kod tarafından oluşturulan [çıktı ODS](90112030.ods) dosyasına bakın.  

### **Örnek Kod**  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get(0, 0).putValue(1);
worksheet.getCells().get(1, 0).putValue(2);
worksheet.getCells().get(2, 0).putValue(3);
worksheet.getCells().get(3, 0).putValue(4);
worksheet.getCells().get(4, 0).putValue(5);
worksheet.getCells().get(5, 0).putValue(6);
worksheet.getCells().get(0, 1).putValue(7);
worksheet.getCells().get(1, 1).putValue(8);
worksheet.getCells().get(2, 1).putValue(9);
worksheet.getCells().get(3, 1).putValue(10);
worksheet.getCells().get(4, 1).putValue(11);
worksheet.getCells().get(5, 1).putValue(12);

const background = worksheet.getPageSetup().getODSPageBackground();

background.setType(AsposeCells.OdsPageBackgroundType.Graphic);
background.setGraphicData(fs.readFileSync(path.join(sourceDir, "background.jpg")));
background.setGraphicType(AsposeCells.OdsPageBackgroundGraphicType.Area);

workbook.save(outputDir + "GraphicBackground.ods", AsposeCells.SaveFormat.Ods);
```  

