---
title: JasperServer ile entegrasyon
type: docs
weight: 30
url: /tr/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Aspose.Cells for JasperReports'i JasperServer ile entegre etmek için aşağıdaki adımları uygulayın.

{{% /alert %}} 

{{% alert color="primary" %}} 

 Aşağıdaki adımların hepsinde<InstallDir> JasperServer kurulum dizini anlamına gelir.

{{% /alert %}} 

1. Aşağıdaki yeni dışa aktarıcı özelliklerini şuraya ekleyin:**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** dosya.

**xml**

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

1.  bulun<util:map id=”exporterConfigMap> içindeki eleman**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** dosyasını açın ve aşağıdaki satırları ekleyin:

**xml**

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




1.  Tüm GIF resimlerini kopyalayın.**\ lib** içindeki klasör**aspose.cells.jasperreports.zip** için*<InstallDir>\apache-tomcat\webapps\jasperserver\images* dosya.
1.  Kopyala**aspose.cells.jasperreports.jar** gelen dosya**\ lib** içindeki klasör**aspose.cells.jasperreports.zip** için**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** dosya.
1.  aşağıdaki satırları ekleyin**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** dosya.
 (Bu fasulye, dışa aktarmayı yapılandırmaya yönelik çeşitli yapılandırma ayarları içerebilir. Örneğin, JasperReports yazı tipi eşleme özelliğini kullanabilir veya Aspose.Cells for JasperReports lisans dosyasının konumunu belirtebilirsiniz.)

**xml**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. JasperServer'ı çalıştırın ve görüntülemek için herhangi bir raporu açın. Önceki adımlar düzgün bir şekilde gerçekleştirildiyse, ek biçim simgeleri kullanılabilir.

**JasperServer'a Aspose.Cells for JasperReports yüklendikten sonra yeni dışa aktarma biçimleri kullanılabilir (sağda)** 

![yapılacaklar:resim_alternatif_Metin](integration-with-jasperserver_1.png)



