---
title: عرض وإخفاء علامات تبويب المصنف في xlsx4j
type: docs
weight: 40
url: /ar/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---
## **Aspose.Cells - عرض وإخفاء علامات تبويب المصنف**
يوفر Aspose.Cells فئة ، مصنف ، يمثل ملف إكسل Microsoft. توفر فئة المصنف مجموعة كبيرة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية علامات التبويب في ملف Excel ، يمكن للمطورين استخدام طريقة setShowTabs لفئة المصنف.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
