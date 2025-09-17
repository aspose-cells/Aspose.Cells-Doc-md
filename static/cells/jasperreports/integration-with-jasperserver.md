##Integration with JasperServer
To integrate Aspose.Cells for JasperReports with JasperServer, perform the steps below.
In all of the following steps <InstallDir> stands for the JasperServer installation directory.
1. Add the following new exporter properties to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file.
**XML**
1. Locate the <util:map id=”exporterConfigMap> element in the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** file and add the following lines:
**XML**
1. Copy all GIF images from the **\lib** folder in the **aspose.cells.jasperreports.zip** to the *<InstallDir>\apache-tomcat\webapps\jasperserver\images* folder.
1. Copy the **aspose.cells.jasperreports.jar** file from the **\lib** folder in the **aspose.cells.jasperreports.zip** to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.** folder.
1. Add the following lines to the **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file.
(This bean may contain various configuration settings intended to configure the export. For example, you can use the JasperReports font mapping feature or specify the location of the Aspose.Cells for JasperReports license file.)
**XML**
1. Run JasperServer and open any report to view. If the previous steps were performed properly, additional format icons are available.
**New export formats available (on the right) after installing Aspose.Cells for JasperReports on JasperServer**
![todo:image_alt_text](integration-with-jasperserver_1.png)
