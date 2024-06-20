---
title: عرض وإخفاء علامات التبويب للدفتر في xlsx4j
type: docs
weight: 40
url: /ar/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---

## **Aspose.Cells - عرض وإخفاء علامات التبويب للدفتر**
توفر Aspose.Cells فئة Workbook التي تمثل ملف Microsoft Excel. توفر فئة Workbook مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية علامات التبويب في ملف Excel، يمكن للمطورين استخدام أسلوب setShowTabs من فئة Workbook.

**Java**

{{< highlight java >}}

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
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
