---  
title: Node.js via C++ ile Dizilerin Kullanım Yolları ve Yeri  
linktitle: Verileri Yinele  
type: docs  
weight: 55  
url: /tr/nodejs-cpp/how-and-where-to-use-enumerators/  
description: Aspose.Cells for Node.js via C++ API kullanarak Dizileri Nasıl Kullanacağınızı Öğrenin.  
keywords: Node.js üzerinden Diziler Nasıl Kullanılır, Cells Enumerator Node.js, Satırlar Dizisi Node.js, Sütunlar Dizisi Node.js  
---  

{{% alert color="primary" %}}  

Bir dizin, bir konteyner veya koleksiyon üzerinde gezinme yeteneği sağlayan bir nesnedir. Diziciler, koleksiyondaki verileri okumak için kullanılabilir, ancak temel koleksiyonu değiştiremezler. Array ise, `getEnumerator` adlı bir yöntemi tanımlayan bir arayüzdür; bu, koleksiyona salt okunur erişim sağlar.  

Aspose.Cells API'ları bir dizi numaralandırıcı sağlar, ancak bu makale genellikle aşağıda listelenen üç türü tartışmaktadır.  

1. Hücreler Numaralandırıcı  
1. Satırlar Numaralandırıcı  
1. Sütunlar Numaralandırıcı  

{{% /alert %}}  

## **Numaralandırıcıları Nasıl Kullanılır**  

### **Hücreler Numaralandırıcı**  

Hücreler Numaralandırıcısına erişmenin çeşitli yolları vardır ve uygulama gereksinimlerine bağlı olarak bu yöntemlerden herhangi biri kullanılabilir. İşte hücreler numaralandırıcısını döndüren yöntemler.  

1. [**Cells.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getEnumerator--)  
1. [**Row.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getEnumerator--)  
1. [**Range.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getEnumerator--)  

Yukarıda bahsedilen tüm yöntemler, başlatılmış hücre koleksiyonunu gezinmeyi sağlayan numaralandırıcıyı döndürür.  

{{% alert color="primary" %}}  

Hücreleri gezinirken koleksiyon değiştirilmemelidir (bir hücreyi yeni bir şekilde oluşturan işlemler veya var olan bir hücreyi sildiren işlemler). Aksi takdirde, numaralandırıcı tüm hücreleri doğru bir şekilde gezinemeyebilir (bazı öğeler tekrarlanabilir veya atlanabilir).  

{{% /alert %}}  

Aşağıdaki kod örneği, bir Hücreler koleksiyonunun `IEnumerator` arayüzü uygulamasını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells().getEnumerator();
for (const cell of cells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rowCells = workbook.getWorksheets().get(0).getCells().getRows().get(0).getEnumerator();
for (const cell of rowCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}

const rangeCells = workbook.getWorksheets().get(0).getCells().createRange("A1:B10").getEnumerator();
for (const cell of rangeCells) {
console.log(`${cell.getName()} ${cell.getValue()}`);
}
```  

### **Satırlar Numaralandırıcı**  

Satırlar Dizici, [**RowCollection.getEnumerator()**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection/#getEnumerator--) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) için `IEnumerator` arayüzü uygulamasını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get RowCollection and iterate using index
const rows = workbook.getWorksheets().get(0).getCells().getRows();
const rowCount = rows.getCount();

// Traverse rows in the collection
for (let i = 0; i < rowCount; i++) {
const row = rows.get(i);
console.log(row.getIndex());
}
```  

### **Sütunlar Numaralandırıcı**  

Sütunlar Dizici, [**ColumnCollection.getEnumerator**](https://reference.aspose.com/cells/nodejs-cpp/columncollection) yöntemi kullanılırken erişilebilir. Aşağıdaki kod örneği, [**ColumnCollection**](https://reference.aspose.com/cells/nodejs-cpp/columncollection) için `IEnumerator` arayüzü uygulamasını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get columns collection
const columns = workbook.getWorksheets().get(0).getCells().getColumns();
// Traverse columns using index
const count = columns.getCount();
for (let i = 0; i < count; i++) {
const col = columns.get(i);
console.log(col.getIndex());
}
```  

## **Numaralandırıcıları Nerede Kullanılacağı**  

Dizicilerin avantajlarını tartışmak için gerçek zamanlı bir örnek ele alalım.  

**Senaryo**  

Bir uygulama gereksinimi, belirli bir [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) içindeki tüm hücreleri gezerek değerlerini okumaktır. Bu hedefi uygulamanın birkaç yolu olabilir. Birkaç örnek aşağıda gösterilmektedir.  

### **Görüntü Aralığı Kullanarak**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells = workbook.getWorksheets().get(0).getCells();

// Get the MaxDisplayRange
const displayRange = cells.getMaxDisplayRange();

// Loop over all cells in the MaxDisplayRange
for (let row = displayRange.getFirstRow(); row < displayRange.getRowCount(); row++) {
for (let col = displayRange.getFirstColumn(); col < displayRange.getColumnCount(); col++) {
// Read the Cell value
console.log(displayRange.get(row, col).getStringValue());
}
}
```  

### **MaxDataRow & MaxDataColumn Kullanarak**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get Cells collection of first worksheet
const cells2 = workbook.getWorksheets().get(0).getCells();
const maxDataRow = cells2.getMaxDataRow();
const maxDataColumn = cells2.getMaxDataColumn();

// Loop over all cells
for (let row = 0; row <= maxDataRow; row++) {
for (let col = 0; col <= maxDataColumn; col++) {
// Read the Cell value
const currentCell = cells2.checkCell(row, col);
if (currentCell) {
console.log(currentCell.getStringValue());
}
}
}
```  

Yukarıda bahsedilen her iki yaklaşımın da, tüm hücreleri döngü içinde dolaşarak hücre değerlerini okuma mantığına daha veya daha az benzer olduğunu gözlemleyebilirsiniz. Bu, aşağıda tartışılan birçok nedenden biri olabilir.  

1. [**getMaxRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxRow--), [**getMaxDataRow()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataRow--), [**getMaxColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxColumn--), [**getMaxDataColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDataColumn--) ve [**getMaxDisplayRange()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMaxDisplayRange--) gibi API'lar, ilgili istatistikleri toplamak için ekstra zaman gerektirir. Veri matrisi (satır x sütun) büyükse, bu API'ların kullanılması performans cezası uygulayabilir.  
1. Çoğu durumda, verilen bir aralıktaki tüm hücreler oluşturulmamıştır. Bu tür durumlarda, matristeki her hücreyi kontrol etmek, yalnızca başlatılmış hücreleri kontrol etmekten daha verimli değildir.  
1. Hücreye döngü içinde Cells satır, sütun olarak erişmek, bir aralıktaki tüm hücre nesnelerinin oluşturulmasına neden olabilir, bu da sonunda OutOfMemoryException'a neden olabilir.  

## **Sonuç**  

Yukarıda belirtilen gerçeklere dayanarak, aşağıdakiler, numaralandırıcıların kullanılması gereken olası senaryolarıdır.  

1. Yalnızca hücre koleksiyonunun salt okunur erişimi gereklidir, yani; gereksinim yalnızca hücreleri incelemektir.  
1. Birçok hücrenin dolaşılması gereklidir.  
1. Yalnızca başlatılmış hücreler/satırlar/sütunlar dolaşılmalıdır.  

{{< app/cells/assistant language="nodejs-cpp" >}}
