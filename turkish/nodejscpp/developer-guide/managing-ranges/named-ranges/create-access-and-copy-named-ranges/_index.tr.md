---  
title: Node.js ve C++ kullanarak Tanımlı Aralıklar Oluşturma ve Kopyalama  
linktitle: Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala  
type: docs  
weight: 200  
url: /tr/nodejs-cpp/create-access-and-copy-named-ranges/  
description: Excel de Aspose.Cells for Node.js via C++ kullanarak tanımlı aralıklar oluşturmayı, erişmeyi ve kopyalamayı öğrenin.  
---  

## **Giriş**  

 Normalde, sütun ve satır etiketleri belirli hücreleri göstermek için kullanılır. Hücreleri, hüreleri, formülleri veya sabit değerleri temsil eden açıklayıcı isimler oluşturmak mümkündür. **isim** kelimesi, hücreleri, hücre aralıklarını, formülleri veya sabit değerleri temsil eden bir karakter dizisini ifade edebilir. Bir aralığa isim atamak, bu aralıktaki hücrelerin adını kullanarak erişilebilmesine olanak tanır. Anlaşılması kolay isimler kullanın, örneğin Satışlar!C20:C30 gibi karmaşık aralıklar yerine Products gibi. Etiketler, aynı sayfada veri referans alan formüllerde kullanılabilir; başka bir sayfadaki aralığı göstermek istiyorsanız, bir isim kullanabilirsiniz. *İsimlendirilmiş aralıklar, liste kontrolleri, pivot tablolar, grafikler ve benzeri kaynak aralığı olarak kullanıldığında Microsoft Excel'in en güçlü özelliklerinden biridir.*  

## **Microsoft Excel Kullanarak Adlandırılmış Aralık İle Çalışma**  

### **Adlandırılmış Aralık Oluştur**  

Aşağıdaki adımlar, **MS Excel** kullanarak hücre veya hücre aralığını nasıl adlandıracağınızı açıklar. Bu yöntem, **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, ve **2002** için geçerlidir.  

1. Adlandırmak istediğiniz hücre veya hücre aralığını seçin.  
2. Formül çubuğunun sol ucundaki **İsim Kutusu**na tıklayın.  
3. Hücreler için isim yazın.  
4. ENTER tuşuna basın.  

{{% alert color="primary" %}}  
Hücre içeriğini değiştirirken hücreye ad veremezsiniz.  
{{% /alert %}}  

## **Aspose.Cells Kullanarak Adlandırılmış Aralık İle Çalışma**  

Burada görevi yapmak için Aspose.Cells API'sını kullanıyoruz.  
Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu sağlar.  

### **İsimlendirilmiş Aralık Oluştur**  

Bir adlandırılmış aralık oluşturmak, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun aşırı yüklenmiş [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) yöntemini çağırarak mümkündür. [**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) yönteminin tipik bir sürümü aşağıdaki parametreleri alır:  

- Sol üst hücrenin adı, aralıktaki sol üst hücrenin adı.  
- Sağ alt hücrenin adı, aralıktaki sağ alt hücrenin adı.  

