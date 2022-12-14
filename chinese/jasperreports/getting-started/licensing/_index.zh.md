---
title: 许可
type: docs
weight: 40
url: /zh/jasperreports/licensing/
---
{{% alert color="primary" %}}

 JasperReports 的 Aspose.Cells 可作为免费、无时间限制的评估从[下载页面](https://downloads.aspose.com/cells/jasperreports).该产品的评估版和许可版是同一个下载。

当您对评估版感到满意时，您可以[购买许可证](https://purchase.aspose.com/).确保您理解并同意许可条款。

订单付款后，可从订单页面下载许可证。许可证是一个明文、数字签名的 XML 文件。许可证包含客户名称、购买的产品和许可证类型等信息。不要修改许可证文件的内容：这样做会使许可证失效。

有两种申请许可证的方法：

- [调用setLicense](/cells/zh/jasperreports/licensing/#call-setlicense)
- [在 applicationContext.xml 中设置导出器参数](/cells/zh/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

安装许可证后，

- [验证它是否有效](/cells/zh/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **调用setLicense**

{{% alert color="primary" %}}

此方法适用于与 JasperReports 一起使用。

{{% /alert %}}

将许可证下载到您的计算机并将其复制到适当的文件夹（例如您的应用程序文件夹或**JasperReports\lib**).
将以下代码添加到您的项目中：

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **在 applicationContext.xml 中设置 licenseFile Exporter Parameter**

{{% alert color="primary" %}}

此方法适用于 JasperServer。

{{% /alert %}}

1. 将许可证下载到您的计算机并将其复制到**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF**文件夹，在哪里**\<安装目录>**代表 JasperServer 安装目录。
1. 找到**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**文件并添加以下行：

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **验证许可证工作**

将任何报告导出为 XLS 格式并检查报告是否包含评估消息。如果没有评估消息，则许可证工作正常。

**Aspose.Cells for JasperReports 在评估模式下注入评估工作表** 

![待办事项：图片_替代_文本](licensing_1.png)

**如果许可证有效，则没有评估工作表** 

![待办事项：图片_替代_文本](licensing_2.png)
