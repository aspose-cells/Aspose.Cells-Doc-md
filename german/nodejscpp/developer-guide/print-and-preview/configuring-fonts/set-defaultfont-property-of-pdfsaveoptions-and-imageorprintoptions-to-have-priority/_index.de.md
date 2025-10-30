---
title: Setzen der DefaultFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions mit Node.js über C++
linktitle: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Entdecken Sie, wie man die DefaultFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions mit Aspose.Cells for Node.js via C++ festlegt. Sicherstellen einer korrekten Schriftartdarstellung, wenn Schriftarten fehlen.
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) könnten Sie erwarten, dass beim Speichern als PDF oder Bild dieser DefaultFont auf den gesamten Text in einer Arbeitsmappe angewendet wird, der eine fehlende (nicht installierte) Schriftart hat.

 Im Allgemeinen versucht Aspose.Cells for Node.js via C++ beim Speichern in PDF oder Bild zunächst, die Standardschriftart der Arbeitsmappe zu setzen (d.h. `Workbook.DefaultStyle.Font`). Wenn die Standardschriftart der Arbeitsmappe weiterhin keinen Text richtig anzeigen/Rendern kann, wird Aspose.Cells versuchen, mit der gegen die DefaultFont-Attribut in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) genannten Schriftart zu rendern.

Um Ihren Erwartungen gerecht zu werden, haben wir eine boolesche Eigenschaft mit dem Namen "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/). Sie können es auf **false** setzen, um das Versuches der Verwendung der Standard-Schriftart der Arbeitsmappe zu deaktivieren oder die Einstellung **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) die Priorität zu haben lassen.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Der folgende Beispielcode öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) enthält den Text "Christmas Time Font text". Der Schriftartname ist "Christmas Time Personal Use", die auf dem Computer nicht installiert ist. Wir setzen das Attribut **DefaultFont** von [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) auf "Times New Roman". Wir setzen auch die boolesche Eigenschaft **CheckWorkbookDefaultFont** auf **"false"**, was sicherstellt, dass der Text der A1-Zelle mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart des Arbeitsbuchs (in diesem Fall "Calibri") verwendet wird. Der Code rendert das erste Arbeitsblatt in die Formate PNG und TIFF. Schließlich wird in das PDF-Format gerendert.

{{% alert color="primary" %}}

Der Standardwert der Eigenschaft **CheckWorkbookDefaultFont** ist **true**.

{{% /alert %}}

Dies ist der Screenshot der im Beispielcode verwendeten [Vorlagendatei](49446913.xlsx).

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Siehe das Ausgabe-[TIFF](48496672.tiff)-Bild nach Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf "Times New Roman".

Siehe die Ausgabe-[PDF](48496673.pdf)-Datei nach Setzen der [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--)-Eigenschaft auf "Times New Roman".

## **Beispielcode**

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
