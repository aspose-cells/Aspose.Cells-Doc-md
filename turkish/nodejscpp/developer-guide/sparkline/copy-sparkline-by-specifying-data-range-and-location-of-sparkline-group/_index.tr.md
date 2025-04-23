---  
title: Node.js ve C++ kullanarak Sparkline Kopyalama (Veri Aralığını ve Sparkline Grubu Konumunu Belirterek)  
linktitle: Belirli Veri Aralığını ve Sparkline Grubu Konumunu Belirterek Sparkline Kopyalama  
type: docs  
weight: 300  
url: /tr/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Excel de, Aspose.Cells for Node.js via C++ kullanarak ver aralığını ve sparkline grubunun konumunu belirterek sparkline kopyalamayı öğrenin.  
---  

{{% alert color="primary" %}}  
Microsoft Excel, bir sparkline grubunun veri aralığını ve konumunu belirterek bir sparkline kopyalamanıza izin verir. Aspose.Cells, bu özelliği destekler.  
{{% /alert %}}  

Microsoft Excel'de sparkline kopyalamak için:  

1. Sparkline içeren hücreyi seçin.  
1. **Tasarım** sekmesinin **Sparkline** bölümünden **Veri Düzenle**'yi seçin.  
1. **Grup Konumunu ve Veriyi Düzenle**'yi seçin.  
1. Veri aralığını ve konumu belirtin.  
1. **Tamam**'a tıklayın.  

Aspose.Cells, sparkline grubunun veri aralığını ve konumunu belirtmek için `SparklineCollection.add(dataRange, row, column)` metodunu sağlar. Aşağıdaki örnek kod, yukarıdaki ekran görüntüsünde gösterildiği gibi kaynak Excel dosyasını yükler, ardından ilk sparkline grubuna erişir ve sparkline grubuna veri aralıkları ve konumlar ekler. Son olarak, çıktı Excel dosyasını disk üzerinde yazar ve bu da yukarıdaki ekran görüntüsünde gösterilmektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

