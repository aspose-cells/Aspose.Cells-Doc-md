---
title: نسخ ونقل أوراق العمل داخل وبين المصنفات
type: docs
weight: 20
url: /ar/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى عدد من أوراق العمل ذات التنسيق المشترك وإدخال البيانات. على سبيل المثال ، إذا كنت تعمل باستخدام ميزانيات ربع سنوية ، فقد ترغب في إنشاء مصنف بأوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

Aspose.Cells يدعم نسخ أوراق العمل أو نقلها داخل مصنفات العمل أو بينها. يتم نسخ أوراق العمل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والمخططات والصور والكائنات الأخرى بأعلى درجات الدقة.

{{% /alert %}}

## **نسخ أوراق العمل ونقلها**

تشرح هذه المقالة كيفية استخدام Aspose.Cells من أجل:

- [انسخ ورقة عمل داخل مصنف](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [انقل ورقة عمل داخل مصنف](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [انسخ ورقة عمل بين المصنفات](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [انقل ورقة عمل بين المصنفات](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **نسخ ورقة عمل داخل مصنف**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. قم بإنشاء مصنفين مع بعض البيانات في Microsoft Excel. لأغراض هذا المثال ، أنشأنا مصنفين جديدين في Microsoft Excel وأدخلنا بعض البيانات في أوراق العمل.

- FirstWorkbook.xls (3 أوراق عمل)
- SecondWorkbook.xls (ورقة عمل واحدة).

  **FirstWorkbook.xls**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. قم بفك ضغطه على جهاز الكمبيوتر الخاص بك.
 الجميع[Aspose](http://www.aspose.com/) المكونات ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.
1. أنشئ مشروعًا:
 1. قم بإنشاء مشروع باستخدام محرر Java مثل Eclipse أو قم بإنشاء برنامج بسيط باستخدام محرر نصوص.
1. أضف مسار الفصل:
1. قم باستخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
 1. قم بتعيين مسار الفصل للمشروع في Eclipse:
 1. حدد مشروعك في Eclipse وانقر فوق القوائم**مشروع** ، ومن بعد**الخصائص**.
 1. حدد**Java بناء مسار** في الجانب الأيسر من مربع الحوار ، ثم حدد علامة التبويب المكتبات ،
 1. انقر فوق**أضف الجرار** أو**إضافة JARs خارجية** لاختيار Aspose.Cells.jar و dom4j_1.6.1.jar وإضافتهم إلى مسارات البناء.

{{% alert color="primary" %}}

أو يمكنك ضبط مسار الفصل في وقت التشغيل في موجه DOS على Windows.
فمثلا:

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. نسخ ورقة العمل داخل مصنف:
 يوجد أدناه الكود المستخدم لإنجاز المهمة. يقوم بنسخ ورقة العمل داخل FirstWorkbook.xls.

يؤدي تنفيذ التعليمات البرمجية إلى نقل ورقة العمل المسماة "نسخ" ضمن FirstWorkbook.xls بالاسم الجديد "الورقة الأخيرة".

**ملف إلاخراج**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **نقل ورقة العمل في مصنف**

فيما يلي الكود المستخدم لإنجاز المهمة.

يؤدي تنفيذ التعليمات البرمجية إلى نقل ورقة العمل الانتقال من الفهرس 1 إلى الفهرس 2 في FirstWorkbook.xls.

**ملف إلاخراج**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **نسخ ورقة عمل بين المصنفات**

يؤدي تنفيذ التعليمات البرمجية إلى نسخ ورقة العمل إلى SecondWorkbook.xls بالاسم الجديد Sheet2.

**ملف إلاخراج**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **نقل ورقة العمل بين المصنفات**

يؤدي تنفيذ التعليمات البرمجية إلى نقل ورقة العمل من FirstWorkbook.xls إلى SecondWorkbook.xls بالاسم الجديد Sheet3.

**إخراج FirstWorkbook.xls**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**إخراج SecondWorkbook.xls**

![ما يجب القيام به: image_بديل_نص](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **استنتاج**

{{% alert color="primary" %}}

تشرح هذه المقالة كيفية نسخ أوراق العمل ونقلها داخل المصنفات وفيما بينها باستخدام Aspose.Cells.

 لقد استفاد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق. نرحب باستفساراتك وتعليقاتك واقتراحاتك على[Aspose.Cells المنتدى](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
