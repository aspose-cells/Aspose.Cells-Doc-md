---
title: Crea tabella pivot
type: docs
weight: 10
url: /it/java/create-pivot-table/
---
## **Crea tabella pivot**

### **Crea tabella pivot utilizzando Aspose.Cells**

{{% alert color="primary" %}}

 Con Aspose.Cells è possibile aggiungere tabelle pivot ai fogli di calcolo. Aspose.Cells ha una serie di classi speciali utilizzate specificamente per creare e controllare tabelle pivot. Queste classi vengono utilizzate per creare e impostare le proprietà di a[**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)oggetto, utilizzato come elementi costitutivi della tabella pivot.

Gli oggetti della tabella pivot sono:

- [**Campo pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): rappresenta un campo in una tabella pivot.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) rappresenta una raccolta di tutte le[**Campo pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)oggetti nella tabella pivot.
- [**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): rappresenta una tabella pivot.
- [**Raccolta di tabelle pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): rappresenta la raccolta di tutti gli oggetti tabella pivot sul foglio di lavoro.

{{% /alert %}}

### **Creazione di una tabella pivot semplice**

Per creare una tabella pivot utilizzando Aspose.Cells, procedi nel seguente modo:

1.  Aggiungi alcuni dati alle celle del foglio di lavoro utilizzando il file[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) dell'oggetto[**valore impostato**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)metodo. Questi dati verranno utilizzati come origine dati per la tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add(com.aspose.cells.PivotTable,%20int,%20int,%20java.lang.String) ) metodo del[**Raccolta di tabelle pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) classe, incapsulata nella[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)oggetto.
1.  Accedi al[**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) oggetto dal[**Raccolta di tabelle pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) passando il[**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)indice.
1.  Utilizzare uno qualsiasi degli oggetti tabella pivot (spiegati sopra) incapsulati nel file[**Tabella pivot**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)oggetto per gestire la tabella pivot.

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve essere impostato da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido; "C3:A1" non è valido.

{{% /alert %}}

L'esempio di codice seguente mostra come creare una semplice tabella pivot seguendo i passaggi di base sopra elencati. Quando si esegue il codice, al foglio di lavoro viene aggiunta una tabella pivot:

**Creazione di una tabella pivot basata su un campo corrispondente**

![cose da fare:immagine_alt_testo](create-pivot-table_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-CreatePivotTable.java" >}}
