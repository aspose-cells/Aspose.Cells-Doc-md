---
title: Formattare parte di una Tabella Pivot
description: Formattare una parte di una tabella pivot in Aspose.Cells for Python via Java applicando stili a regioni semantiche PivotArea o a rettangoli CellArea tramite PivotTable.format, con i formati memorizzati in PivotTable.getPivotFormats() e preservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, Aspose.Cells for Python via Java, tabella pivot, formato, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /it/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
`PivotTable.formatAll` applica un unico stile all'intera tabella pivot ed è trattato nella pagina principale. Non distingue tra etichette, valori, totali o regioni particolari del report.  
Nella pratica, di solito è necessario evidenziare solo una parte della tabella pivot. Gli obiettivi comuni includono le etichette appartenenti a un campo di riga, le celle valore prodotte da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile cella. Un formato di area pivot rimane associato a una regione, ad esempio le etichette di un campo o i valori dei dati, e viene ricalcolato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella, invece, appartiene a quella posizione di cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload `PivotTable.format` in modo che entrambi i tipi di formattazione siano disponibili:
- `format(PivotArea, Style)` associa uno stile a una regione semantica creata con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `format(int row, int column, Style)` mira a una singola cella.
- `formatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un'evidenziazione deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `PivotArea(pivot_table)`. L'oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
2. Selezionare un campo in base alla sua posizione zero‑based su un determinato asse con `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LABEL_ONLY` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DATA_ONLY` seleziona solo le celle dati del campo.
3. Selezionare un campo per nome con `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve nelle celle valore prodotte dagli elementi di quel campo.
4. Creare uno `Style` con `workbook.createStyle()`, configurare il font, il colore di primo piano e il pattern di riempimento solido, quindi passare lo stile a `PivotTable.format(area, style)`.
5. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.getPivotFormats()`.
6. I formati ancorati al campo vengono visualizzati quando i dati pivot sono calcolati. Pertanto, chiamare `PivotTable.calculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente crea una piccola tabella pivot di vendite di frutta, formatta le etichette di riga `Fruit` con `PivotArea.select` e `PivotTableSelectionType.LABEL_ONLY`, formatta le celle valore prodotte dallo stesso campo di riga con `PivotArea.selectField`, quindi ricalcola la tabella pivot affinché entrambi gli stili siano applicati.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Formattare un'area di celle della tabella pivot**
Usare `PivotTable.format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione pivot semantica.  
Un `CellArea` è descritto dalle proprietà `getStartRow()`, `getStartColumn()`, `getEndRow()` e `getEndColumn()`. I valori sono coordinate zero‑based del foglio, e le coordinate finali identificano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale fino a quella finale, inclusa.  
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato immediatamente alle celle. Non è necessario un ulteriore chiamata a `PivotTable.calculateData()` perché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile italic, azzurro chiaro, e salva la cartella di lavoro senza ulteriori ricalcoli.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Come le aree Pivot e le aree Cell si mappano**
Excel memorizza la formattazione della tabella pivot come record `pivotArea` anziché come normali record di stile cella del foglio. Lo stesso modello è usato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot quando viene registrata.  
La relazione tra il `CellArea` fornito dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Un `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene suddiviso in regole separate per etichette e dati, perché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.
- Un'area pivot può risolversi in più istanze `CellArea` disgiunte. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.getCellAreas()` restituisce una raccolta anziché un singolo rettangolo.  
Ogni operazione di formattazione effettuata tramite `PivotTable.format` è registrata in `PivotTable.getPivotFormats()`. Ogni voce `PivotTableFormat` espone l'`PivotArea` associata e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre un `CellArea` che contiene regioni semantiche diverse può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone le bandiere `getOnlyLabel()` e `getOnlyData()`. L'esempio sotto formatta un unico rettangolo che copre sia etichette sia valori, ispeziona `PivotTable.getPivotFormats()` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come normali stili cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot è aggiornata con `PivotTable.refreshData()`, ricalcolata con `PivotTable.calculateData()`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e il relativo stile viene riapplicato.
{{% /alert %}}

Usare un `PivotArea` costruito con `select` o `selectField` quando un'evidenziazione deve rimanere collegata a un campo o a una regione semantica attraverso gli aggiornamenti, e usare un `CellArea` quando è sufficiente formattare un rettangolo fisso nel layout corrente della tabella pivot. L'overload `format(int row, int column, Style)` per una singola cella mira a una cella individuale. Usare `formatAll`, trattato nella pagina principale, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

## **Articoli correlati**
- [Applicare stile alla tabella pivot](/cells/it/python-java/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla tabella pivot](/cells/it/python-java/pivot-table-add-row-and-column-fields/)
- [Gestire campi di valore nella tabella pivot](/cells/it/python-java/manage-value-fields/)
- [Aggiornare la tabella pivot](/cells/it/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}