---
title: Attribuer une macro à une commande de formulaire
type: docs
weight: 60
url: /fr/python-net/assign-macro-to-form-control/
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET vous permet d’assigner un code Macro à un contrôle de formulaire comme un bouton. Veuillez utiliser la propriété [**Shape.macro_name**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/macro_name) pour assigner un nouveau code Macro à un contrôle de formulaire dans le classeur.

{{% /alert %}}

L'exemple de code suivant crée un nouveau classeur, attribue un code de macro à un bouton de formulaire et enregistre la sortie au format XLSM. Une fois que vous ouvrirez le fichier XLSM de sortie dans Microsoft Excel, vous verrez le code de macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Assigner une macro au contrôle de formulaire en Python**

Voici l'exemple de code pour générer le fichier XLSM de sortie avec un code de macro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AssignMacroToFormControl-1.py" >}}
