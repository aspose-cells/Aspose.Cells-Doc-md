---  
title: Satır ve Sütunları Otomatik Boyutlandırma Node.js ve C++ ile  
linktitle: Satırların ve Sütunların Otomatik Sığdırması  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/autofit-rows-and-columns/  
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak hücre aralığında satır, sütun, birleştirilmiş hücrelerin satırlarını ve satırını otomatik olarak boyutlandırmanın nasıl yapılacağını gösterir.  
keywords: Node.js üzerinden C++ ile Otomatik Sığdır Satır, Node.js üzerinden C++ ile Otomatik Sığdır Sütun, Node.js üzerinden C++ ile Bir Hücre Aralığında Satır Sığdır, Node.js üzerinden C++ ile Birleştirilmiş Hücrelerin Satırlarını Sığdır  
---  

{{% alert color="primary" %}}  
Microsoft Excel, hücrelerin içeriğine göre genişlik ve yüksekliği otomatik boyutlandırmanıza izin verir. Bu özellik Aspose.Cells for Node.js via C++ üzerinden de kullanılabilir, böylece geliştiriciler çalışma zamanında hücrenin boyutlarını otomatik olarak ayarlayabilir.  
{{% /alert %}}  

## **Otomatik Uydurma**  

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bu makale, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfını kullanarak satır veya sütunları otomatik sığdırmaya bakıyor.  

### **Satırı Otomatik Uydurma - Basit**  

Bir satırın genişliği ve yüksekliğini otomatik boyutlandırmanın en basit yolu, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) metodunu çağırmaktır. [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-) yöntemi, yeniden boyutlandırılacak satırın satır indeksini parametre olarak alır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileBuffer = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1);

// Saving the modified Excel file
const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath);
```  

### **Hücre Aralığında Satır Otomatik Sığdırma**  

Bir satır, birçok sütundan oluşur. Aspose.Cells, satırdaki hücre aralığındaki içeriğe göre satırı otomatik sığdırmak için [**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) metodunun aşırı yüklenmiş bir versiyonunu çağırmaya izin verir. Aşağıdaki parametreleri alır:  

- **Satır dizini**, otomatik olarak uyarlama yapılacak satırın dizini.  
- **İlk sütun dizini**, satırın ilk sütununun dizini.  
- **Son sütun dizini**, satırın son sütununun dizini.  

[**autoFitRow**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRow-number-number-number-) metodu, satırdaki tüm sütunların içeriğini kontrol eder ve ardından satırı otomatik sığdırır.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileData = fs.readFileSync(inputPath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileData);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the 3rd row of the worksheet
worksheet.autoFitRow(1, 0, 5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Hücre Aralığında Sütun Otomatik Sığdırma**  

Bir sütun, birçok satırdan oluşur. Bir sütunu, sütun içindeki hücre aralığındaki içeriğe göre otomatik sığdırmak mümkündür; bunun için [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) metodunun aşırı yüklenmiş bir versiyonu çağrılır ve aşağıdaki parametreleri alır:  

- **Sütun dizini**, otomatik olarak sığdırılacak sütunun dizini.  
- **İlk satır indeksi**, sütunun ilk satırının indeksi.  
- **Son satır indeksi**, sütunun son satırının indeksi.  

[**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) metodu, sütundaki tüm satırların içeriğini kontrol eder ve sonra sütunu otomatik sığdırır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const workbook = new AsposeCells.Workbook(fs.readFileSync(inputPath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Auto-fitting the Column of the worksheet
worksheet.autoFitColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

### **Birleştirilmiş Hücreler İçin Satırları Otomatik Uydurma**  

Aspose.Cells kullanılarak, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) API'si kullanılarak birleştirilmiş hücreler için bile satırları otomatik sığdırmak mümkündür. [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) sınıfı, birleştirilmiş hücreler için satırları otomatik sığdırmak amacıyla kullanılabilecek [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--) özelliği sağlar. [**AutoFitterOptions.getAutoFitMergedCellsType()**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions/#getAutoFitMergedCellsType--), aşağıdaki üyeleri içeren [**AutoFitMergedCellsType**](https://reference.aspose.com/cells/nodejs-cpp/autofitmergedcellstype) yinelemeli nesnesini kabul eder.  

- Hiçbiri: Birleştirilmiş hücreleri yoksay.  
- FirstLine: Sadece ilk satırın yüksekliğini artırır.  
- LastLine: Sadece son satırın yüksekliğini artırır.  
- EachLine: Her satırın yüksekliğini artırır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(dataDir, "output");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first (default) worksheet
const worksheet = wb.getWorksheets().get(0);

// Create a range A1:B1
const range = worksheet.getCells().createRange(0, 0, 1, 2);

// Merge the cells
range.merge();

// Insert value to the merged cell A1
worksheet.getCells().get(0, 0).setValue("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end");

// Create a style object
const style = worksheet.getCells().get(0, 0).getStyle();

// Set wrapping text on
style.setIsTextWrapped(true);

// Apply the style to the cell
worksheet.getCells().get(0, 0).setStyle(style);

// Create an object for AutoFitterOptions
const options = new AsposeCells.AutoFitterOptions();

// Set auto-fit for merged cells
options.setAutoFitMergedCellsType(AsposeCells.AutoFitMergedCellsType.EachLine);

// Autofit rows in the sheet (including the merged cells)
worksheet.autoFitRows(options);

// Save the Excel file
wb.save(path.join(outputDir, "AutofitRowsforMergedCells.xlsx"));
```  

{{% alert color="primary" %}}  
Ayrıca, seçimli satır/sütun aralığını ve [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) örneğini kabul eden [**autoFitRows**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitRows-number-number-AutoFitterOptions-) ve [**autoFitColumns**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumns-number-number-AutoFitterOptions-) metodlarının aşırı yüklenmiş versiyonlarını kullanarak istenilen [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) ile seçili satır/sütunları otomatik sığdırmak için deneyebilirsiniz.  

Yukarıdaki metodların imzaları aşağıdaki gibidir:  

1. autoFitRows(int startRow, int endRow, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
1. autoFitColumns(int firstColumn, int lastColumn, [**AutoFitterOptions**](https://reference.aspose.com/cells/nodejs-cpp/autofitteroptions) options)  
{{% /alert %}}  

## **Bilinmesi Gerekenler**  

{{% alert color="primary" %}}  
Bir hücre birleştirilmişse, otomatik sığdırma yöntemleri uygulanmaz ki bu da Microsoft Excel'dekiyle aynıdır. Bunu aşmak için autofilter API kullanabilirsiniz. Ayrıca, hücredeki metin sarılmışsa, [**autoFitColumn**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#autoFitColumn-number-) yöntemi de uygulanmaz. Bir diğer önemli nokta, *autoFit* yöntemlerinin zaman alıcı olduğu ve bu nedenle, uygulamanızın verimliliğini sağlamak için bu yöntemleri olabildiğince az kullanmanızdır.  
{{% /alert %}}  

## **Gelişmiş Konular**  
- [Birleştirilmiş Hücreler için Satırları Otomatik Uydurma](/cells/tr/nodejs-cpp/autofit-rows-for-merged-cells/)  

