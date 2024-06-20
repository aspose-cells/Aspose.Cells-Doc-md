---
title: تقسيم النوافذ في Apache POI و Aspose.Cells
type: docs
weight: 70
url: /ar/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - تقسيم الألواح**
Aspose.Cells يوفر فئة Workbook التي تمثل ملف Microsoft Excel. توفر فئة Workbook مجموعة واسعة من الخصائص والأساليب لإدارة ملفات Excel. لتنفيذ عروض متقسمة، استخدم طريقة الفئة Worksheet الخاصة بتقسيم. لإزالة النوافذ المتقسمة، استخدم الطريقة removeSplit.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF و XSSF - تقسيم النوافذ**
يمكن تحقيق وظيفة تقسيم النوافذ عن طريق طريقة createSplitPane أثناء استخدام Apache POI SS (HSSF و XSSF) API

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، يرجى زيارة [تقسيم النوافذ](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
