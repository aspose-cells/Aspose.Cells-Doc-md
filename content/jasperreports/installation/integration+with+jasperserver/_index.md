---
title : "Integration with JasperServer" 
description : "" 
weight : 8020 
toc : false
type: docs
url: /jasperreports/installation/integration+with+jasperserver/
---

# Aspose.Cells for JasperReports : Integration with JasperServer


To integrate Aspose.Cells for JasperReports with JasperServer, perform the steps below.

In all of the following steps <InstallDir> stands for the JasperServer installation directory.

1.  Add the following new exporter properties to the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\flows\\viewReportBeans.xml** file.  
      
    
    **XML**
    
{{< code lang="xml" >}}
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
 
{{< /code >}}
    
      
    
2.  Locate the `<util:map id=”exporterConfigMap>` element in the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\flows\\viewReportBeans.xml** file and add the following lines:  
      
    
    **XML**
    
{{< code lang="xml" >}}
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
 
{{< /code >}}
    
      
      
    
3.  Copy all GIF images from the **\\lib** folder in the **aspose.cells.jasperreports.zip** to the \*<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\images\* folder.
4.  Copy the **aspose.cells.jasperreports.jar** file from the **\\lib** folder in the **aspose.cells.jasperreports.zip** to the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\lib\\.** folder.
5.  Add the following lines to the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\applicationContext.xml** file.  
    (This bean may contain various configuration settings intended to configure the export. For example, you can use the JasperReports font mapping feature or specify the location of the Aspose.Cells for JasperReports license file.)  
      
    
    **XML**
    
{{< code lang="xml" >}}
<bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean"> <!-- Uncomment to apply a license. Check the license path.
<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>
-->
</bean>
 
{{< /code >}}
    
      
      
    
6.  Run JasperServer and open any report to view. If the previous steps were performed properly, additional format icons are available.  
    

**New export formats available (on the right) after installing Aspose.Cells for JasperReports on JasperServer**  
![image](https://docs2.aspose.com/cells/jasperreports/attachments/6619174/6848537.png)  
  

