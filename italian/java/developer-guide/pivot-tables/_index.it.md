---
title: Creare tabella pivot
type: docs
weight: 10
url: /it/java/create-pivot-table/
---

## **Creare tabella pivot**

### **Creare una tabella pivot utilizzando Aspose.Cells**

{{% alert color="primary" %}}

Con Aspose.Cells, è possibile aggiungere tabelle pivot ai fogli di calcolo. Aspose.Cells ha una serie di classi speciali utilizzate specificatamente per creare e controllare tabelle pivot. Queste classi vengono utilizzate per creare e impostare le proprietà di un oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), utilizzato come blocchi di costruzione della tabella pivot.

Gli oggetti tabella pivot sono:

- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): rappresenta un campo in una tabella pivot.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) nella tabella pivot.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): rappresenta una tabella pivot.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): rappresenta la raccolta di tutti gli oggetti tabella pivot sul foglio di lavoro.

{{% /alert %}}

### **Creazione di una semplice tabella pivot**

Per creare una tabella pivot utilizzando Aspose.Cells, segui i passaggi seguenti:

1. Aggiungi alcuni dati alle celle del foglio di lavoro utilizzando il metodo [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) dell'oggetto [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). Questi dati saranno utilizzati come origine dati per la tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-java.lang.String-) della classe [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection), incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. Accedi all'oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) dalla [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) passando l'indice [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
1. Utilizza uno qualsiasi degli oggetti tabella pivot (spiegati sopra) incapsulati nell'oggetto [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) per gestire la tabella pivot.

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve essere impostato dall'angolo in alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido; "C3:A1" non è valido.

{{% /alert %}}

L'esempio di codice qui sotto mostra come creare una semplice tabella pivot seguendo i passaggi di base elencati sopra. Quando si esegue il codice, viene aggiunta una tabella pivot al foglio di lavoro:

**Creazione di una tabella pivot basata su un campo corrispondente**

![todo:image_alt_text](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
