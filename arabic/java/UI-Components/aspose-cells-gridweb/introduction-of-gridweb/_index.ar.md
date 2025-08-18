---
title: مقدمة في GridWeb
type: docs
weight: 10
url: /ar/java/introduction-of-gridweb/
---
## **أساسيات GridWeb**
Aspose.Cells.GridWeb هو عنصر تحكم ويب قائم على واجهة المستخدم الرسومية يمكن تضمينه في صفحات ويب JSP أو أي صفحة HTML في خادم جافا. 
 

من السهل والبسيط في الاستخدام.

يساعدك في بناء محرر ويب على الإنترنت لملف جدول بيانات بسرعة.

يدعم أيضًا استيراد وتصدير جميع أنواع ملفات جدول البيانات والتي تكون 100% متوافقة مع ملف MS Excel.

## **Aspose.Cells.GridWeb - العروض**
 

للحصول على بدء سريع، نحن نوفر عددًا من أمثلة الشفرة والعروض التوضيحية التي تظهر كيفية استخدام واجهة برمجة تطبيقات Aspose.Cells.GridWeb.

يرجى تنزيل العروض من الرابط أدناه:
[عروض Aspose.Cells.GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **كيفية تشغيل أمثلة Aspose.Cells لـ GridWeb Java**
{{% alert color="primary" %}}  

أمثلة Aspose.Cells لـ GridWeb Java من السهل تشغيلها. كل ما عليك فعله هو نشر **gridwebdemo.war** في خادم الويب الخاص بك. يرجى تنزيل العروض من هذا [الرابط](https://forum.aspose.com/uploads/discourse_instance3/22292).

يوضح هذا المقال كيفية تشغيل أمثلة Aspose.Cells لـ GridWeb Java في خادم Apache Tomcat.

{{% /alert %}} 
### **دليل خطوة بخطوة لتشغيل أمثلة GridWeb Java**
1. استخراج **apache-tomcat-7.0.52.zip** في أي دليل على سبيل المثال C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



تظهر الصورة الفوتوغرافية التالية الدلائل والملفات المستخرجة من خادم Apache Tomcat 

![todo:image_alt_text](introduction-of-gridweb_2.png)



قد تحتاج أيضًا إلى تعيين المتغير المحيطي **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

١. افتح ملف **tomcat-users.xml**. 

![todo:image_alt_text](introduction-of-gridweb_4.png)

١. أضف هذا المستخدم:

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**هنا اسم المستخدم هو tomcat وكلمة المرور هي secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

١. قم بتشغيل ملف **startup.bat**.
   سيتم تشغيل خادم Apache Tomcat. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



يتم تشغيل خادم Tomcat في نافذة الأوامر 

![todo:image_alt_text](introduction-of-gridweb_7.png)

١. الآن افتح المتصفح واكتب **localhost:8080**.
   يتم عرض صفحة الويب Apache Tomcat. 

   **صفحة الويب Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. انقر على **Manager App** واكتب اسم المستخدم وكلمة المرور. (كما في الأعلى: tomcat، secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. انتقل إلى الجزء **ملف WAR لنشره** وتصفح ملف **gridwebdemo.war**.
1. انقر على **نشر**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. تصفح ملف **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. انقر على **نشر**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. بمجرد نشره، انقر على **/gridwebdemo** وابدأ تشغيل العروض التوضيحية. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


تتم عرض صفحة عروض توضيحية GridWeb. 

**تتم عرض صفحة عروض توضيحية GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. انقر فوق أي عرض توضيحي وشغله. 

   **تشغيل عرض توضيحي لإنشاء المحتويات** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**تشغيل عرض توضيحي لأوراق العمل** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**تشغيل عرض توضيحي لـ HeaderBar و CommandButton** 

![todo:image_alt_text](introduction-of-gridweb_17.png)



## **ميزات قدرات المتصفحات و Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb هو عنصر تحكم ويب قائم على واجهة المستخدم الرسومية يمكن تضمينه في صفحات JSP ويب مثل عناصر التحكم الويب الأخرى. الشيء الأهم حول عنصر التحكم الويب هو توفير الدعم العرضي المتصفحات المتقاطعة. يوفر Aspose.Cells.GridWeb الدعم العرضي المتصفحات المتقاطعة.
### **مقارنة**
Aspose.Cells.GridWeb مدعوم تمامًا على Internet Explorer (IE) الخاص بمايكروسوفت. ومع ذلك، على المتصفحات الأخرى، يوجد قيود طفيفة. يوفر هذا الموضوع مقارنة مفصلة لما إذا كانت الميزات مدعمة من قبل المتصفحات المختلفة.

|**ميزات الجانب العميل**|**متصفح Internet Explorer الخاص بمايكروسوفت**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|قائمة سياق الخلية|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|التحقق العميلي|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|حدث النقر المزدوج|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|قائمة منسدلة ( *وضع القائمة المنسدلة* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|قائمة منسدلة ( *وضع القائمة المنبثقة* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدخال/تحرير الصيغة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تجميد أو إلغاء تجميد الصفوف/الأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|الارتباطات التشعبية ( *وضع أمر الخلية* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|الارتباطات التشعبية ( *وضع عنوان URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|دمج أو إلغاء دمج الخلايا|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|نسخ/لصق الخلايا متعددة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدخال/تحرير الخلايا متعددة، إرسال مرة أخرى واحدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تنسيق الأرقام|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تقسيم الصفحات|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|الخلايا للقراءة فقط|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|الصفوف/الأعمدة للقراءة فقط|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|التحقق من البيانات باستخدام التعبيرات العادية|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير عرض العمود|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير ارتفاع الصف|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدخال/حذف الصفوف والأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تمرير المحتوى|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تمرير علامات التبويب للورقة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تعيين حدود الخلايا|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تعيين إعدادات الخط للخلايا|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
