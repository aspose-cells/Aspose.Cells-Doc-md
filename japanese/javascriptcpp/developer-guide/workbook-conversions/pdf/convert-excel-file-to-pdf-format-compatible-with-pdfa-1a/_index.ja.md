---
title: ExcelファイルをPDF/A 1a互換のPDFフォーマットに変換します（C++のJavaScript経由）
linktitle: ExcelファイルをPDF/A 1a互換のPDF形式に変換します
type: docs
weight: 130
url: /ja/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: PDF/Aは、長期保存のために設計されたPDFの特殊なバージョンです。ISO標準化されたPDFのアーカイブフォーマットで、使用されているフォントをすべて埋め込みます。PDFと異なり、フォントリンク（フォント埋め込みではなく）や暗号化などの機能を禁止しています。Aspose.Cells for JavaScriptを使えば、ExcelファイルをPDF/A準拠のPDFに保存できます（PDF/A 1a、PDF/A 1b、PDF/A 2a、PDF/A 2b、PDF/A 2u、PDF/A 3a、PDF/A 2ab、PDF/A 3uをサポート）。
---

## **可能な使用シナリオ**  

PDF/A is a unique flavor of PDF designed for the long-term preservation of documents. PDF/A is an ISO-standardized version of the Portable Document Format (PDF) which is an archival format of PDF that embeds all fonts used in the document within the PDF file. PDF/A differs from PDF by prohibiting features, such as font linking (as opposed to font embedding) and encryption. Aspose.Cells for JavaScript via C++ enables you to save the Excel files to PDF/A compliant PDF files (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, and PDF/A-3u are supported). This topic describes how to save the Excel workbook to PDF/A compliant (PDF/A-1a) PDF file.  

## **ExcelファイルをPDF形式に変換して、PDF/A-1aと互換性がある形式にする方法**  

開発者は[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)クラスを使用して変換のさまざまな属性を設定できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)クラスの異なるプロパティを設定することで、出力されるPDFの印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--)で、ExcelファイルをPDF/Aに準拠したPDFファイルとして保存可能です。  

次のサンプルコードは、ExcelファイルをPDF/A-1aに対応したPDFフォーマットに変換する方法を説明しています。その[出力PDF](outputCompliancePdfA1a.pdf)およびスクリーンショットを参考にしてください。  

## **スクリーンショット**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
