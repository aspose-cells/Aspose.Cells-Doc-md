---  
title: Asignar y validar firmas digitales con Node.js vía C++  
linktitle: Firma  
type: docs  
weight: 140  
url: /es/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Firma digital y verificación de archivos Excel usando Aspose.Cells for Node.js via C++. Protege la autenticidad del contenido del libro con firmas digitales.  
keywords: Firma digital de archivos Excel, Añadir firma digital para Excel Node.js via C++, Cómo validar firma digital Node.js vía C++  
---  

{{% alert color="primary" %}}  
Una firma digital proporciona garantía de que un archivo de libro de trabajo es válido y que nadie lo ha alterado. Puedes crear una firma digital personal usando el **Microsoft Selfcert.exe** u otra herramienta, o puedes comprar una firma digital. Después de crear una firma digital, debes adjuntarla a tu libro de trabajo. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tienes cierto nivel de seguridad de que nadie ha manipulado su contenido.  
{{% /alert %}}  

## **Introducción**  

Utilice el cuadro de diálogo de Firma digital para adjuntar una firma digital. El cuadro de diálogo de Firma digital lista los certificados válidos. Puede usar el cuadro de diálogo de Firma digital para ver certificados y seleccionar el que desea utilizar. Si un libro tiene una firma digital, el nombre de la firma aparece en el campo **Nombre del certificado**. Si hace clic en el botón **Quitar** en el cuadro de diálogo de Firma digital, Microsoft Excel también quita la firma digital.  

## **Cómo agregar firma digital para Excel**  

Aspose.Cells proporciona el módulo [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) para realizar el trabajo (asignar y validar firmas digitales). El módulo tiene funciones útiles para agregar y validar firmas digitales.  

Por favor, vea el siguiente código de ejemplo que describe cómo puede realizar la tarea usando la API Aspose.Cells for Node.js via C++.  

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

## **Temas avanzados**  
- [Agregar firma digital a un archivo de Excel ya firmado](/cells/es/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Agregar línea de firma a la hoja de trabajo](/cells/es/nodejs-cpp/add-signature-line/)  
- [Soporte para firma XAdES](/cells/es/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
