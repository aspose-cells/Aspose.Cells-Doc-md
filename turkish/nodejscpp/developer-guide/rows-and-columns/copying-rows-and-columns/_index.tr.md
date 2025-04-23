---  
title: Node.js ile C++ üzerinden Satır ve Sütun Kopyalama  
linktitle: Satır ve Sütunları Kopyalama  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/copying-rows-and-columns/  
description: Bu makale, Aspose.Cells for Node.js via C++ API si kullanılarak satır ve sütunların nasıl kopyalanacağını gösterir.  
keywords: Node.js üzerinden C++, Satır ve Sütun Kopyalama, Node.js de Satırları Kopyala, Node.js kullanarak Sütunları Kopyala, Aspose.Cells for Node.js via C++ kullanarak Satır ve Sütunları Yapıştır, Çoklu Satır veya Sütun yapıştır, Tek Satır veya Sütunu Kopyala ve Yapıştırma.  
---  

## **Giriş**  

Bazen, bir çalışma sayfasında tüm çalışma sayfasını kopyalamadan satır ve sütunları kopyalamanız gerekir. Aspose.Cells ile, çalışma kitapları arasında veya içinde satır ve sütunları kopyalamak mümkündür.  
Bir satır (veya sütun) kopyalandığında, içindeki veriler, güncellenmiş referanslarla formülleri - ve değerleri, yorumları, biçimlendirmeyi, gizli hücreleri, görüntüleri ve diğer çizim nesnelerini içeren veriler de kopyalanır.  

## **Microsoft Excel ile Satırları ve Sütunları Nasıl Kopyalanır**  

1. Kopyalamak istediğiniz satırı veya sütunu seçin.  
1. Satır veya sütunları kopyalamak için **Standart** araç çubuğunda **Kopyala**'yı tıklayın veya **CTRL**+**C**'ye basın.  
1. Kopyalamak istediğiniz seçimin altında veya sağındaki bir satır veya sütunu seçin.  
1. Satır veya sütunları kopyalarken, **Ekle** menüsünde **Kopyalanan Hücreler**'i tıklayın.  

{{% alert color="primary" %}}  
Hedef hücrelerin içeriği herhangi bir içeriği Çıkar veya tıklamak yerine **Standart** araç çubuğunda **Yapıştır**'ı tıklarsanız değiştirilir.  
{{% /alert %}}  

## **Microsoft Excel ile Yapıştırma Seçenekleri Kullanarak Satır ve Sütunları Nasıl Yapıştırılır**  

1. Kopyalamak istediğiniz veri veya diğer özelliklere sahip hücreleri seçin.  
1. Ana sekmede **Kopyala**'yı tıklayın.  
1. Kopyaladığınız şeyi yapıştırmak istediğiniz alanın ilk hücresine tıklayın.  
1. Ana sekmede **Yapıştır**'ın yanındaki oku tıklayın ve ardından **Yapıştırma**'yı seçin.  
1. İstediğiniz **seçenekleri** seçin.  

## **Aspose.Cells for Node.js via C++ Kullanılarak Satır ve Sütunlar Nasıl Kopyalanır**  

## **Tek Satırları Nasıl Kopyalanır**  

Aspose.Cells, [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) metodunu sağlar; bu metod, kaynak satırdan hedef satıra formüller, değerler, yorumlar, hücre biçimleri, gizli hücreler, resimler ve diğer çizim nesneleri dahil olmak üzere tüm veri türlerini kopyalar.  

[**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) yöntemi aşağıdaki parametreleri alır:  

- kaynaktaki [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) nesnesi,  
- kaynak satır dizini, ve  
- hedef satır dizini.  

Bu yöntemi kullanarak bir sayfa içinde veya başka bir sayfaya satır kopyalayabilirsiniz. [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) yöntemi, Microsoft Excel'e benzer şekilde çalışır. Örneğin, hedef satırın yüksekliğini açıkça ayarlamanıza gerek yoktur, bu değer de kopyalanır.  

Aşağıdaki örnek, bir sayfada satır kopyalamayı göstermektedir. Bir şablon Microsoft Excel dosyası kullanır ve ikinci satırı (veri, biçimlendirme, yorumlar, resimler vb. ile birlikte) kopyalar ve aynı sayfadaki 12. satıra yapıştırır.  

