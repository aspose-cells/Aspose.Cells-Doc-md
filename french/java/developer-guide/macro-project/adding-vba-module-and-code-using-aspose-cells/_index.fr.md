---
title: Ajouter un module VBA et du code en utilisant Aspose.Cells
type: docs
weight: 20
url: /fr/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'ajouter un nouveau module VBA et un code macro en utilisant Aspose.Cells. Veuillez utiliser la méthode [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) pour ajouter le nouveau module VBA dans le classeur.

{{% /alert %}}

## **Ajouter un module VBA et du code en utilisant Aspose.Cells**

Le code d'exemple suivant crée un nouveau classeur et ajoute un nouveau module VBA et un code de macro, puis enregistre la sortie au format XLSM. Une fois, vous ouvrirez le fichier XLSM de sortie dans Microsoft Excel et cliquerez sur les commandes de menu **Développeur > Visual Basic**, vous verrez un module nommé "TestModule" et à l'intérieur, vous verrez le code de macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Code d'exemple

Voici un code d'exemple pour générer le fichier de sortie XLSM avec un module VBA et du code Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
