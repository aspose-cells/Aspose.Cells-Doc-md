---
title: نسخ ورقة داخل المصنف
type: docs
weight: 40
url: /ar/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - نقل أو نسخ الأوراق داخل المصنف**
فيما يلي الخطوات المتبعة لنسخ أوراق العمل ونقلها داخل المصنفات أو بينها.

1. لنقل الأوراق أو نسخها داخل المصنفات أو بينها ، افتح المصنف الذي سيتلقى الأوراق.
1. قم بالتبديل إلى المصنف الذي يحتوي على الأوراق التي تريد نقلها أو نسخها ، ثم حدد الأوراق.
1.  على ال**تعديل** القائمة ، انقر فوق**نقل أو نسخ الورقة**.
1. في مربع الكتاب ، انقر فوق المصنف لتلقي الأوراق.
1.  لنقل الأوراق المحددة أو نسخها إلى مصنف جديد ، انقر فوق "موافق"**كتاب جديد**.
1.  في ال**قبل الورقة** في المربع ، انقر فوق الورقة التي تريد إدراج الأوراق المنقولة أو المنسوخة قبلها.
1.  لنسخ الأوراق بدلاً من نقلها ، حدد ملف**قم بإنشاء نسخة** خانة الاختيار.
## **Aspose.Cells - نسخ ورقة داخل المصنف**
{{% alert color="primary" %}} 

يوفر Aspose.Cells طريقة محملة بشكل زائد ، WorksheetCollection.addCopy () ، تُستخدم لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إصدار واحد من الأسلوب يأخذ فهرس ورقة العمل المصدر كمعامل. الإصدار الآخر يأخذ اسم ورقة العمل المصدر.

يوضح المثال التالي كيفية نسخ ورقة عمل موجودة داخل مصنف.

{{% /alert %}} 

نسخ الأوراق باستخدام Aspose.Cells

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - نسخ ورقة داخل المصنف**
{{% alert color="primary" %}} 

Workbook.cloneSheet () يستخدم لنسخ الأوراق مع المصنف.

{{% /alert %}} 

نسخ الأوراق باستخدام Apache POI SS

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / workheets / copysheetwithinworkbook)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[نسخ أوراق العمل ونقلها](/cells/ar/java/copying-and-moving-worksheets).

{{% /alert %}}
