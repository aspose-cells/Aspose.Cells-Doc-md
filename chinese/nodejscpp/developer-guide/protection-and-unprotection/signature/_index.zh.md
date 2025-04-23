---  
title: 通过Node.js与C++签署和验证数字签名  
linktitle: 签名  
type: docs  
weight: 140  
url: /zh/nodejs-cpp/assign-and-validate-digital-signatures/  
description: 使用Aspose.Cells for Node.js via C++对Excel文件进行数字签名和验证。保护工作簿内容的真实性。  
keywords: Excel文件数字签名，添加数字签名到Excel Node.js通过C++，如何验证Node.js通过C++的数字签名  
---  

{{% alert color="primary" %}}  
数字签名可以确保工作簿文件有效，并且没有人篡改它。您可以使用 Microsoft 的 Selfcert.exe 或其它工具创建个人数字签名，也可以购买数字签名。创建数字签名后，您必须将其附加到工作簿。附加数字签名类似于封口一个信封。若收到封好的信封，您可以一定程度上确保没有人篡改其内容。  
{{% /alert %}}  

## **介绍**  

使用数字签名对话框附加数字签名。数字签名对话框列出有效的证书。您可以使用数字签名对话框查看证书并选择要使用的证书。如果工作簿有数字签名，签名的名称会出现在 **证书名称** 栏中。如果在数字签名对话框中点击 **删除** 按钮，Microsoft Excel 也会删除数字签名。  

## **如何为Excel添加数字签名**  

Aspose.Cells提供[**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/)模块以执行此任务（签署和验证数字签名）。该模块具有一些用于添加和验证数字签名的有用功能。  

请参阅以下示例代码，说明如何使用Aspose.Cells for Node.js via C++ API执行此任务。  

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

## **高级主题**  
- [对已签名的 Excel 文件添加数字签名](/cells/zh/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [在工作表中添加签名行](/cells/zh/nodejs-cpp/add-signature-line/)  
- [XAdES 签名的支持](/cells/zh/nodejs-cpp/support-for-xades-signature/)  

