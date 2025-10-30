---  
title: ExcelファイルをPDF/A 1a互換のPDFフォーマットに変換します。  
linktitle: ExcelファイルをPDF/A 1a互換のPDF形式に変換します  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: ExcelファイルをPDF/A準拠のPDFファイルに変換する方法をAspose.Cells for Node.js via C++を使用して学びます。  
---  

## **可能な使用シナリオ**  

PDF/Aは、長期保存のために設計されたPDFのユニークなバージョンです。PDF/Aは、ISO標準化されたPDF（ポータブルドキュメントフォーマット）のバージョンであり、すべてのフォントをPDF内に埋め込むアーカイブ用フォーマットです。PDF/Aは、フォントリンク（フォントの埋め込みではなくリンク）や暗号化などの機能を禁止しており、Aspose.Cells for Node.js via C++を使用してExcelファイルをPDF/A準拠のPDFファイル（PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab、PDF/A-3uをサポート）に保存できます。このトピックでは、ExcelブックをPDF/A準拠（PDF/A-1a）PDFファイルに保存する方法について説明します。  

## **ExcelファイルをPDF形式に変換して、PDF/A-1aと互換性がある形式にする方法**  

開発者は[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)クラスを使用して変換のさまざまな属性を設定できます。[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)クラスの異なるプロパティを設定することで、出力されるPDFの印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは[**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)で、ExcelファイルをPDF/Aに準拠したPDFファイルとして保存可能です。  

次のサンプルコードは、ExcelファイルをPDF/A-1aに対応したPDFフォーマットに変換する方法を説明しています。その[出力PDF](outputCompliancePdfA1a.pdf)およびスクリーンショットを参考にしてください。  

## **スクリーンショット**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
