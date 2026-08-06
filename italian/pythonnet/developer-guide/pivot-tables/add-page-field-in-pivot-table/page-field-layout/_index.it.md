---
title: Modificare il Layout dei Campi Pagina nella Tabella Pivot
linktitle: Modificare il Layout dei Campi Pagina nella Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for Python via .NET, inclusa l'impostazione dell'ordine di visualizzazione, del conteggio di disposizione e dell'ordine dei campi pagina nella parte superiore della tabella pivot.
keywords: Aspose.Cells, Python via .NET library, foglio di calcolo, tabella pivot, campo pagina, ordine campi pagina, conteggio di disposizione campi pagina, spostare campo pagina
type: docs
weight: 191
url: /it/python-net/change-page-field-layout/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è un proseguimento dell'argomento **Aggiungere un Campo Pagina nella Tabella Pivot**. Dimostra come controllare il layout dell'area dei campi pagina, ovvero la striscia di controlli filtro nella parte superiore di una tabella pivot, incluso l'ordine di visualizzazione, il conteggio di disposizione e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una dedicata **area dei campi pagina** che si trova sopra il corpo di righe/colonne/dati della tabella. Questa area viene visualizzata come una striscia di controlli filtro a discesa (uno per ciascun campo pagina) ed è ciò su cui gli utenti finali fanno clic per suddividere la pivot in base a criteri come l'anno o la regione. Aspose.Cells for Python via .NET modella questa area attraverso la raccolta `pivot_table.page_fields` ed espone tre proprietà che controllano il layout visivo della striscia:

- `pivot_table.page_field_order` (un valore `PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti oppure *sotto* di essi.
- `pivot_table.page_field_wrap_count` imposta quanti campi pagina vengono disposti per riga o colonna prima di andare a capo.
- `pivot_table.page_fields.move(curr_index, dest_index)` riordina i campi pagina senza modificare la modalità di ordinamento.

Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un set di dati condiviso, così da poter confrontare i layout risultanti fianco a fianco.

## **Dati di Origine**

Tutti e tre gli esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati per il campo pagina (`Year`, `Region`), un candidato per il campo riga (`Fruit`) e una misura (`Amount`), il che rende significativa l'ispezione della striscia dei campi pagina.

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Tutte le otto righe vengono popolate in ogni esempio di codice, nello stesso ordine, così i dati di origine non differiscono mai tra gli scenari, cambiano solo le proprietà di layout dei campi pagina.

## **Esempio 1: Over Then Down**

Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) per essere visualizzati **affiancati in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse pagina (l'ordine delle chiamate `add_field_to_area` determina l'indice iniziale), aggiungiamo `Amount` (Somma) come campo dati, quindi impostiamo `page_field_order` su `PrintOrderType.OverThenDown` con `page_field_wrap_count = 2`. Con `OverThenDown` e un conteggio di disposizione pari a 2, i due campi pagina vengono disposti orizzontalmente fianco a fianco in un'unica riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```python
import os
import aspose.cells as ac

data_dir = "output"
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)

workbook = ac.Workbook()
worksheets = workbook.worksheets

pivot_data_idx = worksheets.add("PivotData")
pivot_data_sheet = worksheets[pivot_data_idx]
pivot_data_cells = pivot_data_sheet.cells

# Intestazioni (riga 0)
pivot_data_cells[0, 0].put_value("Fruit")
pivot_data_cells[0, 1].put_value("Year")
pivot_data_cells[0, 2].put_value("Region")
pivot_data_cells[0, 3].put_value("Amount")

# Riga 1: Mela, 2022, Nord, 150
pivot_data_cells[1, 0].put_value("Apple")
pivot_data_cells[1, 1].put_value(2022)
pivot_data_cells[1, 2].put_value("North")
pivot_data_cells[1, 3].put_value(150)

# Riga 2: Mela, 2023, Nord, 180
pivot_data_cells[2, 0].put_value("Apple")
pivot_data_cells[2, 1].put_value(2023)
pivot_data_cells[2, 2].put_value("North")
pivot_data_cells[2, 3].put_value(180)

