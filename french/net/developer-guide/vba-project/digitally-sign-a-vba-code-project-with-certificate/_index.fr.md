---
title: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Vous pouvez signer numériquement votre projet de code VBA en utilisant Aspose.Cells avec sa méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). Veuillez suivre ces étapes pour vérifier si votre fichier Excel est numériquement signé avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**
- Cliquez sur **Outils** > **Signatures numériques...** de l'**IDE Visual Basic for Applications**

et il montrera le **Formulaire de Signature Numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat en C#**

Le code d'exemple suivant illustre comment utiliser la méthode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). Voici les fichiers d'entrée et de sortie du code d'exemple. Vous pouvez utiliser n'importe quel fichier Excel et n'importe quel certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
