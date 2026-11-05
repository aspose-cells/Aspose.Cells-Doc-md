---
title: Aggiungere Formattazione Condizionale a una Tabella Pivot
linktitle: Aggiungere Formattazione Condizionale a una Tabella Pivot
description: Aggiungere formattazione condizionale a una tabella pivot in Aspose.Cells for Java – ancorare una regola all'intervallo di dati con applyTo e un ambito PivotConditionFormatScopeType, oppure definire la destinazione con addCellArea e getPivotAreas, quindi collegare regole e stili tramite FormatConditions.addCondition.
keywords: Aspose.Cells for Java, tabella pivot, formattazione condizionale, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Java
type: docs
weight: 30
url: /it/java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Gli stili descritti nella pagina principale e nella pagina sorella sono statici – un intervallo `PivotArea` o `CellArea` viene dipinto una volta e mantiene il proprio stile indipendentemente dai valori. La formattazione condizionale è la controparte basata su regole – evidenziare ogni importo superiore a 200, colorare la fascia centrale del cinquanta percento o segnalare gli elementi con classifica più bassa – e l'evidenziazione segue i valori ogni volta che la tabella pivot viene ricalcolata o aggiornata.  
In Aspose.Cells, la formattazione condizionale delle tabelle pivot vive nella collezione `PivotTable.getConditionalFormats()`. Ogni voce è un `PivotConditionalFormat` che risponde a due domande in modo indipendente:
- **Dove viene applicata la regola?** L'intervallo di destinazione è definito o tramite `applyTo(int row, int column, PivotConditionFormatScopeType scope)`, che rispecchia il selettore di ambito dell’interfaccia utente di Excel, oppure tramite `addCellArea(CellArea)` e la collezione `getPivotAreas()`, che nominano esplicitamente l’intervallo.
- **Cosa verifica la regola?** Una o più condizioni vengono aggiunte a `getFormatConditions()` con `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)`, e ogni condizione porta con sé il proprio `Style`.

{{% alert color="primary" %}}
Non chiamare `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` o `FormatConditionCollection.addArea(CellArea)` sulla collezione `getFormatConditions()` di un formato condizionale pivot. Queste due overload sono ereditate dall’API di formattazione condizionale del foglio di lavoro ordinario e non funzionano per le tabelle pivot – l’intervallo di celle non viene mai convertito in un intervallo pivot, quindi la richiesta viene ignorata **silenziosamente**. Definisci sempre l’intervallo sul `PivotConditionalFormat` stesso (`applyTo`, `addCellArea` o `getPivotAreas()`) e aggiungi la regola con una delle overload `addCondition`.
{{% /alert %}}

## **Applicare una regola con un ambito (modo Excel UI)**
Il primo metodo posiziona la regola come fa l’interfaccia utente di Excel. Una cella della tabella pivot è nominata dalle sue coordinate zero‑based del foglio di lavoro, e un ambito `PivotConditionFormatScopeType` indica ad Aspose.Cells fino a dove deve estendersi la regola a partire da quella cella:
- `PivotConditionFormatScopeType.DATA` – tutte le celle di valore prodotte dalla tabella pivot, inclusi i **totali complessivi**.
- `PivotConditionFormatScopeType.FIELD` – le celle di valore che appartengono al campo identificato dalla cella, esclusi i **totali complessivi**. La cella deve essere una cella di campo, ad esempio un’etichetta di riga; passare una cella di valore genera un’eccezione.
- `PivotConditionFormatScopeType.SELECTION` – solo le celle di valore all’intersezione selezionata dalla cella, tipicamente una singola cella di valore.
L’esempio seguente crea una tabella pivot di vendite di frutta il cui angolo in alto a sinistra è in E3, ancora una formattazione condizionale nella cella F4 (riga 3, colonna 5) con l’ambito `DATA`, e evidenzia ogni importo maggiore di 200 in grassetto bianco su rosso. Con i valori **Mela** 220, **Banana** 330, **Ciliegia** 200 e il **totale complessivo** 750, la regola colora F4, F5 e F7 – l’intervallo risolto è l’intera colonna dati F4:F7, e solo le celle il cui valore supera la soglia si illuminano.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
// Tabella pivot con l'angolo in alto a sinistra in E3
PivotTable pivotTable = sheet.getPivotTables().add("A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Fissa il formato condizionale in F4 (riga 3, colonna 5) con l'ambito Data
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA);
// Regola - evidenzia gli importi maggiori di 200
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.GREATER_THAN, "200", null);
Style style = workbook.createStyle();
style.getFont().setBold(true);
style.getFont().setColor(Color.getWhite());
style.setForegroundColor(Color.getRed());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatData.xlsx");
```

Ancora la stessa regola ancorata all’etichetta del campo di riga E4 (riga 3, colonna 4) con l’ambito `FIELD` risolve a F4:F6 – la stessa colonna dati senza la riga del **totale complessivo** – perché l’ambito ora descrive il campo `Fruit` anziché l’intero intervallo valori. L’ambito `SELECTION` ancorato a F4 si risolve solo a F4.

## **Definire l’intervallo manualmente**
Il secondo metodo evita il selettore di ambito e nomina l’intervallo esplicitamente sul `PivotConditionalFormat`.

### **Un rettangolo del foglio di lavoro con addCellArea**
`addCellArea(CellArea)` registra il rettangolo fornito come destinazione della regola. Le coordinate sono zero‑based del foglio di lavoro, e l’intervallo è esattamente il rettangolo specificato – nessuna espansione alla colonna dati e nessuna logica di totale complessivo. Usalo quando le celle di interesse sono un rettangolo fisso conosciuto del layout pivot corrente.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Individua il rettangolo F4:F6 (le celle di valore senza il totale complessivo)
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
CellArea cellArea = new CellArea();
cellArea.StartRow = 3;
cellArea.StartColumn = 5;
cellArea.EndRow = 5;
cellArea.EndColumn = 5;
format.addCellArea(cellArea);
// Regola - corsivo su giallo chiaro per importi tra 150 e 300
int conditionIndex = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300");
Style style = workbook.createStyle();
style.getFont().setItalic(true);
style.setForegroundColor(Color.getLightYellow());
style.setPattern(BackgroundType.SOLID);
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatCellArea.xlsx");
```

