---
title: Formattare parte di una Tabella Pivot
description: Formattare parte di una tabella pivot in Aspose.Cells for Java applicando stili alle regioni semantiche PivotArea o ai rettangoli CellArea tramite PivotTable.format, con i formati memorizzati in PivotTable.getPivotFormats e conservati quando la tabella pivot viene aggiornata.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Java, tabella pivot, formato, PivotArea, CellArea, PivotTable.format, PivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Java
type: docs
weight: 20
url: /it/java/format-part-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
`PivotTable.formatAll` applica un unico stile all'intera tabella pivot ed è trattato nella pagina principale. Non distingue tra etichette, valori, totali o regioni specifiche del report.  
In pratica, solo una parte della tabella pivot necessita di risaltare. Gli obiettivi comuni includono le etichette di un campo di riga, le celle valore generate da un campo, la riga del totale generale o un rettangolo arbitrario come le prime due righe di elementi.  
Applicare uno stile direttamente alle celle del foglio di lavoro di una tabella pivot non è equivalente. Excel memorizza la formattazione della tabella pivot come regioni semantiche `PivotArea` anziché come normali record di stile cella. Un formato di area pivot rimane collegato a una regione, ad esempio le etichette di un campo o i valori dei dati, e viene rielaborato quando la tabella pivot viene ricalcolata, aggiornata o espansa. Uno stile scritto direttamente su una cella appartiene a quella posizione cella e non è tracciato dal modello pivot.  
Aspose.Cells espone l'intera famiglia di overload `PivotTable.format` in modo che entrambi i tipi di formattazione siano disponibili:
- `format(PivotArea, Style)` associa uno stile a una regione semantica creata con `PivotArea.select` o `PivotArea.selectField`.
- `format(CellArea, Style)` associa uno stile a un rettangolo del foglio di lavoro all'interno della tabella pivot.
- `format(int row, int column, Style)` bersaglia una singola cella.
- `formatAll(Style)` formatta l'intera tabella pivot.

## **Formattare un'area Pivot**
Il flusso di lavoro basato su area semantica è l'approccio consigliato quando un evidenziatore deve seguire un campo o una regione del report.
1. Creare un `PivotArea` con `new PivotArea(pivotTable)`. L'oggetto descrive una regione semantica appartenente a quella specifica tabella pivot.
2. Selezionare un campo in base alla sua posizione zero‑based su un asse dato con `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DATA_AND_LABEL` seleziona sia le etichette sia i dati del campo.
   - `PivotTableSelectionType.LABEL_ONLY` seleziona solo le etichette del campo.
   - `PivotTableSelectionType.DATA_ONLY` seleziona solo le celle dati del campo.
3. Selezionare un campo per nome con `PivotArea.selectField(PivotFieldType axisType, String fieldName)`. Quando un campo di riga è selezionato per nome, la regione si risolve sulle celle valore generate dagli elementi di quel campo.
4. Creare un `Style` con `Workbook.createStyle()`, configurarne il carattere, il colore di primo piano e il motivo di sfondo solido, quindi passare lo stile a `PivotTable.format(area, style)`.
5. Ogni chiamata all'overload `PivotArea` aggiunge una voce `PivotTableFormat` a `PivotTable.getPivotFormats()`.
6. I formati ancorati a un campo vengono applicati quando i dati pivot vengono calcolati. Pertanto, chiamare `PivotTable.calculateData()` dopo aver applicato i formati affinché gli stili diventino visibili.  
L'esempio seguente crea una piccola tabella pivot di vendite di frutta, applica lo stile alle etichette di riga `Fruit` con `PivotArea.select` e `PivotTableSelectionType.LABEL_ONLY`, applica lo stile alle celle valore prodotte dallo stesso campo di riga con `PivotArea.selectField`, quindi ricalcola la tabella pivot affinché entrambi gli stili vengano dipinti.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Fruit sales data
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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.getPivotTables().add("=A1:C7", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.createStyle();
labelStyle.getFont().setBold(true);
labelStyle.setForegroundColor(Color.getYellow());
labelStyle.setPattern(BackgroundType.SOLID);
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY);
pivotTable.format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.createStyle();
valueStyle.setForegroundColor(Color.getLightGreen());
valueStyle.setPattern(BackgroundType.SOLID);
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.selectField(PivotFieldType.ROW, "Fruit");
pivotTable.format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.calculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx");
```

## **Formattare un'area Cell della Tabella Pivot**
Usare `PivotTable.format(CellArea, Style)` quando la regione di interesse è un semplice rettangolo del foglio di lavoro anziché una regione semantica pivot.  
Una `CellArea` è descritta dalle proprietà `getStartRow()`, `getStartColumn()`, `getEndRow()` e `getEndColumn()`. I valori sono coordinate zero‑based del foglio di lavoro, e le coordinate finali indicano l'ultima riga e colonna incluse nel rettangolo, quindi l'area copre le celle dalla posizione iniziale a quella finale, entrambe incluse.  
Diversamente da un formato ancorato a un campo, un formato `CellArea` viene applicato alle celle immediatamente. Non è necessaria un'altra chiamata a `calculateData()` perché lo stile appaia.  
Un rettangolo `CellArea` può contenere sia celle etichetta sia celle valore. La sezione successiva descrive come Aspose.Cells ed Excel rappresentano internamente quel rettangolo.  
L'esempio seguente formatta il rettangolo `E4:F5` della tabella pivot con uno stile corsivo di colore azzurro chiaro e salva la cartella di lavoro senza ulteriori ricalcoli.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx");
```

