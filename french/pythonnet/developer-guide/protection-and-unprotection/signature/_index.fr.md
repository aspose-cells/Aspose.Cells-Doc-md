---
title: Attribuer et valider les signatures numériques
linktitle: Signature
type: docs
weight: 140
url: /fr/python-net/assign-and-validate-digital-signatures/
description: Signature numérique du fichier Excel, vérification. Pour protéger l authenticité du contenu d un classeur Excel, vous pouvez ajouter une signature numérique en utilisant des codes C# avec Aspose.Cells pour Python via .NET.
keywords: Signature numérique de fichier Excel, Ajouter une signature numérique pour Excel, Comment valider une signature numérique.
---

{{% alert color="primary" %}}

Une signature numérique garantit qu'un fichier de classeur est valide et qu'aucune altération n'a été apportée. Vous pouvez créer une signature numérique personnelle en utilisant Microsoft Selfcert.exe ou tout autre outil, ou vous pouvez en acheter une. Après avoir créé une signature numérique, vous devez la joindre à votre classeur. Joindre une signature numérique est similaire à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez une certaine assurance que personne n'a trafiqué son contenu.

{{% /alert %}}

## **Introduction**

Utilisez la boîte de dialogue Signature numérique pour joindre une signature numérique. La boîte de dialogue Signature numérique répertorie les certificats valides. Vous pouvez utiliser la boîte de dialogue Signature numérique pour afficher des certificats et sélectionner celui que vous souhaitez utiliser. Si un classeur a une signature numérique, le nom de la signature apparaît dans le champ **Nom du certificat**. Si vous cliquez sur le bouton **Supprimer** dans la boîte de dialogue Signature numérique, Microsoft Excel supprime également la signature numérique.

## **Comment ajouter une signature numérique pour Excel**

Aspose.Cells pour Python via .NET fournit l'espace de noms [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/python-net/aspose.cells.digitalsignatures/digitalsignature) pour effectuer cette opération (attribuer et valider des signatures numériques). Cet espace de noms dispose de fonctionnalités utiles pour ajouter et valider des signatures numériques.

Veuillez voir le code d'exemple suivant qui décrit comment effectuer la tâche en utilisant l'API Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AssignAndValidateDigitalSignatures.py" >}}



## **Sujets avancés**
- [Ajouter une signature numérique à un fichier Excel déjà signé](/cells/fr/python-net/add-digital-signature-to-an-already-signed-excel-file/)
- [Ajouter une ligne de signature au classeur](/cells/fr/python-net/add-signature-line/)
- [Prise en charge de la signature XAdES](/cells/fr/python-net/support-for-xades-signature/)

