+++
title = "Licensing" 
description = "" 
weight = 8013 
+++

Aspose.Cells for JasperReports : Licensing  

# Aspose.Cells for JasperReports : Licensing


Aspose.Cells for JasperReports is available as a free, time unlimited evaluation from the [download page](http://www.aspose.com/community/files/67/jasperreports-exporters/aspose.cells-for-jasperreports/default.aspx). The evaluation and licensed versions of the product is the same download.

When you are happy with the evaluation version, you can [purchase a license](http://www.aspose.com/purchase/default.aspx). Make sure you understand and agree to the license terms.

The license is available for download from the order page when the order has been paid. The license is a clear text, digitally signed XML file. The license contains information such as the client name, purchased product and license type. Do not modify the content of the license file: doing so invalidates the license.

There are two ways to apply a license:

*   [Call `setLicense`](https://docs2.aspose.com/cells/jasperreports/gettingstarted/licensing)
*   [Set an exporter parameter in applicationContext.xml](https://docs2.aspose.com/cells/jasperreports/gettingstarted/licensing)

After installing the license,

*   [Verify that it works](https://docs2.aspose.com/cells/jasperreports/gettingstarted/licensing).

### Call setLicense

  

This method is applicable for use with JasperReports.

Download the license to your computer and copy it to the appropriate folder (for example your application's folder or **JasperReports\\lib**).  
Add the following code to your project:

**Java**

{{< code lang="java" >}}
import com.aspose.cells.jasperreports.*;
 
// Create a stream object containing the license file
FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");
 
// Set the license through the stream object
License license = new License();
license.setLicense(fstream);
 
{{< /code >}}

### Set the licenseFile Exporter Parameter in applicationContext.xml

  

This method is applicable for use with JasperServer.

1.  Download the license to your computer and copy it to the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF** folder, where **<InstallDir>** stands for the JasperServer installation directory.
2.  Locate the **<InstallDir>\\apache-tomcat\\webapps\\jasperserver\\WEB-INF\\applicationContext.xml** file and add the following lines:
    
    **XML**
    
{{< code lang="xml" >}}
 <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>
</bean>
 
{{< /code >}}
    

### Verify the License Works

Export any report to XLS format and check if the report contains an evaluation message. If there is no evaluation message, then the license is working properly.  

**Aspose.Cells for JasperReports injects an evaluation worksheet in evaluation mode**  
![](https://docs2.aspose.com/cells/jasperreports/attachments/6619153/6848521.png)  
  
**When a valid license there is no evaluation worksheet**  
![](https://docs2.aspose.com/cells/jasperreports/attachments/6619153/6848522.png)

## Attachments:

![](https://docs2.aspose.com/cells/jasperreports/images/icons/bullet_blue.gif) [Licensing-001.png](https://docs2.aspose.com/cells/jasperreports/attachments/6619153/6848521.png) (image/png)  
![](https://docs2.aspose.com/cells/jasperreports/images/icons/bullet_blue.gif) [Licensing-002.png](https://docs2.aspose.com/cells/jasperreports/attachments/6619153/6848522.png) (image/png)  

