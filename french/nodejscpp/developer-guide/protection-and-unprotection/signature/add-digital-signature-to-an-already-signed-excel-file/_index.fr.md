---
title: Ajouter une signature numérique à un fichier Excel déjà signé avec Node.js via C++
linktitle: Ajouter une signature numérique à un fichier Excel déjà signé
type: docs
weight: 20
url: /fr/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Cet article décrit comment ajouter une signature numérique à un fichier Excel déjà signé en utilisant Node.js avec Aspose.Cells for Node.js via C++.
keywords: Ajouter une signature numérique à un fichier Excel déjà signé, comment ajouter une signature numérique à un document Excel déjà signé en utilisant Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for Node.js via C++ fournit la méthode [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) que vous pouvez utiliser pour ajouter une signature numérique à un fichier Excel déjà signé.

{{% alert color="primary" %}}

Veuillez noter qu'en ajoutant une signature numérique à un document Excel déjà signé, si le document original est un document généré par Aspose.Cells, cela fonctionne bien. Mais si le document original est généré par d'autres moteurs (par exemple Microsoft Excel, etc.), Aspose.Cells ne peut pas conserver le fichier identique après le chargement et la sauvegarde, ce qui rendra la signature d'origine invalide.

{{% /alert %}}

## **Comment ajouter une signature numérique à un fichier Excel déjà signé**

Le code d'exemple suivant montre comment utiliser la méthode [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) pour ajouter une signature numérique à un fichier Excel déjà signé. Veuillez vérifier le [fichier Excel d'exemple](50528280.xlsx) utilisé dans ce code. Ce fichier est déjà signé numériquement. Vérifiez le [fichier Excel de sortie](50528281.xlsx) généré par le code. Nous avons utilisé le certificat de démonstration nommé [AsposeDemo.pfx](50528279.pfx), qui a un mot de passe **aspose**. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel de référence après exécution.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Code d'exemple**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
