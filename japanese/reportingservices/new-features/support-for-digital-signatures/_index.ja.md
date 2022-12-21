---
title: デジタル署名のサポート
type: docs
weight: 70
url: /ja/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

デジタル署名は、ワークブックが有効であり、誰も変更していないことを保証します。デジタル署名を添付することは、封筒を封印することに似ています。封筒が封印された状態で届いた場合、だれもその内容を改ざんしていないことをある程度保証できます。

 Microsoft Selfcert.exe またはその他のツールを使用して個人のデジタル署名を作成するか、デジタル署名を購入することができます。スプレッドシートに署名するには、デジタル署名を作成したら、ワークブックに署名を添付します。

 Aspose.Cells for Reporting Services はデジタル署名をサポートしています。

{{% /alert %}} 
### **デジタル署名の操作**
#### **デジタル署名でサポートされている Excel 形式**
Aspose.Cells for Reporting Services は、Excel 2007 および ODS ファイル形式へのエクスポート時にデジタル署名をサポートします。
#### **デジタル署名の構成**
の**Aspose.Cells.ReportingServices.xml**ファイルには、構成情報とデジタル署名のテキストが含まれています。<DigitalSignature>鬼ごっこ：

- DigitalSignature がオフに設定されている場合、Aspose.Cells for Reporting Services はデジタル署名機能をオフにします。
例えば：

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- DigitalSignature の値が on の場合、Aspose.Cells.ReportingServices はデジタル署名の機能をオンにします。
例えば：

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 DigitalSignature セクションには 4 つのパラメーターがあります。これらは ：

- name – デジタル署名が必要なレポートを指します。パラメータが空白の場合、レポートはデジタル署名に PFX ファイルを使用します。
- pfxFilename – PFX ファイルを指します。ファイル名は完全なファイル名でなければなりません。空白の値には設定できません。
- pfxPwd – パスワードを設定します。空欄にすることはできません。
- 目的 - 署名の目的を説明します。空白にすることができます。
例えば：

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
