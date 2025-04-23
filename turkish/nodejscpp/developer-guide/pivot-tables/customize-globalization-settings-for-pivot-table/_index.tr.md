---
title: Globalizasyon Ayarlarını Node.js ve C++ kullanarak Pivot Tablosu için Özelleştir
linktitle: Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir
type: docs
weight: 50
url: /tr/nodejs-cpp/customize-globalization-settings-for-pivot-table/
---

## **Olası Kullanım Senaryoları**

Bazen, *Toplam, Alt Toplam, Genel Toplam, Tüm Öğeler, Çoklu Öğeler, Sütun Etiketleri, Satır Etiketleri, Boş Değerler* metinlerini ihtiyacınıza göre özelleştirmek isteyebilirsiniz. Aspose.Cells for Node.js via C++, pivot tablonuzun globalizasyon ayarlarını özelleştirmenize olanak tanır. Bu özelliği kullanarak bu metinleri Arapça, Hintçe, Lehçe gibi başka dillere de çevirebilirsiniz.

## **Pivot Tablo için Küreselleştirme Ayarlarını Özelleştir**

Aşağıdaki örnek kod, pivot tablosu için globalizasyon ayarlarını nasıl özelleştireceğinizi gösterir. Bu, temel sınıf [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) türetilmiş *CustomPivotTableGlobalizationSettings* sınıfını oluşturur ve tüm gerekli yöntemleri geçersiz kılar. Bu yöntemler, *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* için özelleştirilmiş metni döndürür. Ardından bu sınıfın nesnesi [**WorkbookSettings.getPivotSettings()**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getPivotSettings--) özelliğine atanır. Kod, pivot tablo içeren [kaynak excel dosyasını](40468488.xlsx) yükler, yeniler ve hesaplar, ve sonuçları [çıkış PDF'sine](40468487.pdf) kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çıktı PDF üzerindeki etkisini gösterir. Ekran görüntüsünde görebileceğiniz gibi, pivot tablonun farklı bölümlerinde artık [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/pivotglobalizationsettings/) sınıfının metodlarıyla döndürülen özelleştirilmiş metinler yer alıyor.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class CustomPivotTableGlobalizationSettings extends AsposeCells.PivotGlobalizationSettings {
// Gets the name of "Total" label in the PivotTable.
getTextOfTotal() {
console.log("---------GetPivotTotalName-------------");
return "AsposeGetPivotTotalName";
}

// Gets the name of "Grand Total" label in the PivotTable.
getTextOfGrandTotal() {
console.log("---------GetPivotGrandTotalName-------------");
return "AsposeGetPivotGrandTotalName";
}

// Gets the name of "(Multiple Items)" label in the PivotTable.
getTextOfMultipleItems() {
console.log("---------GetMultipleItemsName-------------");
return "AsposeGetMultipleItemsName";
}

// Gets the name of "(All)" label in the PivotTable.
getTextOfAll() {
console.log("---------GetAllName-------------");
return "AsposeGetAllName";
}

// Gets the name of "Column Labels" label in the PivotTable.
getTextOfColumnLabels() {
console.log("---------GetColumnLabelsOfPivotTable-------------");
return "AsposeGetColumnLabelsOfPivotTable";
}

// Gets the name of "Row Labels" label in the PivotTable.
getTextOfRowLabels() {
console.log("---------GetRowLabelsNameOfPivotTable-------------");
return "AsposeGetRowLabelsNameOfPivotTable";
}

// Gets the name of "(blank)" label in the PivotTable.
getTextOfEmptyData() {
console.log("---------GetEmptyDataName-------------");
return "(blank)AsposeGetEmptyDataName";
}

// Gets the name of PivotFieldSubtotalType type in the PivotTable.
getTextOfSubTotal(subTotalType) {
console.log("---------GetSubTotalName-------------");

switch (subTotalType) {
case AsposeCells.PivotFieldSubtotalType.Sum:
return "AsposeSum";

case AsposeCells.PivotFieldSubtotalType.Count:
return "AsposeCount";

case AsposeCells.PivotFieldSubtotalType.Average:
return "AsposeAverage";

case AsposeCells.PivotFieldSubtotalType.Max:
return "AsposeMax";

case AsposeCells.PivotFieldSubtotalType.Min:
return "AsposeMin";

case AsposeCells.PivotFieldSubtotalType.Product:
return "AsposeProduct";

case AsposeCells.PivotFieldSubtotalType.CountNums:
return "AsposeCount";

case AsposeCells.PivotFieldSubtotalType.Stdev:
return "AsposeStdDev";

case AsposeCells.PivotFieldSubtotalType.Stdevp:
return "AsposeStdDevp";

case AsposeCells.PivotFieldSubtotalType.Var:
return "AsposeVar";

case AsposeCells.PivotFieldSubtotalType.Varp:
return "AsposeVarp";
}

return "AsposeSubTotalName";
}
}

async function run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePivotTableGlobalizationSettings.xlsx"));

workbook.getSettings().setGlobalizationSettings(new AsposeCells.GlobalizationSettings());

// Setting Custom Pivot Table Globalization Settings
workbook.getSettings().getGlobalizationSettings().setPivotSettings(new CustomPivotTableGlobalizationSettings());

// Hide first worksheet that contains the data of the pivot table
workbook.getWorksheets().get(0).setIsVisible(false);

// Access second worksheet
const ws = workbook.getWorksheets().get(1);

// Access the pivot table, refresh and calculate its data
const pt = ws.getPivotTables().get(0);
pt.setRefreshDataFlag(true);
pt.refreshData();
pt.calculateData();
pt.setRefreshDataFlag(false);

// Pdf save options - save entire worksheet on a single pdf page
const options = new AsposeCells.PdfSaveOptions();
options.setOnePagePerSheet(true);

// Save the output pdf 
workbook.save(path.join(dataDir, "outputPivotTableGlobalizationSettings.pdf"), options);
}

run().catch(console.error);
```
