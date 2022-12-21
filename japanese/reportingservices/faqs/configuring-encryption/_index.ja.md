---
title: 暗号化の構成
type: docs
weight: 40
url: /ja/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services は暗号化をサポートしており、暗号化された Microsoft Excel ファイルをレンダリングできます。

{{% /alert %}} 
### **暗号化の種類**
Aspose.Cells for Reporting Services は、Excel ファイルをエクスポートする際の暗号化をサポートします。次の 3 つの暗号化タイプをサポートしています。

- XOR
- 弱い暗号化
- Microsoft 強力な暗号化プロバイダー
### **設定情報**
に暗号化の構成情報があります。**Aspose.Cells.ReportingServices.xml**ファイル。 Encryption の値が「off」に設定されている場合、Aspose.Cells.ReportingServices は暗号化をオフにします。

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

暗号化が「オン」に設定されている場合、Aspose.Cells.ReportingServices は暗号化をオンにします。

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Encryption セクションには、ReportName、Password、EncryptionType、KeyLength の 4 つのパラメーターがあります。

- ReportName – 暗号化設定が必要なレポートを設定します。パラメータが空白の場合、レポートは同じ暗号化方法を使用します。
- パスワード – パスワードを設定します。空欄にすることはできません。
- EncryptionType – 暗号化タイプを設定します。空欄にすることはできません。
-  KeyLength – キーの長さを設定します。空欄にすることはできません。

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
