---
title: 暗号化の設定
type: docs
weight: 40
url: /ja/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Servicesは暗号化をサポートしており、暗号化されたMicrosoft Excelファイルをレンダリングできます。 

{{% /alert %}} 
### **暗号化の種類**
Aspose.Cells for Reporting Servicesは、Excelファイルのエクスポート時に暗号化をサポートします。3つの暗号化タイプをサポートしています。

- XOR
- 弱い暗号化
- Microsoft Strong Cryptographic Provider
### **情報の構成**
**Aspose.Cells.ReportingServices.xml**ファイルには、暗号化の構成情報があります。Encryptionの値が"off"に設定されていると、Aspose.Cells.ReportingServicesは暗号化を解除します。

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

Encryptionが"on"に設定されている場合、Aspose.Cells.ReportingServicesは暗号化を有効にします。

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Encryptionセクションには4つのパラメータがあります: ReportName、Password、EncryptionType、KeyLength。

- ReportName – 暗号化設定が必要なレポートを設定します。パラメータが空白の場合、レポートは同じ暗号化方法を使用します。
- パスワード - パスワードを設定します。空白のままにすることはできません。
- 暗号化タイプ - 暗号化タイプを設定します。空白のままにすることはできません。
- キー長 - キー長を設定します。空白のままにすることはできません。 

**XML**

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
