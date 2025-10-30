---  
title: Node.js üzerinden C++ kullanarak Microsoft Excel dosyalarının Sayfalarını Yönetin  
linktitle: Çalışma Sayfaları  
type: docs  
weight: 90  
url: /tr/nodejs-cpp/manage-worksheets/  
description: Aspose.Cells for Node.js via C++ kullanarak sayfaları ekleyin, kaldırın ve aktif hale getirin.  
---  

{{% alert color="primary" %}}  
Geliştiriciler, Aspose.Cells'in esnek API'sini kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları eklemek ve kaldırmak için yaklaşımlar sağlar. Bu konu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir {2} koleksiyonuna sahip olan bir {0} temsil eden bir Aspose.Cells sınıfını açıklar.  
{{% /alert %}}  

Aspose.Cells, Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan bir [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.  

Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar.  

## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**  

Programlı olarak yeni bir Excel dosyası oluşturmak için:  

1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının bir nesnesini oluşturun.  
1. [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) sınıfının [**WorksheetCollection.add(SheetType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#add-sheettype-) yöntemini çağırın. Boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir. Yeni çalışma sayfasının sayfa indeksini [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonuna geçirerek referans verebilirsiniz.  
1. Bir çalışma sayfası referansı edinin.  
1. Çalışma sayfalarında çalışma yapın.  
1. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) yöntemini çağırarak yeni çalışma sayfalarıyla yeni Excel dosyasını kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().getCount();
workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Tasarımcı Çalışsayfalara Çalışsayfalar Ekleme**  

Tasarımcı çalışma sayfasına sayfa ekleme işlemi, yeni bir çalışma sayfası ekleme ile aynıdır; ancak, Excel dosyası zaten mevcut olmalı ve eklemeden önce açılmalıdır. Tasarımcı çalışma sayfası, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı kullanılarak açılabilir.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Setting the name of the newly added worksheet
worksheet.setName("My Worksheet");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Sayfa Adını Kullanarak Çalışsayfalara Erişme**  

Adını veya dizinini belirterek herhangi bir çalışma sayfasına erişin.  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "book1.xlsx");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(inputPath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing a worksheet using its sheet name
const worksheet = workbook.getWorksheets().get("Sheet1");
const cell = worksheet.getCells().get("A1");
console.log(cell.getValue());
```  

## **Sayfa Adını Kullanarak Çalışsayfaları Kaldırma**  

Bir dosyadan çalışma sayfalarını kaldırmak için, [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) sınıfının [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) yöntemini çağırın. Belirli bir sayfayı kaldırmak için, sayfa adını [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) yöntemine geçirin.  

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

// Removing a worksheet using its sheet name
workbook.getWorksheets().removeAt("Sheet1");

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**  

Sayfa adını kullanarak sayfaları kaldırmak, sayfa adını bildiğiniz zaman iyi çalışır. Sayfa adını bilmiyorsanız, sayfa indeksini alan [**WorksheetCollection.removeAt(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#removeAt-string-) yönteminin aşırı yüklenmiş versiyonunu kullanın.  

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

// Removing a worksheet using its sheet index
workbook.getWorksheets().removeAt(0);

// Save workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```  

## **Sayfaları Etkinleştirme ve Çalışma Sayfasında Aktif Bir Hücre Yapma**  

Bazen, bir kullanıcının Microsoft Excel dosyasını Excel'de açtığında belirli bir çalışma sayfasının aktif ve görüntülenebilir olması gerekir. Benzer şekilde, belirli bir hücreyi etkinleştirmek ve kaydırma çubuklarını etkin hücreyi gösterecek şekilde ayarlamak isteyebilirsiniz. Aspose.Cells bu görevleri yapabilir.  

Bir **etkin sayfa**, üzerinde çalıştığınız bir sayfadır: sekmelerdeki etkin sayfanın adı varsayılan olarak kalın harfle yazılıdır.  

Bir **etkin hücre**, seçilen hücredir, verinin başlatıldığı hücredir. Aynı zamanda yalnızca bir hücre etkindir. Etkin hücre, kalın bir kenarlıkla vurgulanır.  

### **Sayfaları Aktifleştirme ve Bir Hücreyi Etkin Yapma**  

Aspose.Cells, bir sayfayı ve bir hücreyi etkinleştirmek için özel API çağrıları sağlar. Örneğin, [**WorksheetCollection.getActiveSheetIndex()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getActiveSheetIndex--) özelliği, çalışma kitabında etkin sayfayı ayarlamak için kullanışlıdır. Benzer şekilde, [**Worksheet.getActiveCell()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getActiveCell--) özelliği, bir çalışma sayfasında etkin hücreyi ayarlamak ve almak için kullanılır.  

Yatay veya dikey kaydırma çubuklarının, belirli verileri göstermek istediğiniz satır ve sütun konumunda olduğundan emin olmak için [**Worksheet.getFirstVisibleRow()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleRow--) ve [**Worksheet.getFirstVisibleColumn()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFirstVisibleColumn--) özelliklerini kullanın.  

Aşağıdaki örnek, bir çalışma sayfasını etkinleştirmenin ve üzerinde etkin bir hücre oluşturmanın nasıl yapıldığını gösterir. Oluşturulan çıktıda, kaydırmalı çubuklar, ilk görünür satır ve sütun olarak 2. satır ve 2. sütunu yapmak için kaydırılır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Add a worksheet if collection is empty
const worksheets = workbook.getWorksheets();
if (worksheets.getCount() === 0) {
worksheets.add();
}

// Get the first worksheet in the workbook.
const worksheet1 = worksheets.get(0);

// Get the cells in the worksheet.
const cells = worksheet1.getCells();

// Input data into B2 cell.
cells.get(1, 1).putValue("Hello World!");

// Set the first sheet as an active sheet.
workbook.getWorksheets().setActiveSheetIndex(0);

// Set B2 cell as an active cell in the worksheet.
worksheet1.setActiveCell("B2");

// Set the B column as the first visible column in the worksheet.
worksheet1.setFirstVisibleColumn(1);

// Set the 2nd row as the first visible row in the worksheet.
worksheet1.setFirstVisibleRow(1);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```  

## **Gelişmiş Konular**  
- [Çalışma Sayfalarını Kopyalama ve Taşıma](/cells/tr/nodejs-cpp/copying-and-moving-worksheets/)  
- [Çalışma Sayfasındaki Hücre Sayısını Sayma](/cells/tr/nodejs-cpp/count-number-of-cells-in-the-worksheet/)  
- [Boş Çalışma Sayfalarını Algılama](/cells/tr/nodejs-cpp/detecting-empty-worksheets/)  
- [Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma](/cells/tr/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/)  
- [Çalışma sayfası benzersiz kimliğini alın](/cells/tr/nodejs-cpp/get-worksheet-unique-id/)  
- [Çalışma Sayfalarından Senaryo Oluşturma, Hareketlendirme veya Kaldırma](/cells/tr/nodejs-cpp/create-manipulate-or-remove-scenarios-from-worksheets/)  
- [Sayfa Sonlarını Yönetme](/cells/tr/nodejs-cpp/managing-page-breaks/)  
- [Sayfa Ayarı Özellikleri](/cells/tr/nodejs-cpp/page-setup-features/)   
- [Aspose.Cells üzerinde Sheet.SheetId özelliğini kullanarak OpenXml'in faydalanılması](/cells/tr/nodejs-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)  
- [Çalışma Sayfası Görünümleri](/cells/tr/nodejs-cpp/worksheet-views/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
