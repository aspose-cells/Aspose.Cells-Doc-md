---
title: HTML con C++
linktitle: HTML
type: docs
weight: 230
url: /it/cpp/convert-excel-to-html/
description: Converti Excel in formato HTML e MHTML usando Aspose.Cells con C++.
---

## **Conversione di un Workbook Excel in HTML**
L’API Aspose.Cells supporta l’esportazione di fogli di calcolo in formato HTML. Per questo scopo, Aspose.Cells utilizza la classe [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) per fornire la flessibilità di controllare vari aspetti dell’HTML di output.

L’esempio di codice sotto mostra come salvare una cartella di lavoro come file HTML usando C++:

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

## **Conversione della cartella di lavoro Excel in file MHTML**
MHTML combina HTML normale con risorse esterne (ovvero contenuti collegati come immagini, animazioni, audio, ecc.) in un unico file. Sono usati per email con estensione .mht. Aspose.Cells supporta la lettura e la scrittura di file MHTML.

Il seguente esempio di codice mostra come salvare una cartella di lavoro come file MHTML usando C++:

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

## **Argomenti avanzati**
- [Adatta automaticamente colonne e righe durante il caricamento di HTML in Workbook](/cells/it/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Evitare la notazione esponenziale per i grandi numeri durante l'importazione da HTML](/cells/it/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [Modifica il Tipo di Destinazione del Link HTML](/cells/it/cpp/change-the-html-link-target-type/)
- [Convertire Excel in HTML con tooltip](/cells/it/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/it/cpp/create-transparent-image-of-excel-worksheet/)
- [Eliminare gli spazi ridondanti dopo un'interruzione di riga durante l'importazione di HTML](/cells/it/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML](/cells/it/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disabilita l'Esportazione di Script Frame e Proprietà del Documento](/cells/it/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Utilizzare l'Opzione PresentationPreference per una Migliore Impaginazione](/cells/it/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Escludere Stili Non Utilizzati durante la conversione da Excel a HTML](/cells/it/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Espansione del testo da destra a sinistra durante l'esportazione di un file Excel in HTML](/cells/it/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Esportazione di formattazioni condizionali DataBar, ColorScale e IconSet durante la conversione da Excel in HTML](/cells/it/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Esporta commenti durante il salvataggio del file di Excel in HTML](/cells/it/cpp/export-comments-while-saving-excel-file-to/)
- [Esportare le Proprietà del Documento Workbook e del Foglio di Lavoro nella conversione da Excel a HTML](/cells/it/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Esportare Excel in HTML con linee della griglia](/cells/it/cpp/export-excel-to-html-with-gridlines/)
- [Esportare l'intervallo dell'area di stampa in HTML](/cells/it/cpp/export-print-area-range-to/)
- [Esporta uno stile di bordo simile quando lo stile di bordo non è supportato dai browser Web](/cells/it/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Esportare il Foglio di Stile CSS Separatamente nell'HTML di Output](/cells/it/cpp/export-worksheet-css-separately-in-output/)
- [Nascondere il Contenuto Sovrapposto con CrossHideRight durante il salvataggio in HTML](/cells/it/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefisso degli stili degli elementi della tabella con la proprietà HtmlSaveOptions.TableCssId](/cells/it/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Impedire l'Esportazione dei Contenuti dei Fogli Nascosti al Salvataggio in HTML](/cells/it/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Riconoscere i Tag di Chiusura Automatica](/cells/it/cpp/recognise-self-closing-tags/)
- [Rendere il Riempimento a Gradiente per WordArt durante la Conversione di Fogli di Calcolo in HTML](/cells/it/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Imposta la larghezza della colonna su un'unità scalabile come em o percentuale](/cells/it/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Imposta il carattere predefinito durante la rendering del foglio di calcolo in HTML](/cells/it/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType](/cells/it/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Supporta il layout dei tag DIV durante il caricamento di HTML nell'oggetto foglio di calcolo Excel](/cells/it/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [Abilita le Proprietà CSS Personalizzate durante il salvataggio in HTML](/cells/it/cpp/enable-css-custom-properties-while-saving-to-html/)
