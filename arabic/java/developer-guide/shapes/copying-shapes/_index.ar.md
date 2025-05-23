---
title: نسخ الأشكال بين صفحات العمل
type: docs
weight: 250
url: /ar/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى نسخ صور مختلفة ورسوم بيانية وكائنات رسمية أخرى إلى أوراق عمل مختلفة وفقًا لاحتياجاتك. تدعم Aspose.Cells نسخ الأشكال بين أوراق العمل. يتم نسخ الرسوم البيانية والصور والكائنات الأخرى بأعلى درجة من الدقة.

قد تحاول الأتمتة المكتبية ولكن لها عيوبها الخاصة. هناك عدة أسباب وقضايا متعلقة: على سبيل المثال الأمان والاستقرار والتوسع والسرعة والسعر والميزات. باختصار، هناك العديد من الأسباب، مع احتلال الأولى أن مايكروسوفت نفسها توصي بشدة ضد الأتمتة المكتبية من حلول البرمجيات.

في هذا المقال، نقوم بإنشاء تطبيق وحدة التحكم، وأداء نسخ الصور والرسوم البيانية وغير ذلك من كائنات الرسم بين أوراق العمل لدفتر عمل به بضعة وأبسط الأسطر باستخدام Aspose.Cells.

تم تصميم هذا المستند لتوفير للمطورين فهماً مفصلاً حول كيفية نسخ الأشكال (الصور والرسوم البيانية والتحكمات وغيرها من كائنات الرسم) بين أوراق العمل.

{{% /alert %}}

## **نسخ الأشكال**

يشرح هذا المقال كيفية:

- [نسخ صورة من ورقة عمل واحدة إلى أخرى](/cells/ar/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [نسخ رسم بياني من ورقة عمل واحدة إلى أخرى](/cells/ar/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [نسخ التحكمات وغيرها من كائنات الرسم من ورقة عمل واحدة إلى أخرى](/cells/ar/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **نسخ صورة من ورقة عمل إلى أخرى**

#### **الخطوة 1: إنشاء كتاب العمل مع صورة ورسم بياني في برنامج Microsoft Excel**

1. تم إنشاء كتاب عمل جديد في برنامج Microsoft Excel.
1. إضافة صورة في ورقة العمل الأولى ورسم بياني في الورقة العمل الثانية.

   الصور التالية تظهر الورقتين النموذجيتين المنشأتين في برنامج Microsoft Excel.

   **ورقة العمل “الرسم البياني” مع الرسم البياني**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**ورقة العمل “الصورة” مع الصورة**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

الآن، انسخ الصورة في ورقة العمل المسماة “الصورة” إلى الورقة العمل الأخيرة “النتيجة”.

#### **الخطوة 2: تحميل Aspose.Cells.Zip**

1. [تحميل Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. قم بفك الضغط عنها في جهاز التطوير الخاص بك.

   جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.

#### **الخطوة 3: إنشاء مشروع**

يمكنك إما إنشاء مشروع باستخدام محرر Java مثل Eclipse أو إنشاء برنامج بسيط باستخدام Notepad.

#### **الخطوة 4: إضافة مسار الفئة**

لتعيين مسار الفئة باستخدام Eclipse، يرجى إتباع الخطوات التالية:

1. استخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
1. ضبط مسار الفئة للمشروع في Eclipse:
1. حدد مشروعك في Eclipse ثم انقر فوق قوائم Project-Properties.
1. حدد “Java Build Path” في الجانب الأيسر من نافذة العرض المنبثق، ثم حدد علامة التبويب “المكتبات”، انقر على “إضافة JARs” أو “إضافة JARs الخارجية” لتحديد Aspose.Cells.jar و dom4j_1.6.1.jar وأضفها إلى مسارات البناء.
1. كتابة التطبيق لاستدعاء واجهات برمجة التطبيقات من مكونات Aspose.

أو يمكنك تعيينه في وقت التشغيل في سطر الأوامر في ويندوز. على سبيل المثال:

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **الخطوة 5: نسخ صورة من ورقة عمل إلى أخرى**

الكود التالي لإنجاز المهمة. يقوم بنسخ صورة من ورقة العمل المسماة "صورة" إلى ورقة العمل "النتيجة".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **النتيجة المهمة 1:**

بعد تنفيذ الكود أعلاه ، تم نسخ الصورة من ورقة العمل "الصورة" الآن إلى آخر ورقة عمل "النتيجة"

**ورقة عمل "النتيجة" بالصورة المنسوخة**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **المهمة 2: نسخ رسم بياني من ورقة عمل إلى أخرى**

#### **الخطوة 1: نسخ رسم بياني من ورقة عمل إلى أخرى**

الكود الفعلي المستخدم من قبل المكون لإنجاز المهمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **النتيجة المهمة 2**

بعد تنفيذ الكود أعلاه ، تم نسخ الرسم البياني من ورقة العمل "الرسم البياني" إلى ورقة العمل "النتيجة". يُرجى الاطلاع على لقطة الشاشة التالية لورقة العمل الناتجة.

**ورقة العمل "النتيجة" بالصورة المُنسوخة والرسم البياني**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **المهمة 3: نسخ الضوابط والرسوم الأخرى من ورقة عمل إلى أخرى**

**ورقة عمل "التحكم" مع مربع نص وشكل بيضوي**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

يرجى الاطلاع على الخطوات البسيطة التالية التي يجب أن تقوم بها للحصول على النتائج المرجوة.

#### **الخطوة 1: نسخ ورقة عمل بين دفتي عمل**

الكود التالي المستخدم من قبل المكون لإنجاز المهمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **النتيجة المهمة 3**

بعد تنفيذ الكود أعلاه ، تم نسخ الضوابط من ورقة العمل "التحكم" الآن إلى ورقة العمل "النتيجة". يُرجى الاطلاع على لقطة الشاشة التالية لورقة العمل "النتيجة".

**ورقة العمل “النتيجة” مع نسخة من مربع النص والشكل البيضاوي**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **الاستنتاج**

لقد أظهر هذا المقال كيفية نسخ أشكال مختلفة مثل الصور والرسوم البيانية وغيرها من الكائنات الرسمية باستخدام Aspose.Cells. نأمل أن يمنحك ذلك بعض الإلهام، وسوف تكون قادرًا على الاستفادة من هذه الخيارات وفقًا لسيناريوهاتك المختلفة.

يمكن لـ Aspose.Cells أن تقدم مرونة أكبر من غيرها من الحلول وتوفر سرعة وكفاءة وموثوقية استثنائية لتلبية متطلبات التطبيقات التجارية الخاصة. إن النتائج تظهر أن Aspose.Cells استفادت من سنوات من البحث والتصميم والضبط الدقيق.

نرحب بتساؤلاتكم وتعليقاتكم واقتراحاتكم من القلب في [منتدى Aspose.Cells](https://forum.aspose.com/c/cells/9).
{{< app/cells/assistant language="java" >}}