Kaynak satır yüksekliğini almak için [**Cells.getRowHeight(number, boolean, CellsUnitType)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getRowHeight-number-boolean-cellsunittype-) metodunu kullanmadan adımı atlayabilirsiniz, daha sonra hedef satır yüksekliği [**Cells.copyRow(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRow-cells-number-number-) yöntemi ile otomatik olarak ayarlanır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file.
const excelWorkbook1 = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Get the first worksheet in the workbook.
const wsTemplate = excelWorkbook1.getWorksheets().get(0);

// Copy the second row with data, formattings, images and drawing objects
// To the 16th row in the worksheet.
wsTemplate.getCells().copyRow(wsTemplate.getCells(), 1, 15);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

{{% alert color="primary" %}}  
Satırları kopyalarken, ilgili resimler, grafikler veya diğer çizim nesnelerinin Microsoft Excel ile aynı olduğu gibi dikkate alınması önemlidir:  

1. Kaynak satır dizini 5 ise, resim, grafik vb., başlangıç satır dizini 4 ve bitiş satır dizini 6 içinde bulunduruluyorsa kopyalanır.  
1. Var olan resimler, grafikler vb. hedef satırdan silinmez.  
{{% /alert %}}  

## **Birden Fazla Satırın Nasıl Kopyalanacağı**  

Ayrıca, [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) metodunu kullanırken, ek olarak bir tamsayı parametresi alan ve kopyalanacak kaynak satır sayısını belirten toplu satır kopyalama işlemi yapabilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "aspose-sample.xlsx");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(filePath);

// Get the cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Copy the first 3 rows to 7th row
cells.copyRows(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Sütunları Kopyalamak**  

Aspose.Cells, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sınıfının [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) metodunu sağlar, bu yöntem, formüller ve güncellenmiş referanslar dahil olmak üzere tüm veri türlerini, değerleri, yorumları, hücre biçimlerini, gizli hücreleri, resimleri ve diğer çizim nesnelerini kaynak sütundan hedef sütuna kopyalar.  

[**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) yöntemi aşağıdaki parametreleri alır:  

- kaynaktaki [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) nesnesi,  
- kaynak sütun indeksi ve  
- hedef sütun indeksi.  

Bir sayfa içinde veya başka bir sayfaya sütun kopyalamak için [**Cells.copyColumn(Cells, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumn-cells-number-number-) yöntemini kullanabilirsiniz.  

Bu örnek, bir çalışma sayfasından bir sütunu kopyalar ve başka bir iş kitabındaki bir çalışma sayfasına yapıştırır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Create another Workbook.
const excelWorkbook1 = new AsposeCells.Workbook(filePath);

// Get the first worksheet in the book.
const ws1 = excelWorkbook1.getWorksheets().get(0);

// Copy the first column from the first worksheet of the first workbook into
// The first worksheet of the second workbook.
ws1.getCells().copyColumn(ws1.getCells(), ws1.getCells().getColumns().get(0).getIndex(), ws1.getCells().getColumns().get(2).getIndex());

// Autofit the column.
ws1.autoFitColumn(2);

// Save the excel file.
excelWorkbook1.save(path.join(dataDir, "output.xls"));
```  

## **Birden Çok Sütun Nasıl Kopyalanır**  

[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) yöntemine benzer şekilde, Aspose.Cells API'leri de çok sayıda kaynak sütunu yeni konuma kopyalamak için [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) metodunu sağlar.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an instance of Workbook class by loading the existing spreadsheet
const workbook = new AsposeCells.Workbook(path.join(dataDir, "aspose-sample.xlsx"));

// Get the first worksheet's cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Copy the first 3 columns to the 7th column
cells.copyColumns(cells, 0, 6, 3);

// Save the result on disc
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

## **Yapıştırma Seçenekleri ile Satır ve Sütunların Nasıl Yapıştırılacağı**  

Aspose.Cells şimdi, [**PasteOptions**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/) işlevler [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-) ve [**Cells.copyColumns(Cells, number, number, number, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyColumns-cells-number-number-number-pasteoptions-) kullanırken uygun yapıştırma seçeneğini Excel ile benzer şekilde ayarlamayı sağlar.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load sample excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleChangeChartDataSource.xlsx"));

// Access the first sheet which contains chart
const source = workbook.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = workbook.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Set PasteOptions
const pasteOptions = new AsposeCells.PasteOptions();
pasteOptions.setPasteType(AsposeCells.PasteType.Values);
pasteOptions.setOnlyVisibleCells(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options, pasteOptions);

// Save workbook in xlsx format
workbook.save(path.join(outputDir, "outputChangeChartDataSource.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  


