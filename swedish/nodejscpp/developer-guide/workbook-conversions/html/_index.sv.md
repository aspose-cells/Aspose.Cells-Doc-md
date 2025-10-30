---
title: HTML med Node.js via C++
linktitle: HTML
type: docs
weight: 230
url: /sv/nodejs-cpp/convert-excel-to-html/
---

## **Konvertera Excelfil till HTML**
Aspose.Cells API stöder export av kalkylblad till HTML-format. För detta använder Aspose.Cells klassen [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) för att ge flexibilitet att kontrollera flera aspekter av utdata-HTML:en.

Exemplet nedan visar hur man sparar ett arbetsbok som en HTML-fil med Node.js:

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


## **Konvertera Excel arbetsbok till MHTML-filer**
MHTML kombinerar normalt HTML med externa resurser (det vill säga innehåll som vanligtvis länkas in, såsom bilder, animationer, ljud och liknande) i en fil. De används för e-postmeddelanden med filändelsen .mht. Aspose.Cells stöder läsning och skrivning av MHTML-filer.

Följande exempel visar hur man sparar ett arbetsbok som en MHTML-fil med Node.js:

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

## **Fortsatta ämnen**
- [Justera kolumner och rader automatiskt vid inläsning av HTML i arbetsboken](/cells/sv/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Undvik exponentiell notation av stora tal vid import från HTML](/cells/sv/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Ändra HTML-länkens målknapptype](/cells/sv/nodejs-cpp/change-the-html-link-target-type/)
- [Konvertera Excel till HTML med verktygstips](/cells/sv/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/sv/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Ta bort överflödiga mellanslag efter radbrytning vid import av HTML](/cells/sv/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Inaktivera nivånedstiällda avslöjade kommentarer vid sparning till HTML](/cells/sv/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Inaktivera export av ramscript och dokumentegenskaper](/cells/sv/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel till HTML - Använd PresentationPreference-alternativet för bättre layout](/cells/sv/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Uteslut oanvända stilar under Excel till HTML-konvertering](/cells/sv/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expandera text från höger till vänster vid export av Excel-fil till HTML](/cells/sv/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Exportera DataBar, ColorScale och IconSet villkorlig formatering vid Excel till HTML-omvandling](/cells/sv/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Exportera kommentarer vid sparande av Excel-fil till HTML](/cells/sv/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Exportera dokumentarbetsboks- och arbetsbladsegenskaper vid konvertering från Excel till HTML](/cells/sv/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Exportera Excel till HTML med rutnätslinjer](/cells/sv/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Exportera utskriftsområde till HTML](/cells/sv/nodejs-cpp/export-print-area-range-to/)
- [Exportera liknande kantstilmall när kantstil inte stöds av webbläsare](/cells/sv/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Exportera arbetsbladets CSS separat i utdata-HTML-filen](/cells/sv/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Dölja överlagt innehåll med CrossHideRight vid sparande till HTML](/cells/sv/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Förprefixa tabellens elementstilar med HtmlSaveOptions.TableCssId-egenskapen](/cells/sv/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Förhindra export av dolda arbetsbladsinnehåll när du sparar till HTML](/cells/sv/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Ange sökväg till exporterad arbetsbokhtml-fil via IFilePathProvider-gränssnittet](/cells/sv/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Identifiera självstängande taggar](/cells/sv/nodejs-cpp/recognise-self-closing-tags/)
- [Rendera gradientfyllning för WordArt vid konvertering av kalkylblad till HTML](/cells/sv/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Ange kolumnbredd till skalbar enhet som em eller procent](/cells/sv/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Ange standardfonten vid rendering av kalkylblad till HTML](/cells/sv/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType](/cells/sv/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Stödjer layouten för DIV-taggar vid laddning av HTML till excel arbetsbok](/cells/sv/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Aktivera CSS Anpassade Egenskaper under sparande till HTML](/cells/sv/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="nodejs-cpp" >}}
