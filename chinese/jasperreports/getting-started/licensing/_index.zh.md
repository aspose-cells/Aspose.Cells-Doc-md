---
title: 许可证
type: docs
weight: 40
url: /zh/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports可从[下载页面](https://downloads.aspose.com/cells/jasperreports)免费、无时间限制地评估和许可版本。产品的评估版和许可版是相同的下载。

当您对评估版本满意时，可以[购买许可证](https://purchase.aspose.com/)。确保您了解并同意许可证条款。

订购付款后，许可证可以从订单页面下载。许可证是一个明文、数字签名的XML文件。许可证包含客户名称、所购产品和许可证类型等信息。不要修改许可证文件的内容：这样会使许可证无效。

有两种方式来应用许可证：

- [调用setLicense](/cells/zh/jasperreports/licensing/#call-setlicense)
- [在applicationContext.xml中设置导出器参数](/cells/zh/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

安装许可证后，

- [验证许可证是否生效](/cells/zh/jasperreports/licensing/#verify-the-license-works)。

{{% /alert %}}

## **调用setLicense**

{{% alert color="primary" %}}

此方法适用于与JasperReports一起使用。

{{% /alert %}}

将许可证下载到计算机并复制到适当的文件夹（例如应用程序文件夹或**JasperReports\lib**）。
将以下代码添加到您的项目：

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **在applicationContext.xml中设置licenseFile导出器参数**

{{% alert color="primary" %}}

此方法适用于与JasperServer一起使用。

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

XML

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **验证许可证是否生效**

将任何报表导出为XLS格式并检查报表是否包含评估消息。如果没有评估消息，则证书正常工作。

**Aspose.Cells for JasperReports 在评估模式下注入评估工作表** 

![todo:image_alt_text](licensing_1.png)

**当使用有效许可证时，没有评估工作表** 

![todo:image_alt_text](licensing_2.png)
