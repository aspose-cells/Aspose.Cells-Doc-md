---
title: Çalışma Sayfalarından Veri Aktarımı
type: docs
weight: 40
url: /tr/java/export-data-from-worksheets/
---

## **Aspose.Cells - Çalışma Sayfalarından Veri Aktarımı**
Aspose.Cells, kullanıcılarının elektronik tablolara dış veri kaynaklarından veri içe aktarmasının yanı sıra çalışma sayfasındaki veriyi bir diziye aktarmasına da olanak tanır.

**Java**

{{< highlight java >}}

 //Creating a file stream containing the Excel file to be opened

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//Instantiating a Workbook object

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Exporting the contents of 7 rows and 2 columns starting from 1st cell to Array.

Object dataTable [][] = worksheet.getCells().exportArray(4,0,7,8);

for (int i = 0 ; i < dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

//Closing the file stream to free all resources

fstream.close();

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/ExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Sayfalarından Veri Aktarımı](/java/exporting-data-from-worksheets)'ı ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
