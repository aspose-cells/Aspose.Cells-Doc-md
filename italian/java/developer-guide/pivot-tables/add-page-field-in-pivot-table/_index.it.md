---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells per .NET
linktitle: Aggiungere campi filtro
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for Java, inclusi l'aggiunta di campi filtro, il filtro a selezione singola e il filtro a selezione multipla.
keywords: Aspose.Cells, Java, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/java/add-filter-field-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello o tramite la raccolta di livello inferiore `PageFields`, ed è possibile gestire il filtro pagina in modalità a selezione singola, cancellarlo per mostrare ogni voce di pagina, oppure commutare il campo sulla selezione multipla così che gli utenti possano selezionare più voci di pagina contemporaneamente tramite l'interfaccia utente delle caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**

Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato dal corpo della pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una pivot resa in Excel, e selezionando una delle voci di pagina disponibili il corpo della pivot viene ricostruito in modo che vengano riepilogati solo i record appartenenti a quella voce di pagina. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché come `PivotFieldType.Row`, `PivotFieldType.Column`, o `PivotFieldType.Data`.

Un campo filtro può operare in due modalità. Nella modalità predefinita **selezione singola** solo una voce di pagina è visibile alla volta, quindi il corpo della pivot riepiloga esattamente un sottoinsieme. Nella modalità **selezione multipla** il campo espone un elenco di caselle di controllo e il corpo della pivot riepiloga l'unione di ogni voce di pagina selezionata. Lo stesso campo di origine può essere spostato avanti e indietro tra queste modalità attivando/disattivando una singola proprietà.

Aspose.Cells for Java espone due modi equivalenti per registrare un campo filtro. L'API di alto livello è `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")`, che accetta il nome della colonna di origine e aggiunge il campo in un'unica chiamata. L'API di livello inferiore è `PivotTable.PageFields.add(PivotField)`, che viene utilizzata quando si possiede già un riferimento `PivotField` e si desidera aggiungere la stessa istanza di campo all'area filtro. Entrambe le API finiscono per popolare la stessa raccolta `PageFields`, e il resto di questo articolo mostra come scegliere tra esse e come gestire ciascuna modalità di filtro.

## **Aggiunta di un campo filtro**

Esistono due modi per registrare un campo pivot nell'area filtro. La chiamata di alto livello accetta il nome della colonna di origine come stringa ed è il percorso più comune. La chiamata di livello inferiore accetta un'istanza esistente di `PivotField` ed è comoda quando lo stesso oggetto campo deve essere riutilizzato su più aree pivot. Entrambe le chiamate inseriscono il campo in `PivotTable.PageFields`, dopodiché appare come menu a discesa della pagina nella parte superiore della pivot resa.

### Aggiunta di un campo filtro con addFieldToArea

L'esempio seguente crea un piccolo set di dati Frutto / Anno / Importo, posiziona una tabella pivot alla cella E3 con `Fruit` nell'area righe, `Amount` nell'area dati, e `Year` nell'area filtro, aggiorna la pivot e salva la cartella di lavoro.

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

// Aggiungi campi alle loro aree: Frutta come Riga, Quantità come Dati, Anno come Campo Pagina
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year");

// Aggiorna e calcola i dati della tabella pivot
pivotTable.calculateData();

// Salva la cartella di lavoro
workbook.save("pageFieldSample.xlsx");
```

### Aggiunta di un campo filtro con PageFields.add

Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale dell'area filtro viene sostituita con la chiamata API di livello inferiore.

```java
- La tabella pivot e il campo pagina sono costruiti esattamente come nello
  Scenario 1a (dati Fruit/Year/Amount, pivot in E3, Fruit->Riga,
  Amount->Dati). Di seguito otteniamo il PivotField Year dalla
  collezione BaseFields e lo passiamo a PageFields.Add - l'
  alternativa di basso livello ad AddFieldToArea. Il risultato è
  funzionalmente identico allo Scenario 1a.

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

// Aggiorna affinché il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
pivotTable.calculateData();

