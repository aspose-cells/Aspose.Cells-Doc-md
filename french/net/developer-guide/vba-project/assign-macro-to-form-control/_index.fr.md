---
title: Attribuer une macro à une commande de formulaire
type: docs
weight: 60
url: /fr/net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'attribuer un code de macro à une Commande de formulaire comme un bouton. Veuillez utiliser la propriété [**Shape.MarcoName**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/macroname) pour attribuer un nouveau code de macro à une Commande de formulaire à l'intérieur du classeur.

{{% /alert %}}

L'exemple de code suivant crée un nouveau classeur, attribue un code de macro à un bouton de formulaire et enregistre la sortie au format XLSM. Une fois que vous ouvrirez le fichier XLSM de sortie dans Microsoft Excel, vous verrez le code de macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Attribuer une macro à une commande de formulaire en C#**

Voici l'exemple de code pour générer le fichier XLSM de sortie avec un code de macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AssignMacroToFormControl-1.cs" >}}
