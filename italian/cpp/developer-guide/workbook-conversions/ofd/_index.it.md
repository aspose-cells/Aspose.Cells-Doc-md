---
title: Conversione di Excel in formato OFD
linktitle: Conversione di Excel in formato OFD
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta la conversione di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document). Questo articolo mostra come creare contenuto Excel ed esportarlo come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.Ofd, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di cartelle di lavoro Excel direttamente in formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.Ofd`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, le larghezze delle colonne, le altezze delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Ciò rende Aspose.Cells adatto per flussi di lavoro di archiviazione, stampa, deposito normativo e presentazioni governative che richiedono un output a layout fisso.

{{% /alert %}}
## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per rappresentare documenti digitali in un layout fisso basato su pagine. Svolge un ruolo simile a PDF per casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come creato. OFD è ampiamente adottato per le presentazioni governative, i depositi normativi, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.

La conversione di cartelle di lavoro Excel in OFD è un requisito comune negli scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura, con layout bloccato, anziché come foglio di calcolo modificabile. Gli esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o la presentazione di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito tramite il valore di enumerazione `SaveFormat.Ofd`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio di conversione intermedio. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}

L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, inclusi il contenuto delle celle, le celle unite, le larghezze delle colonne e le altezze delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene renderizzata nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come dimensione della carta, orientamento e area di stampa, influenzano il layout del documento OFD risultante.

{{% /alert %}}
## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con dati e quindi salvarla direttamente in formato OFD utilizzando l'enumerazione `SaveFormat.Ofd`. L'esempio seguente crea una fattura da zero. Aggiunge un logo aziendale, informazioni di intestazione, una sezione di fatturazione, voci e totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.
### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro fattura inserendo un'immagine del logo nell'area in alto a sinistra, compilando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" su celle unite, registrando il numero e la data della fattura, elencando il cliente intestatario, costruendo una tabella delle voci con colonne descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale complessivo utilizzando formule nelle celle. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezze delle colonne viene applicata utilizzando gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.Ofd`.

