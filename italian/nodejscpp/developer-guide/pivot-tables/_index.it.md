---
title: Inserisci una tabella pivot
linktitle: Inserisci una tabella pivot
description: Crea e applica la formattazione alle tabelle pivot con Aspose.Cells for Node.js tramite C++.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot.
type: docs
weight: 160
url: /it/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un report riepilogativo interattivo: condensa un ampio blocco di dati grezzi, disposti riga per riga, in una matrice compatta senza ricorrere a formule. Si decide quali colonne diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregate come valori: la tabella pivot esegue il raggruppamento e i calcoli:
- **Sintetizzare** — il totale delle vendite per prodotto, per regione o per trimestre, invece di ricorrere a lunghe catene di formule.
- **Confrontare** — le categorie disposte nelle righe e i periodi nelle colonne trasformano un elenco piatto in un report incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Analisi dettagliata** — fare doppio clic su un valore riepilogato per esaminare le righe di origine.
- **Aggiornare** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero report.
Gli scenari tipici includono dashboard di vendite, analisi delle spese e analisi dell'inventario, per rispondere a domande come «in che modo questi numeri si suddividono per categoria e periodo?». Aspose.Cells for Node.js tramite C++ consente di creare in modo programmatico le stesse tabelle pivot, in modo che le cartelle di lavoro generate dall'applicazione possano contenere report già pronti anziché solo dati grezzi.

### **Modello a oggetti della tabella pivot**
Aspose.Cells for Node.js tramite C++ fornisce un insieme specifico di classi utilizzate per creare e controllare le tabelle pivot. Tali classi consentono di creare e impostare oggetti [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), i componenti fondamentali di una tabella pivot. Gli oggetti sono:
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) rappresenta un campo all'interno di un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) all'interno di un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) rappresenta un oggetto PivotTable su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) su un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
La creazione di una tabella pivot richiede tre passaggi: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e collocare i campi pivot nelle aree delle righe, delle colonne e dei dati.
1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) dell'oggetto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Questi dati verranno utilizzati come origine dei dati della tabella pivot.
2. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) della raccolta [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection): `add(sourceData, row, column)`. `sourceData` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono le coordinate a base zero della cella di destinazione corrispondente all'angolo superiore sinistro della tabella pivot (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
3. Colloca i campi pivot con il metodo `addFieldToArea` dell'oggetto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable): il nome di un campo viene inserito nell'area delle righe (`PivotFieldType.Row`), nell'area delle colonne (`PivotFieldType.Column`) o nell'area dei dati (`PivotFieldType.Data`).
4. Salva la cartella di lavoro: la tabella pivot viene scritta nel file salvato.
Dopo l'esecuzione del codice di esempio, una tabella pivot viene aggiunta al foglio di lavoro.

```javascript
const AsposeCells = require("aspose.cells.node");

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

// Aggiungi una tabella pivot alla cella di destinazione E3, utilizzando A1:C8 come origine
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Salva il workbook
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dei dati, l'intervallo deve andare dall'angolo superiore sinistro a quello inferiore destro. Ad esempio, "A1:C3" è valido, ma "C3:A1" non lo è.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}