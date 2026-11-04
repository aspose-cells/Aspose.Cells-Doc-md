---
title: Formattare una parte di una Tabella Pivot
description: Formattare una parte di una tabella pivot in Aspose.Cells for Python via .NET applicando stili a regioni semantiche PivotArea o rettangoli CellArea tramite PivotTable.format, con i formati memorizzati in PivotTable.pivot_formats e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, tabella pivot, formato, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /it/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
`PivotTable.format_all` applica un unico stile all'intera tabella pivot ed è trattato nella pagina principale. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
In pratica, solo una parte di una tabella pivot solitamente deve risaltare. Gli obiettivi più comuni includono le etichette appartenenti a un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile delle celle. Un formato di area pivot rimane associato a una regione, ad esempio le etichette di un campo o i valori dei dati, ed è ricalcolato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload `PivotTable.format` in modo che siano disponibili entrambi i tipi di formattazione:
- `format(PivotArea, Style)` associa uno stile a una regione semantica creata con `PivotArea.select` o `PivotArea.select_field`.
- `format(CellArea, Style)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `format(int row, int column, Style)` mira a una singola cella.
- `format_all(Style)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un evidenziatore deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `PivotArea(pivot_table)`. L'oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
1. Selezionare un campo in base alla sua posizione zero‑based su un dato asse con `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LABEL_ONLY` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DATA_ONLY` seleziona solo le celle dati del campo.
1. Selezionare un campo per nome con `PivotArea.select_field(PivotFieldType axis_type, string field_name)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle valore generate dagli elementi di quel campo.
1. Creare un `Style` con `Workbook.create_style()`, configurarne il carattere, il colore di primo piano e il modello di riempimento solido, e passare lo stile a `PivotTable.format(area, style)`.
1. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.pivot_formats`.
1. I formati ancorati al campo vengono applicati quando i dati pivot vengono calcolati. Pertanto, chiamare `PivotTable.calculate_data()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente crea una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.select` e `PivotTableSelectionType.LABEL_ONLY`, formatta le celle valore generate dallo stesso campo di riga con `PivotArea.select_field`, quindi ricalcola la tabella pivot affinché entrambi gli stili siano applicati.

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **Formattare un'area di celle della Tabella Pivot**
Usare `PivotTable.format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione pivot semantica.  
Un `CellArea` è descritto dalle proprietà `start_row`, `start_column`, `end_row` e `end_column`. I valori sono coordinate zero‑based del foglio di lavoro e le coordinate di fine identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale a quella finale, inclusa.  
A differenza di un formato ancorato a un campo, un formato `CellArea` viene applicato immediatamente alle celle. Un'ulteriore chiamata a `calculate_data()` non è necessaria perché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo di colore azzurro chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

```python
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Come le aree Pivot e le aree di celle si mappano**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile delle celle del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot quando viene registrata.  
La relazione tra il `CellArea` fornito dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Un `CellArea` può produrre diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.
- Un'area pivot può risolversi in diverse istanze `CellArea` disgiunte. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.get_cell_areas()` restituisce una collezione anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.format` è registrata in `PivotTable.pivot_formats`. Ogni voce `PivotTableFormat` espone il `PivotArea` associato e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone i flag `only_label` e `only_data`. L'esempio sottostante formatta un singolo rettangolo che copre sia etichette sia valori, analizza `PivotTable.pivot_formats` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come normali stili di cella, sopravvivono al ricalcolo e all'aggiornamento. Quando la tabella pivot viene aggiornata con `PivotTable.refresh_data`, ricalcolata con `calculate_data`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e lo stile viene riapplicato.
{{% /alert %}}

Usare un `PivotArea` costruito con `select` o `select_field` quando un evidenziatore deve rimanere ancorato a un campo o a una regione semantica attraverso gli aggiornamenti, e usare un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout attuale della tabella pivot. L'overload `format(int row, int column, Style)` per una singola cella mira a una cella individuale. Usare `format_all`, trattato nella pagina principale, quando l'intera tabella pivot deve essere riformattata in una sola operazione.

## **Articoli correlati**
- [Applicare stile a Tabella Pivot](/cells/it/python-net/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla Tabella Pivot](/cells/it/python-net/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella Tabella Pivot](/cells/it/python-net/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}