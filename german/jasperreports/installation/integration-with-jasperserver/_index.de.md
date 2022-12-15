---
title: Integration mit JasperServer
type: docs
weight: 30
url: /de/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Führen Sie die folgenden Schritte aus, um Aspose.Cells for JasperReports in JasperServer zu integrieren.

{{% /alert %}} 

{{% alert color="primary" %}} 

 In allen folgenden Schritten<InstallDir> steht für das JasperServer-Installationsverzeichnis.

{{% /alert %}} 

1. Fügen Sie die folgenden neuen Exporter-Eigenschaften zu der hinzu**<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** Datei.

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

1.  Suchen Sie die<util:map id=”exporterConfigMap> Element in der**<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** Datei und fügen Sie die folgenden Zeilen hinzu:

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




1.  Kopieren Sie alle GIF-Bilder aus der**\lib** Ordner im**aspose.cells.jasperreports.zip** zum*<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\images* Mappe.
1.  Kopiere das**aspose.cells.jasperreports.jar** Datei aus der**\lib** Ordner im**aspose.cells.jasperreports.zip** zum**<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** Mappe.
1.  Fügen Sie die folgenden Zeilen hinzu**<Installationsverzeichnis>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** Datei.
 (Diese Bean kann verschiedene Konfigurationseinstellungen enthalten, die zum Konfigurieren des Exports bestimmt sind. Sie können beispielsweise die JasperReports-Funktion zur Schriftartzuordnung verwenden oder den Speicherort der Lizenzdatei Aspose.Cells for JasperReports angeben.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. Führen Sie JasperServer aus und öffnen Sie einen beliebigen Bericht, um ihn anzuzeigen. Wenn die vorherigen Schritte ordnungsgemäß ausgeführt wurden, sind zusätzliche Formatsymbole verfügbar.

**Neue Exportformate verfügbar (rechts) nach der Installation von Aspose.Cells for JasperReports auf JasperServer** 

![todo: Bild_alt_Text](integration-with-jasperserver_1.png)



