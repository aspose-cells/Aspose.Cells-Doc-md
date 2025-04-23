---
title: Signer numériquement un projet de code VBA avec un certificat
type: docs
weight: 110
url: /fr/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Vous pouvez signer numériquement votre projet VBA à l'aide d'Aspose.Cells pour Python via .NET avec sa méthode [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Veuillez suivre ces étapes pour vérifier si votre fichier Excel est signé numériquement avec un certificat.

- Cliquez sur **Visual Basic** dans l'onglet **Développeur** pour ouvrir **l'EDI VBA (Environnement de Développement Intégré Visual Basic pour Applications)**
- Cliquez sur **Outils** > **Signatures numériques...** de l'**IDE Visual Basic for Applications**

et il montrera le **Formulaire de Signature Numérique** indiquant si le document est signé numériquement avec un certificat ou non.

{{% /alert %}} 

## **Signer numériquement un projet de code VBA avec un certificat en Python**

Le code d'exemple suivant illustre comment utiliser la méthode [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Voici les fichiers d'entrée et de sortie du code d'exemple. Vous pouvez utiliser n'importe quel fichier Excel et n'importe quel certificat pour tester ce code.

- [Fichier Excel source](5115028.xlsm) utilisé dans le code d'exemple.
- [Fichier pfx de l'exemple](5115039.pfx) pour créer une signature numérique. Veuillez l'installer sur votre ordinateur pour exécuter ce code. Son mot de passe est 1234.
- [Fichier Excel de sortie](5115029.xlsm) généré par le code d'exemple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

