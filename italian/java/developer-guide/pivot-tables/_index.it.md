---
title: Crea una tabella pivot
linktitle: Crea una tabella pivot
description: Crea e formatta tabelle pivot con Aspose.Cells for Java.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot.
type: docs
weight: 160
url: /it/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un report riepilogativo interattivo: condensa un ampio blocco di dati grezzi organizzati riga per riga in una matrice compatta senza utilizzare alcuna formula. Si decide quali colonne utilizzare come etichette di riga, quali come etichette di colonna e quali aggregare come valori: la tabella pivot esegue il raggruppamento e i calcoli:
- **Riepilogare** — vendite totali per prodotto, per regione o per trimestre, anziché lunghe catene di formule.
- **Confrontare** — categorie sulle righe e periodi sulle colonne trasformano un elenco piano in un report incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Analizzare in dettaglio** — fare doppio clic su un valore riepilogato per esaminare le righe di origine sottostanti.
- **Aggiornare** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero report.
Gli scenari tipici sono dashboard di vendita, analisi delle spese e analisi dell'inventario, ossia qualunque domanda del tipo «come si suddividono questi numeri per categoria e tempo?». Aspose.Cells for Java consente di creare a livello di codice le stesse tabelle pivot, in modo che le cartelle di lavoro generate dall'applicazione possano contenere report pronti all'uso anziché solo dati grezzi.

### **Creazione di una tabella pivot con Aspose.Cells**

{{% alert color="primary" %}}
Con Aspose.Cells, è possibile aggiungere tabelle pivot ai fogli di lavoro. Aspose.Cells dispone di una serie di classi dedicate specificamente alla creazione e al controllo delle tabelle pivot. Queste classi sono utilizzate per creare e impostare le proprietà di un oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), che costituisce l'elemento di base per la creazione di tabelle pivot.
Gli oggetti relativi alle tabelle pivot sono:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): rappresenta un campo in una tabella pivot.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) presenti nella tabella pivot.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): rappresenta una tabella pivot.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): rappresenta la raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) presenti sul foglio di lavoro.
{{% /alert %}}

### **Creazione di una tabella pivot semplice**
La creazione di una tabella pivot richiede tre operazioni: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e collocare i campi nelle aree delle righe, delle colonne e dei dati.
1. Aggiungere i dati alle celle del foglio di lavoro utilizzando il metodo [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) dell'oggetto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) (`putValue` nella maggior parte degli esempi). Questi dati costituiranno l'origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) della classe [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): `add(sourceData, row, column)`. `sourceData` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono le coordinate, indicizzate da zero, della cella di destinazione in cui si trova l'angolo superiore sinistro della tabella pivot (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
3. Collocare i campi della tabella pivot mediante il metodo `addFieldToArea` dell'oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): il nome di un campo viene assegnato all'area delle righe (`PivotFieldType.ROW`), all'area delle colonne (`PivotFieldType.COLUMN`) o all'area dei dati (`PivotFieldType.DATA`).
4. Salvare la cartella di lavoro — la tabella pivot viene scritta nel file salvato.
L'esempio di codice seguente crea una tabella pivot semplice seguendo questi passaggi. Quando viene eseguito, aggiunge al foglio di lavoro una tabella pivot basata sui dati di origine:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Crea una nuova cartella di lavoro e ottieni il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Scrivi i dati di origine: vendite per sport e trimestre
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Aggiungi una tabella pivot alla cella di destinazione E3, usando A1:C8 come origine
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Salva la cartella di lavoro
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Quando un intervallo di celle viene assegnato come origine dei dati, deve essere specificato dall'angolo superiore sinistro a quello inferiore destro. Ad esempio, "A1:C3" è valido; "C3:A1" non è valido.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}