---
title: Attribuer un code macro à un contrôle de formulaire
type: docs
weight: 400
url: /fr/java/assign-macro-code-to-form-control/
---

{{% alert color="primary" %}} 

Aspose.Cells vous permet d'attribuer un code macro à un contrôle de formulaire comme un bouton. Veuillez utiliser la méthode [ShapeCollection.addShape()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape\(int,%20int,%20int,%20int,%20int,%20int,%20int\)) pour attribuer un nouveau code macro à un contrôle de formulaire dans le classeur.

{{% /alert %}} 
## **Attribuer un code macro à un contrôle de formulaire en utilisant Aspose.Cells**
Le code d'exemple suivant crée un nouveau classeur, attribue un code macro à un bouton de formulaire et enregistre la sortie au format XLSM. Une fois que vous ouvrirez le fichier XLSM de sortie dans Microsoft Excel, vous verrez le code macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Voici un code d'exemple pour générer le fichier de sortie XLSM avec du code Macro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AssignMacroToFormControl-AssignMacroToFormControl.java" >}}
