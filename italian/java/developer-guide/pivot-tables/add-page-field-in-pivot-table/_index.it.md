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
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
// Imposta la riga di intestazione
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Popola 9 righe di dati di esempio: Frutta, Anno, Quantità
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
// Aggiungi una tabella pivot ancorata alla cella E3
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Aggiungi i campi alle rispettive aree: Frutta come Riga, Quantità come Dati, Anno come campo Pagina
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Aggiorna e calcola i dati della tabella pivot
pivotTable.calculateData();
// Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx");
```

### Aggiungere un campo filtro con PageFields.add
Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area del filtro viene sostituita con la chiamata API di livello inferiore.

```java
import com.aspose.cells.*;
// - La tabella pivot e il campo pagina sono costruiti esattamente come in
//   Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit->Riga,
//   Amount->Dati). Di seguito otteniamo il PivotField Year dalla
//   collezione BaseFields e lo passiamo a PageFields.Add - l'
//   alternativa di basso livello ad AddFieldToArea. Il risultato è
//   funzionalmente identico allo Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
// Intestazioni
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");
// Dati di esempio (9 righe)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100);
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150);
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200);
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300);
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400);
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500);
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250);
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350);
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450);
// Aggiunge tabella pivot in E3 coprendo A1:C10
int pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Fruit -> Riga, Amount -> Dati (Year andrà in Page sotto)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Approccio di basso livello: prendi il PivotField Year esistente da BaseFields
// e registralo nell'area Page tramite PageFields.Add(PivotField).
PivotField yearField = pivotTable.getBaseFields().get("Year");
pivotTable.getPageFields().add(yearField);
// Aggiorna così che il nuovo campo pagina venga riflesso nel workbook salvato
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
// Popola i dati Frutto/Anno/Importo
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
// Crea tabella pivot in E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int index = pivotTables.add("=A1:C7", "E3", "PivotTable1");
PivotTable pivot = pivotTables.get(index);
// Configura i campi pivot: Frutto in Riga, Importo in Dati, Anno in Pagina
pivot.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivot.addFieldToArea(PivotFieldType.DATA, "Amount");
pivot.addFieldToArea(PivotFieldType.PAGE, "Year");
pivot.calculateData();
// Cancella il filtro di pagina in modo che ogni elemento nel campo pagina sia visibile.
// 0x7FFD (decimale 32765) è il valore sentinella speciale che significa "tutti gli elementi",
// equivalente a selezionare "(Tutti)" nel menu a discesa del campo pagina di Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);
workbook.save("output.xlsx");
```

### Mostra di un singolo elemento specifico
L'impostazione di `CurrentPageItem` su un indice reale seleziona solo quel singolo elemento del filtro. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```java
import com.aspose.cells.*;
// Crea cartella di lavoro
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();
// Aggiungi dati di esempio (Frutto/Anno/Importo)
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
// Aggiungi tabella pivot in E3
PivotTableCollection pivotTables = sheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Aggiungi campi: Frutto→Riga, Importo→Dati, Anno→Pagina
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// Operazioni specifiche del campo pagina
pivotTable.getPageFields().get(0).setCurrentPageItem((short) 1); // 1 = secondo elemento nell'ordine ordinato (es. "2021")
// Aggiorna e calcola la tabella pivot
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
// Dati di esempio: Frutta | Anno | Importo
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
int pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots.get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");
// -- Abilita selezione multipla sul campo pagina
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);
// Parte A -- seleziona TUTTI gli elementi (rendi visibile ogni elemento)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}
// Parte B -- seleziona solo elementi specifici per valore di origine
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