---
title: Modificare il layout dei campi pagina nella Tabella Pivot
linktitle: Modificare il layout dei campi pagina nella Tabella Pivot
description: Impara come controllare il layout dell'area dei campi pagina in una Tabella Pivot utilizzando Aspose.Cells for Python via Java, inclusa l'impostazione dell'ordine di visualizzazione, del conteggio di disposizione e dell'ordine dei campi dei campi pagina nella parte superiore della Tabella Pivot.
keywords: Aspose.Cells for Python via Java, libreria Python Java, foglio di calcolo, tabella pivot, campo pagina, ordine campi pagina, conteggio disposizione campi pagina, sposta campo pagina
type: docs
weight: 191
url: /it/python-java/change-page-field-layout/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è un proseguimento dell'argomento **Aggiungere un campo pagina nella Tabella Pivot**. Dimostra come controllare il layout dell'area dei campi pagina — la striscia di controlli filtro nella parte superiore di una tabella pivot — inclusi l'ordine di visualizzazione, il conteggio di disposizione e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una **area dei campi pagina** dedicata che si trova sopra il corpo delle righe/colonne/dati della tabella. Quest'area viene visualizzata come una striscia di controlli filtro a discesa (uno per ogni campo pagina) ed è ciò che gli utenti finali cliccano per suddividere la tabella pivot in base a criteri come anno o regione. Aspose.Cells for Python via Java modella quest'area tramite la raccolta `pivot_table.page_fields` ed espone tre proprietà che controllano come la striscia viene disposta visivamente:

- `pivot_table.page_field_order` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti oppure *sotto* di essi.
- `pivot_table.page_field_wrap_count` imposta quanti campi pagina vengono posizionati per riga o colonna prima di andare a capo.
- `pivot_table.page_fields.move(curr_index, dest_index)` riordina i campi pagina senza modificare la modalità di ordine.

Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un dataset condiviso, in modo da poter confrontare i layout risultanti fianco a fianco.

## **Dati di origine**

Tutti e tre gli esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati per i campi pagina (`Year`, `Region`), un candidato per il campo riga (`Fruit`) e una misura (`Amount`), il che rende la striscia dei campi pagina significativa da analizzare.

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

Tutte e otto le righe vengono popolate in ogni esempio di codice, nello stesso ordine, quindi i dati di origine non differiscono mai tra gli scenari — cambiano solo le proprietà di layout dei campi pagina.

## **Esempio 1: Over Then Down**

Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) in modo che appaiano **affiancati in una singola riga** nella parte superiore della tabella pivot. Assegniamo `Fruit` all'asse delle righe, posizioniamo `Year` per primo e `Region` per secondo sull'asse della pagina (l'ordine delle chiamate `add_field_to_area` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati, e quindi impostiamo `page_field_order` su `PrintOrderType.OVER_THEN_DOWN` con `page_field_wrap_count = 2`. Con `OVER_THEN_DOWN` e un conteggio di disposizione pari a 2, i due campi pagina vengono disposti orizzontalmente fianco a fianco in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorksheetCollection, Worksheet, Cells, PivotTableCollection, PivotTable, PivotFieldType, ConsolidationFunction, PrintOrderType

dataDir = "output"
if not os.path.exists(dataDir):
    os.makedirs(dataDir, exist_ok=True)

workbook = Workbook()
worksheets = workbook.getWorksheets()

pivotDataIdx = worksheets.add("PivotData")
pivotDataSheet = worksheets.get(pivotDataIdx)
pivotDataCells = pivotDataSheet.getCells()

# Intestazioni (riga 0)
pivotDataCells.get(0, 0).putValue("Fruit")
pivotDataCells.get(0, 1).putValue("Year")
pivotDataCells.get(0, 2).putValue("Region")
pivotDataCells.get(0, 3).putValue("Amount")

# Riga 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple")
pivotDataCells.get(1, 1).putValue(2022)
pivotDataCells.get(1, 2).putValue("North")
pivotDataCells.get(1, 3).putValue(150)

# Riga 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple")
pivotDataCells.get(2, 1).putValue(2023)
pivotDataCells.get(2, 2).putValue("North")
pivotDataCells.get(2, 3).putValue(180)

# Riga 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana")
pivotDataCells.get(3, 1).putValue(2022)
pivotDataCells.get(3, 2).putValue("South")
pivotDataCells.get(3, 3).putValue(120)

# Riga 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana")
pivotDataCells.get(4, 1).putValue(2023)
pivotDataCells.get(4, 2).putValue("South")
pivotDataCells.get(4, 3).putValue(140)

# Riga 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry")
pivotDataCells.get(5, 1).putValue(2022)
pivotDataCells.get(5, 2).putValue("East")
pivotDataCells.get(5, 3).putValue(200)

# Riga 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry")
pivotDataCells.get(6, 1).putValue(2023)
pivotDataCells.get(6, 2).putValue("East")
pivotDataCells.get(6, 3).putValue(220)

# Riga 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape")
pivotDataCells.get(7, 1).putValue(2022)
pivotDataCells.get(7, 2).putValue("West")
pivotDataCells.get(7, 3).putValue(90)

# Riga 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape")
pivotDataCells.get(8, 1).putValue(2023)
pivotDataCells.get(8, 2).putValue("West")
pivotDataCells.get(8, 3).putValue(110)

# Aggiungi foglio PivotTableReport
pivotTableSheetIdx = worksheets.add("PivotTableReport")
pivotTableSheet = worksheets.get(pivotTableSheetIdx)
pivotTables = pivotTableSheet.getPivotTables()

# Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# Aggiungi campi
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)   # Frutta
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)  # Anno
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)  # Regione
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)  # Importo
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM)