### **Un intervallo pivot semantico con getPivotAreas**
`getPivotAreas()` restituisce lo stesso modello di intervallo semantico che la pagina sorella utilizza per gli stili statici. Costruisci un `PivotArea`, seleziona un campo o un intervallo con `select` o `selectField`, e aggiungilo con `getPivotAreas().addPivotArea(PivotArea)`. Un intervallo semantico resta collegato al proprio campo, quindi la formattazione condizionale segue il campo quando la tabella pivot viene aggiornata e il layout si sposta. L’overload `getPivotAreas().add(PivotArea)` compila ancora ma è contrassegnato come obsoleto – preferisci `addPivotArea`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
String[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
for (int i = 0; i < fruits.length; i++)
{
    cells.get(i + 1, 0).putValue(fruits[i]);
    cells.get(i + 1, 1).putValue(years[i]);
    cells.get(i + 1, 2).putValue(amounts[i]);
}
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Attach the rule to the Amount data field as a semantic region
int index = pivotTable.getConditionalFormats().add();
PivotConditionalFormat format = pivotTable.getConditionalFormats().get(index);
PivotArea area = new PivotArea(pivotTable);
area.selectField(PivotFieldType.DATA, "Amount");
format.getPivotAreas().addPivotArea(area);
// Rule - grey text for amounts below 150
int conditionIndex = format.getFormatConditions().addCondition(
        FormatConditionType.CELL_VALUE, OperatorType.LESS_THAN, "150", null);
Style style = workbook.createStyle();
style.getFont().setColor(Color.getGray());
format.getFormatConditions().get(conditionIndex).setStyle(style);
workbook.save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dove vengono memorizzate le regole e come sopravvivono a un ricaricamento**
Ogni chiamata `getConditionalFormats().add()` aggiunge un `PivotConditionalFormat` alla tabella pivot. Le condizioni, le loro formule e i relativi stili sono salvati con la **cartella di lavoro** – riaprire il file nell’esempio seguente mostra la stessa regola con il rispettivo tipo, operatori e formule intatto, e `getCellAreas()` riporta gli stessi intervalli. Le voci che non hanno mai ricevuto una condizione vengono scartate al salvataggio della **cartella di lavoro**, proprio come Excel elimina una formattazione condizionale senza regola.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
System.out.println("Conditional formats: " + pivotTable.getConditionalFormats().getCount());
for (int i = 0; i < pivotTable.getConditionalFormats().getCount(); i++)
{
    PivotConditionalFormat format = pivotTable.getConditionalFormats().get(i);
    for (int j = 0; j < format.getFormatConditions().getCount(); j++)
    {
        FormatCondition condition = format.getFormatConditions().get(j);
        System.out.println("Format " + i + ": " + condition.getType() + " " + condition.getOperator() + " formula1=" + condition.getFormula1());
    }
    for (CellArea area : format.getCellAreas())
    {
        System.out.println("    rows " + (area.StartRow + 1) + "-" + (area.EndRow + 1)
                + ", columns " + (area.StartColumn + 1) + "-" + (area.EndColumn + 1));
    }
}
// Questo stampa:
// Formati condizionali: 1
// Formato 0: CellValue GreaterThan formula1==200
//     righe 4-7, colonne 6-6        (F4:F7, la regione dati risolta)
```

## **Articoli correlati**
- [Applicare stile alla tabella pivot](/cells/it/java/apply-style-to-pivot-table/)
- [Formattare parte della tabella pivot](/cells/it/java/format-part-of-pivot-table/)
- [Mostrare o filtrare i primi 10 nella tabella pivot](/cells/it/java/top-10-show-or-filter-in-pivot-table/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="java" >}}