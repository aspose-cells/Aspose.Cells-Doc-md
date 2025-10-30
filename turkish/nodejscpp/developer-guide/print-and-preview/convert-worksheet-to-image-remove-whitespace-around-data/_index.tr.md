---
title: İçeriğin etrafındaki boşluğu kaldırmak ve çalışma sayfasını resme dönüştürmek için Node.js ve C++ ile.
linktitle: Elektronik tabloyu Görüntüye Dönüştür  Veri Etrafındaki Boşlukları Kaldırma
type: docs
weight: 40
url: /tr/nodejs-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: Microsoft Excel çalışma sayfalarını görsellere dönüştürmeyi öğrenin ve Aspose.Cells for Node.js via C++ kullanarak verilerin etrafındaki boşluğu kaldırın. 
---

{{% alert color="primary" %}}

Bazen, çalışma sayfalarını uygulamalarda veya web sayfalarında sunmanız gerekebilir. Örneğin, çalışma sayfalarını bir Word belgesine, bir PDF dosyasına, bir PowerPoint sunumuna veya başka bir belgeye yerleştirmeniz gerekebilir. Temelde, bir çalışma sayfasını bir görüntü olarak oluşturmak ve başka uygulamalara yapıştırmak istersiniz. Aspose.Cells, Microsoft Excel çalışma sayfalarını görüntülere dönüştürmenizi sağlar.

{{% /alert %}}

## **Veri Etrafındaki Boşlukları Kaldır**

[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API'si, örneğin görüntü biçimi, sayfa sayfalama çalışma sayfaları vb. gibi belirli özelliklere sahip bir çalışma sayfasını bir görüntü dosyasına dönüştürür. BMP, GIF, JPG, TIFF ve EMF gibi birçok görüntü formatı desteklenir.

Sayfa görüntüleme özelliğini kullandığınızda, çıktı görüntüsü varsayılan olarak etrafında boşluk bulunur. Bu, kaynak çalışma sayfası için üst, alt, sol ve sağ sayfa düzeni kenarlarını 0 olarak ayarlayarak ve buna uygun [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) özniteliklerini belirleyerek kaldırabilirsiniz.

Aşağıdaki kod parçası, çıktı görüntüsündeki veri etrafındaki boşluğu kaldırır.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");

// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);

// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);

// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
