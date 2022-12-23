---
title: فرز البيانات في xlsx4j
type: docs
weight: 60
url: /ar/java/sort-data-in-xlsx4j/
---
## **Aspose.Cells - فرز البيانات**
لفرز البيانات في جدول بيانات باستخدام Aspose.Cells ، ما عليك سوى استدعاء طريقة DataSorter.sorter () بعد تعيين عدد قليل من خصائص منطقة الخلية سهلة التعيين.
Java كود مذكور أدناه:

**Java**

{{< highlight "java" >}}

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/sortdata/AsposeDataSort.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[فرز البيانات](/java/sort-data) أو[فرز البيانات](/cells/ar/java/data-sorting).

{{% /alert %}}
