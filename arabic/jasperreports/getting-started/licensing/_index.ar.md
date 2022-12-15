---
title: الترخيص
type: docs
weight: 40
url: /ar/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports متاح كتقييم مجاني غير محدود للوقت من[صفحة التحميل](https://downloads.aspose.com/cells/jasperreports). التقييم والإصدارات المرخصة للمنتج هي نفس التنزيل.

 عندما تكون سعيدًا بإصدار التقييم ، يمكنك ذلك[شراء رخصة](https://purchase.aspose.com/). تأكد من أنك تفهم وتوافق على شروط الترخيص.

الترخيص متاح للتنزيل من صفحة الطلب عند دفع الطلب. الترخيص عبارة عن ملف XML نصي واضح وموقع رقميًا. يحتوي الترخيص على معلومات مثل اسم العميل والمنتج الذي تم شراؤه ونوع الترخيص. لا تقم بتعديل محتوى ملف الترخيص: القيام بذلك يبطل الترخيص.

هناك طريقتان لتطبيق الترخيص:

- [ترخيص مجموعة الاتصال](/cells/ar/jasperreports/licensing/#call-setlicense)
- [قم بتعيين معامل المصدر في applicationContext.xml](/cells/ar/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

بعد تثبيت الترخيص ،

- [تحقق من أنه يعمل](/cells/ar/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **ترخيص مجموعة الاتصال**

{{% alert color="primary" %}}

هذه الطريقة قابلة للتطبيق للاستخدام مع JasperReports.

{{% /alert %}}

 قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك وانسخه إلى المجلد المناسب (على سبيل المثال مجلد التطبيق الخاص بك أو**جاسبر ريبورتس \ ليب**).
أضف الكود التالي إلى مشروعك:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **قم بتعيين معلمة مصدر الترخيص في applicationContext.xml**

{{% alert color="primary" %}}

هذه الطريقة قابلة للتطبيق للاستخدام مع JasperServer.

{{% /alert %}}

1.  قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك وانسخه إلى ملف**\ <InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF**المجلد ، حيث**\ <InstallDir>** لتقف على دليل التثبيت JasperServer.
1.  حدد موقع ملف**\ <InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF \ applicationContext.xml** ملف وإضافة الأسطر التالية:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **تحقق من عمل الترخيص**

قم بتصدير أي تقرير إلى تنسيق XLS وتحقق مما إذا كان التقرير يحتوي على رسالة تقييم. إذا لم تكن هناك رسالة تقييم ، فهذا يعني أن الترخيص يعمل بشكل صحيح.

**Aspose.Cells for JasperReports يضخ ورقة عمل التقييم في وضع التقييم** 

![ما يجب القيام به: image_بديل_نص](licensing_1.png)

**عندما يكون الترخيص ساري المفعول لا توجد ورقة عمل للتقييم** 

![ما يجب القيام به: image_بديل_نص](licensing_2.png)