# Riga 3: Banana, 2022, Sud, 120
pivot_data_cells[3, 0].put_value("Banana")
pivot_data_cells[3, 1].put_value(2022)
pivot_data_cells[3, 2].put_value("South")
pivot_data_cells[3, 3].put_value(120)

# Riga 4: Banana, 2023, Sud, 140
pivot_data_cells[4, 0].put_value("Banana")
pivot_data_cells[4, 1].put_value(2023)
pivot_data_cells[4, 2].put_value("South")
pivot_data_cells[4, 3].put_value(140)

# Riga 5: Ciliegia, 2022, Est, 200
pivot_data_cells[5, 0].put_value("Cherry")
pivot_data_cells[5, 1].put_value(2022)
pivot_data_cells[5, 2].put_value("East")
pivot_data_cells[5, 3].put_value(200)

# Riga 6: Ciliegia, 2023, Est, 220
pivot_data_cells[6, 0].put_value("Cherry")
pivot_data_cells[6, 1].put_value(2023)
pivot_data_cells[6, 2].put_value("East")
pivot_data_cells[6, 3].put_value(220)

# Riga 7: Uva, 2022, Ovest, 90
pivot_data_cells[7, 0].put_value("Grape")
pivot_data_cells[7, 1].put_value(2022)
pivot_data_cells[7, 2].put_value("West")
pivot_data_cells[7, 3].put_value(90)

# Riga 8: Uva, 2023, Ovest, 110
pivot_data_cells[8, 0].put_value("Grape")
pivot_data_cells[8, 1].put_value(2023)
pivot_data_cells[8, 2].put_value("West")
pivot_data_cells[8, 3].put_value(110)

# Aggiungi foglio PivotTableReport
pivot_table_sheet_idx = worksheets.add("PivotTableReport")
pivot_table_sheet = worksheets[pivot_table_sheet_idx]
pivot_tables = pivot_table_sheet.pivot_tables

# Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
pivot_index = pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# Aggiungi campi
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)   # Frutta
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)  # Anno
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)  # Regione
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)  # Importo
pivot_table.data_fields[0].function = ac.ConsolidationFunction.SUM

# Configura layout dell'area dei campi pagina: posiziona i campi pagina prima in orizzontale, va a capo dopo ogni 2
pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

# Aggiorna e calcola
pivot_table.calculate_data()

# Salva
workbook.save(os.path.join(data_dir, "pageFieldLayout_overThenDown.xlsx"))
```

## **Esempio 2: Down Then Over**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse pagina (con `Year` per primo) e `Amount` (Somma) come campo dati, esattamente come nell'Esempio 1. Quindi impostiamo `page_field_order` su `PrintOrderType.DownThenOver` e `page_field_wrap_count` su `2`. Con `DownThenOver` e un conteggio di disposizione pari a 2, i due campi pagina vengono impilati verticalmente, `Year` in alto, `Region` direttamente sotto, formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

```python
import aspose.cells as ac

workbook = ac.Workbook()
pivot_data = workbook.worksheets[0]
pivot_data.name = "PivotData"
pivot_report_idx = workbook.worksheets.add("PivotTableReport")
pivot_report = workbook.worksheets[pivot_report_idx]

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivot_data.cells[0, c].put_value(headers[c])

data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        pivot_data.cells[r + 1, c].put_value(data[r][c])

idx = pivot_report.pivot_tables.add("PivotData!A1:D9", "A1", "PivotTable")
pivot_table = pivot_report.pivot_tables[idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.DOWN_THEN_OVER
pivot_table.page_field_wrap_count = 2

pivot_table.calculate_data()

workbook.save("pageFieldLayout_downThenOver.xlsx")
```

## **Esempio 3: Spostare un Campo Pagina**

Nel terzo scenario manteniamo questo set di dati e l'allocazione dei campi, impostiamo un layout neutro (`OverThenDown` con conteggio di disposizione `2`) e quindi dimostriamo l'operazione `page_fields.move`. La chiamata `move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) nella posizione 1, e il campo pagina che era nella posizione 1 (`Region`) si sposta nella posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di disposizione e l'ordine rimangono invariati, quindi la striscia viene ancora visualizzata orizzontalmente fianco a fianco, viene scambiato solo l'ordine dei due menu a discesa.

