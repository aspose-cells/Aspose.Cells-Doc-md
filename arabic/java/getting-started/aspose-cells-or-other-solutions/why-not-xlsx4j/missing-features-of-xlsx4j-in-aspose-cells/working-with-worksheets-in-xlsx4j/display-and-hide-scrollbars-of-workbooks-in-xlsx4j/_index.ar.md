---
title: عرض وإخفاء أشرطة التمرير للمصنفات في xlsx4j
type: docs
weight: 30
url: /ar/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---
## **Aspose.Cells - عرض وإخفاء أشرطة تمرير مصنفات العمل**
 Aspose.Cells يوفر فصل دراسي ،**دفتر العمل** يمثل ملف Excel.**دفتر العمل** توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. ولكن للتحكم في رؤية أشرطة التمرير في ملف Excel ، يمكن للمطورين استخدام ملفات**setVScrollBarVisible** & **setHScrollBarVisible** طرق**دفتر العمل** صف دراسي.

**Java**

{{< highlight "java" >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)