# Configura il layout dell'area dei campi pagina: posiziona i campi pagina prima in orizzontale, va a capo dopo ogni 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

# Aggiorna e calcola
pivotTable.calculateData()

# Salva
workbook.save(os.path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"))

jpype.shutdownJVM()
```

## **Esempio 2: Down Then Over**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse della pagina (con `Year` per primo) e `Amount` (Sum) come campo dati — esattamente come nell'Esempio 1. Quindi impostiamo `page_field_order` su `PrintOrderType.DOWN_THEN_OVER` e `page_field_wrap_count` su `2`. Con `DOWN_THEN_OVER` e un conteggio di disposizione pari a 2, i due campi pagina vengono impilati verticalmente — `Year` in alto, `Region` direttamente sotto — formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PrintOrderType

workbook = Workbook()
pivotData = workbook.getWorksheets().get(0)
pivotData.setName("PivotData")
pivotReportIdx = workbook.getWorksheets().add("PivotTableReport")
pivotReport = workbook.getWorksheets().get(pivotReportIdx)

headers = ["Fruit", "Year", "Region", "Amount"]
for c in range(len(headers)):
    pivotData.getCells().get(0, c).putValue(headers[c])

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
        pivotData.getCells().get(r + 1, c).putValue(data[r][c])

idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable")
pivotTable = pivotReport.getPivotTables().get(idx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)
pivotTable.setPageFieldWrapCount(2)

pivotTable.calculateData()

workbook.save("pageFieldLayout_downThenOver.xlsx")

jpype.shutdownJVM()
```

## **Esempio 3: Spostare un campo pagina**

Nel terzo scenario manteniamo lo stesso dataset e la stessa allocazione dei campi, impostiamo un layout neutro (`OVER_THEN_DOWN` con conteggio di disposizione `2`), e quindi dimostriamo l'operazione `page_fields.move`. La chiamata `move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) alla posizione 1, e il campo pagina che era alla posizione 1 (`Region`) si sposta alla posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di disposizione e l'ordine rimangono invariati, quindi la striscia viene ancora visualizzata orizzontalmente fianco a fianco — è stato scambiato solo l'ordine dei due menu a discesa.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PrintOrderType

workbook = Workbook()

dataSheet = workbook.getWorksheets().get(0)
dataSheet.setName("PivotData")

dataSheet.getCells().get("A1").putValue("Fruit")
dataSheet.getCells().get("B1").putValue("Year")
dataSheet.getCells().get("C1").putValue("Region")
dataSheet.getCells().get("D1").putValue("Amount")

dataSheet.getCells().get("A2").putValue("Apple")
dataSheet.getCells().get("B2").putValue(2022)
dataSheet.getCells().get("C2").putValue("North")
dataSheet.getCells().get("D2").putValue(150)

dataSheet.getCells().get("A3").putValue("Apple")
dataSheet.getCells().get("B3").putValue(2023)
dataSheet.getCells().get("C3").putValue("North")
dataSheet.getCells().get("D3").putValue(180)

dataSheet.getCells().get("A4").putValue("Banana")
dataSheet.getCells().get("B4").putValue(2022)
dataSheet.getCells().get("C4").putValue("South")
dataSheet.getCells().get("D4").putValue(120)

dataSheet.getCells().get("A5").putValue("Banana")
dataSheet.getCells().get("B5").putValue(2023)
dataSheet.getCells().get("C5").putValue("South")
dataSheet.getCells().get("D5").putValue(140)

dataSheet.getCells().get("A6").putValue("Cherry")
dataSheet.getCells().get("B6").putValue(2022)
dataSheet.getCells().get("C6").putValue("East")
dataSheet.getCells().get("D6").putValue(200)

dataSheet.getCells().get("A7").putValue("Cherry")
dataSheet.getCells().get("B7").putValue(2023)
dataSheet.getCells().get("C7").putValue("East")
dataSheet.getCells().get("D7").putValue(220)

dataSheet.getCells().get("A8").putValue("Grape")
dataSheet.getCells().get("B8").putValue(2022)
dataSheet.getCells().get("C8").putValue("West")
dataSheet.getCells().get("D8").putValue(90)

dataSheet.getCells().get("A9").putValue("Grape")
dataSheet.getCells().get("B9").putValue(2023)
dataSheet.getCells().get("C9").putValue("West")
dataSheet.getCells().get("D9").putValue(110)

pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport")
pivotSheet = workbook.getWorksheets().get(pivotSheetIdx)

pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable")
pivotTable = pivotSheet.getPivotTables().get(pivotIdx)

pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1)
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2)
pivotTable.addFieldToArea(PivotFieldType.DATA, 3)

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)
pivotTable.setPageFieldWrapCount(2)

pivotTable.getPageFields().move(0, 1)

pivotTable.calculateData()

workbook.save("pageFieldLayout_move.xlsx")

jpype.shutdownJVM()
```

## **Articoli correlati**

- [Aggiungere un campo pagina nella Tabella Pivot](/cells/it/python-java/add-page-field-in-pivot-table/) — la pagina padre che introduce come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi di riga e colonna nella Tabella Pivot](/cells/it/python-java/row-and-column-fields/) — illustra l'allocazione dei campi agli assi di riga e colonna, integrando il lavoro sull'asse della pagina mostrato qui.
- [Gestire i campi valore nella Tabella Pivot](/cells/it/python-java/manage-value-fields/) — descrive come configurare l'area dei dati (valore), inclusa l'aggregazione `SUM` utilizzata in questo articolo.
- [Aggiornare la Tabella Pivot](/cells/it/python-java/refresh-pivot-table/) — spiega `refresh_data` e `calculate_data`, che sono necessari dopo il riordino dei campi pagina.
- [Applicare uno stile alla Tabella Pivot](/cells/it/python-java/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot resa dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="python" >}}