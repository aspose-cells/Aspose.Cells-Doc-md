---
title: تطبيق التنسيق الشرطي في الأوراق العمل
type: docs
weight: 40
url: /ar/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

يهدف هذا المقال إلى توفير فهم مفصل حول كيفية إضافة التنسيق الشرطي إلى مجموعة من الخلايا في ورقة عمل.

التنسيق الشرطي هو ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق التنسيقات على مجموعة من الخلايا وأن يتغير ذلك التنسيق اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكن أن تكون خلفية الخلية حمراء لتسليط الضوء على قيمة سالبة، أو يمكن أن لون النص يكون أخضرًا لقيمة موجبة. عندما تفي قيمة الخلية بشرط التنسيق، يتم تطبيق التنسيق. إذا لم تف بقيمة الخلية شرط التنسيق، يتم استخدام التنسيق الافتراضي للخلية.

من الممكن تطبيق التنسيق الشرطي بواسطة Office Automation، ولكن ذلك يأتي مع عيوبه. هناك أسباب وقضايا عديدة متضمنة: مثلاً، الأمان، الاستقرار، التوسع السريع والسرعة. السبب الرئيسي للبحث عن حل آخر هو أن Microsoft نفسها تنص بشدة على عدم استخدام Office Automation لحلول البرنامج.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة التحكم، وإضافة التنسيق الشرطي للخلايا ببضعة أسطر بسيطة باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

## **العمل مع التنسيق الشرطي**

يعمل هذا المقال على إنجاز المهام التالية:

1. [استخدام Aspose.Cells لتطبيق التنسيق الشرطي استنادًا إلى قيمة الخلية](/cells/ar/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [استخدام Aspose.Cells لتطبيق التنسيق الشرطي استنادًا إلى صيغة](/cells/ar/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **المهمة 1: استخدام Aspose.Cells لتطبيق التنسيق الشرطي استناداً إلى قيمة الخلية**

1. **تنزيل وتثبيت Aspose.Cells.zip**: 
   1. [تحميل](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. قم بفك الضغط عنها في جهاز التطوير الخاص بك.
      جميع مكونات Aspose، عند تثبيتها، تعمل في وضع التقييم. ويتوفر وضع التقييم بدون حد زمني ويضيف فقط علامات مائية إلى المستندات المنتجة.
1. **إنشاء مشروع**.
   إما إنشاء مشروع باستخدام محرر Java مثل Eclipse أو إنشاء برنامج بسيط باستخدام محرر نصوص.
1. **إضافة مسار الصف الخاص**.
   لتعيين مسار الفئة باستخدام Eclipse، يرجى إتباع الخطوات التالية:
   1. استخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
   1. ضبط مسار الفئة للمشروع في Eclipse:
      1. حدد مشروعك في Eclipse ثم حدد **الخصائص** من قائمة **المشروع**.
      1. حدد "Java Build Path" على اليمين من الصندوق.
      1. على علامة التبويب **المكتبات**، حدد **إضافة JARs** أو **إضافة JARs الخارجية** لتحديد Aspose.Cells.jar و dom4j_1.6.1.jar وإضافتها إلى مسارات البناء.
   1. كتابة التطبيق لاستدعاء واجهات برمجة التطبيقات من مكونات Aspose.
      أو يمكنك تعيين المسار عند التشغيل في موجه DOS في نظام التشغيل Windows.

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **تطبيق التنسيق الشرطي استنادًا إلى قيمة الخلية**.
   أدناه هو الكود المستخدم من قبل المكون لإنجاز المهمة. يطبق التنسيق الشرطي على خلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

عند تنفيذ الكود أعلاه، يتم تطبيق التنسيق الشرطي على الخلية "A1" في ورقة العمل الأولى للملف الناتج (output.xls). التنسيق الشرطي المطبق على A1 يعتمد على قيمة الخلية. إذا كانت قيمة الخلية في A1 بين 50 و 100 فإن لون الخلفية يكون أحمرًا بسبب التنسيق الشرطي المطبق. يرجى الرجوع إلى لقطات الشاشة التالية للملف XLS الناتج.

**ملف Excel الناتج بقيمة A1 أقل من 50**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**ملف Excel الناتج بقيمة A1 بين 50 و 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **المهمة 2: استخدام Aspose.Cells لتطبيق التنسيق الشرطي استنادًا إلى صيغة**

1. **تطبيق التنسيق الشرطي اعتمادًا على الصيغة**.
   أدناه هو الكود الفعلي المستخدم من قبل المكون لإنجاز المهمة. يطبق التنسيق الشرطي على "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

عند تنفيذ الكود أعلاه، يتم تطبيق التنسيق الشرطي على الخلية "B3" في الورقة الأولى للملف الناتج (output.xls). يعتمد التنسيق الشرطي المطبق على الصيغة التي تحسب قيمة "B3" كمجموع B1 و B2. الرجاء الرجوع إلى لقطات الشاشة التالية للملف XLS الناتج بقيمة B3 أقل من 100.

**ملف Excel الناتج مع قيمة B3 أقل من 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**ملف إكسل الناتج مع B3 أكبر من 100**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **الاستنتاج**

{{% alert color="primary" %}}

يوضح هذا المقال كيفية تطبيق التنسيق الشرطي على الخلايا في ورقة العمل باستخدام واجهة برمجة التطبيقات Aspose.Cells. على أمل أن يوفر لك بعض الرؤى بحيث يمكنك استخدام هذه الخيارات في سيناريوهاتك الخاصة.

تقدم Aspose.Cells مرونة كبيرة للحلول وتوفر سرعة وكفاءة وموثوقية متميزة لتلبية متطلبات تطبيقات الأعمال الخاصة. تستفيد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق.

نرحب باستفساراتكم وتعليقاتكم واقتراحاتكم في [منتديات Aspose.Cells](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
