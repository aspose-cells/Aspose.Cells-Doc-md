---
title: 许可
type: docs
weight: 40
url: /zh/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports可以从[下载页面](https://downloads.aspose.com/cells/jasperreports)免费获取不受时间限制的评估。产品的评估版本和许可版本是相同的下载。

当您对评估版本满意时，您可以[购买许可证](https://purchase.aspose.com/)。确保您了解并同意许可条款。

许可证在订单支付后可从订单页面下载。许可证是一个明文的、数字签名的XML文件。许可证包含客户名称、已购买产品和许可证类型等信息。不要修改许可证文件的内容：这样会使许可证失效。

有两种应用许可证的方法：

- [调用setLicense](/cells/zh/jasperreports/licensing/#call-setlicense)
- [在applicationContext.xml中设置一个导出器参数](/cells/zh/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

安装许可证后

- [验证其有效性](/cells/zh/jasperreports/licensing/#verify-the-license-works)。

{{% /alert %}}

## **调用setLicense**

{{% alert color="primary" %}}

此方法适用于与JasperReports一起使用。

{{% /alert %}}

将许可证下载到计算机并复制到适当的文件夹中（例如您的应用程序文件夹或**JasperReports\lib**）。
将以下代码添加到您的项目中：

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

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **验证许可证是否有效**

将任何报告导出为XLS格式，检查报告是否包含评估消息。 如果没有评估消息，则许可证正常工作。

Aspose.Cells for JasperReports在评估模式下注入一个评估工作表 

![todo:image_alt_text](licensing_1.png)

当存在有效许可证时，没有评估工作表 

![todo:image_alt_text](licensing_2.png)
