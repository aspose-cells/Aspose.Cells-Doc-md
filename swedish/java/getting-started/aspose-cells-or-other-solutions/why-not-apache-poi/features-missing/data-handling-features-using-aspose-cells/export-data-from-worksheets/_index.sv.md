---
title: Exportera data från kalkylblad
type: docs
weight: 40
url: /sv/java/export-data-from-worksheets/
---
## **Aspose.Cells - Exportera data från arbetsblad**
Aspose.Cells låter inte bara sina användare importera data till kalkylblad från externa datakällor utan låter dem också exportera kalkylbladsdata till en array.

**Java**

{{< highlight "java" >}}

 //Skapa en filström som innehåller Excel-filen som ska öppnas

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Instantiering av ett arbetsboksobjekt

Arbetsbok arbetsbok = ny arbetsbok(fstream);

//Åtkomst till det första kalkylbladet i Excel-filen

Arbetsblad arbetsblad = workbook.getWorksheets().get(0);

//Exportera innehållet i 7 rader och 2 kolumner från 1:a cellen till Array.

Objektdatatabell [][]= kalkylblad.getCells().exportArray(4,0,7,8);

 för (int i = 0 ; i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

//Closing the file stream to free all resources

fstream.close();

{{< /highlight >}}
## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 För mer information, besök[Exportera data från arbetsblad](/java/exporting-data-from-worksheets).

{{% /alert %}}
