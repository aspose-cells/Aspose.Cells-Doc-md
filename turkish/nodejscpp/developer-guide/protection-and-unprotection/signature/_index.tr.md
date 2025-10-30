---  
title: Dijital İmzalar Atma ve Doğrulama ile Node.js ve C++ kullanma  
linktitle: İmza  
type: docs  
weight: 140  
url: /tr/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Aspose.Cells for Node.js via C++ kullanılarak Excel dosyasına dijital imza atma ve doğrulama. Çalışma kitabı içeriğinin özgünlüğünü dijital imzalarla koruyun.  
keywords: Excel dosyasına dijital imza ekleme, Node.js ve C++ kullanarak, Node.js ile dijital imzayı nasıl doğrularsınız?  
---  

{{% alert color="primary" %}}  
Bir dijital imza, bir çalışma kitabı dosyasının geçerli olduğunu ve kimse tarafından değiştirilmediğini sağlar. Kişisel bir dijital imza, **Microsoft Selfcert.exe** veya herhangi bir diğer araç kullanılarak veya satın alınarak oluşturulabilir. Dijital bir imza oluşturduktan sonra, çalışma kitabınıza eklemelisiniz. Bir dijital imza eklemek, bir zarfı mühürlemekle benzerdir. Bir mühürlü zarf gelirse, içeriği kimseyle oynamadığınızın belirli bir düzeyde güvencesine sahipsiniz demektir.  
{{% /alert %}}  

## **Giriş**  

Dijital İmza penceresini kullanarak bir dijital imza ekleyin. Dijital İmza iletişim kutusu geçerli sertifikaları listeler. Dijital İmza iletişim kutusunu, sertifikaları görüntülemek ve kullanmak istediğiniz birini seçmek için kullanabilirsiniz. Bir çalışma kitabı dijital bir imzaya sahipse, imzanın adı **Sertifika Adı** alanında görünür. Dijital İmza iletişim kutusundaki **Kaldır** düğmesine tıklarsanız, Microsoft Excel dijital imzayı da kaldırır.  

## **Excel için Dijital İmza Ekleme**  

Aspose.Cells, işi yapmak için [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) modülünü sağlar (dijital imzaları atma ve doğrulama). Bu modül, dijital imza ekleme ve doğrulama için kullanışlı özellikler içerir.  

Aşağıdaki örnek kod, Aspose.Cells for Node.js via C++ API kullanılarak bu işlemin nasıl gerçekleştirileceğini anlatır.  

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

## **Gelişmiş Konular**  
- [Daha önceden imzalanmış Excel dosyasına Dijital İmza ekleme](/cells/tr/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Çalışma sayfasına İmza satırı eklemek](/cells/tr/nodejs-cpp/add-signature-line/)  
- [XAdES İmzası Desteği](/cells/tr/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
