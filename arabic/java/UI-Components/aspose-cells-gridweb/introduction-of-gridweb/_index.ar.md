---
title: مقدمة عن GridWeb
type: docs
weight: 10
url: /ar/java/introduction-of-gridweb/
---
##  **أساسيات الشبكة العنكبوتية**
 Aspose.Cells.GridWeb عبارة عن عنصر تحكم ويب يعتمد على واجهة المستخدم الرسومية ويمكن تضمينه في صفحات ويب JSP أو أي صفحة html في خادم جافا.
{{% alert color="primary" %}} 

إنه سهل وبسيط الاستخدام.

يساعدك على إنشاء محرر ويب عبر الإنترنت لملف جدول البيانات بسرعة.

كما أنه يدعم استيراد وتصدير جميع أنواع ملفات تنسيق جداول البيانات المتوافقة بنسبة 100% مع ملف MS excel.

##  **Aspose.Cells.GridWeb - العروض التوضيحية**
{{% alert color="primary" %}} 

لتنشيطك وتشغيلك بسرعة، نقدم عددًا من أمثلة التعليمات البرمجية والعروض التوضيحية التي توضح كيفية استخدام Aspose.Cells.GridWeb API.

يرجى تنزيل العروض التوضيحية من الرابط أدناه:
[Aspose.Cells. عروض GridWeb](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **كيفية تشغيل Aspose.Cells لـ GridWeb Java العروض التوضيحية**
{{% alert color="primary" %}} 

 من السهل تشغيل العروض التوضيحية Aspose.Cells لـ GridWeb Java. تحتاج فقط إلى النشر**Gridwebdemo.war** في خادم الويب الخاص بك. يرجى تنزيل العروض التوضيحية من هذا[وصلة](https://forum.aspose.com/uploads/discourse_instance3/22292).

توضح هذه المقالة كيفية تشغيل Aspose.Cells للعروض التوضيحية لـ GridWeb Java في خادم Apache Tomcat.

{{% /alert %}} 
###  **دليل خطوة بخطوة لتشغيل GridWeb Java العروض التوضيحية**
1.  يستخرج**أباتشي-تومكات-7.0.52.zip** في أي دليل على سبيل المثال C:\Tomcat

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_1.png)



 تُظهر اللقطة التالية الدلائل والملفات المستخرجة لخادم Apache Tomcat

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_2.png)



 قد تحتاج أيضًا إلى تعيين متغير البيئة**CATALINA_HOME** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_3.png)

1.  افتح ال**Tomcat-users.xml** ملف.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_4.png)

1. أضف هذا المستخدم:

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**هنا اسم المستخدم هو Tomcat وكلمة المرور سرية** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_5.png)

1.  تشغيل**start.bat** ملف.
 سيتم تشغيل خادم Apache Tomcat.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_6.png)



**خادم Tomcat يعمل في نافذة الأوامر** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_7.png)

1. الآن افتح المتصفح واكتب *localhost:8080**.
 يتم عرض صفحة ويب Apache Tomcat.

   **صفحة الويب Apache Tomcat** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_8.png)

1.  انقر**تطبيق مدير** واكتب اسم المستخدم وكلمة المرور. (كما هو مذكور أعلاه: القط، سر)

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_9.png)

1.  قم بالتمرير لأسفل إلى القسم**ملف WAR للنشر** وتصفح**Gridwebdemo.war** ملف.
1.  انقر على *نشر**.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_10.png)

1. تصفح**Gridwebdemo.war** ملف.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_11.png)

1.  انقر على *نشر**.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_12.png)

1.  بمجرد نشره، انقر فوق**/gridwebdemo** وابدأ في تشغيل العروض التوضيحية.

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_13.png)


 يتم عرض صفحة العرض التجريبي لـ GridWeb.

**صفحة العرض التجريبي لـ GridWeb** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_14.png)

1.  انقر فوق أي عرض توضيحي وتشغيله.

   **إنشاء عرض توضيحي للمحتويات قيد التشغيل** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_15.png)



**جاري تشغيل العرض التوضيحي لأوراق العمل** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_16.png)



**يتم تشغيل العرض التوضيحي لـ HeaderBar وCommandButton** 

![ما يجب القيام به:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **قدرات المتصفحات وAspose.Cells.GridWeb**
Aspose.Cells.GridWeb عبارة عن عنصر تحكم ويب يعتمد على واجهة المستخدم الرسومية ويمكن تضمينه في صفحات ويب JSP مثل عناصر تحكم الويب الأخرى. أهم شيء في التحكم في الويب هو توفير الدعم عبر المستعرضات. Aspose.Cells.GridWeb يوفر الدعم عبر المستعرضات.
###  **مقارنة**
Aspose.Cells.GridWeb مدعوم بالكامل على Microsoft Internet Explorer (IE). ومع ذلك، في المتصفحات الأخرى، هناك قيود بسيطة. يوفر هذا الموضوع مقارنة تفصيلية للميزات التي تدعمها المتصفحات المختلفة.

|**ميزات جانب العميل**|**Microsoft انترنت اكسبلورر**|**Google كروم**|**موزيلا فايرفوكس**|**الأوبرا**|
| :- | :- | :- | :- | :- |
|قائمة السياق Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|التحقق من جانب العميل|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|حدث النقر المزدوج|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| قائمة منسدلة (*وضع التحرير والسرد* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| قائمة منسدلة (*وضع القائمة المنبثقة* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدخال/تحرير الصيغة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تجميد أو إلغاء تجميد الصفوف/الأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| الارتباطات التشعبية (*وضع قيادة الخلية* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| الارتباطات التشعبية (*وضع URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|دمج أو إلغاء دمج Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|متعددة Cells نسخ / لصق|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|متعددة Cells الإدخال/التحرير، إعادة النشر واحدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تنسيق الرقم|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ترحيل الصفحات|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|للقراءة فقط Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|الصفوف/الأعمدة للقراءة فقط|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|التحقق من صحة البيانات باستخدام التعبيرات العادية|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير حجم عرض العمود|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تغيير حجم ارتفاع الصف|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|إدراج/حذف الصفوف والأعمدة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|قم بتمرير المحتوى|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تمرير علامات تبويب الورقة|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|تعيين حدود Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|ضبط إعدادات الخط على Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} لا يمكن تنشيط قائمة السياق الخاصة بالخلية إلا عن طريق النقر فوق زر القائمة من جانب العميل.
