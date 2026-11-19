---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Java
linktitle: Aggiungere campi filtro a una tabella pivot
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Java, inclusi l'aggiunta di campi filtro, il filtro a selezione singola e il filtro a selezione multipla.
keywords: Aspose.Cells, Java, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/java/add-page-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello di comodo uso oppure tramite la raccolta di livello inferiore `PageFields`, e gestire il filtro in modalità selezione singola, cancellarlo per mostrare ogni elemento del filtro oppure commutare il campo sulla selezione multipla in modo che gli utenti possano scegliere più elementi del filtro contemporaneamente tramite l'interfaccia utente a caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**
Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato nel corpo della pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una pivot resa in Excel, e selezionando uno degli elementi del filtro disponibili il corpo della pivot viene ricostruito in modo che vengano riepilogati solo i record appartenenti a quell'elemento del filtro. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Aggiungere un campo filtro**

### Aggiungere un campo filtro con addFieldToArea
L'esempio seguente crea un piccolo set di dati Frutta / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area delle righe, `Amount` nell'area dei dati e `Year` nell'area del filtro, aggiorna la pivot e salva la cartella di lavoro.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Set up the header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
Object[][] data = new Object[][]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.length; i++)
{
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0]);
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1]);
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Refresh and calculate the pivot table data
pivotTable.calculateData();
// Save the workbook
workbook.save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con PageFields.add
Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area del filtro viene sostituita con la chiamata API di livello inferiore.

```java
import com.aspose.cells.*;
// - The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit->Row,
//   Amount->Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add - the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Headers
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtro a selezione singola (visualizzazione di un singolo elemento del filtro)**
Nel comportamento predefinito di selezione singola, il campo filtro viene reso come un singolo menu a discesa e il valore intero `PivotField.CurrentPageItem` seleziona quale elemento del filtro guida il corpo della pivot. L'assegnazione di un indice specifico seleziona esattamente quell'elemento; l'assegnazione del valore sentinella speciale `0x7FFD` (decimale 32765) cancella il filtro in modo che ogni elemento del filtro venga riepilogato contemporaneamente. La selezione singola è l'impostazione predefinita; non è necessario abilitarla esplicitamente.

### Mostra di tutti gli elementi
L'impostazione di `CurrentPageItem` sul valore magico `0x7FFD` equivale a cancellare il filtro: il corpo della pivot riepiloga ogni elemento del filtro come se non fosse applicato alcun filtro.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
Object[][] data = new Object[][]
{
    {"Apple", 2022, 100},
    {"Apple", 2023, 150},
    {"Banana", 2022, 80},
    {"Banana", 2023, 120},
    {"Cherry", 2022, 200},
    {"Cherry", 2023, 250}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        sheet.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
// Create pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivot = pivotTables.add("=A1:C7", 2, 4);
// Configure pivot fields: Fruit to Row, Amount to Data, Year to Page
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Clear the page filter so every item in the page field is visible.
// 0x7FFD (decimal 32765) is the special sentinel value that means "all items",
// equivalent to selecting "(All)" in Excel's page-field dropdown.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Mostra di un singolo elemento specifico
L'impostazione di `CurrentPageItem` su un indice reale seleziona solo quel singolo elemento del filtro. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```java
import com.aspose.cells.*;
// Create workbook
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit");
cells.get("B1").putValue("Year");
cells.get("C1").putValue("Amount");
cells.get("A2").putValue("Apple");
cells.get("B2").putValue("2020");
cells.get("C2").putValue("100");
cells.get("A3").putValue("Apple");
cells.get("B3").putValue("2021");
cells.get("C3").putValue("150");
cells.get("A4").putValue("Banana");
cells.get("B4").putValue("2020");
cells.get("C4").putValue("200");
cells.get("A5").putValue("Banana");
cells.get("B5").putValue("2021");
cells.get("C5").putValue("250");
// Add pivot table at E3
PivotTableCollection pivotTables = sheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.calculateData();
workbook.save("output.xlsx");
```

## **Filtro a selezione multipla**
Il filtro a selezione multipla trasforma il menu a discesa del filtro in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi del filtro contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia utente a selezione multipla abbia effetto. Una volta abilitata, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento oppure inserire in una whitelist solo elementi specifici.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit");
cells.get(0, 1).putValue("Year");
cells.get(0, 2).putValue("Amount");
String[][] data = new String[][]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.length; i++)
{
    cells.get(i + 1, 0).putValue(data[i][0]);
    cells.get(i + 1, 1).putValue(Integer.parseInt(data[i][1]));
    cells.get(i + 1, 2).putValue(Integer.parseInt(data[i][2]));
}
Worksheet pivotSheet = workbook.getWorksheets().add("Pivot");
PivotTableCollection pivots = pivotSheet.getPivotTables();
PivotTable pivotTable = pivots.add("A1:C10", 2, 4);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Part A -- select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Part B -- select only specific items by source value
for (int i = 0; i < pivotItems.getCount(); i++)
{
    switch (pivotItems.get(i).getStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems.get(i).setHidden(false);
            break;
        default:
            pivotItems.get(i).setHidden(true);
            break;
    }
}
pivotTable.calculateData();
workbook.save("output.xlsx");
```

> **Nota:** Quando si utilizza il filtro a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni elemento è nascosto, Excel si arresta in modo anomalo all'apertura del file oppure rende una pivot vuota. Verificare sempre che la whitelist di selezione multipla includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità devo usare?**
La tabella seguente riassume quando utilizzare ciascuna API e modalità, in modo da poter scegliere la combinazione giusta senza dover leggere ogni scenario in dettaglio.
| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro per nome della colonna di origine (caso più comune) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/d | Alto livello, una sola riga. Utilizzare questa opzione a meno che non sia necessario un riferimento `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/d | Utilizzare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare un singolo elemento del filtro (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / cancellare il filtro | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è il valore sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia utente a selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata `IsHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per ogni elemento | Almeno un elemento deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si arresta in modo anomalo all'apertura oppure rende una pivot vuota. Costruire la whitelist in base ai dati di origine in modo che almeno un elemento rimanga visibile, e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}