```cpp
// Esempio di Aspose.Cells per C++
// Compilare con Aspose.Cells 26.6.0 (o successivo) e un compilatore C++17 (o successivo)

#include "Aspose.Cells.h"
#include <string>
#include <ctime>

using namespace Aspose::Cells;

int main()
{
    // Inizializza Aspose.Cells
    Aspose::Cells::Startup();

    // Directory per le risorse e l'output
    const char16_t* dataDir = u"C:\\Temp\\";

    // Crea una nuova cartella di lavoro
    Workbook workbook;

    // Ottieni il primo foglio di lavoro
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Imposta la larghezza delle colonne
    cells.SetColumnWidth(0, 5.0);
    cells.SetColumnWidth(1, 35.0);
    cells.SetColumnWidth(2, 12.0);
    cells.SetColumnWidth(3, 15.0);
    cells.SetColumnWidth(4, 15.0);
    cells.SetColumnWidth(5, 5.0);

    // Inserisci il logo dell'azienda
    worksheet.GetPictures().Add(1, 1, U16String(dataDir) + u"logo.png");

    // Nome dell'azienda e dettagli di contatto
    cells.Get(u"B3").PutValue(u"Acme Corporation");
    cells.Get(u"B4").PutValue(u"123 Business Street");
    cells.Get(u"B5").PutValue(u"City, State 12345");
    cells.Get(u"B6").PutValue(u"Phone: (555) 123-4567");

    // Titolo INVOICE - unisci celle
    cells.Merge(7, 1, 2, 4);
    Cell titleCell = cells.Get(u"B8");
    titleCell.PutValue(u"INVOICE");

    Style titleStyle = workbook.CreateStyle();
    titleStyle.GetFont().SetIsBold(true);
    titleStyle.GetFont().SetSize(20);
    titleStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    titleCell.SetStyle(titleStyle);

    // Numero e data della fattura
    cells.Get(u"B11").PutValue(u"Invoice Number:");
    cells.Get(u"C11").PutValue(u"INV-2024-001");
    cells.Get(u"B12").PutValue(u"Date:");

    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char dateBuffer[11];
    std::strftime(dateBuffer, sizeof(dateBuffer), "%Y-%m-%d", now);
    cells.Get(u"C12").PutValue(U16String(dateBuffer));

    // Sezione "Fatturare a"
    cells.Get(u"B14").PutValue(u"Bill To:");
    cells.Get(u"B15").PutValue(u"Client Name");
    cells.Get(u"B16").PutValue(u"Client Address");
    cells.Get(u"B17").PutValue(u"Client City, State");

    // Intestazione delle voci
    Cell headerDesc = cells.Get(u"B19");
    Cell headerQty = cells.Get(u"C19");
    Cell headerPrice = cells.Get(u"D19");
    Cell headerTotal = cells.Get(u"E19");

    headerDesc.PutValue(u"Description");
    headerQty.PutValue(u"Quantity");
    headerPrice.PutValue(u"Unit Price");
    headerTotal.PutValue(u"Total");

    Style headerStyle = workbook.CreateStyle();
    headerStyle.GetFont().SetIsBold(true);
    headerStyle.GetFont().SetColor(Color::White());
    headerStyle.SetForegroundColor(Color{0, 0, 128});
    headerStyle.SetPattern(BackgroundType::Solid);
    headerStyle.SetHorizontalAlignment(TextAlignmentType::Center);
    headerStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    headerStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    headerDesc.SetStyle(headerStyle);
    headerQty.SetStyle(headerStyle);
    headerPrice.SetStyle(headerStyle);
    headerTotal.SetStyle(headerStyle);

    // Stile valuta con bordi
    Style currencyStyle = workbook.CreateStyle();
    currencyStyle.SetCustom(u"\"$\"#,##0.00");
    currencyStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    currencyStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Stile con bordo semplice per le celle descrizione/quantità
    Style borderStyle = workbook.CreateStyle();
    borderStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    borderStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);

    // Righe delle voci
    struct LineItem { const char16_t* desc; int qty; double price; };
    LineItem lineItems[] = {
        {u"Product A - Widget", 2, 50.00},
        {u"Product B - Gadget", 3, 75.00},
        {u"Product C - Service", 1, 100.00}
    };

    for (int i = 0; i < 3; i++)
    {
        int row = 20 + i;
        Cell descCell = cells.Get(row, 1);
        Cell qtyCell = cells.Get(row, 2);
        Cell priceCell = cells.Get(row, 3);
        Cell totalCell = cells.Get(row, 4);

        descCell.PutValue(lineItems[i].desc);
        qtyCell.PutValue(lineItems[i].qty);
        priceCell.PutValue(lineItems[i].price);

        std::string formula = "C" + std::to_string(row) + "*D" + std::to_string(row);
        totalCell.SetFormula(U16String(formula.c_str()));

        descCell.SetStyle(borderStyle);
        qtyCell.SetStyle(borderStyle);
        priceCell.SetStyle(currencyStyle);
        totalCell.SetStyle(currencyStyle);
    }

    // Subtotale, imposta, totale complessivo
    cells.Get(u"B24").PutValue(u"Subtotal:");
    Cell subtotalCell = cells.Get(u"E24");
    subtotalCell.SetFormula(u"SUM(E20:E22)");

    cells.Get(u"B25").PutValue(u"Tax (10%):");
    Cell taxCell = cells.Get(u"E25");
    taxCell.SetFormula(u"E24*0.1");

    cells.Get(u"B26").PutValue(u"Grand Total:");
    Cell grandTotalCell = cells.Get(u"E26");
    grandTotalCell.SetFormula(u"E24+E25");

    // Stile in grassetto + valuta per i valori totali
    Style totalStyle = workbook.CreateStyle();
    totalStyle.GetFont().SetIsBold(true);
    totalStyle.SetCustom(u"\"$\"#,##0.00");

    subtotalCell.SetStyle(totalStyle);
    taxCell.SetStyle(totalStyle);
    grandTotalCell.SetStyle(totalStyle);

    // Stile in grassetto per le etichette dei totali
    Style boldStyle = workbook.CreateStyle();
    boldStyle.GetFont().SetIsBold(true);

    cells.Get(u"B24").SetStyle(boldStyle);
    cells.Get(u"B25").SetStyle(boldStyle);
    cells.Get(u"B26").SetStyle(boldStyle);

    // Salva la cartella di lavoro come file OFD
    workbook.Save(U16String(dataDir) + u"Invoice.ofd", SaveFormat::Ofd);

    // Rilascia le risorse di Aspose.Cells
    Aspose::Cells::Cleanup();

    return 0;
}
```
## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente in formato OFD. Ciò è utile per pipeline di conversione batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve solo essere riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica modifiche opzionali di impostazione della pagina e salva il risultato come documento OFD.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>
#include <ctime>

