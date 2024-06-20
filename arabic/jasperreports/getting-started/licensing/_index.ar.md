---
title: ترخيص
type: docs
weight: 40
url: /ar/jasperreports/licensing/
---

{{% alert color="primary" %}}

يتوفر Aspose.Cells for JasperReports بشكل مجاني كنسخة تقييمية غير محددة المدة من [صفحة التنزيل](https://downloads.aspose.com/cells/jasperreports). الإصدارات التقييمية والمرخصة للمنتج هي نفس التنزيل.

عندما تكون راضيًا عن الإصدار التجريبي، يمكنك [شراء ترخيص](https://purchase.aspose.com/). تأكد من فهم والموافقة على شروط الترخيص.

تتوفر الترخيص للتنزيل من صفحة الطلب بعد دفع الطلب. يعد الترخيص ملف XML موقع نصي وقع رقميًا. يحتوي الترخيص على معلومات مثل اسم العميل والمنتج المشترى ونوع الترخيص. لا تقم بتعديل محتوى ملف الترخيص: فعل ذلك يبطل الترخيص.

هناك طريقتان لتطبيق ترخيص:

- [اتصل ب setLicense](/cells/ar/jasperreports/licensing/#call-setlicense)
- [قم بتعيين معلمة مصدر في applicationContext.xml](/cells/ar/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

بعد تثبيت الترخيص،

- [تحقق مما إذا كان يعمل](/cells/ar/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **اتصل ب setLicense**

{{% alert color="primary" %}}

هذه الطريقة قابلة للاستخدام مع JasperReports.

{{% /alert %}}

قم بتنزيل الترخيص إلى جهاز الكمبيوتر الخاص بك وانسخه إلى المجلد المناسب (على سبيل المثال، مجلد التطبيق الخاص بك أو **JasperReports\lib**).
أضف الكود التالي إلى مشروعك:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **قم بتعيين معلمة تصدير licenseFile في applicationContext.xml**

{{% alert color="primary" %}}

هذه الطريقة قابلة للاستخدام مع JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **تحقق من عمل الترخيص**

قم بتصدير أي تقرير إلى تنسيق XLS وتحقق مما إذا كان يحتوي التقرير على رسالة تقييم. إذا لم تكن هناك رسالة تقييم، فإن الترخيص يعمل بشكل صحيح.

**يقوم Aspose.Cells for JasperReports بحقن ورقة عمل تقييم بوضع التقييم** 

![todo:image_alt_text](licensing_1.png)

**عندما يكون هناك ترخيص صالح لا توجد ورقة عمل تقييم** 

![todo:image_alt_text](licensing_2.png)
