---  
title: Node.js ile C++ kullanarak LightCells API kullanımı  
linktitle: LightCells API sını Kullanma  
type: docs  
weight: 160  
url: /tr/nodejs-cpp/using-lightcells-api/  
description: LightCells API kullanarak Node.js de büyük Excel dosyalarını okuma ve yazma yöntemlerini öğrenin. Performansı ve verimliliği artırmak, daha az bellek kullanımıyla çalışmak için.  
---  

{{% alert color="primary" %}}  

Bazen büyük bir veri veya içeriğe sahip büyük Microsoft Excel dosyalarını okumak ve yazmak isteyebilirsiniz. Hafif Hücreler API'sı, bu iş için kullanışlıdır: daha az bellek kullanarak daha iyi performans ve verimlilik elde edersiniz.  

{{% /alert %}}  
# Olay Tabanlı Mimari  
Aspose.Cells, özellikle bellekte bir veri modeli bloğu oluşturmadan hücre verilerini bir bir işlemek için tasarlanmış olan LightCells API'sını sağlar (Hücre koleksiyonu vb. kullanılmadan). Olay temelli modda çalışır.  

Çalışma kitaplarını kaydetmek için kaydederken hücre içeriğini hücre hücre sağlayın ve bileşen bunu doğrudan çıktı dosyasına kaydeder.  

Şablon dosyalarını okurken bileşen her hücreyi ayrı ayrı ayrıştırır ve değerlerini tek tek sağlar.  

Her iki işlemde de, bir Hücre nesnesi işlenir ve sonra atılır; Çalışma kitabı nesnesi koleksiyonu tutmaz. Bu modda, bu nedenle, büyük veri kümesine sahip Microsoft Excel dosyalarını ithal ederken ve dışa aktarırken bellek tasarrufu sağlanır, aksi takdirde çok fazla bellek kullanabilir.  

LightCells API, XLSX ve XLS dosyaları için hücreleri aynı şekilde işlemesine rağmen (bütün hücreleri belleğe yüklemez ama bir hücreyi işler ve ardından atar), XLSX dosyaları için XLS dosyalarına göre belleği daha etkili bir şekilde saklar çünkü iki formatın farklı veri modelleri ve yapıları vardır.  

Ancak, **XLS dosyaları için**, daha fazla bellek tasarrufu sağlamak adına, geliştiriciler, Kaydetme işlemi sırasında oluşturulan geçici veriyi kaydetmek için geçici bir konum belirleyebilir. Yaygın olarak, **LightCells API kullanarak XLSX dosyalarını kaydetmek geleneksel yöntemden %50 veya daha fazla bellek tasarrufu sağlayabilir; **XLS kaydetmek ise yaklaşık %20-40 bellek tasarrufu sağlayabilir.  

## Büyük Bir Excel Dosyası Yazma  
Aspose.Cells, programınızda uygulanması gereken `LightCellsDataProvider` arayüzü sağlar. Bu arayüz, hafif modda büyük hesap tablosu dosyalarını kaydetmek için veri sağlayıcıyı temsil eder.  

Bu modda çalışma kitabı kaydederken, `StartSheet(int)` her çalışma sayfası kaydedilirken kontrol edilir. Bir sayfa için, eğer `StartSheet(int)` doğru ise, bu sayfada satırların ve hücrelerin tüm verileri ve özellikleri bu uygulama tarafından sağlanır. İlk olarak, kaydedilecek bir sonraki satır indeksini almak için `NextRow()` çağrılır. Geçerli bir satır indeksi döndürülürse (satırların artan sırayla olması gerekir), bu satırı temsil eden bir Satır nesnesi, `StartRow(Row)` ile özelliklerini ayarlaması için uygulanmaya sağlanır.  

Bir satır için, önce `NextCell()` kontrol edilir. Geçerli bir sütun indeksi döndürülürse (bütün hücrelerin artan sırayla olması gerekir), bu hücreyi temsil eden bir Hücre nesnesi uygulanmaya sağlanır ve `StartCell(Cell)` ile verileri ve özellikleri ayarlanır. Hücrenin verileri ayarlandıktan sonra, hücre doğrudan oluşturulan hesap tablosu dosyasına kaydedilir ve bir sonraki hücre kontrol edilir ve işlenir.  
### Büyük Bir Excel Dosyasını Yazmak: Örnek  
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.  

