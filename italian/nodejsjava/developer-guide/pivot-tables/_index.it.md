---
title: Inserisci una tabella pivot
linktitle: Inserisci una tabella pivot
description: Crea e formatta tabelle pivot in file di cartella di lavoro di Excel utilizzando Aspose.Cells for Node.js via Java.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /it/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un rapporto di riepilogo interattivo: condensa un ampio blocco di dati grezzi, disposti riga per riga, in una matrice compatta senza una sola formula. Si decide quali colonne diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregate come valori; la tabella pivot si occupa del raggruppamento e dei calcoli:
- **Riepilogare** — le vendite totali per prodotto, per regione o per trimestre, invece di lunghe catene di formule.
- **Confrontare** — le categorie nelle righe e i periodi nelle colonne trasformano un elenco piatto in un rapporto incrociato in cui le tendenze sono immediatamente visibili.
- **Analizzare in dettaglio** — fare doppio clic su un valore riepilogato per esaminare le righe di origine.
- **Aggiornare** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero rapporto.
Scenari tipici sono i dashboard di vendita, la ripartizione delle spese e l'analisi dell'inventario: qualsiasi domanda del tipo «come si suddividono questi numeri per categoria e periodo?». Aspose.Cells for Node.js via Java consente di creare le stesse tabelle pivot a livello di programmazione, in modo che le cartelle di lavoro generate dall'applicazione possano contenere rapporti già pronti anziché soltanto dati grezzi.

### **Modello a oggetti della tabella pivot**
Aspose.Cells fornisce un insieme di classi utilizzate per creare e controllare le tabelle pivot. Gli elementi costitutivi sono:
- `PivotField` rappresenta un campo in una `PivotTable`.
- `PivotFieldCollection` rappresenta una raccolta di tutti gli oggetti `PivotField` nella `PivotTable`.
- `PivotTable` rappresenta una tabella pivot in un foglio di lavoro.
- `PivotTableCollection` rappresenta una raccolta di tutti gli oggetti `PivotTable` in un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
La creazione di una tabella pivot richiede tre passaggi: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e collocare i campi pivot nelle aree delle righe, delle colonne e dei dati.
1. Aggiungere i dati a un foglio di lavoro utilizzando il metodo `putValue` della cella. Questi dati verranno utilizzati come origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo `add` della raccolta `PivotTables`: `add(sourceData, row, column)`. `sourceData` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono le coordinate della cella di destinazione nell'angolo superiore sinistro della tabella pivot, con indicizzazione base 0 (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto `PivotTable`.
3. Posizionare i campi pivot con il metodo `addFieldToArea` dell'oggetto `PivotTable`: il nome di un campo viene assegnato all'area delle righe (`PivotFieldType.ROW`), all'area delle colonne (`PivotFieldType.COLUMN`) o all'area dei dati (`PivotFieldType.DATA`).
4. Salvare la cartella di lavoro: la tabella pivot viene scritta nel file salvato.
Dopo l'esecuzione del codice di esempio, una tabella pivot viene aggiunta al foglio di lavoro.

```javascript
const AsposeCells = require("aspose.cells");

// Crea un nuovo workbook e ottieni il primo foglio di lavoro
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Scrivi i dati di origine: vendite per sport e trimestre
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Aggiungi una tabella pivot nella cella di destinazione E3, usando A1:C8 come origine
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Salva il workbook
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve procedere dall'angolo superiore sinistro a quello inferiore destro. Ad esempio, "A1:C3" è valido, mentre "C3:A1" non lo è.
{{% /alert %}}

## Articoli correlati
- [Aggiungere campi di filtro a una tabella pivot in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Modificare il layout dei campi pagina in una tabella pivot](/cells/it/nodejs-java/change-page-field-layout/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Gestire i campi valore delle tabelle pivot in Aspose.Cells for Node.js via Java](/cells/it/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}