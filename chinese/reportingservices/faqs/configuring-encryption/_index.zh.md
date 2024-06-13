---
title: 配置加密
type: docs
weight: 40
url: /zh/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services 支持加密，您可以渲染加密的 Microsoft Excel 文件。 

{{% /alert %}} 
### **加密类型**
在导出 Excel 文件时，Aspose.Cells for Reporting Services 支持加密。它支持三种加密类型：

- XOR
- 弱加密
- Microsoft强加密提供程序
### **配置信息**
**Aspose.Cells.ReportingServices.xml**文件中有有关加密的配置信息。当加密的值设置为"off"时，Aspose.Cells.ReportingServices将关闭加密。

XML

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

当加密设置为"on"时，Aspose.Cells.ReportingServices将打开加密。

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

加密部分有四个参数：报表名称、密码、加密类型和密钥长度。

- ReportName – 设置需要加密设置的报表。当参数为空时，报表使用相同的加密方式。
- Password – 设置密码。不可为空。
- EncryptionType – 设置加密类型。不可为空。
- KeyLength – 设置密钥长度。不可为空。 

XML

{{< highlight csharp >}}

 <Encryption value="on">

<Report name="Test" >

<Password value="12345"/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

<Report name="" >

<Password value="123456"/>

<EncryptionType value="XOR"/>

<KeyLength value="128"/>

</Report>

</Encryption>



{{< /highlight >}}
