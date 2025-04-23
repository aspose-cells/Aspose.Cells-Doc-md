---
title: Node.js ile C++ kullanarak Formülleri Hesapla
linktitle: Formülleri Hesapla
description: Bu makale, Aspose.Cells kütüphanesini kullanarak Node.js üzerinden C++ ile Microsoft Excel’de formüllerin nasıl hesaplanacağını tanıtmaktadır. Var olan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan metodları kullanarak formülü hesaplayabilir ve sonucu alabilirsiniz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, formüller, hesaplamalar, Formülün Doğrudan Hesaplanması, Formülleri Tekrar Hesapla, Node.js ile C++ kullanımıyla formüller ekleme
type: docs
weight: 125
url: /tr/nodejs-cpp/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells gömülü bir formül hesaplama motoruna sahiptir. Tasarımcı şablonlarından ithal edilen formülleri tekrar hesaplamanın yanı sıra, çalışma zamanında eklenen formüllerin sonuçlarını da hesaplamayı destekler.

Aspose.Cells, Microsoft Excel'in (desteklenen fonksiyonların listesini [bu bağlantıda]( /cells/tr/nodejs-cpp/supported-formula-functions/ ) bulabilirsiniz) birçoğu ile uyumlu formülleri veya fonksiyonları destekler. Bu fonksiyonlar API'ler veya tasarımcı tabloları aracılığıyla kullanılabilir. Aspose.Cells, matematiksel, dize, mantıksal, tarih/zaman, istatistiksel, veritabanı, arama ve referans formüllerinin büyük bir kümesine destek sağlar.

Bir hücreye formül eklemek için [**getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormula--) sınıfının [**setFormula(string, object)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setFormula-string-object-) özelliği veya [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) metodunu kullanın. Bir formül uygularken, her zaman Microsoft Excel'de formül oluştururken yaptığınız gibi eşittir (=) ile başlayın ve fonksiyon parametrelerini ayırmak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı [**calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) metodunu çağırabilir; bu metod, bir Excel dosyasına gömülü tüm formülleri işler. Alternatif olarak, yine [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfının [**calculateFormula(string)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-) metodunu çağırarak, bir sayfaya gömülü tüm formülleri işleyebilirsiniz. Ayrıca, yalnızca bir Hücre’nin formülünü işleyen [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#calculate-calculationoptions-) metodunu da çağırabilirsiniz:

```javascript
const path = require("path");
const fs = require("fs");
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

### **Formüller İçin Bilinmesi Gerekenler**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının **Formül** özelliği ve **setFormula(...)** metodları, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ve [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıflarının **calculate** metodlarından farklı çalışır. Bu **Formül** özelliği ve **setFormula(...)** metodları, formülü yalnızca hücreye ekler, ancak çalışma zamanı sonucunu hesaplamaz. Formüllerin sonucunu almak için lütfen **calculate** metodlarını çağırın.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

B sometimes, doğrudan formül sonuçlarını hesaplamanız gerekebilir, ve bu sonuçları çalışma sayfasına eklemeden de yapabilirsiniz. Formülde kullanılan hücrelerin değerleri zaten bir çalışma sayfasında mevcuttur ve sizin yapmanız gereken, bu değerlerin sonucunu Microsoft Excel formülleri kullanarak bulmaktır, formülü çalışma sayfasına ekmeden.

Aspose.Cells’ın formül hesaplama motoru API’lerini kullanarak, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) ile [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) arasındaki formüllerin sonuçlarını, bunları çalışma sayfasına eklemeden alabilirsiniz:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put 20 in cell A1
const cellA1 = worksheet.getCells().get("A1");
cellA1.putValue(20);

// Put 30 in cell A2
const cellA2 = worksheet.getCells().get("A2");
cellA2.putValue(30);

// Calculate the Sum of A1 and A2
const results = worksheet.calculateFormula("=Sum(A1:A2)");

// Print the output
console.log("Value of A1: " + cellA1.getStringValue());
console.log("Value of A2: " + cellA2.getStringValue());
console.log("Result of Sum(A1:A2): " + results.toString());
```

Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri tekrar tekrar hesaplama**

Çok sayıda formül bulunduğunda ve sadece küçük bir kısmını değiştirilerek tekrar hesaplanması gerekiyorsa, performans açısından hesaplama zincirini etkinleştirmek faydalı olabilir: [**formulaSettings.getEnableCalculationChain()**](https://reference.aspose.com/cells/nodejs-cpp/formulasettings/#getEnableCalculationChain--).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load the template workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Print the time before formula calculation
console.log(new Date());

// Set the CreateCalcChain as true
workbook.getSettings().getFormulaSettings().setEnableCalculationChain(true);

// Calculate the workbook formulas
workbook.calculateFormula();

// Print the time after formula calculation
console.log(new Date());

// Change the value of one cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("newvalue");

// Re-calculate those formulas which depend on cell A1
workbook.calculateFormula();
```

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak, hesaplama zinciri devre dışıdır. Zincirin oluşturulması ek zaman alır, bu yüzden ilk defa formülleri ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)) hesaplarken, zincirsiz hesaplamaya kıyasla daha fazla CPU işlem süresi ve belleğin kullanılması muhtemeldir. Eğer kullanıcı formülleri tekrar tekrar hesaplamıyorsa, varsayılan davranış (formülü doğrudan hesaplama ve hesaplama Zinciri oluşturmama) daha iyi olur.

{{% /alert %}}

## **Gelişmiş Konular**
- [Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme](/cells/tr/nodejs-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells ile IFNA işlevinin hesaplanması](/cells/tr/nodejs-cpp/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formül Hesaplama](/cells/tr/nodejs-cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/nodejs-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Hücre.hesapla metodunun Hesaplama Süresini Azaltın](/cells/tr/nodejs-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Dairesel Referansı Algılama](/cells/tr/nodejs-cpp/detecting-circular-reference/)
- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/nodejs-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/nodejs-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek](/cells/tr/nodejs-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/nodejs-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/nodejs-cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'te FormulaText Fonksiyonu Kullanma](/cells/tr/nodejs-cpp/using-formulatext-function-in-aspose-cells/)
