---
title: نسخ ورقة داخل سجل العمل
type: docs
weight: 40
url: /ar/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - نقل أو نسخ الأوراق داخل سجل العمل**
فيما يلي الخطوات المعنية بنسخ ونقل ورقات العمل داخل أو بين سجلات العمل.

1. لنقل أو نسخ الأوراق داخل أو بين سجلات العمل، افتح سجل العمل الذي سيتلقى الأوراق.
1. انتقل إلى دفتر العمل الذي يحتوي على الأوراق التي ترغب في نقلها أو نسخها، ثم حدد الأوراق.
1. في قائمة **تحرير**، انقر فوق **نقل أو نسخ الصفحة**.
1. في مربع الكتابة To book، انقر فوق جدول البيانات لاستلام الصفحات.
1. لنقل أو نسخ الصفحات المحددة إلى جدول بيانات جديد، انقر فوق **كتاب جديد**.
1. في مربع **قبل الصفحة**، انقر فوق الصفحة التي ترغب في إدراج الصفحات المنقولة أو المنسوخة قبلها.
1. لنسخ الصفحات بدلاً من نقلها، حدد مربع الاختيار **إنشاء نسخة**.
## **Aspose.Cells - نسخ الصفحة ضمن جدول البيانات**
{{% alert color="primary" %}} 

يوفر Aspose.Cells طريقة محملة، WorksheetCollection.addCopy()، التي يتم استخدامها لإضافة صفحة عمل إلى المجموعة ونسخ البيانات من صفحة العمل الحالية. إصدار واحد من الطريقة يأخذ فهرس صفحة العمل المصدر كمعلمة. الإصدار الآخر يأخذ اسم صفحة العمل المصدر.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

{{% /alert %}} 

نسخ الصفحات باستخدام Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **أباتشي POI SS - نسخ الصفحة ضمن جدول البيانات**
{{% alert color="primary" %}} 

تُستخدم Workbook.cloneSheet() لنسخ الصفحات ضمن جدول البيانات.

{{% /alert %}} 

نسخ الصفحات باستخدام Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [نسخ ونقل الأوراق العمل](/cells/ar/java/copying-and-moving-worksheets).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
