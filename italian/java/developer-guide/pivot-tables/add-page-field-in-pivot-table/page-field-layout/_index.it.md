---
title: Modificare il Layout dei Campi Pagina in una Tabella Pivot
linktitle: Modificare il Layout dei Campi Pagina in una Tabella Pivot
description: Scopri come controllare il layout dell'area dei campi pagina in una tabella pivot utilizzando Aspose.Cells for Java, incluse l'impostazione dell'ordine di visualizzazione, del conteggio di disposizione e dell'ordine dei campi pagina nella parte superiore della tabella pivot.
keywords: Aspose.Cells, libreria Java, foglio di calcolo, tabella pivot, campo pagina, ordine dei campi pagina, conteggio di disposizione dei campi pagina, spostare campo pagina
type: docs
weight: 191
url: /it/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Questo articolo è una continuazione del tema **Aggiungere un Campo Pagina in una Tabella Pivot**. Illustra come controllare il layout dell'area dei campi pagina, ovvero la striscia di controlli filtro nella parte superiore di una tabella pivot, inclusi l'ordine di visualizzazione, il conteggio di disposizione e il riordino dei campi.

{{% /alert %}}

## **Introduzione**

Una tabella pivot in Microsoft Excel espone una dedicata **area dei campi pagina** che si trova sopra il corpo di righe/colonne/dati della tabella. Questa area viene visualizzata come una striscia di controlli filtro a discesa (uno per ciascun campo pagina) ed è ciò su cui l'utente finale fa clic per sezionare la pivot in base a criteri come anno o regione. Aspose.Cells modella questa area attraverso la raccolta `pivotTable.getPageFields()` ed espone tre proprietà che controllano come la striscia viene visivamente disposta:

- `pivotTable.getPageFieldOrder()` (un valore `Aspose.Cells.PrintOrderType`) decide se i campi pagina aggiuntivi vengono posizionati *accanto* a quelli esistenti oppure *sotto* di essi.
- `pivotTable.getPageFieldWrapCount()` imposta quanti campi pagina vengono posizionati per riga o colonna prima di andare a capo.
- `pivotTable.getPageFields().move(currIndex, destIndex)` riordina i campi pagina senza modificare la modalità di ordine.

Questo articolo illustra tre esempi di codice che dimostrano ciascuna di queste operazioni su un dataset condiviso, in modo che tu possa confrontare i layout risultanti fianco a fianco.

## **Dati di Origine**

Tutti e tre gli esempi seguenti caricano queste otto righe di dati di vendita in un foglio di lavoro denominato `PivotData`. I dati contengono due candidati come campo pagina (`Year`, `Region`), un candidato come campo riga (`Fruit`) e una misura (`Amount`), il che rende significativo ispezionare la striscia dei campi pagina.

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

Tutte le otto righe sono popolate in ogni esempio di codice, nello stesso ordine, quindi i dati di origine non differiscono mai tra gli scenari: cambiano solo le proprietà del layout dei campi pagina.

## **Esempio 1: Da Sinistra a Destra poi in Basso**

Nel primo scenario configuriamo i due campi pagina (`Year`, `Region`) in modo che appaiano **affiancati in una singola riga** nella parte superiore della tabella pivot. Assegnamo `Fruit` all'asse delle righe, posizioniamo `Year` prima e `Region` dopo sull'asse pagina (l'ordine delle chiamate `addFieldToArea` determina l'indice iniziale), aggiungiamo `Amount` (Sum) come campo dati e quindi impostiamo `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` con `pivotTable.setPageFieldWrapCount(2)`. Con `OVER_THEN_DOWN` e un conteggio di disposizione di 2, i due campi pagina sono disposti orizzontalmente fianco a fianco in una singola riga nella parte superiore della tabella pivot, quindi la striscia occupa una riga di larghezza due.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// Intestazioni (riga 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// Riga 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Riga 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Riga 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Riga 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Riga 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Riga 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Riga 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Riga 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// Aggiungi foglio PivotTableReport
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// Crea tabella pivot con origine da PivotData!A1:D9 posizionata in A1 su PivotTableReport
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// Aggiungi campi
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Frutta
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // Anno
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Regione
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Importo
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// Configura il layout dell'area dei campi pagina: posiziona prima i campi pagina in orizzontale, va a capo ogni 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// Aggiorna e calcola
pivotTable.calculateData();

// Salva
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```

## **Esempio 2: Dall'Alto in Basso poi a Destra**

In questo esempio posizioniamo `Fruit` sull'asse delle righe, `Year` e `Region` sull'asse pagina (con `Year` prima), e `Amount` (Sum) come campo dati, esattamente come nell'Esempio 1. Quindi impostiamo `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` e `pivotTable.setPageFieldWrapCount(2)`. Con `DOWN_THEN_OVER` e un conteggio di disposizione di 2, i due campi pagina sono impilati verticalmente, `Year` in alto, `Region` direttamente sotto, formando una singola colonna nella parte superiore della tabella pivot. La striscia occupa quindi due righe di larghezza uno, in contrasto con l'Esempio 1.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");

String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Esempio 3: Spostare un Campo Pagina**

Nel terzo scenario manteniamo questo dataset e l'allocazione dei campi, impostiamo un layout neutro (`OVER_THEN_DOWN` con conteggio di disposizione `2`), e quindi dimostriamo l'operazione `pageFields.move`. La chiamata `move(0, 1)` sposta il campo pagina all'indice 0 (`Year`) nella posizione 1, e il campo pagina che era nella posizione 1 (`Region`) si sposta nella posizione 0. Dopo questa chiamata, `Region` è il primo campo pagina e `Year` è il secondo. La modalità di disposizione e di ordine rimangono invariate, quindi la striscia è ancora visualizzata orizzontalmente fianco a fianco: solo l'ordine dei due menu a discesa è stato scambiato.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");

int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```

## **Articoli Correlati**

- [Aggiungere un Campo Pagina in una Tabella Pivot](/cells/it/java/add-page-field-in-pivot-table/) — la pagina padre che introduce come i campi pagina vengono aggiunti a una tabella pivot.
- [Campi Riga e Colonna in una Tabella Pivot](/cells/it/java/row-and-column-fields/) — copre l'allocazione dei campi agli assi di riga e colonna, completando il lavoro sull'asse pagina mostrato qui.
- [Gestire i Campi Valore in una Tabella Pivot](/cells/it/java/manage-value-fields/) — descrive come configurare l'area dati (valore), inclusa l'aggregazione `Sum` utilizzata in questo articolo.
- [Aggiornare una Tabella Pivot](/cells/it/java/refresh-pivot-table/) — spiega `refreshData()` e `calculateData()`, che sono necessari dopo aver riordinato i campi pagina.
- [Applicare uno Stile a una Tabella Pivot](/cells/it/java/apply-style-to-pivot-table/) — mostra come formattare la tabella pivot renderizzata dopo che la striscia dei campi pagina è stata disposta.

{{< app/cells/assistant language="java" >}}