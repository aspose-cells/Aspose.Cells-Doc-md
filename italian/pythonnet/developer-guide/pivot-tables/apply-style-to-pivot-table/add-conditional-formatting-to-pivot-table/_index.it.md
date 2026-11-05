---
title: Aggiungere Formattazione Condizionale a una Tabella Pivot
linktitle: Aggiungere Formattazione Condizionale a una Tabella Pivot
description: Aggiungere la formattazione condizionale a una tabella pivot in Aspose.Cells for Python via .NET, ancorare una regola all'intervallo di dati con apply_to e un ambito PivotConditionFormatScopeType, oppure definire il target con add_cell_area e pivot_areas, quindi collegare regole e stili tramite format_conditions.add_condition.
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, tabella pivot, formattazione condizionale, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /it/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina principale e nella pagina sorella sono statici: un’area `PivotArea` o `CellArea` viene dipinta una volta e mantiene il suo stile indipendentemente dai valori. La formattazione condizionale è l’equivalente basato su regole – evidenziare ogni importo superiore a 200, ombreggiare la metà centrale dei valori o segnalare gli elementi con ranking più basso – e l’evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale per le tabelle pivot vive nella raccolta `pivot_table.conditional_formats`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** La regione target è definita tramite `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)`, che riprende il selettore di ambito dell’interfaccia Excel, oppure tramite `add_cell_area(cell_area: CellArea)` e la raccolta `pivot_areas`, che nominano esplicitamente la regione.
- **Cosa testa la regola?** Una o più condizioni vengono aggiunte a `format_conditions` con `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)`, e ogni condizione porta con sé il proprio `style`.

{{% alert color="primary" %}}
Non chiamare `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` o `format_conditions.add_area(cell_area: CellArea)` sull’oggetto `format_conditions` di un formato condizionale pivot. Queste due overload sono ereditate dall’API di formattazione condizionale dei normali fogli di lavoro e non funzionano per le tabelle pivot: l’area cella non viene mai convertita in un’area pivot, quindi la richiesta viene ignorata silenziosamente. Definisci sempre la regione sul `pivot_conditional_format` stesso (`apply_to`, `add_cell_area` o `pivot_areas`) e aggiungi la regola con una delle overload `add_condition`.
{{% /alert %}}

## **Applicare una regola con ambito (come nell’interfaccia Excel)**
Il primo metodo posiziona la regola nello stesso modo in cui lo fa l’interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate zero‑based nel foglio di lavoro, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a che punto la regola deve estendersi dalla cella:
- `PivotConditionFormatScopeType.DATA` – tutte le celle di valore generate dalla tabella pivot, inclusi i totali generali.
- `PivotConditionFormatScopeType.FIELD` – le celle di valore appartenenti al campo identificato dalla cella, esclusi i totali generali. La cella deve essere una cella di campo, ad esempio l’etichetta di un campo di riga; se si passa una cella di valore viene sollevata un’eccezione.
- `PivotConditionFormatScopeType.SELECTION` – solo le celle di valore all’intersezione selezionata dalla cella, tipicamente una singola cella di valore.
L’esempio seguente crea una tabella pivot di vendite di frutta il cui angolo in alto a sinistra è in E3, ancora una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l’ambito `PivotConditionFormatScopeType.DATA`, e evidenzia ogni importo maggiore di 200 in bianco grassetto su rosso. Con i valori Mela 220, Banana 330, Ciliegia 200 e il totale generale 750, la regola colora F4, F5 e F7 – la regione risolta è tutta la colonna dati F4:F7, e solo le celle il cui valore soddisfa la regola si illuminano.

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
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
# Tabella pivot con l'angolo in alto a sinistra in E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Ancorare il formato condizionale in F4 (riga 3, colonna 5) con l'ambito Data
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Regola - evidenziare gli importi superiori a 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

Ancorare la stessa regola sull’etichetta del campo di riga E4 (riga 3, colonna 4) con l’ambito `PivotConditionFormatScopeType.FIELD` risolve a F4:F6 – la stessa colonna dati senza la riga del totale generale – perché l’ambito descrive ora il campo `Fruit` anziché l’intera area dei valori. L’ambito `PivotConditionFormatScopeType.SELECTION` ancorato a F4 si risolve solo a F4.

## **Definire la Regione Manualmente**
Il secondo metodo evita il selettore di ambito e nomina la regione esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con add_cell_area**
`add_cell_area(cell_area: CellArea)` registra il rettangolo fornito come target della regola. Le coordinate sono zero‑based nel foglio di lavoro, e la regione è esattamente il rettangolo specificato – nessuna espansione alla colonna dati e nessuna logica di totale generale. Usalo quando le celle di interesse sono un rettangolo fisso noto nella disposizione corrente della tabella pivot.

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
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
# Mirare al rettangolo F4:F6 (le celle di valore senza il totale generale)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Regola - corsivo su giallo chiaro per importi tra 150 e 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **Una regione pivot semantica con pivot_areas**
`pivot_areas` è lo stesso modello di regione semantica utilizzato dalla pagina sorella per gli stili statici. Crea un `PivotArea`, seleziona un campo o una regione con `select` o `select_field`, e aggiungilo con `pivot_areas.add_pivot_area(pivot_area)`. Una regione semantica resta collegata al suo campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e la disposizione cambia. L’overload `pivot_areas.add(pivot_area)` è ancora compilabile ma è contrassegnato come obsoleto – preferisci `add_pivot_area`.

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
# Attacca la regola al campo dati Amount come area semantica
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Regola - testo grigio per importi inferiori a 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **Dove le regole vengono memorizzate e come sopravvivono a un ricaricamento**
Ogni chiamata a `pivot_table.conditional_formats.add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprire il file nell’esempio seguente mostra la stessa regola con il suo tipo, operatore e formula intatti, e `get_cell_areas()` restituisce le stesse regioni. Le voci che non hanno mai ricevuto una condizione vengono rimosse quando la cartella di lavoro viene salvata, nello stesso modo in cui Excel scarta una formattazione condizionale senza regola.

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# Questo stampa:
# Formati condizionali: 1
# Formato 0: CellValue GreaterThan formula1==200
#     righe 4-7, colonne 6-6        (F4:F7, l'area dati risolta)
```

## **Articoli correlati**
- [Applicare uno stile a una Tabella Pivot](/cells/it/python-net/apply-style-to-pivot-table/)
- [Formattare una parte di una Tabella Pivot](/cells/it/python-net/format-part-of-pivot-table/)
- [Mostrare o filtrare i primi 10 in una Tabella Pivot](/cells/it/python-net/top-10-show-or-filter-in-pivot-table/)
- [Filtrare le Tabelle Pivot per Etichetta o Valore](/cells/it/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}