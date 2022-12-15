---
title: 支持数字签名
type: docs
weight: 70
url: /zh/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

数字签名可确保工作簿有效并且没有人更改过它。附加数字签名类似于密封信封。如果信封到达时是密封的，您可以在一定程度上保证没有人篡改过其中的内容。

您可以使用 Microsoft Selfcert.exe 或任何其他工具创建个人数字签名，也可以购买数字签名。要签署电子表格，请在创建数字签名后将签名附加到您的工作簿。

 Aspose.Cells for Reporting Services 支持数字签名。

{{% /alert %}} 
### **使用数字签名**
#### **数字签名支持的 Excel 格式**
Aspose.Cells for Reporting Services 导出到Excel 2007 和ODS 文件格式时支持数字签名。
#### **配置数字签名**
这**Aspose.Cells.ReportingServices.xml**文件中包含数字签名的配置信息和文本<DigitalSignature>标签：

- 当 DigitalSignature 设置为关闭时，Aspose.Cells for Reporting Services 关闭数字签名功能。
例如：

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- 当DigitalSignature的值为on时，Aspose.Cells.ReportingServices开启数字签名功能。
例如：

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature 部分有四个参数。这些是 ：

- name – 指向需要数字签名的报告。参数为空时报表使用PFX文件进行数字签名。
- pfxFilename——指向 PFX 文件。文件名必须是完整的文件名。它不能设置为空值。
- pfxPwd – 设置密码。它不能留空。
- 目的——解释签名的目的。它可以是空白的。
例如：

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
