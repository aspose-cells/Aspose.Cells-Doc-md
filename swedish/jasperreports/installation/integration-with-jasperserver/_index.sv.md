---
title: Integration med JasperServer
type: docs
weight: 30
url: /sv/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

För att integrera Aspose.Cells for JasperReports med JasperServer, utför stegen nedan.

{{% /alert %}} 

{{% alert color="primary" %}} 

 I alla följande steg<InstallDir> står för installationskatalogen JasperServer.

{{% /alert %}} 

1. Lägg till följande nya exportöregenskaper till**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** fil.

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

1.  Leta upp<util:map id=”exporterConfigMap> element i**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** fil och lägg till följande rader:

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




1.  Kopiera alla GIF-bilder från**\lib** mapp i**aspose.cells.jasperreports.zip** till*<InstallDir>\apache-tomcat\webapps\jasperserver\images* mapp.
1.  Kopiera**aspose.cells.jasperreports.jar** fil från**\lib** mapp i**aspose.cells.jasperreports.zip** till**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** mapp.
1.  Lägg till följande rader till**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** fil.
 (Den här bönan kan innehålla olika konfigurationsinställningar som är avsedda att konfigurera exporten. Du kan till exempel använda JasperReports teckensnittsmappningsfunktion eller ange platsen för licensfilen Aspose.Cells for JasperReports.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. Kör JasperServer och öppna valfri rapport att visa. Om de föregående stegen utfördes korrekt finns ytterligare formatikoner tillgängliga.

**Nya exportformat tillgängliga (till höger) efter installation av Aspose.Cells for JasperReports på JasperServer** 

![todo:image_alt_text](integration-with-jasperserver_1.png)



