---
title: Inserisci tabella pivot
description: Creare e formattare tabelle pivot di file di fogli di calcolo di Excel.
linktitle: Tabelle Pivot
url: /it/net/pivot-tables/
type: docs
weight: 160
keywords: Creare Tabella Pivot, Inserire Tabella Pivot, Formattare Tabella Pivot.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Creare tabella pivot**
È possibile utilizzare Aspose.Cells per aggiungere tabelle pivot ai fogli di calcolo in modo programmato.

### **Modello di oggetto di tabella pivot**
Aspose.Cells fornisce un insieme speciale di classi nello spazio dei nomi [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) che vengono utilizzate per creare e controllare le tabelle pivot. Queste classi vengono utilizzate per creare e impostare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), i mattoni di costruzione di una tabella pivot. Gli oggetti sono:
- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**
1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) dell'oggetto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) della raccolta [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (spiegati sopra) per gestire la tabella pivot.
Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.
{{% /alert %}}

{{< app/cells/assistant language="csharp" >}}