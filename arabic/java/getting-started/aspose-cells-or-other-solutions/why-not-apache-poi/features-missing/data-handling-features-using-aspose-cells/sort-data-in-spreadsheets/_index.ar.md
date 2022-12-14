---
title: فرز البيانات في جداول البيانات
type: docs
weight: 70
url: /ar/java/sort-data-in-spreadsheets/
---
## **Aspose.Cells - فرز البيانات في جداول البيانات**
{{% alert color="primary" %}} 

لفرز البيانات في جدول بيانات باستخدام Aspose.Cells ، ما عليك سوى استدعاء طريقة DataSorter.sorter () بعد تعيين عدد قليل من خصائص منطقة الخلية سهلة التعيين.

Java كود مذكور أدناه.

{{% /alert %}} 

فرز البيانات باستخدام Aspose.Cells

**Java**

{{< highlight "java" >}}

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

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/AsposeDataSort.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[فرز البيانات](/java/sort-data) ، أو[فرز البيانات](/cells/ar/java/data-sorting).

{{% /alert %}}
