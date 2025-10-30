---
title: PdfSaveOptions ve ImageOrPrintOptions özelliklerinin DefaultFont ayarını Node.js ile C++ kullanarak öncelikli hale getirin
linktitle: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Aspose.Cells for Node.js via C++ kullanarak PdfSaveOptions ve ImageOrPrintOptions nesnelerinin DefaultFont özelliğini nasıl ayarlayacağınızı keşfedin. Yazı tipleri eksik olduğunda uygun yazı tipi görünümünü sağlayın.
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) **DefaultFont** özelliğini ayarlarken, PDF veya görüntüye kaydetmenin eksik (yüklü olmayan) bir yazı tipi karakterine sahip çalışma kitabındaki tüm metni ayarlayacağınızı bekleyebilirsiniz.

Genellikle, PDF veya görsele kaydederken, Aspose.Cells for Node.js via C++ ilk olarak çalışma kitabının varsayılan yazı tipini (yani `Workbook.DefaultStyle.Font`) ayarlamaya çalışır. Eğer çalışma kitabının varsayılan yazı tipi düzgün metin gösterebilir veya render edemezse, Aspose.Cells yukarıda belirtilen DefaultFont özelliklerine uygun yazı tipleriyle render yapmaya çalışacaktır.

Beklentinize uyum sağlamak için, [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)'de "**CheckWorkbookDefaultFont**" adında bir Boolean özelliğimiz bulunmaktadır. Bu, çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakmak için **false** olarak ayarlayabilir veya **CheckWorkbookDefaultFont** özelliğinin önceliği olmasını sağlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)'deki **DefaultFont** ayarına öncelik verebilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyasını açar. İlk çalışma sayfasındaki A1 hücresinde "Christmas Time Font text" metni ayarlanmıştır. Yazı tipi adı "Christmas Time Personal Use" olup, makineye yüklenmemiştir. {0}/{1} içindeki **DefaultFont** özniteliğini "Times New Roman" olarak ayarlarız. Ayrıca, {2}/{3} içindeki Boolean özellik olan **CheckWorkbookDefaultFont**'u **"false"** olarak ayarlarız, böylece A1 hücresinin metni "Times New Roman" fontu ile render edilir ve çalışma kitabının varsayılan fontu (bu durumda "Calibri") kullanılmaz. Kod, ilk çalışma sayfasını PNG ve TIFF görüntü formatlarına render eder. Son olarak, PDF dosya formatına render edilir.

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446913.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliği "Times New Roman" olarak ayarlandıktan sonra oluşan çıktı PNG görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) özelliği "Times New Roman" olarak ayarlandıktan sonra ortaya çıkan [TIFF](48496672.tiff) görüntüsüne bakın.

Ayarlandıktan sonra çıkan [PDF](48496673.pdf) dosyasına bakın.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
