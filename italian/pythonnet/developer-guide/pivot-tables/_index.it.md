---
title: Inserisci tabella pivot
description: Creare e formattare Tabella Pivot con Aspose.Cells per Python via .NET.
linktitle: Tabelle Pivot
url: /it/python-net/pivot-tables/
type: docs
weight: 160
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
keywords: Creare Tabella Pivot, Inserire Tabella Pivot, Formattare Tabella Pivot.
---

## **Creare tabella pivot**
È possibile utilizzare Aspose.Cells per Python via .NET per aggiungere tabelle pivot ai fogli di calcolo in modo programmatico.

### **Modello di oggetto di tabella pivot**
Aspose.Cells per Python via .NET fornisce un insieme speciale di classi nello spazio dei nomi [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) che vengono utilizzate per creare e controllare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), i mattoni di costruzione di una tabella pivot. Gli oggetti sono:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**
1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) dell'oggetto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) della raccolta [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (spiegati sopra) per gestire la tabella pivot.
Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.
{{% /alert %}}

## **Argomenti avanzati**

{{< app/cells/assistant language="python-net" >}}