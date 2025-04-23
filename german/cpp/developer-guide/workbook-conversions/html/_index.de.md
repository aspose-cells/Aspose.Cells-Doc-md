---
title: HTML mit C++
linktitle: HTML
type: docs
weight: 230
url: /de/cpp/convert-excel-to-html/
description: Excel in HTML und MHTML Format mit Aspose.Cells und C++ konvertieren.
---

## **Excel-Arbeitsmappe in HTML konvertieren**
Die API von Aspose.Cells bietet Unterstützung für den Export von Tabellenblättern in das HTML-Format. Für diesen Zweck verwendet Aspose.Cells die [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions)-Klasse, um die Flexibilität bei der Steuerung mehrerer Aspekte des HTML-Ausgangs zu gewährleisten.

Das unten stehende Codebeispiel zeigt, wie man eine Arbeitsmappe mit C++ als HTML-Datei speichert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Excel-Arbeitsmappe in MHTML-Dateien konvertieren**
MHTML kombiniert normales HTML mit externen Ressourcen (also Inhalte, die gewöhnlich verlinkt sind, wie Bilder, Animationen, Audio usw.) in einer einzigen Datei. Sie werden für E-Mails mit der Erweiterung .mht verwendet. Aspose.Cells unterstützt das Lesen und Schreiben von MHTML-Dateien.

Das folgende Codebeispiel zeigt, wie man eine Arbeitsmappe mit C++ als MHTML-Datei speichert.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Spalten und Zeilen automatisch anpassen beim Laden von HTML in Arbeitsmappe](/cells/de/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Vermeiden Sie die exponentielle Notation großer Zahlen beim Importieren aus HTML.](/cells/de/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [Ändern Sie den HTML-Link-Zieltyp](/cells/de/cpp/change-the-html-link-target-type/)
- [Excel in HTML mit Tooltip konvertieren](/cells/de/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/de/cpp/create-transparent-image-of-excel-worksheet/)
- [Löschen überflüssiger Leerzeichen nach einem Zeilenumbruch beim Importieren von HTML](/cells/de/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Beim Speichern als HTML-Wrap Kommentare ausblenden](/cells/de/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Deaktivieren des Exports von Rahmen-Skripten und Dokumenteigenschaften.](/cells/de/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel zu HTML - Verwenden Sie die Option für die Präsentationspräferenz für ein besseres Layout.](/cells/de/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Ausnutzen nicht verwendeter Stile während der Konvertierung von Excel in HTML ausschließen](/cells/de/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Text von rechts nach links erweitern, während Excel-Datei in HTML exportiert wird](/cells/de/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Datenleiste, Farbskala und IconSet-Bedingte Formatierung beim Konvertieren von Excel in HTML exportieren](/cells/de/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Kommentare beim Speichern einer Excel-Datei in HTML exportieren](/cells/de/cpp/export-comments-while-saving-excel-file-to/)
- [Export von Arbeitsmappe- und Arbeitsblatteigenschaften in Excel zur HTML-Konvertierung](/cells/de/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Excel in HTML mit Rasterlinien exportieren](/cells/de/cpp/export-excel-to-html-with-gridlines/)
- [Druckbereichsbereich als HTML exportieren](/cells/de/cpp/export-print-area-range-to/)
- [Ähnlichen Randstil exportieren, wenn der Randstil von Webbrowsern nicht unterstützt wird](/cells/de/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Arbeitsblatt-CSS separat im ausgegebenen HTML exportieren](/cells/de/cpp/export-worksheet-css-separately-in-output/)
- [Überlagerter Inhalt mit CrossHideRight beim Speichern in HTML ausblenden](/cells/de/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Vorabtabellenelementstilen mit der HtmlSaveOptions.TableCssId-Eigenschaft](/cells/de/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Verhindern des Exportierens von versteckten Arbeitsblattinhalten beim Speichern als HTML](/cells/de/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Selbstschließende Tags erkennen.](/cells/de/cpp/recognise-self-closing-tags/)
- [Verlaufsfüllung für WordArt beim Konvertieren von Tabellenkalkulationen in HTML rendern.](/cells/de/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Spaltenbreite auf skalierbare Einheit wie em oder Prozent setzen.](/cells/de/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Legen Sie die Standardschriftart beim Rendern der Tabellenkalkulation in HTML fest](/cells/de/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Geben Sie an, wie die Zeichenfolge im Ausgabe-HTML mit HtmlCrossType gekreuzt wird.](/cells/de/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Unterstützt das Layout von DIV-Tags beim Laden von HTML in die Excel-Arbeitsmappe](/cells/de/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [Aktivieren Sie CSS Standard-Eigenschaften beim Speichern in HTML](/cells/de/cpp/enable-css-custom-properties-while-saving-to-html/)
