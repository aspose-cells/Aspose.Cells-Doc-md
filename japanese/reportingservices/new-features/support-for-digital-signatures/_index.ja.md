---
title: デジタル署名のサポート
type: docs
weight: 70
url: /ja/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

デジタル署名は、ワークブックが有効であり、誰もがそれを改ざんしていないことを保証します。デジタル署名をアタッチすることは封筒を封をすることに似ています。封がされた封筒が届くと、その中身が誰によっても改ざんされていないというある程度の保証があります。 

Microsoft Selfcert.exeやその他のツールを使用してまたはデジタル署名を購入して、個人のデジタル署名を作成することができます。スプレッドシートに署名するには、デジタル署名を作成した後、ワークブックに署名をアタッチします。 

Aspose.Cells for Reporting Servicesはデジタル署名をサポートしています。 

{{% /alert %}} 
### **デジタル署名の取り扱い**
#### **デジタル署名のサポートされるExcelフォーマット**
Aspose.Cells for Reporting Servicesは、Excel 2007やODSファイルフォーマットにエクスポートする際にデジタル署名をサポートしています。
#### **デジタル署名の構成**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- DigitalSignatureがオフに設定されていると、Aspose.Cells for Reporting Servicesではデジタル署名機能がオフになります。
  例: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- DigitalSignatureの値がオンになっている場合、Aspose.Cells.ReportingServicesはデジタル署名の機能をオンにします。
  例: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

DigitalSignatureセクションには4つのパラメータがあります。それらは次のとおりです： 

- name - デジタル署名が必要なレポートを指します。パラメータが空白の場合、レポートはデジタル署名にPFXファイルを使用します。
- pfxFilename - PFXファイルを指します。ファイル名は完全である必要があります。空白の値に設定することはできません。
- pfxPwd - パスワードを設定します。空白にすることはできません。
- purpose - 署名の目的を説明します。空白にすることも可能です。
  例: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
