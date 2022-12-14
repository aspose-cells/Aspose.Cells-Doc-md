---
title: التكامل مع JasperServer
type: docs
weight: 30
url: /ar/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

لدمج Aspose.Cells لـ JasperReports مع JasperServer ، قم بتنفيذ الخطوات أدناه.

{{% /alert %}} 

{{% alert color="primary" %}} 

 في جميع الخطوات التالية<InstallDir> لتقف على دليل التثبيت JasperServer.

{{% /alert %}} 

1.  أضف خصائص المُصدِّر الجديدة التالية إلى ملف**<InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF \ Flows \ viewReportBeans.xml** ملف.

**XML**

{{< highlight "csharp" >}}

 <bean id="reportACXlsExporter" class="com.aspose.cells.jasperreports.ACReportXlsExporter" parent="baseReportExporter">

   <property name="exportParameters" ref="excelACExportParameters"/>

   <property name="setResponseContentLength" value="true"/>

</bean>

<bean id="xlsACExporterConfiguration" class="com.jaspersoft.jasperserver.war.action.ExporterConfigurationBean">

   <property name="descriptionKey" value="XLS - Excel Presentation via Aspose.Cells"/>

   <property name="iconSrc" value="/images/xls.gif"/>

   <property name="parameterDialogName" value="excelACExportParams"/>

   <property name="exportParameters" ref="excelACExportParameters"/>

   <property name="currentExporter" ref="reportACXlsExporter"/>

</bean>



{{< /highlight >}}

1.  حدد موقع ملف<util:map id=”exporterConfigMap> عنصر في**<InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF \ Flows \ viewReportBeans.xml** ملف وإضافة الأسطر التالية:

**XML**

{{< highlight "csharp" >}}

 <util:map id="exporterConfigMap">

   <entry key="pdf" value-ref="pdfExporterConfiguration"/>

   <entry key="xls" value-ref="xlsExporterConfiguration"/>

   <entry key="rtf" value-ref="rtfExporterConfiguration"/>

   <entry key="csv" value-ref="csvExporterConfiguration"/>

   <entry key="swf" value-ref="swfExporterConfiguration"/>

<!-- START of ADDED LINES -->

   <entry key="xls" value-ref="xlsACExporterConfiguration"/>

<!-- END of NEW LINES -->

</util:map>



{{< /highlight >}}




1.  انسخ جميع صور GIF من ملف**\ ليب** مجلد في**aspose.cells.jasperreports.zip** الى*<InstallDir> \ apache-tomcat \ webapps \ jasperserver \ images* مجلد.
1.  انسخ ال**aspose.cells.jasperreports.jar** ملف من**\ ليب** مجلد في**aspose.cells.jasperreports.zip** الى**<InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF \ lib \.** مجلد.
1.  أضف الأسطر التالية إلى ملف**<InstallDir> \ apache-tomcat \ webapps \ jasperserver \ WEB-INF \ applicationContext.xml** ملف.
 (قد تحتوي هذه الوحدة على إعدادات تكوين مختلفة تهدف إلى تكوين التصدير. على سبيل المثال ، يمكنك استخدام ميزة تعيين خط JasperReports أو تحديد موقع ملف ترخيص Aspose.Cells لملف ترخيص JasperReports.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1.  قم بتشغيل JasperServer وافتح أي تقرير لعرضه. إذا تم تنفيذ الخطوات السابقة بشكل صحيح ، فستتوفر رموز تنسيق إضافية.

**تتوفر تنسيقات تصدير جديدة (على اليمين) بعد تثبيت Aspose.Cells لـ JasperReports على JasperServer** 

![ما يجب القيام به: image_بديل_نص](integration-with-jasperserver_1.png)