[**createRange(string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-) yöntemi çağrıldığında, yeni oluşturulan aralık, [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) sınıfının bir örneği olarak döner. Bu [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesini, isimlendirilmiş aralığı yapılandırmak için kullanın. Örneğin, [**getName()**](https://reference.aspose.com/cells/nodejs-cpp/range/#getName--) özelliğini kullanarak aralığın adını ayarlayın. Aşağıdaki örnek, B4:G14 üzerine uzanan hücrelerin adlandırılmış bir aralık oluşturmak için nasıl yapılacağını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Creating a named range
const range = worksheet.getCells().createRange("B4", "G14");

// Setting the name of the named range
range.setName("TestRange");

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```  

### **Adı Verilen Aralıktaki Hücrelere Veri Girişi**  

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir  

- **JavaScript**: Range[row,sütun]  

A1:C4'ü kapsayan bir isimlendirilmiş aralığınız olduğunu düşünün. Matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:  

- firstRow, adlandırılmış aralıktaki ilk satırın indeksini döndürür.  
- firstColumn, adlandırılmış aralıktaki ilk sütunun indeksini döndürür.  
- rowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.  
- columnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.  

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first worksheet in the workbook.
const worksheet1 = workbook.getWorksheets().get(0);

// Create a range of cells based on H1:J4.
const range = worksheet1.getCells().createRange("H1", "J4");

// Name the range.
range.setName("MyRange");

// Input some data into cells in the range.
range.get(0, 0).setValue("USA");
range.get(0, 1).setValue("SA");
range.get(0, 2).setValue("Israel");
range.get(1, 0).setValue("UK");
range.get(1, 1).setValue("AUS");
range.get(1, 2).setValue("Canada");
range.get(2, 0).setValue("France");
range.get(2, 1).setValue("India");
range.get(2, 2).setValue("Egypt");
range.get(3, 0).setValue("China");
range.get(3, 1).setValue("Philipine");
range.get(3, 2).setValue("Brazil");

// Save the excel file.
workbook.save(path.join(dataDir, "rangecells.out.xls"));
```  

### **İsimlendirilmiş Aralıktaki Hücreleri Tanımlama**  

Bir aralıktaki bireysel hücrelere veri ekleyebilirsiniz. İzlenecek desen aşağıdaki gibidir:  

- **JavaScript**: Range[row,sütun]  

Eğer A1:C4'ü kapsayan bir isimlendirilmiş aralığınız varsa, matris 4 * 3 = 12 hücre yaratır. Bireysel aralık hücreleri ardışık olarak düzenlenir: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

Aralıktaki hücreleri tanımlamak için aşağıdaki özellikleri kullanın:  

- firstRow, adlandırılmış aralıktaki ilk satırın indeksini döndürür.  
- firstColumn, adlandırılmış aralıktaki ilk sütunun indeksini döndürür.  
- rowCount, adlandırılmış aralıktaki toplam satır sayısını döndürür.  
- columnCount, adlandırılmış aralıktaki toplam sütun sayısını döndürür.  

Aşağıdaki örnek, belirtilen bir aralıktaki hücrelere bazı değerler girmeyi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

// Identify range cells.
console.log("First Row : " + range.getFirstRow());
console.log("First Column : " + range.getFirstColumn());
console.log("Row Count : " + range.getRowCount());
console.log("Column Count : " + range.getColumnCount());
```  

### **İsimlendirilmiş Aralıklara Eriş**  

#### **Belirli Bir Adlandırılmış Aralığa Erişme**  

Belirli bir adlandırılmış aralığa erişmek için [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) koleksiyonunun [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) yöntemini çağırın. Tipik bir [**getRangeByName(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getRangeByName-string-) yöntemi, adlandırılmış aralığın adını alır ve belirtilen adlandırılmış aralığı [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) sınıfının bir örneği olarak döndürür. Aşağıdaki örnek, adına göre belirtilen bir aralığa nasıl erişileceğini göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1_testrange.xls"));

// Getting the specified named range
const range = workbook.getWorksheets().getRangeByName("TestRange");

if (range !== null) 
{
console.log("Named Range : " + range.getRefersTo());
}
```  

#### **Bir Elektronik Tablodaki Tüm İsimlendirilmiş Aralıklara Eriş**  

Bir elektronik tabloda tüm adlandırılmış aralıkları almak için [**worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) koleksiyonunun [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) metodunu çağırın. [**getNamedRanges()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getNamedRanges--) metodu, [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) koleksiyonundaki tüm adlandırılmış aralıkların dizisini döndürür.  

Aşağıdaki örnek, bir çalışma kitabındaki tüm adlandırılmış aralıklara erişmeyi gösterir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Getting all named ranges
const ranges = workbook.getWorksheets().getNamedRanges();

if (ranges != null) {
console.log("Total Number of Named Ranges: " + ranges.length);
}
```  

### **İsimlendirilmiş Aralıkları Kopyala**  

Aspose.Cells, bir hücre aralığını biçimlendirmesiyle birlikte başka bir aralığa kopyalamak için [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-pasteoptions-) yöntemi sağlar.  

Aşağıdaki örnek, kaynak hücre aralığını başka adlandırılmış bir aralığa kopyalamanın nasıl yapıldığını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Get the first worksheet in the worksheets collection.
const worksheet = workbook.getWorksheets().get(0);

// Create a range of cells.
const range1 = worksheet.getCells().createRange("E12", "I12");

// Name the range.
range1.setName("MyRange");

// Set the outline border to the range.
range1.setOutlineBorder(AsposeCells.BorderType.TopBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.BottomBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.LeftBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));
range1.setOutlineBorder(AsposeCells.BorderType.RightBorder, AsposeCells.CellBorderType.Medium, new AsposeCells.Color(0, 0, 128));

// Input some data with some formattings into
// A few cells in the range.
range1.get(0, 0).putValue("Test");
range1.get(0, 4).putValue("123");

// Create another range of cells.
const range2 = worksheet.getCells().createRange("B3", "F3");

// Name the range.
range2.setName("testrange");

// Copy the first range into second range.
range2.copy(range1);

// Save the excel file.
workbook.save(path.join(dataDir, "copyranges.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
