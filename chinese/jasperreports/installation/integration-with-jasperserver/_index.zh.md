---
title: 与 JasperServer 集成
type: docs
weight: 30
url: /zh/jasperreports/integration-with-jasperserver/
---
{{% alert color="primary" %}} 

要将 Aspose.Cells for JasperReports 与 JasperServer 集成，请执行以下步骤。

{{% /alert %}} 

{{% alert color="primary" %}} 

在以下所有步骤中<InstallDir>代表 JasperServer 安装目录。

{{% /alert %}} 

1. 将以下新的导出器属性添加到**<安装目录>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**文件。

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

1. 找到<util:map id=”exporterConfigMap>中的元素**<安装目录>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml**文件并添加以下行：

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




1. 复制所有 GIF 图像**\库**中的文件夹**aspose.cells.jasperreports.zip**到*<安装目录>\apache-tomcat\webapps\jasperserver\images*文件夹。
1. 复制**aspose.cells.jasperreports.jar**文件来自**\库**中的文件夹**aspose.cells.jasperreports.zip**到**<安装目录>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\。**文件夹。
1. 将以下行添加到**<安装目录>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**文件。
 （此 bean 可能包含旨在配置导出的各种配置设置。例如，您可以使用 JasperReports 字体映射功能或为 JasperReports 许可证文件指定 Aspose.Cells 的位置。）

**XML**

{{< highlight "csharp" >}}

 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

-->

</bean>



{{< /highlight >}}




1. 运行 JasperServer 并打开任何报告进行查看。如果正确执行了前面的步骤，则可以使用其他格式图标。

**在 JasperServer 上为 JasperReports 安装 Aspose.Cells 后可用的新导出格式（右侧）** 

![待办事项：图片_替代_文本](integration-with-jasperserver_1.png)



