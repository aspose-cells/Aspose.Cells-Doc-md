---  
title: Attribuer et valider les signatures numériques avec Node.js via C++  
linktitle: Signature  
type: docs  
weight: 140  
url: /fr/nodejs-cpp/assign-and-validate-digital-signatures/  
description: Signature numérique et vérification d un fichier Excel en utilisant Aspose.Cells for Node.js via C++. Protégez l authenticité du contenu du classeur avec des signatures numériques.  
keywords: Signature numérique de fichier Excel, ajouter une signature numérique pour Excel Node.js via C++, comment valider une signature numérique avec Node.js via C++  
---  

{{% alert color="primary" %}}  
Une signature numérique garantit qu'un fichier de classeur est valide et qu'aucune altération n'a été apportée. Vous pouvez créer une signature numérique personnelle en utilisant Microsoft Selfcert.exe ou tout autre outil, ou vous pouvez en acheter une. Après avoir créé une signature numérique, vous devez la joindre à votre classeur. Joindre une signature numérique est similaire à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez une certaine assurance que personne n'a trafiqué son contenu.  
{{% /alert %}}  

## **Introduction**  

Utilisez la boîte de dialogue Signature numérique pour joindre une signature numérique. La boîte de dialogue Signature numérique répertorie les certificats valides. Vous pouvez utiliser la boîte de dialogue Signature numérique pour afficher des certificats et sélectionner celui que vous souhaitez utiliser. Si un classeur a une signature numérique, le nom de la signature apparaît dans le champ **Nom du certificat**. Si vous cliquez sur le bouton **Supprimer** dans la boîte de dialogue Signature numérique, Microsoft Excel supprime également la signature numérique.  

## **Comment ajouter une signature numérique pour Excel**  

Aspose.Cells fournit le module [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature/) pour effectuer la tâche (attribuer et valider des signatures numériques). Le module possède plusieurs fonctionnalités utiles pour ajouter et valider des signatures numériques.  

Veuillez consulter le code d'exemple ci-dessous qui décrit comment effectuer cette tâche en utilisant l'API Aspose.Cells for Node.js via C++.  

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

## **Sujets avancés**  
- [Ajouter une signature numérique à un fichier Excel déjà signé](/cells/fr/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/)  
- [Ajouter une ligne de signature au classeur](/cells/fr/nodejs-cpp/add-signature-line/)  
- [Prise en charge de la signature XAdES](/cells/fr/nodejs-cpp/support-for-xades-signature/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
