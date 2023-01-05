---
title: Attribuer et valider des signatures numériques
linktitle: Signature
type: docs
weight: 100
url: /fr/java/assign-and-validate-digital-signatures/
description: Signature numérique du fichier Excel, vérification. Pour protéger l'authenticité du contenu d'un classeur dans un fichier Excel, vous pouvez ajouter une signature numérique en utilisant les codes C# avec Aspose.Cells pour .Net.
---
{{% alert color="primary" %}}

 Une signature numérique garantit qu'un fichier de classeur est valide et que personne ne l'a modifié. Vous pouvez créer une signature numérique personnelle en utilisant le**AUTOCERT** outil livré avec la suite Office Microsoft ou tout autre outil. Vous pouvez même acheter une signature numérique. Après avoir créé ou acquis une signature numérique, vous devez la joindre à votre classeur. Joindre une signature numérique revient à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez un certain niveau d'assurance que personne n'a altéré son contenu.

 Aspose.Cells for Java API fournissent le[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) classes pour signer les feuilles de calcul et les valider.

{{% /alert %}}

## **Signature des feuilles de calcul**

Le processus de signature nécessite un certificat, comme indiqué ci-dessus. En plus du certificat, il faut également avoir son mot de passe pour signer avec succès les feuilles de calcul en utilisant le Aspose.Cells API.

L'extrait de code suivant illustre l'utilisation de Aspose.Cells for Java API pour signer une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 Si le mot de passe spécifié ne correspond pas au mot de passe du certificat, une exception de type*javax.crypto.BadPaddingException* sera jeté.

{{% /alert %}}

## **Validation des feuilles de calcul**

L'extrait de code suivant illustre l'utilisation de Aspose.Cells for Java API pour valider la feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
