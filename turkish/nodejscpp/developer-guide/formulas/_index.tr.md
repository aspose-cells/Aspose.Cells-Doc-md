---
title: Node.js ve C++ kullanarak Excel dosyalarının formüllerini yönetme
linktitle: Formüller
type: docs
weight: 122
url: /tr/nodejs-cpp/using-formulas-or-functions-to-process-data/
description: Excel dosyalarının formüllerini Yönetmeyi Aspose.Cells for Node.js via C++ aracılığıyla öğrenin. Aspose.Cells kolayca Excel dosyalarının formüllerini alabilir, ayarlayabilir ve hesaplayabilir.
keywords: Node.js ve C++ kullanarak formülleri nasıl hesaplarım, Node.js ve C++ kullanarak Formüller ve Fonksiyonlar, Node.js ve C++ ile Yerleşik Fonksiyonları Yönetme, Node.js ve C++ ile Eklenti Fonksiyonlarını Kullanma, Node.js ve C++ ile Dizi Formüllerini Kullanma, Node.js ile R1C1 Formülü Kullanma
---

## **Giriş**

Microsoft Excel'in etkileyici özelliklerinden biri, verileri formüller ve fonksiyonlar ile işleyebilme yeteneğidir. Microsoft Excel, karmaşık hesaplamaları hızlıca yapmaya yardımcı olan yerleşik fonksiyonlar ve formüller sunar. Aspose.Cells ayrıca, gelişmiş fonksiyon ve formüllerin büyük bir kümesini sağlar ve ayrıca eklenti fonksiyonlarını da destekler. Ayrıca, Aspose.Cells, dizi ve R1C1 formüllerini destekler.

## **Formüller ve Fonksiyonları Nasıl Kullanılır**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonu içerir. Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu sağlar. Hücreler koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfından bir nesneyi temsil eder.

Aşağıda daha detaylı olarak tartışılan [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının özellikleri ve metotları kullanılarak hücrelere formül uygulamak mümkündür.

- Yerleşik fonksiyonları kullanarak.
- Eklenti fonksiyonlarını kullanarak.
- Dizi formülleri ile çalışma.
- Bir R1C1 formülü oluşturma.

## **Yerleşik Fonksiyonları Nasıl Kullanılır**

Yerleşik fonksiyonlar veya formüller, geliştirme sürecini kolaylaştırmak ve zamandan tasarruf etmek için hazır fonksiyonlar olarak sunulur. Aspose.Cells tarafından desteklenen yerleşik fonksiyonların [listesine](/cells/tr/nodejs-cpp/supported-formula-functions/) bakın. Fonksiyonlar alfabetik sıralı listelenmiştir. Gelecekte daha fazla fonksiyon desteklenecektir.

Aspose.Cells, Microsoft Excel tarafından sunulan çoğu formül veya fonksiyonu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablosu](/cells/tr/nodejs-cpp/what-is-a-designer-spreadsheet/) aracılığıyla kullanabilir. Aspose.Cells, çok geniş bir matematiksel, dize, Boolean, tarih/zaman, istatistiksel, veritabanı, arama ve referans formülleri seti sağlar.

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) özelliğini kullanarak hücreye formül ekleyin. Örneğin **Karmaşık formüller**

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, Aspose.Cells'te de desteklenir. Bir hücreye formül uygularken, her zaman dizeye bir eşitlik işareti (=) ile başlayın (Microsoft Excel'de formül oluştururken olduğu gibi) ve bir virgül (,) kullanarak fonksiyon parametrelerini ayırın.

