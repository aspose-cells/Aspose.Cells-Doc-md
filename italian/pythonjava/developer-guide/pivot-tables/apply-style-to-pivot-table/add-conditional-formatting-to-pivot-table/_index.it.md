---
title: Aggiungere formattazione condizionale a una Tabella Pivot
linktitle: Aggiungere formattazione condizionale a una Tabella Pivot
description: Aggiungere formattazione condizionale a una tabella pivot in Aspose.Cells for Python via Java - ancorare una regola all'area dati con applyTo e un ambito PivotConditionFormatScopeType, oppure definire l'obiettivo con addCellArea e getPivotAreas, quindi allegare regole e stili tramite getFormatConditions().addCondition.
keywords: Aspose.Cells for Python via Java, tabella pivot, formattazione condizionale, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /it/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina principale e nella pagina sorella sono statici: un'area `PivotArea` o `CellArea` viene dipinta una sola volta e mantiene il proprio stile indipendentemente dai valori. La formattazione condizionale è l'equivalente basato su regole – evidenzia ogni importo superiore a 200, sfuma il cinquanta percento centrale o segnala gli elementi con classifica più bassa – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale delle tabelle pivot vive nella collezione `PivotTable.getConditionalFormats()`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove si applica la regola?** L'area di destinazione è definita o tramite `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)`, che riflette il selettore di ambito dell'interfaccia utente di Excel, oppure tramite `PivotConditionalFormat.addCellArea(CellArea)` e la collezione `PivotConditionalFormat.getPivotAreas()`, che nominano esplicitamente l'area.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `PivotConditionalFormat.getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, e ogni condizione porta il proprio `Style`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` o `FormatConditionCollection.addArea(CellArea)` sull'oggetto `PivotConditionalFormat.getFormatConditions()` di una formattazione condizionale pivot. Queste due overload provengono dall'API di formattazione condizionale dei fogli di lavoro ordinari e non funzionano per le tabelle pivot – l'area della cella non viene mai convertita in un'area pivot, quindi la richiesta viene silenziosamente ignorata. Definisci sempre l'area sul `PivotConditionalFormat` stesso (`applyTo`, `addCellArea` o `getPivotAreas()`) e aggiungi la regola con una delle overload `addCondition`.
{{% /alert %}}

## **Applicare una regola con un ambito (modo UI di Excel)**
Il primo metodo posiziona la regola nello stesso modo in cui lo fa l'interfaccia utente di Excel. Una cella della tabella pivot è identificata dalle sue coordinate di foglio di lavoro a indice zero, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a dove deve estendersi la regola da quella cella:
- `PivotConditionFormatScopeType.DATA` – tutte le celle valore generate dalla tabella pivot, incluse le totali generali.
- `PivotConditionFormatScopeType.FIELD` – le celle valore appartenenti al campo identificato dalla cella, escludendo le totali generali. La cella deve essere una cella di campo, ad esempio un'etichetta di riga; fornire una cella valore genera un'eccezione.
- `PivotConditionFormatScopeType.SELECTION` – solo le celle valore all'intersezione selezionata dalla cella, tipicamente una singola cella valore.  
L'esempio seguente crea una tabella pivot sulle vendite di frutta con l'angolo in alto a sinistra in E3, ancorare una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l'ambito `DATA`, e evidenzia ogni importo superiore a 200 in bianco grassetto su rosso. Con i valori Apple 220, Banana 330, Cherry 200 e il totale generale 750, la regola colora F4, F5 e F7 – l'area determinata è l'intera colonna dati F4:F7, e solo le celle il cui valore soddisfa la regola si illuminano.

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
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
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
# Tabella pivot con l'angolo in alto a sinistra in E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Ancorare il formato condizionale in F4 (riga 3, colonna 5) con l'ambito Dati
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Regola - evidenziare importi maggiori di 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

Ancora, ancorando la stessa regola all'etichetta del campo di riga E4 (riga 3, colonna 4) con l'ambito `FIELD` la zona risolta diventa F4:F6 – la stessa colonna dati senza la riga del totale generale – perché ora l'ambito descrive il campo `Fruit` anziché l'intera area dei valori. L'ambito `SELECTION` ancorato a F4 risolve solo F4.

## **Definire manualmente l'area**
Il secondo metodo evita il selettore di ambito e nomina l'area esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo di foglio di lavoro con addCellArea()**
`addCellArea(CellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono a indice zero del foglio di lavoro, e l'area è esattamente il rettangolo indicato – senza espansione alla colonna dei dati e senza logica di totale generale. Da utilizzare quando le celle d'interesse costituiscono un rettangolo fisso noto del layout pivot corrente.

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Seleziona il rettangolo F4:F6 (le celle di valore senza il totale generale)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Regola - corsivo su giallo chiaro per importi compresi tra 150 e 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **Una regione pivot semantica con getPivotAreas()**
La collezione `getPivotAreas()` è lo stesso modello di area semantica utilizzato dalla pagina sorella per gli stili statici. Crea un `PivotArea`, seleziona un campo o un'area con `PivotArea.select(...)` o `PivotArea.selectField(...)`, e aggiungilo con `getPivotAreas().addPivotArea(PivotArea)`. Una regione semantica rimane collegata al suo campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout si sposta. L'overload `getPivotAreas().add(PivotArea)` compila ancora ma è contrassegnato obsoleto – preferisci `addPivotArea`.

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
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Allega la regola al campo dati Amount come una regione semantica
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Regola - testo grigio per importi inferiori a 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **Dove vengono archiviate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata `PivotTable.getConditionalFormats().add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i loro stili vengono salvati con la cartella di lavoro – riaprendo il file nell'esempio seguente si visualizzano la stessa regola con il suo tipo, operatore e formula intatti, e `PivotConditionalFormat.getCellAreas()` riporta le stesse aree. Le voci che non hanno mai ricevuto una condizione vengono scartate al salvataggio della cartella di lavoro, proprio come Excel elimina una formattazione condizionale priva di regola.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# Questo stampa:
# Formati condizionali: 1
# Formato 0: CellValue GreaterThan formula1==200
#     righe 4-7, colonne 6-6        (F4:F7, la regione dati risolta)
jpype.shutdownJVM()
```

## **Articoli correlati**
- [Applicare uno stile alla Tabella Pivot](/cells/it/python-java/apply-style-to-pivot-table/)
- [Formattare parte di una Tabella Pivot](/cells/it/python-java/format-part-of-pivot-table/)
- [Top 10 Mostra o filtra nella Tabella Pivot](/cells/it/python-java/top-10-show-or-filter-in-pivot-table/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}