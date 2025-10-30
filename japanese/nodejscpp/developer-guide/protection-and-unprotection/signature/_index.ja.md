---  
title: Node.js経由のC++を使ったデジタル署名の割り当てと検証  
linktitle: 署名  
type: docs  
weight: 140  
url: /ja/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Aspose.Cells for Node.js via C++を使用したExcelファイルのデジタル署名と検証。ブックの内容の信頼性をデジタル署名で保護します。  
keywords: Excelファイルのデジタル署名、Node.js経由のC++でデジタル署名を追加、Node.jsとC++でデジタル署名を検証する方法  
---  

{{% alert color="primary" %}}  
デジタル署名は、ブックファイルが有効であり、誰もがそれを変更していないことを保証します。 **Microsoft Selfcert.exe**または他のツールを使用して個人用のデジタル署名を作成したり、デジタル署名を購入したりすることができます。デジタル署名を作成した後は、それをブックに添付する必要があります。デジタル署名を添付することは、封筒を封印することと似ています。封がされた封筒が届いた場合、その内容が誰もが触れていないレベルの保証が得られます。  
{{% /alert %}}  

## **紹介**  

デジタル署名を添付するには、デジタル署名ダイアログを使用します。デジタル署名ダイアログには有効な証明書が一覧表示されます。デジタル署名ダイアログでは、証明書を表示し、使用する証明書を選択することができます。ブックにデジタル署名がある場合、署名の名前が**証明書名**フィールドに表示されます。デジタル署名ダイアログの**削除**ボタンをクリックすると、Microsoft Excelはデジタル署名も削除します。  

## **Excelにデジタル署名を追加する方法**  

Aspose.Cellsは[**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/)モジュールを提供し、デジタル署名の割り当てと検証を行います。このモジュールには、デジタル署名を追加・検証するための便利な機能があります。  

以下のサンプルコードをご覧ください。これにより、Aspose.Cells for Node.js via C++ APIを使ったタスクの実行方法がわかります。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const certPassword = "aa";

// dsc is signature collection that contains one or more signatures needed to sign
const dsc = new AsposeCells.DigitalSignatureCollection();

// Cert must contain a private key, it can be constructed from a cert file or Windows certificate collection.
const cert = new AsposeCells.DigitalSignature(dataDir + "mykey2.pfx", certPassword, "test for sign", new Date());
dsc.add(cert);

const wb = new AsposeCells.Workbook();

// wb.setDigitalSignature signs all signatures in dsc
wb.setDigitalSignature(dsc);
wb.save(path.join(dataDir, "newfile_out.xlsx"));

// open the file
const wb2 = new AsposeCells.Workbook(path.join(dataDir, "newfile_out.xlsx"));
console.log(wb2.isDigitallySigned);

// Get digitalSignature collection from workbook
const dsc2 = wb2.getDigitalSignature();
const digitalSignatures = dsc2.getEnumerator();
for (var dst of digitalSignatures)
{
    console.log(dst.getComments()); // test for sign - OK
    console.log(dst.getSignTime()); // 11/25/2010 1:22:01 PM - OK
    console.log(dst.isValid()); // True - OK
}

```  

## **高度なトピック**  
- [すでに署名されたExcelファイルにデジタル署名を追加する](/cells/ja/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [ワークシートに署名行を追加](/cells/ja/nodejs-cpp/add-signature-line/)  
- [XAdES署名のサポート](/cells/ja/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
