---  
title: Tilldela och validera digitala signaturer med Node.js via C++  
linktitle: Signatur  
type: docs  
weight: 140  
url: /sv/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Digital signatur och verifiering av Excel fil med Aspose.Cells for Node.js via C++. Skydda äktheten av arbetsbokens innehåll med digitala signaturer.  
keywords: Digital signatur för Excel fil, Lägg till digital signatur för Excel Node.js via C++, Hur man validerar digital signatur Node.js via C++  
---  

{{% alert color="primary" %}}  
En digital signatur ger försäkran om att en arbetsboksfil är giltig och att ingen har ändrat den. Du kan skapa en personlig digital signatur med Microsoft Selfcert.exe eller något annat verktyg, eller så kan du köpa en digital signatur. När du har skapat en digital signatur måste du bifoga den till din arbetsbok. Att bifoga en digital signatur är liknande att försegla ett kuvert. Om ett kuvert kommer förseglad har du en viss nivå av försäkran om att ingen har manipulerat dess innehåll.  
{{% /alert %}}  

## **Introduktion**  

Använd Digital Signature dialogrutan för att bifoga en digital signatur. Digital Signature dialogrutan listar giltiga certifikat. Du kan använda Digital Signature dialogrutan för att visa certifikat och välja det du vill använda. Om en arbetsbok har en digital signatur, visas namnet på signaturen i fältet Certifikatnamn. Om du klickar på knappen Ta bort i Digital Signature dialogrutan, tar Microsoft Excel bort den digitala signaturen också.  

## **Så här lägger du till digital signatur för Excel**  

Aspose.Cells tillhandahåller modulen [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) för att utföra jobbet (tilldela och validera digitala signaturer). Modulen har några användbara funktioner för att lägga till och validera digitala signaturer.  

Vänligen se följande exempel på kod som beskriver hur du utför uppgiften med Aspose.Cells for Node.js via C++ API.  

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

## **Fortsatta ämnen**  
- [Lägg till digital signatur i en redan signerad Excel-fil](/cells/sv/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Lägg till signaturraden i arbetsbladet](/cells/sv/nodejs-cpp/add-signature-line/)  
- [Stöd för XAdES-signatur](/cells/sv/nodejs-cpp/support-for-xades-signature/)  

