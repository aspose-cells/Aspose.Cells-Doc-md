---
title: HTML with Node.js via C++
linktitle: HTML
type: docs
weight: 230
url: /nodejs-cpp/convert-excel-to-html/
---

## **Converting Excel Workbook to HTML**
The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) class to provide the flexibility to control several aspects of the output HTML.

The code example below shows how to save a workbook as an HTML file using Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **Converting Excel Workbook to MHTML Files**
MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension. Aspose.Cells supports reading and writing MHTML files.

The code example below shows how to save a workbook as an MHTML file using Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **Advance topics**
- [AutoFit Columns and Rows while loading HTML in Workbook](/cells/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Avoid exponential notation of large numbers while importing from HTML](/cells/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Change the HTML Link Target Type](/cells/nodejs-cpp/change-the-html-link-target-type/)
- [Convert Excel to HTML with tooltip](/cells/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Delete redundant spaces after line break while importing HTML](/cells/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disable Downlevel Revealed Comments while saving to HTML](/cells/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disable Exporting Frame Scripts and Document Properties](/cells/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Use PresentationPreference Option for Better Layout](/cells/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Exclude Unused Styles during Excel to HTML conversion](/cells/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expanding text from right to left while exporting Excel file to HTML](/cells/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion](/cells/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Export Comments while Saving Excel file to HTML](/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Export Document Workbook and Worksheet Properties in Excel to HTML conversion](/cells/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Export Excel to HTML with GridLines](/cells/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Export print area range to HTML](/cells/nodejs-cpp/export-print-area-range-to/)
- [Export similar Border Style when Border Style is not supported by Web Browsers](/cells/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Export Worksheet CSS Separately in Output HTML](/cells/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Hiding Overlaid Content with CrossHideRight while saving to HTML](/cells/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefix Table Elements Styles with HtmlSaveOptions.TableCssId property](/cells/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Prevent Exporting Hidden Worksheet Contents on Saving to HTML](/cells/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Provide exported worksheet html file path via IFilePathProvider interface](/cells/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Recognise Self Closing Tags](/cells/nodejs-cpp/recognise-self-closing-tags/)
- [Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML](/cells/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Set column width to scalable unit like em or percent](/cells/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Set Default Font while rendering spreadsheet to HTML](/cells/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specify how to cross string in output HTML using HtmlCrossType](/cells/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Support the layout of DIV tags while loading HTML to excel workbook](/cells/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Enable CSS Custom Properties while saving to HTML](/cells/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)