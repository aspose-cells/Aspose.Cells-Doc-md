---
title: Signer numériquement un projet de code VBA avec un certificat dans C++
linktitle: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Apprenez comment signer numériquement votre projet de code VBA en utilisant Aspose.Cells for C++ avec un certificat.
---

{{% alert color="primary" %}} 

Vous pouvez signer numériquement votre projet de code VBA avec Aspose.Cells en utilisant sa méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Suivez ces étapes pour vérifier si votre fichier Excel est signé numériquement avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **VBA IDE**.
- Cliquez sur **Outils** > **Signatures numériques...** dans **VBA IDE**.

Cela affichera le **Formulaire de signature numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat dans C++**

Le code d'exemple suivant illustre comment utiliser la méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Voici les fichiers d'entrée et de sortie de l'exemple de code. Vous pouvez utiliser n'importe quel fichier Excel et tout certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
