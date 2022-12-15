---
title: Integrazione con JasperServer
type: docs
weight: 30
url: /it/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Per integrare Aspose.Cells for JasperReports con JasperServer, eseguire i passaggi seguenti.

{{% /alert %}} 

{{% alert color="primary" %}} 

 In tutti i passaggi successivi<InstallDir> sta per la directory di installazione di JasperServer.

{{% /alert %}} 

1.  Aggiungere le seguenti nuove proprietà dell'esportatore al file**<DirInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file.

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

1.  Individua il<util:map id=”exporterConfigMap> elemento nel**<DirInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file e aggiungere le seguenti righe:

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




1.  Copia tutte le immagini GIF dal file**\lib** cartella in**aspose.cells.jasperreports.zip** al*<DirInstall>\apache-tomcat\webapps\jasperserver\images* cartella.
1.  Copia il**aspose.cells.jasperreports.jar** file dal**\lib** cartella in**aspose.cells.jasperreports.zip** al**<DirInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** cartella.
1.  Aggiungere le seguenti righe al file**<DirInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file.
 (Questo bean può contenere varie impostazioni di configurazione destinate a configurare l'esportazione. Ad esempio, è possibile utilizzare la funzione di mappatura dei caratteri JasperReports o specificare la posizione del file di licenza Aspose.Cells for JasperReports.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1.  Eseguire JasperServer e aprire qualsiasi report da visualizzare. Se i passaggi precedenti sono stati eseguiti correttamente, sono disponibili icone di formato aggiuntive.

**Nuovi formati di esportazione disponibili (a destra) dopo aver installato Aspose.Cells for JasperReports su JasperServer** 

![cose da fare:immagine_alt_testo](integration-with-jasperserver_1.png)



