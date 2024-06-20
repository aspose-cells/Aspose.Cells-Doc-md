---
title: Intégration avec JasperServer
type: docs
weight: 30
url: /fr/jasperreports/integration-with-jasperserver/
---

{{% alert color="primary" %}} 

Pour intégrer Aspose.Cells for JasperReports avec JasperServer, effectuez les étapes ci-dessous.

{{% /alert %}} 

{{% alert color="primary" %}} 

In all of the following steps <InstallDir> stands for the JasperServer installation directory. 

{{% /alert %}} 

1. Add the following new exporter properties to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file. 

**XML**

{{< highlight csharp >}}

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

1. Locate the <util:map id=”exporterConfigMap> element in the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file and add the following lines: 

**XML**

{{< highlight csharp >}}

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




1. Copy all GIF images from the **\lib** folder in the **aspose.cells.jasperreports.zip** to the *<InstallDir>\apache-tomcat\webapps\jasperserver\images* folder.
1. Copy the **aspose.cells.jasperreports.jar** file from the **\lib** folder in the **aspose.cells.jasperreports.zip** to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** folder.
1. Add the following lines to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file.
   (Ce bean peut contenir divers paramètres de configuration destinés à configurer l'exportation. Par exemple, vous pouvez utiliser la fonction de mappage de police JasperReports ou spécifier l'emplacement du fichier de licence Aspose.Cells for JasperReports.) 

**XML**

{{< highlight csharp >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. Exécutez JasperServer et ouvrez n'importe quel rapport pour le visualiser. Si les étapes précédentes ont été effectuées correctement, des icônes de format supplémentaires sont disponibles. 

**Nouveaux formats d'exportation disponibles (à droite) après l'installation de Aspose.Cells for JasperReports sur JasperServer** 

![todo:image_alt_text](integration-with-jasperserver_1.png)



