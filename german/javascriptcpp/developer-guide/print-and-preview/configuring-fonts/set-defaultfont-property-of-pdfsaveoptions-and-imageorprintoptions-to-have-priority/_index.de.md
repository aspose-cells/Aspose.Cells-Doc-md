---
title: Setzen Sie die DefaultFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions mit JavaScript via C++ mit Priorität
linktitle: StandardFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions Priorität einräumen
type: docs
weight: 30
url: /de/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Entdecken Sie, wie Sie die DefaultFont Eigenschaft von PdfSaveOptions und ImageOrPrintOptions mit Aspose.Cells for JavaScript via C++ einstellen. Stellen Sie eine ordnungsgemäße Schriftartendarstellung sicher, wenn Schriftarten fehlen.
---

## **Mögliche Verwendungsszenarien**

Beim Setzen der **DefaultFont**-Eigenschaft von [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) und [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) könnten Sie erwarten, dass beim Speichern als PDF oder Bild dieser DefaultFont auf den gesamten Text in einer Arbeitsmappe angewendet wird, der eine fehlende (nicht installierte) Schriftart hat.

Im Allgemeinen versucht Aspose.Cells for JavaScript via C++, beim Speichern in PDF oder Bild zunächst die Standardschriftart des Arbeitsbuchs festzulegen (d.h. `Workbook.DefaultStyle.Font`). Wenn die Standard-Schriftart des Arbeitsbuchs immer noch keine Texte richtig anzeigen/rendern kann, wird Aspose.Cells versuchen, mit der in [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) genannten Schriftart zu rendern. 

Um Ihren Erwartungen gerecht zu werden, haben wir eine boolesche Eigenschaft mit dem Namen "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Sie können es auf **false** setzen, um das Versuches der Verwendung der Standard-Schriftart der Arbeitsmappe zu deaktivieren oder die Einstellung **DefaultFont** in [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) die Priorität zu haben lassen.

## **StandardFont-Eigenschaft von PdfSaveOptions/ImageOrPrintOptions festlegen**

Der folgende Beispielcode öffnet eine Excel-Datei. Die Zelle A1 (im ersten Arbeitsblatt) enthält den Text "Christmas Time Font text". Der Schriftartname ist "Christmas Time Personal Use", die auf dem Computer nicht installiert ist. Wir setzen das Attribut **DefaultFont** von [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) auf "Times New Roman". Wir setzen auch die boolesche Eigenschaft **CheckWorkbookDefaultFont** auf **"false"**, was sicherstellt, dass der Text der A1-Zelle mit der Schriftart "Times New Roman" gerendert wird und nicht die Standardschriftart des Arbeitsbuchs (in diesem Fall "Calibri") verwendet wird. Der Code rendert das erste Arbeitsblatt in die Formate PNG und TIFF. Schließlich wird in das PDF-Format gerendert.

{{% alert color="primary" %}}

Der Standardwert der Eigenschaft **CheckWorkbookDefaultFont** ist **true**.

{{% /alert %}}

Dies ist der Screenshot der im Beispielcode verwendeten [Vorlagendatei](49446913.xlsx).

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Dies ist das Ausgabe-PNG-Bild nach Setzen der [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-Eigenschaft auf "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

Siehe das Ausgabe-[TIFF](48496672.tiff)-Bild nach Setzen der [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--)-Eigenschaft auf "Times New Roman".

Siehe die Ausgabe-[PDF](48496673.pdf)-Datei nach Setzen der [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--)-Eigenschaft auf "Times New Roman".

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
