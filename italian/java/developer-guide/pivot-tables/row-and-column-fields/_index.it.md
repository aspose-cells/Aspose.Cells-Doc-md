---
title: Campi di riga e colonna in Aspose.Cells for Java
linktitle: Campi di riga e colonna
description: Scopri come aggiungere campi di base alle aree di riga e colonna di una tabella pivot e come controllare i subtotali dei campi pivot utilizzando PivotField.setSubtotals in Aspose.Cells for Java.
keywords: Aspose.Cells, Java, tabella pivot, campo di riga, campo di colonna, PivotField, setSubtotals, PivotFieldSubtotalType, subtotali
type: docs
weight: 220
url: /it/java/row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

I campi di riga e colonna sono gli elementi costitutivi di una tabella pivot. Un campo inserito nell'area delle righe appare verticalmente a sinistra della tabella pivot, mentre un campo inserito nell'area delle colonne appare orizzontalmente nella parte superiore. Questo articolo mostra come aggiungere campi di base a queste aree in modo programmatico e come controllare i subtotali che vengono visualizzati tra i gruppi di campi utilizzando il metodo `PivotField.setSubtotals`.

## **Aggiunta di un campo all'area di riga o colonna**

Il metodo `PivotTable.addFieldToArea(int fieldType, String fieldName)` sposta un campo di base dai dati di origine in una delle quattro aree della tabella pivot. L'argomento `fieldType` accetta uno dei seguenti valori di `PivotFieldType`.

- `ROW` — campi posizionati verticalmente a sinistra
- `COLUMN` — campi posizionati orizzontalmente nella parte superiore
- `DATA` — campi i cui valori vengono aggregati
- `PAGE` — campi utilizzati come filtri del report

Dopo aver aggiunto i campi, è possibile accedervi tramite le proprietà `PivotTable.getRowFields()` e `PivotTable.getColumnFields()`. Ciascuna proprietà restituisce un `PivotFieldCollection`. Il campo all'indice 0 di `RowFields` è il campo di riga più esterno, mentre gli indici successivi rappresentano i campi annidati al suo interno. La stessa convenzione di indicizzazione si applica a `ColumnFields`.

L'ordine di annidamento dei campi è importante. Aggiungere `Category` all'area delle righe prima e poi `Item` produce una tabella pivot il cui raggruppamento esterno è `Category` e il cui raggruppamento interno è `Item`. Invertendo l'ordine si inverte la gerarchia.

## **Subtotali dei campi pivot**

Il metodo `PivotField.setSubtotals(int subtotalType, boolean shown)` controlla quali righe di subtotale vengono visualizzate per un campo pivot. Ogni chiamata attiva/disattiva un singolo tipo di subtotale in modo indipendente. Passando `shown = true` viene visualizzato il subtotale, mentre `shown = false` lo nasconde. Poiché ogni chiamata influisce su un solo tipo, chiamare il metodo più volte con valori diversi di `subtotalType` consente di creare un sottoinsieme personalizzato di subtotali.

L'enum `PivotFieldSubtotalType` definisce i tipi di subtotale disponibili.

- `AUTOMATIC` — Aspose.Cells sceglie la selezione predefinita (tipicamente `SUM` per i campi numerici)
- `NONE` — elimina ogni riga di subtotale
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
I subtotali vengono visualizzati solo quando sono presenti due o più campi pivot nell'area delle righe (o nell'area delle colonne). Un singolo campo non ha elementi significativi tra cui calcolare i subtotali, pertanto in tal caso le chiamate a `setSubtotals` non hanno alcun effetto visibile. Per questo motivo, in tutti gli esempi di questo articolo vengono inseriti due campi di riga (`Category` esterno, `Item` interno), in modo che il confine dei subtotali tra ciascun gruppo `Category` sia visibile.
{{% /alert %}}

## **Scenario 1 — Subtotali automatici (predefiniti)**

Quando non si chiama affatto `setSubtotals`, Aspose.Cells applica la selezione `AUTOMATIC` ai campi numerici. L'esempio seguente conferma esplicitamente questo comportamento chiamando `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` sul campo di riga esterno `Category`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Scenario 2 — Eliminazione di tutti i subtotali (None)**

Chiamando `setSubtotals(PivotFieldSubtotalType.NONE, true)` vengono rimosse tutte le righe di subtotale dalla tabella pivot, lasciando solo le righe dei campi e il totale generale in basso. Ciò è utile quando si desiderano i dati raggruppati grezzi senza righe di riepilogo.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Scenario 3 — Sottoinsieme personalizzato di subtotali (Somma + Media)**

Non si è limitati a un singolo tipo di subtotale. Ogni chiamata a `setSubtotals` opera in modo indipendente su un solo tipo, quindi chiamare il metodo due volte — una volta con `SUM` e una volta con `AVERAGE` — produce un sottoinsieme personalizzato di due righe di subtotale per ciascun gruppo `Category`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

PivotTableCollection pivotTables = worksheet.getPivotTables();
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```

## **Riepilogo**

I tre scenari precedenti condividono lo stesso dataset e la stessa struttura della tabella pivot. L'unica differenza tra essi è la chiamata a `setSubtotals` applicata al campo di riga esterno `Category`. Ricordare la regola dei due campi: un singolo campo in un'area non ha elementi tra cui calcolare i subtotali, quindi inserire sempre almeno due campi nell'area delle righe o delle colonne quando si desidera che `setSubtotals` abbia un effetto visibile.

## **Articoli correlati**

- [Campi pagina nelle tabelle pivot](/cells/it/java/add-page-field-in-pivot-table/)
- [Aggiornamento delle tabelle pivot in Aspose.Cells for Java](/cells/it/java/refresh-pivot-table/)
- [Applicazione di stili alle tabelle pivot](/cells/it/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
