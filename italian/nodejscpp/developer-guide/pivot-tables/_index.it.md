---
title: Inserisci tabella pivot
linktitle: Tabelle Pivot
type: docs
weight: 160
url: /it/nodejs-cpp/create-pivot-table/
description: Creare e formattare tabelle pivot di file di fogli di calcolo di Excel.
---

## **Creare tabella pivot**

È possibile usare Aspose.Cells for Node.js via C++ per aggiungere tabelle pivot ai fogli di calcolo in modo programmato.

### **Modello di oggetto di tabella pivot**

Aspose.Cells for Node.js via C++ fornisce un set speciale di classi utilizzate per creare e controllare tabelle pivot. Queste classi sono utilizzate per creare e impostare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), i mattoni fondamentali di una tabella pivot. Gli oggetti sono:

- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**

1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) dell'oggetto [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) della raccolta [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-create-pivot-table.js" >}}

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.

{{% /alert %}}
