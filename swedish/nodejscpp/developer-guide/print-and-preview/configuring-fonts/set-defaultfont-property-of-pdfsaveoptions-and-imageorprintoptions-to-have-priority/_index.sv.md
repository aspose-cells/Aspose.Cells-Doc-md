---
title: Ställ in DefaultFont egenskapen för PdfSaveOptions och ImageOrPrintOptions för prioritet med Node.js via C++
linktitle: Ange egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions för att prioritera den
type: docs
weight: 30
url: /sv/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Upptäck hur du ställer in egenskapen DefaultFont för PdfSaveOptions och ImageOrPrintOptions med Aspose.Cells for Node.js via C++. Säkerställ korrekt fontrendering när typsnitt saknas.
---

## **Möjliga användningsscenario**

När du ställer in **DefaultFont**-egenskapen för [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) kan du förvänta dig att vid sparande till PDF eller bild kommer den inställda StandardFonten att gälla för all text i en arbetsbok som har en saknad (ej installerad) font.

 Generellt, när du sparar till PDF eller bild, kommer Aspose.Cells for Node.js via C++ först försöka att ställa in arbetsbokens standardfont (dvs. `Workbook.DefaultStyle.Font`). Om arbetsbokens standardfont fortfarande inte kan visa/rendra text korrekt, kommer Aspose.Cells att försöka rendera med fonten som nämns mot DefaultFont-attributet i [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/).

För att möta dina förväntningar har vi en boolesk egenskap som heter "**CheckWorkbookDefaultFont**" i [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Du kan ställa in den till **false** för att inaktivera försöket att använda arbetsbokens standardfont eller låta inställningen för **DefaultFont** i [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) ha prioritet.

## **Ange egenskapen DefaultFont för PdfSaveOptions/ImageOrPrintOptions**

Följande exempel kod öppnar en Excel-fil. A1-cellen (i det första kalkylbladet) har satt texten "Jul Tid Teckensnitt". Teckensnittsnamnet är "Christmas Time Personal Use" som inte är installerat på maskinen. Vi ställer in **DefaultFont**-attributet för [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) till "Times New Roman". Vi sätter också den booleska egenskapen **CheckWorkbookDefaultFont** till **"falsk"** vilket säkerställer att texten i A1-cellen renderas med "Times New Roman" teckensnitt och inte använder kalkylbladets standardteckensnitt ("Calibri" i detta fall). Koden renderar det första kalkylbladet till PNG och TIFF bildeformat. Slutligen renderas det till en PDF-fil.

{{% alert color="primary" %}}

Standardvärdet för egenskapen **CheckWorkbookDefaultFont** är **sant**.

{{% /alert %}}

Detta är skärmbilden av [mallfilen](49446913.xlsx) som används i exempelkoden.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Detta är utdata PNG-bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) till "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Se utdata [TIFF](48496672.tiff) bild efter att ha ställt in egenskapen [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) till "Times New Roman".

 Se utdata [PDF](48496673.pdf) fil efter att ha ställt in [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--)-egenskapen till "Times New Roman".

## **Exempelkod**

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
