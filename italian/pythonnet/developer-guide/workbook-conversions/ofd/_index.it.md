---
title: Conversione di Excel in formato OFD
description: Aspose.Cells for Python via .NET è una libreria di elaborazione di fogli di calcolo che supporta la conversione di cartelle di lavoro Excel in formato OFD (Open Fixed-layout Document). Questo articolo mostra come creare contenuto Excel ed esportarlo come OFD, nonché come convertire file Excel esistenti in OFD utilizzando Aspose.Cells.
linktitle: Conversione di Excel in formato OFD
keywords: Aspose.Cells, libreria Python via .NET, foglio di calcolo, Excel in OFD, conversione OFD, SaveFormat.OFD, documento a layout fisso, esportazione cartella di lavoro
type: docs
weight: 195
url: /it/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la conversione delle cartelle di lavoro Excel direttamente in formato OFD (Open Fixed-layout Document) utilizzando il valore di enumerazione `SaveFormat.OFD`. Il documento OFD risultante preserva il layout visibile, il contenuto, le celle unite, le larghezze delle colonne, le altezze delle righe, i caratteri, i colori, i bordi e i formati numerici della cartella di lavoro. Ciò rende Aspose.Cells adatto per flussi di lavoro di archiviazione, stampa, deposito normativo e presentazione alle autorità governative che richiedono un output a layout fisso.
{{% /alert %}}

## **Introduzione**
OFD (Open Fixed-layout Document) è uno standard nazionale cinese (GB/T 33190-2016) per la rappresentazione di documenti digitali in un layout fisso, basato su pagine. Svolge un ruolo simile a quello del PDF per i casi d'uso in cui l'aspetto visivo del documento sorgente deve essere preservato esattamente come è stato creato. OFD è ampiamente adottato per le presentazioni alle autorità governative, i depositi normativi, le fatture elettroniche e l'archiviazione a lungo termine nella Repubblica Popolare Cinese.
La conversione di cartelle di lavoro Excel in OFD è un requisito comune negli scenari in cui il contenuto del foglio di calcolo deve essere distribuito come artefatto di sola lettura, con layout bloccato, anziché come foglio di calcolo modificabile. Alcuni esempi includono l'invio di una fattura finalizzata a un cliente, l'archiviazione di un rapporto finanziario trimestrale o la presentazione di un foglio di calcolo del budget a un'autorità di regolamentazione. Aspose.Cells soddisfa questo requisito tramite il valore di enumerazione `SaveFormat.OFD`, che scrive la cartella di lavoro direttamente in OFD senza richiedere un passaggio intermedio di conversione. L'output OFD preserva i valori delle celle, gli intervalli uniti, i caratteri, i colori, i bordi, i formati numerici e le opzioni di impostazione della pagina configurate sulla cartella di lavoro.

{{% alert color="primary" %}}
L'output OFD generato da Aspose.Cells preserva il layout visibile della cartella di lavoro sorgente, inclusi il contenuto delle celle, le celle unite, le larghezze delle colonne e le altezze delle righe. Anche la formattazione delle celle come caratteri, colori, bordi, allineamento e formati numerici viene riprodotta nell'output a layout fisso. Le opzioni di impostazione della pagina configurate sul foglio di lavoro, come il formato della carta, l'orientamento e l'area di stampa, influenzano il layout del documento OFD risultante.
{{% /alert %}}

## **Creazione di una cartella di lavoro Excel e salvataggio come OFD**
Aspose.Cells consente di creare una cartella di lavoro a livello di codice, popolarla con i dati e quindi salvarla direttamente in formato OFD utilizzando l'enumerazione `SaveFormat.OFD`. L'esempio seguente crea una fattura da zero. Aggiunge il logo dell'azienda, le informazioni di intestazione, una sezione destinatario, le voci e i totali calcolati, quindi esporta la cartella di lavoro in un documento OFD.

### **Creazione di una fattura con un logo**
L'esempio costruisce un foglio di lavoro di fatturazione inserendo un'immagine del logo nell'area in alto a sinistra, compilando il nome dell'azienda e i dettagli di contatto, aggiungendo un titolo "INVOICE" (FATTURA) su celle unite, registrando il numero e la data della fattura, elencando il cliente nella sezione "fatturare a", costruendo una tabella delle voci con colonne descrizione, quantità, prezzo unitario e totale, e calcolando il subtotale, l'imposta e il totale complessivo utilizzando formule nelle celle. La formattazione come intestazioni in grassetto, formato valuta per i prezzi, bordi e larghezze delle colonne viene applicata utilizzando gli oggetti `Style` e `Font`. Infine, la cartella di lavoro viene salvata con l'estensione `.ofd` utilizzando `SaveFormat.OFD`.

