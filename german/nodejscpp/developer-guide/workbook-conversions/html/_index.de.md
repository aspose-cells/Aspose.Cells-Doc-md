---
title: HTML mit Node.js über C++
linktitle: HTML
type: docs
weight: 230
url: /de/nodejs-cpp/convert-excel-to-html/
---

## **Excel-Arbeitsmappe in HTML konvertieren**
Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

Das folgende Codebeispiel zeigt, wie man eine Arbeitsmappe mit Node.js als HTML-Datei speichert:

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


## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**
MHTML kombiniert normales HTML mit externen Ressourcen (also Inhalte, die gewöhnlich verlinkt sind, wie Bilder, Animationen, Audio usw.) in einer einzigen Datei. Sie werden für E-Mails mit der Erweiterung .mht verwendet. Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das folgende Codebeispiel zeigt, wie man eine Arbeitsmappe mit Node.js als MHTML-Datei speichert:

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

## **Erweiterte Themen**
- [Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe](/cells/de/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Vermeiden Sie die exponentielle Notation großer Zahlen beim Importieren aus HTML.](/cells/de/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [Ändern Sie den HTML-Link-Zieltyp](/cells/de/nodejs-cpp/change-the-html-link-target-type/)
- [Excel in HTML mit Tooltip konvertieren](/cells/de/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/de/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [Löschen überflüssiger Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML](/cells/de/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Beim Speichern als HTML-Wrap Kommentare ausblenden](/cells/de/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften.](/cells/de/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel zu HTML - Verwenden Sie die Option für die Präsentationspräferenz für ein besseres Layout.](/cells/de/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen](/cells/de/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird](/cells/de/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Datenleiste, Farbskala und IconSet-Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren](/cells/de/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Kommentare beim Speichern einer Excel-Datei in HTML exportieren](/cells/de/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [Export von Arbeitsmappe- und Arbeitsblatteigenschaften in Excel zur HTML-Konvertierung](/cells/de/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel in HTML mit Rasterlinien exportieren](/cells/de/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [Druckbereichsbereich als HTML exportieren](/cells/de/nodejs-cpp/export-print-area-range-to/)
- [Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird](/cells/de/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren](/cells/de/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [Überlagerter Inhalt mit CrossHideRight beim Speichern in HTML ausblenden](/cells/de/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft](/cells/de/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Verhindern des Exportierens von versteckten Arbeitsblattinhalten beim Speichern als HTML](/cells/de/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Stellen Sie den Pfad der exportierten Arbeitsblatt-HTML-Datei über das IFilePathProvider-Interface bereit.](/cells/de/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [Selbstschließende Tags erkennen.](/cells/de/nodejs-cpp/recognise-self-closing-tags/)
- [Verlaufsfüllung für WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern.](/cells/de/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Spaltenbreite auf skalierbare Einheit wie em oder Prozent setzen.](/cells/de/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest](/cells/de/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.](/cells/de/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Unterstützt das Layout von DIV-Tags beim Laden von HTML in die Excel-Arbeitsmappe](/cells/de/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML](/cells/de/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
