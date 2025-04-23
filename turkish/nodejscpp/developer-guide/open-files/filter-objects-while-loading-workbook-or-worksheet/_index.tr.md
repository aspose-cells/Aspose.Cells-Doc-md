---
title: Node.js ile C++ kullanarak Çalışma Kitabı veya Çalışma Sayfasını Yüklerken Nesneleri Filtrele
linktitle: Çalışma Kitabı veya Çalışsayfa Yüklenirken Nesneleri Filtrele
type: docs
weight: 330
url: /tr/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitapları veya çalışma sayfaları yüklerken verileri nasıl filtreleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**
Verileri filtrelerken [LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) özelliğini kullanın. Ancak, bireysel çalışma sayfalarından veri filtrelemek istiyorsanız, [LoadFilter.startSheet(Worksheet)] metodunu geçersiz kılmanız gerekecek. Lütfen, [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) enumundan uygun değeri sağlayın ve [LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter) ile çalışırken kullanın.

 [LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) enumunun olası değerleri şunlardır.

- Tümü
- KitapAyarları
- HücreBoş
- HücreBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Chart
- ConditionalFormatting
- DataValidation
- DefinedNames
- DocumentProperties
- Formula
- Hyperlinkler
- MergedArea
- PivotTable
- Settings
- Shape
- SheetData
- SheetSettings
- Structure
- Style
- Table
- VBA
- XmlMap

## **Çalışma Kitabını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kodlar, çalışma kitabından grafikleri filtrelemenin nasıl yapıldığını göstermektedir. Lütfen bu kodda kullanılan [örnek excel dosyasını](5115258.xlsx) ve bunun tarafından oluşturulan [çıktı PDF'yi](5115257.pdf) kontrol edin. Çıktı PDF'de, tüm grafiklerin çalışma kitabından filtrelenmiş olduğunu görebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **Çalışma Sayfasını Yüklerken Filtreleme Nesneleri**
Aşağıdaki örnek kod, [kaynak excel dosyasını](5115255.xlsx) yükler ve çalışma sayfalarından aşağıdaki verileri özel bir filtreden geçirir.

- Tablo adı NoCharts olan çalışma sayfasından Grafikleri filtreler.
- Tablo adı NoShapes olan çalışma sayfasından Şekilleri filtreler.
- Tablo adı NoConditionalFormatting olan çalışma sayfasından Koşullu Biçimlendirmeyi filtreler.

Özel bir filtreden sonra [kaynak excel dosyasını](5115255.xlsx) yüklediğinde, tüm çalışma sayfalarının resimlerini sırayla alır. Referansınız için çıktı resimleri aşağıdadır. Görebileceğiniz gibi, ilk resimde grafik yok, ikinci resimde şekiller yok ve üçüncü resimde koşullu biçimlendirme yok.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

Bu, özel filtrenin çalışma sayfası adlarına göre nasıl kullanılacağının örneğidir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
