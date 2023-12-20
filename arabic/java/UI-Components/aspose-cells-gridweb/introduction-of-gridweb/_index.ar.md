---
title: مقدمة من GridWeb
type: docs
weight: 10
url: /ar/java/introduction-of-gridweb/
---
## **كيفية تشغيل Aspose.Cells لـ GridWeb Java Demos**
{{% alert color="primary" %}} 

 Aspose.Cells لـ GridWeb Java العروض التوضيحية سهلة التشغيل. تحتاج فقط إلى النشر**Gridwebdemo.war** في خادم الويب الخاص بك. الرجاء تحميل العروض من هذا[حلقة الوصل](https://forum.aspose.com/uploads/discourse_instance3/22292).

توضح هذه المقالة كيفية تشغيل Aspose.Cells لـ GridWeb Java Demos في Apache Tomcat Server.

{{% /alert %}} 
### **دليل خطوة بخطوة لتشغيل GridWeb Java Demos**
1.  استخراج**اباتشي تومكات-7.0.52.zip** في أي دليل مثل C: \ Tomcat

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_1.png)



 تُظهر اللقطة التالية الأدلة والملفات المستخرجة لخادم Apache Tomcat

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_2.png)



 قد تحتاج أيضًا إلى تعيين متغير البيئة**CATALINA_HOME** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_3.png)

1. افتح ال**tomcat-users.xml** ملف.

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_4.png)

1. أضف هذا المستخدم:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**هنا اسم المستخدم هو القط وكلمة المرور سرية** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_5.png)

1.  قم بتشغيل**startup.bat** ملف.
 سيتم تشغيل خادم Apache Tomcat.

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_6.png)



**خادم Tomcat يعمل في نافذة الأوامر** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_7.png)

1.  الآن افتح المتصفح واكتب**المضيف المحلي: 8080**.
 يتم عرض صفحة ويب Apache Tomcat.

   **صفحة ويب Apache Tomcat** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_8.png)

1.  انقر**تطبيق المدير** واكتب اسم المستخدم وكلمة المرور. (على النحو الوارد أعلاه: القط ، سر)

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_9.png)

1.  انتقل لأسفل إلى القسم**ملف WAR للنشر** وتصفح ملفات**Gridwebdemo.war** ملف.
1.  انقر**نشر**. 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_10.png)

1.  تصفح**Gridwebdemo.war** ملف.

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_11.png)

1.  انقر**نشر**. 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_12.png)

1.  بمجرد نشره ، انقر فوق**gridwebdemo** وابدأ في تشغيل العروض التوضيحية.

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_13.png)


 يتم عرض صفحة GridWeb Demo.

**صفحة GridWeb التجريبي** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_14.png)

1.  انقر فوق أي عرض وتشغيله.

   **إنشاء عرض المحتويات قيد التشغيل** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_15.png)



**عرض أوراق العمل قيد التشغيل** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_16.png)



**يتم تشغيل العرض التوضيحي لـ HeaderBar و CommandButton** 

![ما يجب القيام به: image_بديل_نص](introduction-of-gridweb_17.png)
## **Aspose.Cells.GridWeb - عروض توضيحية**
{{% alert color="primary" %}} 

لتنشيطك وتشغيله بسرعة ، نقدم عددًا من أمثلة التعليمات البرمجية والعروض التوضيحية التي توضح كيفية استخدام Aspose.Cells.GridWeb API.

يرجى تنزيل العروض التوضيحية من الرابط أدناه:
[Aspose.Cells.GridWeb العروض التوضيحية](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)

{{% /alert %}} 
## **إمكانيات المتصفحات و Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb هو عنصر تحكم ويب قائم على واجهة المستخدم الرسومية ويمكن تضمينه في صفحات ويب JSP مثل عناصر تحكم الويب الأخرى. أهم شيء في التحكم في الويب هو توفير دعم عبر المتصفحات. Aspose.Cells.GridWeb يوفر الدعم عبر المستعرضات.
### **مقارنة**
Aspose.Cells.GridWeb مدعوم بالكامل على Internet Explorer (IE) الخاص بـ Microsoft. ومع ذلك ، في المتصفحات الأخرى ، لديها قيود طفيفة. يوفر هذا الموضوع مقارنة تفصيلية للميزات التي تدعمها المستعرضات المختلفة.

|**ميزات جانب العميل**|**Microsoft إنترنت إكسبلورر**|**Google كروم**|**موزيلا فايرفوكس**|**أوبرا**|
|:- |:- |:- |:- |:- |
|قائمة السياق Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|التحقق من جانب العميل|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|انقر نقرا مزدوجا فوق حدث|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| قائمة منسدلة (*وضع ComboBox* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| قائمة منسدلة (*وضع القائمة المنبثقة* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدخال / تحرير الصيغة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تجميد أو إلغاء تجميد الصفوف / الأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| الارتباطات التشعبية (*وضع CellCommand* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| الارتباطات التشعبية (*وضع URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|دمج أو إلغاء الدمج Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|متعددة Cells نسخ / لصق|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Cells إدخال / تحرير متعدد ، إعادة إحالة واحدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تنسيق الأرقام|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ورقة الترحيل|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|للقراءة فقط Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|صفوف / أعمدة للقراءة فقط|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|التحقق من صحة البيانات باستخدام التعبيرات العادية|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير حجم عرض العمود|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير حجم ارتفاع الصف|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدراج / حذف صفوف وأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|محتوى التمرير|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|علامات تبويب ورقة التمرير|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ضع حدود Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تعيين إعدادات الخط Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} لا يمكن تنشيط قائمة السياق للخلية إلا بالنقر فوق زر القائمة الجانبية للعميل.
