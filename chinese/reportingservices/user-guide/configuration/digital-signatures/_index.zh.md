---
title: 数字签名
type: docs
weight: 50
url: /zh/reportingservices/digital-signatures/
---
Aspose.Cells for Reporting Services 在导出 Microsoft Excel 2007 文件或 ODS 文件时支持数字签名。我们有一些数字签名的配置信息，可以在**Aspose.Cells.ReportingServices.xml**文件。

当 DigitalSignature 的值为**离开**Aspose.Cells 用于 Reporting Services 关闭数字签名。

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

当 DigitalSignature 的值为**上**Reporting Services 的 Aspose.Cells 打开数字签名。

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature 部分有四个参数。这些是：

- **姓名**：代表需要数字签名的报告。当该参数留空时，报告使用 PFX 文件进行数字签名。
- **pfx文件名**指的是 PFX 文件。文件名应该是完全限定的文件名，包括路径和文件扩展名。不能为空。
- **pfx密码**：设置密码。不能为空。
- **目的**签名的描述。可以为空。

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
