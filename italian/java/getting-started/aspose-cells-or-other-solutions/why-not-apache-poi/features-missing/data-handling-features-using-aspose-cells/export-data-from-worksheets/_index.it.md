---
title: Esporta dati da fogli di lavoro
type: docs
weight: 40
url: /it/java/export-data-from-worksheets/
---
## **Aspose.Cells - Esporta dati da fogli di lavoro**
Aspose.Cells non solo consente ai suoi utenti di importare dati in fogli di lavoro da fonti di dati esterne, ma consente anche loro di esportare i dati del foglio di lavoro in un array.

**Giava**

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

//Closing the file stream to free all resources

fstream.close();

{{< /highlight >}}
## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Scarica il codice di esempio**
- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Esportazione di dati da fogli di lavoro](/java/exporting-data-from-worksheets).

{{% /alert %}}
