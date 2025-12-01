---  
title: Assign and Validate Digital Signatures with Node.js via C++  
linktitle: Signature  
type: docs  
weight: 140  
url: /nodejs-cpp/assign-and-validate-digital-signatures/  
description: Excel file digital signature and verification using Aspose.Cells for Node.js via C++. Protect the authenticity of workbook content with digital signatures.  
keywords: Excel file digital signature, Add digital signature for Excel Node.js via C++, How to validate digital signature Node.js via C++  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  
A digital signature provides assurance that a workbook file is valid and no one has altered it. You can create a personal digital signature by using the **Microsoft Selfcert.exe** or any other tool, or you can purchase a digital signature. After you create a digital signature, you must attach it to your workbook. Attaching a digital signature is similar to sealing an envelope. If an envelope arrives sealed, you have some level of assurance that no one has tampered with its contents.  
{{% /alert %}}  

## **Introduction**  

Use the Digital Signature dialog to attach a digital signature. The Digital Signature dialog lists valid certificates. You can use the Digital Signature dialog to view certificates and to select the one you want to use. If a workbook has a digital signature, the name of the signature appears in the **Certificate Name** field. If you click the **Remove** button in the Digital Signature dialog, Microsoft Excel removes the digital signature as well.  

## **How to Add Digital Signature for Excel**  

Aspose.Cells provides the [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) module to perform the job (assign and validate digital signatures). The module has some useful features for adding and validating digital signatures.  

Please see the following sample code that describes how you can perform the task using the Aspose.Cells for Node.js via C++ API.  

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

## **Advance topics**  
- [Add Digital Signature to an already signed Excel file](/cells/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Add Signature line to the worksheet](/cells/nodejs-cpp/add-signature-line/)  
- [Support for XAdES Signature](/cells/nodejs-cpp/support-for-xades-signature/)  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
