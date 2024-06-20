---
title: Attribuer et valider les signatures numériques
linktitle: Signature
type: docs
weight: 100
url: /fr/java/assign-and-validate-digital-signatures/
description: Signature numérique de fichier Excel, vérification. Pour protéger l authenticité du contenu d un classeur Excel, vous pouvez ajouter une signature numérique en utilisant des codes C# avec Aspose.Cells pour .Net.
---

{{% alert color="primary" %}}

Une signature numérique assure qu'un fichier de classeur est valide et que personne ne l'a modifié. Vous pouvez créer une signature numérique personnelle en utilisant l'outil **SELFCERT** inclus dans le pack Microsoft Office ou tout autre outil. Vous pouvez également acheter une signature numérique. Une fois que vous avez créé ou acquis une signature numérique, vous devez la joindre à votre classeur. Joindre une signature numérique est similaire à sceller une enveloppe. Si une enveloppe arrive scellée, vous avez un certain niveau d'assurance que personne n'a altéré son contenu.

L'API Aspose.Cells for Java fournit les classes [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) et [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) pour signer les feuilles de calcul ainsi que les valider.

{{% /alert %}}

## **Signature des feuilles de calcul**

Le processus de signature nécessite un certificat comme discuté ci-dessus. En plus du certificat, il faut également connaître son mot de passe pour signer avec succès les feuilles de calcul à l'aide de l'API Aspose.Cells.

L'extrait de code suivant montre l'utilisation de l'API Aspose.Cells for Java pour signer une feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

Dans le cas où le mot de passe spécifié ne correspond pas au mot de passe du certificat, une exception du type *javax.crypto.BadPaddingException* sera levée.

{{% /alert %}}

## **Validation des feuilles de calcul**

L'extrait de code suivant montre l'utilisation de l'API Aspose.Cells for Java pour valider la feuille de calcul.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