Aşağıdaki örnekte, bir çalışma sayfasının [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun ilk hücresine karmaşık bir formül uygulanmıştır. Formül, Aspose.Cells tarafından sağlanan yerleşik bir **IF** fonksiyonunu kullanır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A4").setFormula("=SUM(A1:A3)");

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A4").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Eklenti Fonksiyonlarını Nasıl Kullanılır**

Excel'e dahil etmek istediğimiz bazı kullanıcı tanımlı formüllere excel eklentisi olarak eklemek istiyoruz. Hücre.Formül işlevi yerleşik fonksiyonları kullanırken sorunsuz çalışır, ancak eklenti fonksiyonlarını veya formülleri ayarlamak için bir ihtiyaç vardır.

Aspose.Cells, [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-) kullanarak eklenti fonksiyonlarını kaydetme özellikleri sağlar. Daha sonra hücre.Formül = anyFunctionFromAddIn şeklinde ayarlandığında, çıktı Excel dosyası, AddIn fonksiyonundan hesaplanan değeri içerir.

Aşağıdaki örnek kodda, eklenti fonksiyonunu kaydetmek için aşağıdaki XLAM dosyası indirilmelidir. Benzer şekilde, çıktı dosyası olan "test_udf.xlsx"yi indirerek çıktıyı kontrol edebilirsiniz.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Register macro enabled add-in along with the function name
const id = workbook.getWorksheets().registerAddInFunction(path.join(dataDir, "TESTUDF.xlam"), "TEST_UDF", false);

// Register more functions in the file (if any)
workbook.getWorksheets().registerAddInFunction(id, "TEST_UDF1"); // in this way you can add more functions that are in the same file

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first cell
const cell = worksheet.getCells().get("A1");

// Set formula name present in the add-in
cell.setFormula("=TEST_UDF()");

// Save workbook to output XLSX format.
workbook.save(path.join(outputDir, "test_udf.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Dizi Formülü Nasıl Kullanılır**

Dizi formüller, formülün bileşenlerine argüman olarak tek sayılar yerine dizileri alan formüllerdir. Dizi formülü gösterildiğinde, süslü parantezlerle ({}) çevrilidir.

Bazı Microsoft Excel fonksiyonları değerler dizileri döndürür. Bir dizi formülü ile birden çok sonucu hesaplamak için, diziyi formül argümanları olarak kullanarak aynı satır ve sütun sayısına sahip bir hücre aralığına girin.

Bir dizi formülünü, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) yöntemini çağırarak bir hücreye uygulamak mümkündür. [**setArrayFormula(string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setArrayFormula-string-number-number-) yöntemi aşağıdaki parametreleri alır:

- **Dizi Formülü**, dizi formülü.
- **Satır Sayısı**, dizi formülünün sonucunu doldurmak için satır sayısı.
- **Sütun Sayısı**, dizi formülünün sonuçlarını doldurmak için sütun sayısı.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a value to "A1" cell
worksheet.getCells().get("A1").putValue(1);

// Adding a value to "A2" cell
worksheet.getCells().get("A2").putValue(2);

// Adding a value to "A3" cell
worksheet.getCells().get("A3").putValue(3);

// Adding a value to B1
worksheet.getCells().get("B1").putValue(4);

// Adding a value to "B2" cell
worksheet.getCells().get("B2").putValue(5);

// Adding a value to "B3" cell
worksheet.getCells().get("B3").putValue(6);

// Adding a value to C1
worksheet.getCells().get("C1").putValue(7);

// Adding a value to "C2" cell
worksheet.getCells().get("C2").putValue(8);

// Adding a value to "C3" cell
worksheet.getCells().get("C3").putValue(9);

// Adding a SUM formula to "A4" cell
worksheet.getCells().get("A6").setArrayFormula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3);

// Calculating the results of formulas
workbook.calculateFormula();

// Get the calculated value of the cell
const value = worksheet.getCells().get("A6").getValue().toString();

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **R1C1 Formülünü Nasıl Kullanılır**

Bir **R1C1** referans stili formülünü, [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının [**getR1C1Formula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getR1C1Formula--) özelliği ile bir hücreye ekleyin.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Setting an R1C1 formula on the "A11" cell, 
// Row and Column indices are relative to destination index
worksheet.getCells().get("A11").setR1C1Formula("=SUM(R[-10]C[0]:R[-7]C[0])");

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Gelişmiş Konular**
- [Öncüler ve Bağımlılar](/cells/tr/nodejs-cpp/precedents-and-dependents/)
- [Formüllerde Harici Bağlantıları Ayarla](/cells/tr/nodejs-cpp/set-external-links-in-formulas/)
- [Yeni satırlara veri girilirken Tablo veya List Objesinde Formülü otomatik olarak çoğaltın](/cells/tr/nodejs-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Adlandırılmış Aralık için Formül Ayarlama](/cells/tr/nodejs-cpp/setting-formula-for-named-range/)
- [Formülleri Ayarlama - Diğer Dilleri Kullanan Kullanıcılar İçin Uyarı](/cells/tr/nodejs-cpp/setting-formulas-notice-for-non-english-users/)
- [Paylaşılan Formülü Ayarlama](/cells/tr/nodejs-cpp/setting-shared-formula/)
- [Paylaşılan Formülün Maksimum Satırlarını Belirtme](/cells/tr/nodejs-cpp/specify-maximum-rows-of-shared-formula/)
- [Desteklenen Excel İşlevleri](/cells/tr/nodejs-cpp/supported-formula-functions/)

