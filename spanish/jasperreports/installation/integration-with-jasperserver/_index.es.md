---
title: Integración con JasperServer
type: docs
weight: 30
url: /es/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Para integrar Aspose.Cells para JasperReports con JasperServer, realice los pasos a continuación.

{{% /alert %}} 

{{% alert color="primary" %}} 

 En todos los pasos siguientes<InstallDir> significa el directorio de instalación de JasperServer.

{{% /alert %}} 

1.  Agregue las siguientes nuevas propiedades del exportador al**<Dir de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** expediente.

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

1.  Localiza el<util:map id=”exporterConfigMap> elemento en el**<Dir de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** archivo y agregue las siguientes líneas:

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




1.  Copie todas las imágenes GIF del**\lib** carpeta en el**aspose.cells.jasperreports.zip** hacia*<dirección de instalación>\apache-tomcat\webapps\jasperserver\images* carpeta.
1.  Copia el**aspose.cells.jasperreports.jar** archivo de la**\lib** carpeta en el**aspose.cells.jasperreports.zip** hacia**<Dir de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** carpeta.
1.  Agregue las siguientes líneas al**<Dir de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** expediente.
 (Este bean puede contener varios ajustes de configuración destinados a configurar la exportación. Por ejemplo, puede utilizar la función de asignación de fuentes de JasperReports o especificar la ubicación del archivo de licencia Aspose.Cells para JasperReports).

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1.  Ejecute JasperServer y abra cualquier informe para verlo. Si los pasos anteriores se realizaron correctamente, hay iconos de formato adicionales disponibles.

**Nuevos formatos de exportación disponibles (a la derecha) después de instalar Aspose.Cells para JasperReports en JasperServer** 

![todo:imagen_alternativa_texto](integration-with-jasperserver_1.png)



