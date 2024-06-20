---
title: تنزيل وتكوين Aspose.Cells في PHP
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-cells-in-php/
---

## **تحميل المكتبات المطلوبة**
قم بتحميل المكتبات المطلوبة المذكورة أدناه. هذه المكتبات مطلوبة لتنفيذ أمثلة Aspose.Cells Java لـ PHP.

- **أسبوز:** [Aspose.Cells for Java مكون](https://downloads.aspose.com/cells/java/)
- [جسر PHP/Java](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip/download/)
## **تحميل الأمثلة من مواقع الترميز الاجتماعي**
الإصدارات التالية لأمثلة تشغيل متوفرة للتنزيل على المواقع التالية المذكورة أدناه:

-----
### **GitHub**
- **أمثلة Aspose.Cells Java لـ PHP** 
  - [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP)
## **كيفية تكوين رمز المصدر على منصة Linux**
يرجى اتباع هذه الخطوات البسيطة لفتح وتوسيع الكود المصدري أثناء الاستخدام:
## **1. تثبيت خادم Tomcat**
لتثبيت خادم tomcat، قم بإصدار الأمر التالي في وحدة التحكم في Linux. سيقوم هذا بتثبيت خادم tomcat بنجاح. 

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}
## **2. تنزيل وتكوين PHP/JavaBridge**
من أجل تنزيل برامج PHP/JavaBridge الثنائية، قم بإصدار الأمر التالي في وحدة التحكم في Linux. 

{{< highlight actionscript3 >}}

  wget https://iweb.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


فك ضغط برامج PHP/JavaBridge الثنائية بإصدار الأمر التالي في وحدة التحكم في Linux. 

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip 

{{< /highlight >}}


سيتم استخراج ملف JavaBridge.war. انسخه إلى مجلد webapps tomcat88 بإصدار الأمر التالي في وحدة التحكم في نظام Linux. 

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war 

{{< /highlight >}}


By copying, tomcat8 will automatically create a new folder "**JavaBridge**" in **webapps**. Once the folder is created, make sure your tomcat8 is running and then check <http://localhost:8080/JavaBridge> in browser, it should open a default page of JavaBridge. 

إذا ظهر أي رسالة خطأ، ثم قم بتثبيت FastCGI من خلال إصدار الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi 

{{< /highlight >}}

After installing php5.5 cgi, restart tomcat8 server and check <http://localhost:8080/JavaBridge> again in the browser.

If **JAVA_HOME** error is displayed, then open /etc/default/tomcat8 file and uncomment the line that sets the JAVA_HOME. Check <http://localhost:8080/JavaBridge> in browser again, it should come with PHP/JavaBridge Examples page. 
## **3. تكوين Aspose.Cells Java لأمثلة PHP**
استنسخ أمثلة PHP من خلال إصدار الأوامر التالية داخل مجلد webapps/JavaBridge.  

{{< highlight actionscript3 >}}

 $ git init&nbsp;

$ git clone [https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP] 

{{< /highlight >}}

## **كيفية تكوين كود المصدر على منصة Windows**
يرجى اتباع الخطوات البسيطة أدناه لتكوين جسر PHP/Java على نظام Windows

\1. قم بتثبيت PHP5 وتكوينه كما تفعل عادة
\2. قم بتثبيت JRE 6 (Java Runtime Environment) إذا لم يكن لديك بالفعل. يمكنك التحقق من ذلك في C:\Program Files الخ. يمكنك تنزيله من هنا. أنا استخدم JRE 6 لأنه متوافق مع جسر PHP Java (PJB).

\3. قم بتثبيت Apache Tomcat 8.0. يمكنك تنزيله من هنا

4. قم بتنزيل [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). انسخ هذا الملف إلى مجلد webapps tomcat.
(مثال: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

\5. أعد تشغيل خدمة tomcat apache.

6.Go to <http://localhost:8080/JavaBridge/test.php> to check if php works. You can find other examples in there

7.انسخ ملف JAR الخاص بـ Aspose.Cells Java الخاص بك إلى C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

\8. استنسخ [Aspose.Cells Java for PHP](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_PHP) أمثلة داخل مجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\

\8. انسخ مجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java إلى مجلد الأمثلة PHP الخاص بك لـ Aspose.Cells Java for PHP.

\10. أعد تشغيل خدمة apache tomcat وابدأ في استخدام الأمثلة. 