Program, bir çalışma sayfasında **10.000 (10000x30 matris) kayıt** içeren devasa bir dosya oluşturur ve bunları sahte verilerle doldurur. `Main()` metodundaki `rowsCount` ve `colsCount` değişkenlerini değiştirerek kendi matrisinizi belirtebilirsiniz.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class TestDataProvider {
constructor(workbook, maxRows, maxColumns) {
this._workbook = workbook;
this.maxRows = maxRows;
this.maxColumns = maxColumns;
this._row = -1;
this._column = -1;
}

isGatherString() {
return false;
}

nextCell() {
this._column++;
if (this._column < this.maxColumns) {
return this._column;
} else {
this._column = -1;
return -1;
}
}

nextRow() {
this._row++;
if (this._row < this.maxRows) {
this._column = -1;
return this._row;
} else {
return -1;
}
}

startCell(cell) {
cell.putValue(this._row + this._column);
if (this._row !== 1) {
cell.setFormula("=Rand() + A2");
}
}

startRow(row) {
}

startSheet(sheetIndex) {
return sheetIndex === 0;
}
}

const run = async () => {
const dataDir = path.join(__dirname, "data");

const rowsCount = 10000;
const colsCount = 30;

const workbook = new AsposeCells.Workbook();
const ooxmlSaveOptions = new AsposeCells.OoxmlSaveOptions();

ooxmlSaveOptions.setLightCellsDataProvider(new TestDataProvider(workbook, rowsCount, colsCount));

await workbook.saveAsync(path.join(dataDir, "output.out.xlsx"), ooxmlSaveOptions);
};

run();
```  

## Büyük Excel Dosyalarını Okuma  
Aspose.Cells, programınızda uygulanması gereken `LightCellsDataHandler` arayüzü sağlar. Bu arayüz, hafif modda büyük hesap tablosu dosyalarını okuma veri sağlayıcısını temsil eder.  

Bu modda bir çalışma kitabı okunurken, `StartSheet` her çalışma sayfası okunurken kontrol edilir. Bir sayfa için, eğer `StartSheet` doğru ise, sayfadaki hücrelerin tüm verileri ve özellikleri bu arayüzün uygulanması tarafından kontrol edilir ve işlenir. Her satır için, `StartRow` çağrılır ve işlenmesi gerekip gerekmediği kontrol edilir. Eğer satır işlenecekse, ilk olarak özellikleri okunur ve geliştirici `ProcessRow` ile erişebilir. Satırın hücreleri de işlenmek isteniyorsa, `ProcessRow` true döndürmelidir ve her varolan hücre için `StartCell` çağrılır, böylece hücrelerin işlenip işlenmediği kontrol edilir.  
### Büyük Excel Dosyalarını Okuma: Örnek  
Lütfen LightCells API'nin çalışmasını görmek için aşağıdaki örnek kodu inceleyin. Kod segmentlerini ihtiyacınıza göre ekleyin, kaldırın veya güncelleyin.  

Program, milyonlarca kaydı olan büyük bir dosyayı bir çalışma sayfasında okur. Çalışma kitabındaki her sayfayı okumak biraz zaman alır. Örnek kod dosyayı okur ve toplam hücre sayısını, dize sayısını ve formül sayısını her çalışma sayfasında getirir.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class LightCellsDataHandlerVisitCells {
constructor() {
this.cellCount = 0;
this.formulaCount = 0;
this.stringCount = 0;
}

get CellCount() {
return this.cellCount;
}

get FormulaCount() {
return this.formulaCount;
}

get StringCount() {
return this.stringCount;
}

StartSheet(sheet) {
console.log("Processing sheet[" + sheet.getName() + "]");
return true;
}

StartRow(rowIndex) {
return true;
}

ProcessRow(row) {
return true;
}

StartCell(column) {
return true;
}

ProcessCell(cell) {
this.cellCount++;
if (cell.isFormula()) {
this.formulaCount++;
} else if (cell.getType() === AsposeCells.CellValueType.IsString) {
this.stringCount++;
}
return false;
}
}

async function run() {
const dataDir = path.join(__dirname, "data");
const opts = new AsposeCells.LoadOptions();
const v = new LightCellsDataHandlerVisitCells();
opts.setLightCellsDataHandler(v);
const wb = new AsposeCells.Workbook(path.join(dataDir, "LargeBook1.xlsx"), opts);
const sheetCount = wb.getWorksheets().getCount();
console.log("Total sheets: " + sheetCount + ", cells: " + v.CellCount
+ ", strings: " + v.StringCount + ", formulas: " + v.FormulaCount);
}

run();
```  