using namespace Aspose::Cells;

std::string GetCurrentTimestamp() {
    std::time_t t = std::time(nullptr);
    std::tm* now = std::localtime(&t);
    char buffer[20];
    std::strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", now);
    return std::string(buffer);
}

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "C:\\Examples\\";

    // Apri una cartella di lavoro Excel esistente dal disco
    Workbook workbook(U16String((dataDir + "SampleBook.xlsx").c_str()));

    // (1) Leggi e mostra i valori delle celle selezionate per confermare il caricamento del file
    Worksheet firstSheet = workbook.GetWorksheets().Get(0);
    U16String sheetName = firstSheet.GetName();
    Cell a1 = firstSheet.GetCells().Get(u"A1");
    Cell b1 = firstSheet.GetCells().Get(u"B1");
    Cell c1 = firstSheet.GetCells().Get(u"C1");

    std::cout << "First sheet name: " << sheetName.ToUtf8() << std::endl;
    std::cout << "Cell A1: " << a1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell B1: " << b1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Cell C1: " << c1.GetStringValue().ToUtf8() << std::endl;

    // (2) Itera sulla collezione Worksheets per enumerare i fogli disponibili
    std::cout << "\nAvailable worksheets:" << std::endl;
    WorksheetCollection sheets = workbook.GetWorksheets();
    int sheetCount = sheets.GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet ws = sheets.Get(i);
        U16String wsName = ws.GetName();
        std::cout << "  [" << i << "] " << wsName.ToUtf8() << std::endl;
    }

    // (3) Facoltativamente aggiorna una cella con il timestamp per riflettere la conversione
    std::string timestamp1 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A1").PutValue(U16String(("Converted on: " + timestamp1).c_str()));

    // Aggiungi una riga di intestazione di riepilogo all'inizio del blocco di dati
    firstSheet.GetCells().InsertRow(0);
    firstSheet.GetCells().Get(u"A1").PutValue(u"Conversion Summary");

    std::string timestamp2 = GetCurrentTimestamp();
    firstSheet.GetCells().Get(u"A2").PutValue(U16String(("Generated: " + timestamp2).c_str()));

    // (4) Configura le proprietà di PageSetup sul foglio di lavoro
    PageSetup pageSetup = firstSheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    pageSetup.SetFitToPagesTall(1);
    pageSetup.SetFitToPagesWide(1);

    // (5) Facoltativamente imposta l'area di stampa per l'output OFD
    int lastRow = firstSheet.GetCells().GetMaxDataRow();
    int lastCol = firstSheet.GetCells().GetMaxDataColumn();
    U16String lastColLetter = CellsHelper::ColumnIndexToName(lastCol);
    std::string printArea = "A1:" + lastColLetter.ToUtf8() + std::to_string(lastRow + 1);
    firstSheet.GetPageSetup().SetPrintArea(U16String(printArea.c_str()));
    std::cout << "\nPrint area set to: " << printArea << std::endl;

    // (6) Salva la cartella di lavoro come file OFD
    workbook.Save(U16String((dataDir + "SampleBook.ofd").c_str()), SaveFormat::Ofd);
    std::cout << "\nFile successfully converted to OFD format: " << dataDir << "SampleBook.ofd" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/cpp/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/cpp/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/cpp/dbf/)
- [Conversione di Sparkline in immagine e HTML in Aspose.Cells for C++](/cells/it/cpp/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="cpp" >}}