## **Come le aree Pivot e le aree Cell si mappano**
Excel memorizza la formattazione delle tabelle pivot come record `pivotArea` anziché come normali record di stile cella del foglio di lavoro. Lo stesso modello è utilizzato da Aspose.Cells, quindi una richiesta di formattazione viene tradotta in aree pivot al momento della registrazione.  
La relazione tra la `CellArea` fornita dall'utente e le aree pivot memorizzate internamente è molti‑a‑molti in entrambe le direzioni.
- Una `CellArea` può generare diverse aree pivot. Se il rettangolo comprende sia celle etichetta sia celle valore, viene scomposto in regole separate per etichette e dati, poiché il modello pivot tratta indipendentemente la formattazione delle etichette e dei dati.
- Un'area pivot può risolversi in diverse istanze disgiunte di `CellArea`. Una regione semantica come una riga di totale generale, o un campo i cui elementi non sono contigui, può coprire più rettangoli. Per questo `PivotArea.getCellAreas()` restituisce una collezione anziché un singolo rettangolo.  
Ogni operazione di formattazione eseguita tramite `PivotTable.format` è registrata in `PivotTable.getPivotFormats()`. Ogni voce `PivotTableFormat` espone la `PivotArea` associata e lo `Style` applicato. L'overload `PivotArea` aggiunge esattamente una voce per chiamata, mentre una `CellArea` che contiene regioni semantiche differenti può aggiungere più voci.  
Per distinguere le regioni memorizzate, ogni `PivotArea` espone le bandiere `getOnlyLabel()` e `getOnlyData()`. L'esempio sotto formatta un singolo rettangolo che copre sia etichette sia valori, esamina `PivotTable.getPivotFormats()` e stampa le coordinate `CellArea` a cui ciascuna area pivot memorizzata si risolve.

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
Style highlightStyle = workbook.createStyle();
highlightStyle.getFont().setItalic(true);
highlightStyle.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF));
highlightStyle.setPattern(BackgroundType.SOLID);
// ONE rectangle in...
CellArea rectangle = new CellArea();
rectangle.StartRow = 3;
rectangle.StartColumn = 4;
rectangle.EndRow = 4;
rectangle.EndColumn = 5;
pivotTable.format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
System.out.println("Stored formats: " + pivotTable.getPivotFormats().getCount());
for (int i = 0; i < pivotTable.getPivotFormats().getCount(); i++)
{
    PivotArea storedArea = pivotTable.getPivotFormats().get(i).getPivotArea();
    System.out.println("Format " + i + ": OnlyLabel=" + storedArea.getOnlyLabel()
            + ", OnlyData=" + storedArea.getOnlyData());
    for (CellArea resolved : storedArea.getCellAreas())
    {
        System.out.println("    rows " + (resolved.StartRow + 1) + "-" + (resolved.EndRow + 1)
                + ", columns " + (resolved.StartColumn + 1) + "-" + (resolved.EndColumn + 1));
    }
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=true, OnlyData=false
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=false, OnlyData=true
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Poiché i formati sono memorizzati come aree pivot anziché come normali stili cella, sopravvivono a ricalcoli e aggiornamenti. Quando la tabella pivot viene aggiornata con `PivotTable.refreshData`, ricalcolata con `calculateData`, o salvata e ricaricata, ogni area pivot memorizzata si risolve nuovamente nella posizione corrente della sua regione e lo stile viene riapplicato.
{{% /alert %}}

Utilizzare un `PivotArea` creato con `select` o `selectField` quando un evidenziatore deve rimanere associato a un campo o a una regione semantica attraverso gli aggiornamenti, e utilizzare un `CellArea` quando è sufficiente formattare un rettangolo fisso nella disposizione corrente della tabella pivot. L'overload `format(int row, int column, Style)` per una singola cella è adatto per un singolo punto. Usare `formatAll`, trattato nella pagina principale, quando l'intera tabella pivot deve essere riformattata in un'unica operazione.

## **Articoli correlati**
- [Applicare stile alla Tabella Pivot](/cells/it/java/apply-style-to-pivot-table/)
- [Aggiungere campi di riga e colonna alla Tabella Pivot](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Gestire i campi valore nella Tabella Pivot](/cells/it/java/manage-value-fields/)
- [Aggiornare la Tabella Pivot](/cells/it/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}