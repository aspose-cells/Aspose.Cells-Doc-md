---
title: JavaScript kullanarak C++ ile PdfSaveOptions ve ImageOrPrintOptions in DefaultFont özelliğini öncelikli olacak şekilde ayarla
linktitle: PdfSaveOptions ve ImageOrPrintOptions ın DefaultFont özelliğinin önceliği olması
type: docs
weight: 30
url: /tr/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: C++ ile Aspose.Cells for JavaScript kullanarak PdfSaveOptions ve ImageOrPrintOptions in DefaultFont özelliğini ayarlama yöntemlerini keşfedin. Fontlar eksik olduğunda düzgün font işleme sağlayın.
---

## **Olası Kullanım Senaryoları**

[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) ve [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) **DefaultFont** özelliğini ayarlarken, PDF veya görüntüye kaydetmenin eksik (yüklü olmayan) bir yazı tipi karakterine sahip çalışma kitabındaki tüm metni ayarlayacağınızı bekleyebilirsiniz.

Genellikle, PDF veya resme kaydederken, C++ ile Aspose.Cells for JavaScript önce Çalışma Kitabı'nın varsayılan fontunu (yani, `Workbook.DefaultStyle.Font`) ayarlamaya çalışır. Eğer çalışma kitabının varsayılan fontu metni düzgün gösteremiyorsa veya render edemiyorsa, Aspose.Cells belirtilen varsayılan font ile render etmeye çalışacaktır. 

Beklentinize uyum sağlamak için, [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)'de "**CheckWorkbookDefaultFont**" adında bir Boolean özelliğimiz bulunmaktadır. Bu, çalışma kitabının varsayılan yazı tipini denemeyi devre dışı bırakmak için **false** olarak ayarlayabilir veya **CheckWorkbookDefaultFont** özelliğinin önceliği olmasını sağlamak için [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)'deki **DefaultFont** ayarına öncelik verebilirsiniz.

## **PdfSaveOptions/ImageOrPrintOptions'ın DefaultFont özelliğini ayarlayın**

Aşağıdaki örnek kod, bir Excel dosyasını açar. İlk çalışma sayfasındaki A1 hücresinde "Christmas Time Font text" metni ayarlanmıştır. Yazı tipi adı "Christmas Time Personal Use" olup, makineye yüklenmemiştir. {0}/{1} içindeki **DefaultFont** özniteliğini "Times New Roman" olarak ayarlarız. Ayrıca, {2}/{3} içindeki Boolean özellik olan **CheckWorkbookDefaultFont**'u **"false"** olarak ayarlarız, böylece A1 hücresinin metni "Times New Roman" fontu ile render edilir ve çalışma kitabının varsayılan fontu (bu durumda "Calibri") kullanılmaz. Kod, ilk çalışma sayfasını PNG ve TIFF görüntü formatlarına render eder. Son olarak, PDF dosya formatına render edilir.

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont** özelliğinin varsayılan değeri **true**'dur.

{{% /alert %}}

Bu, örnek kodda kullanılan [şablon dosyası](49446913.xlsx) ekran görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

Bu, [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) özelliği "Times New Roman" olarak ayarlandıktan sonra oluşan çıktı PNG görüntüsüdür.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

[**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) özelliği "Times New Roman" olarak ayarlandıktan sonra ortaya çıkan [TIFF](48496672.tiff) görüntüsüne bakın.

Ayarlandıktan sonra çıkan [PDF](48496673.pdf) dosyasına bakın.

## **Örnek Kod**

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