```python
import aspose.cells as ac
from datetime import datetime
data_dir = "C:\\Temp\\"
# Create a new Workbook
workbook = ac.Workbook()
# Obtain the first worksheet
worksheet = workbook.worksheets[0]
# Set column widths
worksheet.cells.set_column_width(0, 5.0)
worksheet.cells.set_column_width(1, 35.0)
worksheet.cells.set_column_width(2, 12.0)
worksheet.cells.set_column_width(3, 15.0)
worksheet.cells.set_column_width(4, 15.0)
worksheet.cells.set_column_width(5, 5.0)
# Insert company logo
worksheet.pictures.add(1, 1, data_dir + "logo.png")
# Company name and contact details
worksheet.cells.get("B3").put_value("Acme Corporation")
worksheet.cells.get("B4").put_value("123 Business Street")
worksheet.cells.get("B5").put_value("City, State 12345")
worksheet.cells.get("B6").put_value("Phone: (555) 123-4567")
# INVOICE title - merge cells
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells.get("B8")
title_cell.put_value("INVOICE")
title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)
# Invoice number and date
worksheet.cells.get("B11").put_value("Invoice Number:")
worksheet.cells.get("C11").put_value("INV-2024-001")
worksheet.cells.get("B12").put_value("Date:")
worksheet.cells.get("C12").put_value(datetime.now().strftime("%Y-%m-%d"))
# Bill-to section
worksheet.cells.get("B14").put_value("Bill To:")
worksheet.cells.get("B15").put_value("Client Name")
worksheet.cells.get("B16").put_value("Client Address")
worksheet.cells.get("B17").put_value("Client City, State")
# Line items header
header_desc = worksheet.cells.get("B19")
header_qty = worksheet.cells.get("C19")
header_price = worksheet.cells.get("D19")
header_total = worksheet.cells.get("E19")
header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")
header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
header_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)
# Currency style with borders
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
currency_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# Plain border style for description/quantity cells
border_style = workbook.create_style()
border_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
border_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
# Line items rows
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]
for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells.get(row, 1)
    qty_cell = worksheet.cells.get(row, 2)
    price_cell = worksheet.cells.get(row, 3)
    total_cell = worksheet.cells.get(row, 4)
    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)
    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)
# Subtotal, tax, grand total
worksheet.cells.get("B24").put_value("Subtotal:")
subtotal_cell = worksheet.cells.get("E24")
subtotal_cell.formula = "SUM(E20:E22)"
worksheet.cells.get("B25").put_value("Tax (10%):")
tax_cell = worksheet.cells.get("E25")
tax_cell.formula = "E24*0.1"
worksheet.cells.get("B26").put_value("Grand Total:")
grand_total_cell = worksheet.cells.get("E26")
grand_total_cell.formula = "E24+E25"
# Bold + currency style for total values
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"
subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)
# Bold style for total labels
bold_style = workbook.create_style()
bold_style.font.is_bold = True
worksheet.cells.get("B24").set_style(bold_style)
worksheet.cells.get("B25").set_style(bold_style)
worksheet.cells.get("B26").set_style(bold_style)
# Save the workbook as an OFD file
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.OFD)
```

## **Conversione di un file Excel esistente in OFD**
Aspose.Cells può anche caricare una cartella di lavoro Excel esistente dal disco ed esportarla direttamente in formato OFD. Ciò è utile per pipeline di conversione in batch, flussi di lavoro di archiviazione e scenari in cui la cartella di lavoro sorgente è stata prodotta da un altro strumento e deve solo essere riemessa come artefatto a layout fisso. L'esempio seguente carica una cartella di lavoro `.xlsx` esistente, legge i dati dalle sue celle, applica eventuali regolazioni delle impostazioni di pagina e salva il risultato come documento OFD.

```python
import aspose.cells as ac
from datetime import datetime
dataDir = "C:\\Examples\\"
# Open an existing Excel workbook from disk
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")
# (1) Read and display values from selected cells to confirm the file was loaded
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells.get("A1").string_value)
print("Cell B1: " + firstSheet.cells.get("B1").string_value)
print("Cell C1: " + firstSheet.cells.get("C1").string_value)
# (2) Iterate over the Worksheets collection to enumerate available sheets
print("\nAvailable worksheets:")
for i in range(len(workbook.worksheets)):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)
# (3) Optionally update a timestamp cell to reflect the conversion
firstSheet.cells.get("A1").put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# Append a summary header row at the top of the data block
firstSheet.cells.insert_row(0)
firstSheet.cells.get("A1").put_value("Conversion Summary")
firstSheet.cells.get("A2").put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# (4) Configure PageSetup properties on the worksheet
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1
# (5) Optionally set the print area for the OFD output
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)
# (6) Save the workbook as an OFD file
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.OFD)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Articoli correlati**
- [Divisione di file Excel in più file](/cells/it/python-net/splitting-excel-files-into-multiple-files/)
- [Inserimento di un'immagine in una cella](/cells/it/python-net/inserting-an-image-into-a-cell/)
- [Lettura e scrittura di file DBF](/cells/it/python-net/dbf/)
- [Conversione di Sparkline in immagine e HTML in Aspose.Cells per Aspose.Cells per Python via .NET](/cells/it/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python-net" >}}