---
title: تنزيل وتهيئة Aspose.Cells في PHP
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-cells-in-php/
---
## **تحميل المكتبات المطلوبة**
تحميل المكتبات المطلوبة المذكورة أدناه. هذه هي المطلوبة لتنفيذ Aspose.Cells Java for PHP أمثلة.

- **Aspose:** [Aspose.Cells for Java مكون](https://downloads.aspose.com/cells/java/)
- [جسر PHP / Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **تنزيل أمثلة من مواقع الترميز الاجتماعي**
الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل على مواقع الترميز الاجتماعي المذكورة أدناه:

-----
### **جيثب**
- **Aspose.Cells Java for PHP أمثلة** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **كيفية تكوين الكود المصدري على منصة Linux**
يرجى اتباع هذه الخطوات البسيطة لفتح كود المصدر وتوسيعه أثناء استخدام:
## **1. قم بتثبيت خادم Tomcat**
 لتثبيت خادم tomcat ، قم بإصدار الأمر التالي على وحدة تحكم Linux. سيؤدي هذا إلى تثبيت خادم tomcat بنجاح.

{{< highlight "actionscript3" >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. قم بتنزيل وتهيئة PHP / JavaBridge**
 لتنزيل ثنائيات PHP / JavaBridge ، قم بإصدار الأمر التالي على وحدة تحكم linux.

{{< highlight "actionscript3" >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


قم بفك ضغط ثنائيات PHP / JavaBridge بإصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight "actionscript3" >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


هذا سوف يستخرج**JavaBridge.war**ملف. انسخه إلى tomcat88**تطبيقات الويب** المجلد بإصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight "actionscript3" >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


عن طريق النسخ ، سيقوم tomcat8 بإنشاء مجلد جديد تلقائيًا "**جافا بريدج**" في**تطبيقات الويب**. بمجرد إنشاء المجلد ، تأكد من تشغيل tomcat8 ثم تحقق<http://localhost:8080/JavaBridge> في المتصفح ، يجب أن يفتح صفحة افتراضية من JavaBridge.

 إذا ظهرت أي رسالة خطأ ، فقم بالتثبيت**FastCGI**بإصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight "actionscript3" >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

بعد تثبيت php5.5 cgi ، أعد تشغيل خادم tomcat8 وتحقق من<http://localhost:8080/JavaBridge>مرة أخرى في المتصفح.

إذا**JAVA_HOME**يتم عرض خطأ ، ثم افتح ملف / etc / default / tomcat8 وأزل التعليق عن السطر الذي يحدد JAVA_HOME. تحقق من <http: // localhost: 8080 / JavaBridge> في المستعرض مرة أخرى ، يجب أن يأتي مصحوبًا بصفحة أمثلة PHP / JavaBridge.
## **3. قم بتكوين Aspose.Cells Java for PHP أمثلة**
 استنساخ ، أمثلة PHP عن طريق إصدار الأوامر التالية داخل مجلد webapps / JavaBridge.

{{< highlight "actionscript3" >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP]{{< /highlight >}}

## **كيفية تكوين كود المصدر على النظام الأساسي Windows**
برجاء اتباع الخطوات البسيطة التالية لتهيئة PHP / Java Bridge على النظام الأساسي Windows

\ 1. قم بتثبيت PHP5 وتكوينه كما تفعل عادةً
\ 2. قم بتثبيت JRE 6 (Java Runtime Environment) إذا لم يكن لديك بالفعل. يمكنك التحقق من ذلك في C: \ Program Files وما إلى ذلك. يمكنك تنزيله من هنا. أنا أستخدم JRE 6 لأنه متوافق مع PHP Java Bridge (PJB).

\ 3. قم بتثبيت Apache Tomcat 8.0. يمكنك تحميله من هنا

 4. تحميل[JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). انسخ هذا الملف إلى دليل تطبيقات الويب tomcat.
(على سبيل المثال: C: \ Program Files \ Apache Software Foundation \ Tomcat 8.0 \ webapps)

\ 5. أعد تشغيل خدمة اباتشي القط.

 6- اذهب إلى<http://localhost:8080/JavaBridge/test.php> للتحقق مما إذا كان php يعمل. يمكنك أن تجد أمثلة أخرى هناك

7. انسخ ملف جرة Aspose.Cells Java إلى C: \ Program Files \ Apache Software Foundation \ Tomcat 8.0 \ webapps \ JavaBridge \ WEB-INF \ lib

 \ 8. استنساخ[Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) أمثلة داخل المجلد C: \ Program Files \ Apache Software Foundation \ Tomcat 8.0 \ webapps \ folder.

\ 8. انسخ المجلد C: \ Program Files \ Apache Software Foundation \ Tomcat 8.0 \ webapps \ JavaBridge \ java إلى مجلد الأمثلة Aspose.Cells Java for PHP.

 \ 10. أعد تشغيل خدمة apache tomcat وابدأ في استخدام الأمثلة.
