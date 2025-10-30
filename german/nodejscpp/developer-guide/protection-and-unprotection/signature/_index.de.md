---  
title: Digitale Signaturen mit Node.js über C++ zuweisen und verifizieren  
linktitle: Signatur  
type: docs  
weight: 140  
url: /de/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Digitale Signatur und Verifizierung von Excel Dateien mit Aspose.Cells for Node.js via C++. Schützen Sie die Authentizität des Arbeitsbuchinhalts mit digitalen Signaturen.  
keywords: Digitale Signatur einer Excel Datei, digitale Signatur für Excel in Node.js via C++ hinzufügen, wie man die digitale Signatur in Node.js via C++ validiert  
---  

{{% alert color="primary" %}}  
Eine digitale Signatur gewährleistet, dass eine Arbeitsmappe gültig ist und niemand sie verändert hat. Sie können eine persönliche digitale Signatur mithilfe des **Microsoft Selfcert.exe** oder eines anderen Tools erstellen oder eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt haben, müssen Sie sie Ihrer Arbeitsmappe hinzufügen. Das Anhängen einer digitalen Signatur ähnelt dem Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheit, dass niemand seinen Inhalt manipuliert hat.  
{{% /alert %}}  

## **Einführung**  

Verwenden Sie den Digital Signature-Dialog, um eine digitale Signatur anzuhängen. Der Digital Signature-Dialog listet gültige Zertifikate auf. Sie können den Digital Signature-Dialog verwenden, um Zertifikate anzuzeigen und das gewünschte Zertifikat auszuwählen. Wenn eine Arbeitsmappe eine digitale Signatur hat, erscheint der Name der Signatur im **Zertifikatname**-Feld. Wenn Sie auf die Schaltfläche **Entfernen** im Digital Signature-Dialog klicken, entfernt Microsoft Excel auch die digitale Signatur.  

## **Wie man eine digitale Signatur für Excel hinzufügt**  

Aspose.Cells bietet das [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) Modul, um die Aufgabe auszuführen (digitale Signaturen zuzuweisen und zu validieren). Das Modul verfügt über nützliche Funktionen zum Hinzufügen und Überprüfen digitaler Signaturen.  

Siehe den folgenden Beispielcode, der beschreibt, wie Sie die Aufgabe mit der API Aspose.Cells for Node.js via C++ ausführen können.  

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

## **Erweiterte Themen**  
- [Fügen Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu](/cells/de/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Fügen Sie der Arbeitsmappe eine Signaturzeile hinzu](/cells/de/nodejs-cpp/add-signature-line/)  
- [Unterstützung für XAdES-Signatur](/cells/de/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
