---
title: تقسيم الأجزاء في Apache POI و Aspose.Cells
type: docs
weight: 70
url: /ar/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - تقسيم الأجزاء**
يوفر Aspose.Cells فئة ، مصنف يمثل Microsoft ملف Excel. توفر فئة المصنف مجموعة كبيرة من الخصائص والأساليب لإدارة ملفات Excel. لتنفيذ طرق العرض المقسمة ، استخدم طريقة تقسيم فئة ورقة العمل. لإزالة الأجزاء المنقسمة ، استخدم طريقة removeSplit.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - تقسيم الأجزاء**
يمكن تحقيق وظيفة تقسيم الأجزاء عن طريق طريقة createSplitPane أثناء استخدام Apache POI SS (HSSF & XSSF) API

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)src / main / java / com / aspose / cells / أمثلة / featurescomparison / cellrowscolumns / splitpanes)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تقسيم الأجزاء](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}
