---
title: تطبيق التنسيق الشرطي في أوراق العمل
type: docs
weight: 40
url: /ar/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

تم تصميم هذه المقالة لتوفير فهم تفصيلي لكيفية إضافة تنسيق شرطي إلى نطاق من الخلايا في ورقة عمل.

التنسيق الشرطي هو ميزة متقدمة في Microsoft Excel تسمح لك بتطبيق التنسيقات على نطاق من الخلايا ، وتغيير التنسيق بناءً على قيمة الخلية أو قيمة الصيغة. على سبيل المثال ، قد تكون خلفية الخلية حمراء لتمييز قيمة سالبة ، أو قد يكون لون النص أخضر لقيمة موجبة. عندما تفي قيمة الخلية بشرط التنسيق ، يتم تطبيق التنسيق. إذا كانت قيمة الخلية لا تفي بشرط التنسيق ، فسيتم استخدام التنسيق الافتراضي للخلية.

من الممكن تطبيق التنسيق الشرطي باستخدام Microsoft Office Automation ولكن هذا له عيوبه. هناك العديد من الأسباب والمشكلات المعنية: على سبيل المثال ، الأمان والاستقرار وقابلية التوسع والسرعة. السبب الرئيسي لإيجاد حل آخر هو أن Microsoft أنفسهم يوصون بشدة ضد أتمتة المكاتب لحلول البرمجيات.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم ، وإضافة تنسيق شرطي على الخلايا مع أبسط أسطر من التعليمات البرمجية باستخدام Aspose.Cells API.

{{% /alert %}}

## **العمل مع التنسيق الشرطي**

تعمل هذه المقالة من خلال المهام التالية:

1. [استخدام Aspose.Cells لتطبيق التنسيق الشرطي على أساس قيمة الخلية](/cells/ar/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [استخدام Aspose.Cells لتطبيق التنسيق الشرطي بناءً على معادلة](/cells/ar/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **المهمة 1: استخدام Aspose.Cells لتطبيق التنسيق الشرطي على أساس قيمة Cell**

1. **قم بتنزيل وتثبيت Aspose.Cells.zip**:
   1. [تحميل](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
 1. قم بفك ضغطه على جهاز الكمبيوتر الخاص بك.
 جميع مكونات Aspose ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.
1. **أنشئ مشروعًا**.
 أنشئ مشروعًا باستخدام محرر Java مثل Eclipse أو أنشئ برنامجًا بسيطًا باستخدام محرر نصوص.
1. **أضف مسار الفصل**.
 لتعيين مسار الفصل باستخدام Eclipse ، يرجى اتباع الخطوات التالية:
1. قم باستخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
 1. قم بتعيين مسار الفصل للمشروع في Eclipse:
 1. حدد مشروعك في Eclipse ثم حدد**الخصائص** من**مشروع** قائمة.
 1. حدد "Java Build Path" على يسار مربع الحوار.
 1. على**مكتبات** علامة التبويب ، حدد**أضف الجرار** أو**إضافة JARs خارجية** لاختيار Aspose.Cells.jar و dom4j_1.6.1.jar وإضافتهم إلى مسارات البناء.
 1. اكتب تطبيقًا لاستدعاء واجهات برمجة التطبيقات لمكونات Aspose.
 أو يمكنك تعيين المسار في وقت التشغيل على موجه DOS في Windows.

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **تطبيق التنسيق الشرطي على أساس قيمة الخلية**.
 يوجد أدناه الرمز الذي يستخدمه المكون لإنجاز المهمة. يتم تطبيق التنسيق الشرطي على الخلية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

عند تنفيذ الكود أعلاه ، يتم تطبيق التنسيق الشرطي على الخلية "A1" في ورقة العمل الأولى من ملف الإخراج (output.xls). يعتمد التنسيق الشرطي المطبق على A1 على قيمة الخلية. إذا كانت قيمة الخلية A1 بين 50 و 100 ، يكون لون الخلفية أحمر بسبب التنسيق الشرطي المطبق. يرجى الاطلاع على لقطات الشاشة التالية لملف XLS الذي تم إنشاؤه.

**إخراج ملف Excel بقيمة A1 أقل من 50**

![ما يجب القيام به: image_بديل_نص](apply-conditional-formatting-in-worksheets_1.png)

**إخراج ملف Excel مع A1 بين 50 و 100**

![ما يجب القيام به: image_بديل_نص](apply-conditional-formatting-in-worksheets_2.png)

### **المهمة 2: استخدام Aspose.Cells لتطبيق الصياغة الشرطية بناءً على صيغة**

1. **تطبيق التنسيق الشرطي حسب الصيغة**.
 يوجد أدناه الكود الفعلي الذي يستخدمه المكون لإنجاز المهمة. يتم تطبيق التنسيق الشرطي على "B3".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

عند تنفيذ الكود أعلاه ، يتم تطبيق التنسيق الشرطي على الخلية "B3" في ورقة العمل الأولى لملف الإخراج (output.xls). يعتمد التنسيق الشرطي المطبق على الصيغة التي تحسب قيمة "B3" كمجموع B1 & B2. يرجى الاطلاع على لقطات الشاشة التالية لملف XLS الذي تم إنشاؤه.

**إخراج ملف Excel بقيمة B3 أقل من 100**

![ما يجب القيام به: image_بديل_نص](apply-conditional-formatting-in-worksheets_3.png)

**إخراج ملف Excel مع B3 أكبر من 100**

![ما يجب القيام به: image_بديل_نص](apply-conditional-formatting-in-worksheets_4.png)

### **استنتاج**

{{% alert color="primary" %}}

توضح هذه المقالة كيفية تطبيق التنسيق الشرطي على الخلايا في ورقة عمل باستخدام API Aspose.Cells. ونأمل أن تعطيك بعض الأفكار حتى تتمكن من استخدام هذه الخيارات في السيناريوهات الخاصة بك.

يوفر Aspose.Cells مرونة كبيرة للحلول ويوفر سرعة وكفاءة وموثوقية فائقة لتلبية متطلبات تطبيقات الأعمال المحددة. يستفيد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق.

 نرحب باستفساراتكم وتعليقاتكم واقتراحاتكم في[Aspose.Cells المنتدى](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
