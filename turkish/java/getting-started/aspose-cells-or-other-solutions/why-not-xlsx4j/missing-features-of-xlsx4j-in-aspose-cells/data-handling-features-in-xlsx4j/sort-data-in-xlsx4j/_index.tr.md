---
title: xlsx4j de Veriyi Sırala
type: docs
weight: 60
url: /tr/java/sort-data-in-xlsx4j/
---

## **Aspose.Cells - Veriyi Sırala**
Aspose.Cells kullanarak elektronik tabloda veriyi sıralamak için, hücre alanının kolayca ayarlanabilen bazı özelliklerini ayarladıktan sonra DataSorter.sorter() metodunu çağırın.
Aşağıda Java kodu belirtilmiştir:

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "AsposeDataInput.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Get the cells collection in the sheet

Cells cells = worksheet.getCells();

//Obtain the DataSorter object in the workbook

DataSorter sorter = workbook.getDataSorter();

//Set the first order

sorter.setOrder1(SortOrder.ASCENDING);

//Define the first key.

sorter.setKey1(0);

//Set the second order

sorter.setOrder2(SortOrder.ASCENDING);

//Define the second key

sorter.setKey2(1);

//Create a cells area (range).

CellArea ca = new CellArea();

//Specify the start row index.

ca.StartRow = 1;

//Specify the start column index.

ca.StartColumn = 0;

//Specify the last row index.

ca.EndRow = 9;

//Specify the last column index.

ca.EndColumn = 2;

//Sort data in the specified data range (A2:C10)

sorter.sort(cells, ca);

//Saving the excel file

workbook.save(dataDir + "AsposeSortedData_Out.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/sortdata/AsposeDataSort.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Veri Sıralama](/java/veri-sıralama) veya [Veri Sıralama](/hücreler/tr/java/veri-sıralama) adresini ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
