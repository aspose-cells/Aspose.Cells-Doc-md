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
Aspose.Cells for Reporting Services 导出Excel文件时支持加密。它支持三种加密类型：

- 异或
- 弱加密
- Microsoft 强大的加密提供程序
### **配置信息**
里面有加密的配置信息**Aspose.Cells.ReportingServices.xml**文件。当 Encryption 的值设置为“off”时，Aspose.Cells.ReportingServices 将关闭加密。

**XML**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

当加密设置为“打开”时，Aspose.Cells.ReportingServices 将打开加密。

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Encryption 部分有四个参数：ReportName、Password、EncryptionType 和KeyLength。

- ReportName – 设置需要加密设置的报告。当参数为空时，报告使用相同的加密方式。
- 密码 – 设置密码。它不能留空。
- EncryptionType – 设置加密类型。它不能留空。
-  KeyLength – 设置密钥长度。它不能留空。

**XML**

{{< highlight "csharp" >}}

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
