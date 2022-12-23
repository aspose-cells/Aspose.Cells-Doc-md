---
title: Ajout du module et du code VBA à l'aide de Aspose.Cells
type: docs
weight: 20
url: /fr/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells vous permet d'ajouter un nouveau module VBA et un code macro à l'aide de Aspose.Cells. Veuillez utiliser le[**Classeur.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet)) méthode pour ajouter le nouveau module VBA dans le classeur

{{% /alert %}}

## **Ajout du module et du code VBA à l'aide de Aspose.Cells**

L'exemple de code suivant crée un nouveau classeur et ajoute un nouveau module VBA et un code de macro et enregistre la sortie au format XLSM. Une fois, vous ouvrirez le fichier de sortie XLSM dans Microsoft Excel et cliquez sur le**Développeur > Visual Basic** commandes de menu, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code macro suivant.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Exemple de code

Voici un exemple de code pour générer le fichier de sortie XLSM avec le module VBA et le code macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
