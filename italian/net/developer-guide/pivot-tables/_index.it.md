---
title: Inserire una tabella pivot
linktitle: Inserire una tabella pivot
description: Creare e formattare tabelle pivot in file di fogli di calcolo Excel.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot.
type: docs
weight: 160
url: /it/net/create-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un rapporto riassuntivo interattivo: condensa un ampio blocco di dati grezzi, organizzati riga per riga, in una matrice compatta senza utilizzare alcuna formula. Si decide quali campi diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregati come valori: la tabella pivot si occupa del raggruppamento e dei calcoli:
- **Riepilogare** — mostra il totale delle vendite per prodotto, per regione o per trimestre, anziché utilizzare lunghe catene di formule.
- **Confrontare** — disporre le categorie sulle righe e i periodi sulle colonne trasforma un elenco piatto in un rapporto incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Scendere ai dettagli** — fare doppio clic su un valore riepilogato per esaminare le righe di origine sottostanti.
- **Aggiornare** — quando cambiano i dati di origine, un singolo aggiornamento ricalcola l'intero rapporto.
Gli scenari tipici includono cruscotti di vendita, analisi delle spese per categoria e analisi dell'inventario, ossia qualunque domanda del tipo "come si suddividono questi numeri per categoria e periodo?". Aspose.Cells for .NET consente di creare programmaticamente le stesse tabelle pivot, in modo che le cartelle di lavoro generate dall'applicazione possano contenere rapporti pronti all'uso anziché soltanto dati grezzi.

### **Modello a oggetti della tabella pivot**
Aspose.Cells fornisce un insieme specifico di classi nel namespace [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) utilizzate per creare e controllare le tabelle pivot. Queste classi vengono utilizzate per creare e configurare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), i componenti fondamentali di una tabella pivot. Gli oggetti sono:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) rappresenta un campo in una [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) in una [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) rappresenta un oggetto PivotTable su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) presenti su un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
La creazione di una tabella pivot richiede tre operazioni: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e collocare i campi nelle aree delle righe, delle colonne e dei dati.
1. Aggiungere i dati a un foglio di lavoro utilizzando il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) dell'oggetto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell). Questi dati verranno utilizzati come origine dei dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) della raccolta [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection): `Add(sourceData, row, column)`. `sourceData` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono le coordinate della cella di destinazione nell'angolo superiore sinistro della tabella pivot, espresse con indici a base zero (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
3. Collocare i campi con il metodo `AddFieldToArea` dell'oggetto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable): il nome di un campo va nell'area delle righe (`PivotFieldType.Row`), nell'area delle colonne (`PivotFieldType.Column`) o nell'area dei dati (`PivotFieldType.Data`).
4. Salvare la cartella di lavoro — la tabella pivot viene scritta nel file salvato.
Dopo l'esecuzione del codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Crea un nuovo workbook e ottieni il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Scrivi i dati di origine: vendite per sport e trimestre
sheet.Cells["A1"].PutValue("Sport");
sheet.Cells["B1"].PutValue("Quarter");
sheet.Cells["C1"].PutValue("Sales");
sheet.Cells["A2"].PutValue("Golf");
sheet.Cells["B2"].PutValue("Qtr3");
sheet.Cells["C2"].PutValue(1500);
sheet.Cells["A3"].PutValue("Golf");
sheet.Cells["B3"].PutValue("Qtr4");
sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Tennis");
sheet.Cells["B4"].PutValue("Qtr3");
sheet.Cells["C4"].PutValue(600);
sheet.Cells["A5"].PutValue("Tennis");
sheet.Cells["B5"].PutValue("Qtr4");
sheet.Cells["C5"].PutValue(1500);
sheet.Cells["A6"].PutValue("Tennis");
sheet.Cells["B6"].PutValue("Qtr3");
sheet.Cells["C6"].PutValue(4070);
sheet.Cells["A7"].PutValue("Tennis");
sheet.Cells["B7"].PutValue("Qtr4");
sheet.Cells["C7"].PutValue(5000);
sheet.Cells["A8"].PutValue("Golf");
sheet.Cells["B8"].PutValue("Qtr3");
sheet.Cells["C8"].PutValue(6430);

// Aggiungi una tabella pivot nella cella di destinazione E3, utilizzando A1:C8 come origine
PivotTable pivotTable = sheet.PivotTables.Add("A1:C8", 2, 4);

// Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Quarter");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");

// Salva il workbook
workbook.Save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dei dati, l'intervallo deve essere compreso tra l'angolo in alto a sinistra e quello in basso a destra. Ad esempio, "A1:C3" è valido, ma "C3:A1" non lo è.
{{% /alert %}}

## Articoli correlati
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modificare il layout dei campi di pagina in una tabella pivot](/cells/it/net/change-page-field-layout/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/net/filter-by-label-or-value-of-pivot-table/)
- [Gestire i campi valore delle tabelle pivot in Aspose.Cells for .NET](/cells/it/net/manage-value-fields/)

{{< app/cells/assistant language="csharp" >}}