---
title: Vérifiez le mot de passe à modifier en utilisant Aspose.Cells
type: docs
weight: 190
url: /fr/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Vous pouvez attribuer un**Mot de passe pour ouvrir** et un**Mot de passe à modifier** lors de la création de vos classeurs dans Microsoft Excel. Veuillez consulter cette capture d'écran qui montre l'interface Microsoft fournie par Excel pour spécifier ces mots de passe.

![tâche : image_autre_texte](check-password-to-modify-using-aspose-cells_1.png)

 Parfois, vous devez vérifier si le mot de passe donné correspond au**Mot de passe à modifier** par programme. Aspose.Cells fournit[**classeur.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String)) méthode que vous pouvez utiliser pour vérifier si le mot de passe donné à modifier est correct ou non.

{{% /alert %}}

## Java code à vérifier Mot de passe à modifier avec Aspose.Cells

 Les exemples de codes suivants chargent le[source Excel](5473057.xlsx) dossier. Il a un mot de passe pour s'ouvrir en tant que*1234* et mot de passe à modifier au fur et à mesure*5678* . Le code vérifie d'abord si*567* est le mot de passe correct à modifier et il renvoie**faux** puis il vérifie si*5678* est le mot de passe à modifier et il retourne**vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Sortie console générée par le code Java

 Voici la sortie de la console de l'exemple de code ci-dessus après le chargement du[source Excel](5473057.xlsx) dossier.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
