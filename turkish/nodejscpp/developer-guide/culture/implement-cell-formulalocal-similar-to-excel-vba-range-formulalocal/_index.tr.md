---
title: Excel VBA Range.FormulaLocal ile benzer şekilde Cell.FormulaLocal uygulamasını Node.js ve C++ kullanarak gerçekleştirin
linktitle: Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal ı Uygula
type: docs
weight: 30
url: /tr/nodejs-cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Aspose.Cells for Node.js via C++ kullanarak Excel VBA Range.FormulaLocal ile benzer şekilde Cell.FormulaLocal uygulamasını yapmayı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Microsoft Excel formülleri farklı bölgelerde veya dillerde farklı isimlere sahip olabilir. Örneğin, **SUM** fonksiyonu Almanca'da **SUMME** olarak adlandırılır. Aspose.Cells, İngilizce olmayan fonksiyon isimleriyle çalışamaz. Microsoft Excel VBA'da, dil veya bölgeye göre fonksiyon adını döndüren **Range.FormulaLocal** özelliği vardır. Aspose.Cells for Node.js via C++ ayrıca bu amaçla [**Cell.getFormulaLocal()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getFormulaLocal--) özelliğini de sağlar. Ancak, bu özellik yalnızca [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) metodunu uyguladığınızda çalışır.

## **Excel VBA Range.FormulaLocal benzeri Cell.FormulaLocal'ı uygulamanın nasıl olduğunu aşağıdaki örnek kod açıklar. Metod, standart fonksiyonun yerel adını döndürür. Standart fonksiyon adı **SUM** ise **UserFormulaLocal_SUM** döndürür. Kodu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını döndürebilirsiniz, örneğin **SUM** Almanca'da **SUMME** ve Rusça'da **TEXT** için **ТЕКСТ** olur. Lütfen aşağıdaki örnek kodun konsol çıktısını inceleyin.**

Aşağıdaki örnek kod, [**GlobalizationSettings.getLocalFunctionName(standardName)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getLocalFunctionName-string-) metodunun nasıl uygulanacağını açıklar. Metod, standart fonksiyonun yerel adını döner. Eğer standart fonksiyon adı **SUM** ise, **UserFormulaLocal_SUM** döner. Kodunuzu ihtiyaçlarınıza göre değiştirebilir ve doğru yerel fonksiyon adlarını dönebilirsiniz, örn. **SUM** Almanca'da **SUMME**, **TEXT** Rusça'da **ТЕКСТ**. Ayrıca, aşağıdaki örnek kodun konsol çıktısına bakmak faydalı olacaktır.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");

class GS extends AsposeCells.GlobalizationSettings {
getLocalFunctionName(standardName) {
// Change the SUM function name as per your needs.
if (standardName === "SUM") {
return "UserFormulaLocal_SUM";
}

// Change the AVERAGE function name as per your needs.
if (standardName === "AVERAGE") {
return "UserFormulaLocal_AVERAGE";
}

return "";
}
}

function run() {
// Create workbook
const wb = new AsposeCells.Workbook();

// Assign GlobalizationSettings implementation class
wb.getSettings().setGlobalizationSettings(new GS());

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access some cell
const cell = ws.getCells().get("C4");

// Assign SUM formula and print its FormulaLocal
cell.setFormula("SUM(A1:A2)");
console.log("Formula Local: " + cell.getFormulaLocal());

// Assign AVERAGE formula and print its FormulaLocal
cell.setFormula("=AVERAGE(B1:B2, B5)");
console.log("Formula Local: " + cell.getFormulaLocal());
}

// Call the run function
run();
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