workbook.save("output.xlsx");
```

## **Filtro a selezione singola (visualizzazione di una voce di pagina)**

Nella modalità predefinita a selezione singola, il campo filtro viene reso come un singolo menu a discesa e l'intero `PivotField.CurrentPageItem` seleziona quale voce di pagina guida il corpo della pivot. Assegnando un indice specifico viene selezionata solo quella voce; assegnando il valore sentinella speciale `0x7FFD` (decimale 32765) il filtro viene cancellato così che ogni voce di pagina venga riepilogata immediatamente. La selezione singola è la modalità predefinita; non è necessario abilitarla esplicitamente.

### Visualizzazione di tutte le voci

Impostare `CurrentPageItem` sul valore magico `0x7FFD` equivale a cancellare il filtro pagina: il corpo della pivot riepiloga ogni voce di pagina come se non fosse applicato alcun filtro.

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

// Crea una tabella pivot in E3
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
// equivalente a selezionare "(Tutto)" nel menu a discesa del campo pagina di Excel.
pivot.getPageFields().get(0).setCurrentPageItem((short)0x7FFD);

workbook.save("output.xlsx");
```

### Visualizzazione di una voce specifica

Impostare `CurrentPageItem` su un indice reale seleziona solo quella voce di pagina. L'indice è la posizione della voce nell'elenco ordinato delle voci del campo filtro, quindi ad esempio `1` seleziona la seconda voce dopo l'ordinamento.

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

Il filtro a selezione multipla trasforma il menu a discesa della pagina in un elenco di caselle di controllo e consente all'utente finale di selezionare più voci di pagina contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia utente a selezione multipla abbia qualsiasi effetto. Dopo averlo abilitato, `PivotItem.IsHidden` controlla quali voci compaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni voce oppure includere nella whitelist solo voci specifiche.

Il codice seguente abilita la selezione multipla sullo stesso campo filtro Year costruito nello Scenario 1a, e poi mostra due schemi: la Parte A rivela ogni voce di pagina lasciando `IsHidden` impostato su `false` per ogni voce, mentre la Parte B include nella whitelist solo i valori di origine scelti e nasconde tutto il resto tramite un blocco `switch (pivotItems[i].getStringValue())`.

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

// -- Abilita la selezione multipla sul campo pagina
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(true);

// Parte A -- seleziona TUTTI gli elementi (rendi visibile ogni elemento)
PivotItemCollection pivotItems = pivotTable.getPageFields().get(0).getPivotItems();
for (int i = 0; i < pivotItems.getCount(); i++)
{
    pivotItems.get(i).setHidden(false);
}

// Parte B -- seleziona solo elementi specifici per valore sorgente
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

> **Nota:** Quando si utilizza il filtro a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni voce è nascosta, Excel si arresta in modo anomalo durante l'apertura del file oppure rende una pivot vuota. Verificare sempre che la whitelist a selezione multipla includa almeno una voce dei propri dati di origine.

## **Quale API e quale modalità devo usare?**

La tabella seguente riassume quando utilizzare ciascuna API e modalità così che sia possibile scegliere la combinazione giusta senza leggere ogni scenario in dettaglio.

| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro tramite il nome della colonna di origine (caso più comune) | `PivotTable.addFieldToArea(PivotFieldType.PAGE, "fieldName")` | n/a | Alto livello, una sola riga. Usare questa opzione a meno che non sia necessario un riferimento `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.PageFields.add(PivotField)` | n/a | Usare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare su una singola voce di pagina (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra la seconda voce nell'elenco ordinato. |
| Mostrare tutte le voci / cancellare il filtro pagina | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è il valore sentinella per "tutte le voci". |
| Abilitare l'interfaccia utente a selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata `IsHidden` abbia effetto. |
| Nascondere / mostrare singole voci in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per voce | Almeno una voce deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricordare sempre il vincolo di visibilità quando si configura il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si arresta in modo anomalo all'apertura oppure rende una pivot vuota. Costruire la whitelist in base ai propri dati di origine in modo che almeno una voce rimanga visibile, e le cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}
