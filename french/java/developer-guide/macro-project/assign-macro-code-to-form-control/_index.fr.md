---
title: Attribuer un code de macro au contrôle de formulaire
type: docs
weight: 400
url: /fr/java/assign-macro-code-to-form-control/
---
{{% alert color="primary" %}} 

 Aspose.Cells vous permet d'attribuer un code de macro à un contrôle de formulaire comme un bouton. Veuillez utiliser le[ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) pour attribuer un nouveau code de macro à un contrôle de formulaire dans le classeur.

{{% /alert %}} 
## **Affectation d'un code de macro au contrôle de formulaire à l'aide de Aspose.Cells**
L'exemple de code suivant crée un nouveau classeur, attribue un code de macro à un bouton de formulaire et enregistre la sortie au format XLSM. Une fois, vous ouvrirez le fichier de sortie XLSM dans Microsoft Excel, vous verrez le code macro suivant.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Voici un exemple de code pour générer le fichier de sortie XLSM avec Macro Code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
