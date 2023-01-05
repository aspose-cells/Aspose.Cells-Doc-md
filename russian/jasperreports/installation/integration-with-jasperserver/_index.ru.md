---
title: Интеграция с JasperServer
type: docs
weight: 30
url: /ru/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

Чтобы интегрировать Aspose.Cells for JasperReports с JasperServer, выполните следующие действия.

{{% /alert %}} 

{{% alert color="primary" %}} 

 Во всех следующих шагах<InstallDir> обозначает каталог установки JasperServer.

{{% /alert %}} 

1. Добавьте следующие новые свойства экспортера в**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** файл.

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

1.  Найдите<util:map id=”exporterConfigMap> элемент в**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** файл и добавьте следующие строки:

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




1.  Скопируйте все изображения GIF из**\lib** папка в**aspose.cells.jasperreports.zip** к*<InstallDir>\apache-tomcat\webapps\jasperserver\images* папка.
1.  Скопируйте**aspose.cells.jasperreports.jar** файл из**\lib** папка в**aspose.cells.jasperreports.zip** к**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** папка.
1.  Добавьте следующие строки в**<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** файл.
 (Этот bean-компонент может содержать различные параметры конфигурации, предназначенные для настройки экспорта. Например, вы можете использовать функцию сопоставления шрифтов JasperReports или указать расположение файла лицензии Aspose.Cells for JasperReports.)

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. Запустите JasperServer и откройте любой отчет для просмотра. Если предыдущие шаги были выполнены правильно, доступны дополнительные значки формата.

**Доступны новые форматы экспорта (справа) после установки Aspose.Cells for JasperReports на JasperServer** 

![дело:изображение_альтернативный_текст](integration-with-jasperserver_1.png)



