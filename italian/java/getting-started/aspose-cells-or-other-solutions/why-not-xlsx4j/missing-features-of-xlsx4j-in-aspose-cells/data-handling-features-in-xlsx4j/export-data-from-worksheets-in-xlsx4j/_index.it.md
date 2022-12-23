---
title: Esporta dati da fogli di lavoro in xlsx4j
type: docs
weight: 20
url: /it/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - Esporta dati da fogli di lavoro**
Aspose.Cells non solo consente ai suoi utenti di importare dati in fogli di lavoro da fonti di dati esterne, ma consente anche loro di esportare i dati del foglio di lavoro in un array.

**Java**

{{< highlight "java" >}}

 //Creazione di un flusso di file contenente il file Excel da aprire

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Creazione di un'istanza di un oggetto Workbook

Cartella di lavoro cartella di lavoro = nuova cartella di lavoro(fstream);

//Accesso al primo foglio di lavoro nel file Excel

Foglio di lavoro foglio di lavoro = workbook.getWorksheets().get(0);

//Esportazione del contenuto di 7 righe e 2 colonne a partire dalla prima cella in Array.

Object dataTable [][]= worksheet.getCells().exportArray(4,0,7,8);

 per (int i = 0 ; i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **Scarica il codice in esecuzione**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Esportazione di dati da fogli di lavoro](/java/exporting-data-from-worksheets).

{{% /alert %}}
