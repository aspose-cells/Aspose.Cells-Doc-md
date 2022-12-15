---
title: Intégration avec JasperServer
type: docs
weight: 30
url: /fr/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Pour intégrer Aspose.Cells for JasperReports à JasperServer, suivez les étapes ci-dessous.

{{% /alert %}} 

{{% alert color="primary" %}} 

 Dans toutes les étapes suivantes<InstallDir> représente le répertoire d'installation de JasperServer.

{{% /alert %}} 

1. Ajoutez les nouvelles propriétés d'exportateur suivantes au**<RépInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** dossier.

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

1.  Localisez le<util:map id=”exporterConfigMap> élément dans le**<RépInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** fichier et ajoutez les lignes suivantes :

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




1.  Copiez toutes les images GIF du**\lib** dossier dans le**aspose.cells.jasperreports.zip** au*<RépInstall>\apache-tomcat\webapps\jasperserver\images* dossier.
1.  Copiez le**aspose.cells.jasperreports.jar** dossier de la**\lib** dossier dans le**aspose.cells.jasperreports.zip** au**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** dossier.
1.  Ajoutez les lignes suivantes au**<RépInstall>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** dossier.
 (Ce bean peut contenir divers paramètres de configuration destinés à configurer l'exportation. Par exemple, vous pouvez utiliser la fonctionnalité de mappage de polices JasperReports ou spécifier l'emplacement du fichier de licence Aspose.Cells for JasperReports.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. Exécutez JasperServer et ouvrez n'importe quel rapport à afficher. Si les étapes précédentes ont été effectuées correctement, des icônes de format supplémentaires sont disponibles.

**Nouveaux formats d'exportation disponibles (à droite) après l'installation de Aspose.Cells for JasperReports sur JasperServer** 

![tâche : image_autre_texte](integration-with-jasperserver_1.png)



