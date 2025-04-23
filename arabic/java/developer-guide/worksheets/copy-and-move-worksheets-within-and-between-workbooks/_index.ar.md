---
title: نسخ ونقل أوراق العمل داخل وبين أوراق العمل
type: docs
weight: 20
url: /ar/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عدد من أوراق العمل مع تنسيقات وإدخال بيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الربعية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

يدعم Aspose.Cells نسخ أو نقل الأوراق داخل أو بين أوراق العمل. تتم نسخ الأوراق بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسومات والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

يشرح هذا المقال كيفية استخدام Aspose.Cells لـ:

- [نسخ ورقة عمل داخل دفتر عمل](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [نقل ورقة عمل داخل دفتر عمل](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [نسخ ورقة عمل بين دفاتر العمل](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [نقل ورقة عمل بين دفاتر العمل](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. أنشئ معينين بيانات في Microsoft Excel. لأغراض هذا المثال، قمنا بإنشاء معينين جديدين في Microsoft Excel وإدخال بعض البيانات إلى أوراق العمل.

- FirstWorkbook.xls (3 ورقات عمل)
- SecondWorkbook.xls (1 ورقة عمل).

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. قم بفك الضغط عنها في جهاز التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. أنشئ مشروعًا:
   1. إنشاء مشروع باستخدام محرر جافا مثل Eclipse أو إنشاء برنامج بسيط باستخدام محرر نصي.
1. إضافة مسار فئة:
   1. استخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
   1. ضبط مسار الفئة للمشروع في Eclipse:
      1. حدد مشروعك في Eclipse وانقر على القوائم **Project**, ثم **Properties**.
      1. حدد **Java Build Path** في الجهة اليسرى من الصندوق، ثم حدد علامة التبويب Libraries،
      1. انقر على **Add JARs** أو **Add External JARs** لتحديد Aspose.Cells.jar و dom4j_1.6.1.jar وإضافتهما إلى مسارات البناء.

{{% alert color="primary" %}}

أو يمكنك تعيين مسار الفئة أثناء التشغيل في نافذة DOS على Windows.
على سبيل المثال:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. نسخ ورقة العمل داخل كتاب عمل:
   أدناه الكود المستخدم لإنجاز المهمة. يقوم بنسخ ورقة العمل النسخ داخل FirstWorkbook.xls.

تنفيذ الكود ينقل ورقة العمل بالاسم نسخة داخل FirstWorkbook.xls بالاسم الجديد الورقة الأخيرة.

**ملف الإخراج**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **نقل ورقة العمل داخل مصنف**

أدناه هو الكود المستخدم لإنجاز المهمة.

تنفيذ الكود ينقل ورقة العمل Move من الفهرس 1 إلى الفهرس 2 في FirstWorkbook.xls.

**ملف الإخراج**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **نسخ ورقة العمل بين دفاتر العمل**

تنفيذ الكود ينسخ ورقة العمل بالاسم Copy إلى SecondWorkbook.xls بالاسم الجديد Sheet2.

**ملف الإخراج**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **نقل ورقة العمل بين دفاتر العمل**

تنفيذ الكود ينقل ورقة العمل move من FirstWorkbook.xls إلى SecondWorkbook.xls بالاسم الجديد Sheet3.

**ملف FirstWorkbook.xls الإخراج**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**ملف SecondWorkbook.xls الإخراج**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **الاستنتاج**

{{% alert color="primary" %}}

يشرح هذا المقال كيفية نسخ ونقل أوراق العمل داخل وبين مصنفات باستخدام Aspose.Cells.

ستفاد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق. نرحب باستفساراتكم وتعليقاتكم واقتراحاتكم في [منتدى Aspose.Cells](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
