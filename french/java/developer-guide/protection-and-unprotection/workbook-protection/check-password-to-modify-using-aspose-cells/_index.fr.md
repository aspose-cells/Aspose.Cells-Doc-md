---
title: Vérifiez le mot de passe pour modifier en utilisant Aspose.Cells
type: docs
weight: 190
url: /fr/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Vous pouvez attribuer un **Mot de passe pour ouvrir** et un **Mot de passe pour modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface fournie par Microsoft Excel pour spécifier ces mots de passe.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Parfois, vous devez vérifier si le mot de passe donné correspond au **Mot de passe pour modifier** de manière programmatique. Aspose.Cells fournit la méthode [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-) que vous pouvez utiliser pour vérifier si le mot de passe donné pour la modification est correct ou non.

{{% /alert %}}

## Code Java pour vérifier le mot de passe de modification à l'aide d'Aspose.Cells

Les extraits de code suivants chargent le fichier Excel source (5473057.xlsx). Il a un mot de passe pour ouvrir *1234* et un mot de passe pour modifier *5678*. Le code vérifie d'abord si *567* est un mot de passe correct pour la modification et il renvoie **faux**, puis il vérifie si *5678* est le mot de passe pour la modification et il renvoie **vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Sortie console générée par le code Java

Voici la sortie console du code d'exemple ci-dessus après avoir chargé le fichier Excel source (5473057.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
