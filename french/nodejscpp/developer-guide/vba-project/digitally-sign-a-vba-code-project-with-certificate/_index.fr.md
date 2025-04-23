---
title: Signer numériquement un projet de code VBA avec un certificat en utilisant Node.js via C++
linktitle: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Apprenez comment signer numériquement un projet de code VBA avec un certificat en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Vous pouvez signer numériquement votre projet de code VBA avec Aspose.Cells en utilisant sa méthode [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Suivez ces étapes pour vérifier si votre fichier Excel est signé numériquement avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**
- Cliquez sur **Outils** > **Signatures numériques...** dans **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**

et il montrera le **Formulaire de Signature Numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat dans Node.js**

Le code d'exemple suivant illustre comment utiliser la méthode [**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-). Voici les fichiers d'entrée et de sortie du code d'exemple. Vous pouvez utiliser n'importe quel fichier Excel et tout certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