```python
import aspose.cells as ac

workbook = ac.Workbook()

data_sheet = workbook.worksheets[0]
data_sheet.name = "PivotData"

data_sheet.cells["A1"].put_value("Fruit")
data_sheet.cells["B1"].put_value("Year")
data_sheet.cells["C1"].put_value("Region")
data_sheet.cells["D1"].put_value("Amount")

data_sheet.cells["A2"].put_value("Apple")
data_sheet.cells["B2"].put_value(2022)
data_sheet.cells["C2"].put_value("North")
data_sheet.cells["D2"].put_value(150)

data_sheet.cells["A3"].put_value("Apple")
data_sheet.cells["B3"].put_value(2023)
data_sheet.cells["C3"].put_value("North")
data_sheet.cells["D3"].put_value(180)

data_sheet.cells["A4"].put_value("Banana")
data_sheet.cells["B4"].put_value(2022)
data_sheet.cells["C4"].put_value("South")
data_sheet.cells["D4"].put_value(120)

data_sheet.cells["A5"].put_value("Banana")
data_sheet.cells["B5"].put_value(2023)
data_sheet.cells["C5"].put_value("South")
data_sheet.cells["D5"].put_value(140)

data_sheet.cells["A6"].put_value("Cherry")
data_sheet.cells["B6"].put_value(2022)
data_sheet.cells["C6"].put_value("East")
data_sheet.cells["D6"].put_value(200)

data_sheet.cells["A7"].put_value("Cherry")
data_sheet.cells["B7"].put_value(2023)
data_sheet.cells["C7"].put_value("East")
data_sheet.cells["D7"].put_value(220)

data_sheet.cells["A8"].put_value("Grape")
data_sheet.cells["B8"].put_value(2022)
data_sheet.cells["C8"].put_value("West")
data_sheet.cells["D8"].put_value(90)

data_sheet.cells["A9"].put_value("Grape")
data_sheet.cells["B9"].put_value(2023)
data_sheet.cells["C9"].put_value("West")
data_sheet.cells["D9"].put_value(110)

pivot_sheet_idx = workbook.worksheets.add("PivotTableReport")
pivot_sheet = workbook.worksheets[pivot_sheet_idx]

pivot_idx = pivot_sheet.pivot_tables.add("PivotData!A1:D9", "A3", "PivotTable")
pivot_table = pivot_sheet.pivot_tables[pivot_idx]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, 0)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 1)
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, 2)
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, 3)

pivot_table.page_field_order = ac.PrintOrderType.OVER_THEN_DOWN
pivot_table.page_field_wrap_count = 2

pivot_table.page_fields.move(0, 1)

pivot_table.calculate_data()

workbook.save("pageFieldLayout_move.xlsx")
```

## **Articoli Correlati**

- [Aggiungere un Campo Pagina nella Tabella Pivot](/cells/it/python-net/add-page-field-in-pivot-table/) — la pagina principale che illustra come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi Riga e Colonna nella Tabella Pivot](/cells/it/python-net/row-and-column-fields/) — tratta l'allocazione dei campi sugli assi di riga e colonna, completando il lavoro sull'asse pagina mostrato qui.
- [Gestire i Campi Valore nella Tabella Pivot](/cells/it/python-net/manage-value-fields/) — descrive come configurare l'area dei dati (valori), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare la Tabella Pivot](/cells/it/python-net/refresh-pivot-table/) — spiega `refresh_data` e `calculate_data`, che sono necessari dopo aver riordinato i campi pagina.
- [Applicare uno Stile alla Tabella Pivot](/cells/it/python-net/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot visualizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="python-net" >}}