---
title: عرض وإخفاء علامات التبويب للورقة العمل باستخدام Aspose.Cells
type: docs
weight: 50
url: /ar/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

