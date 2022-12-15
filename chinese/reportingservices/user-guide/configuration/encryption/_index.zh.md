---
title: 加密
type: docs
weight: 40
url: /zh/reportingservices/encryption/
---
Aspose.Cells for Reporting Services 支持三种加密方式：XOR、WEAK ENCRYPTION、Microsoft Strong Cryptographic Provider。查看加密配置信息中的**Aspose.Cells.ReportingServices.xml**文件。

当加密的值为**离开**Aspose.Cells for Reporting Services 关闭加密功能。

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

当加密的值为**上**, Aspose.Cells for Reporting Services 打开加密。

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

加密部分有四个参数：

- **报告名称**指向需要加密的报告。如果该参数留空，则所有报告使用相同的加密方法。
- **密码**：设置密码。不能是空白的。
- **加密类型**：设置加密类型。不能是空白的。
- **密钥长度**：设置密钥长度。不能是空白的。

{{< highlight "java" >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
