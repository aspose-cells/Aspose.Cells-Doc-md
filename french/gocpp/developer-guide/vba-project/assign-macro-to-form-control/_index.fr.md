---
title: Assigner une macro à un contrôle de formulaire avec Golang via C++
linktitle: Attribuer une macro à une commande de formulaire
type: docs
weight: 60
url: /fr/go-cpp/assign-macro-to-form-control/
description: Apprenez comment attribuer un code macro à un contrôle de formulaire comme un bouton en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'attribuer un code de macro à une Commande de formulaire comme un bouton. Veuillez utiliser la propriété [**Shape.GetMacroName()**](https://reference.aspose.com/cells/go-cpp/shape/getmacroname/) pour attribuer un nouveau code de macro à une Commande de formulaire à l'intérieur du classeur.

{{% /alert %}}

Le code d'exemple suivant crée un nouveau classeur, attribue un code macro à un bouton de formulaire, et sauvegarde le résultat au format XLSM. Une fois que vous ouvrez le fichier XLSM dans Microsoft Excel, vous verrez le code macro suivant.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Attribuer une macro à un contrôle de formulaire en C++**

Voici l'exemple de code pour générer le fichier XLSM de sortie avec un code de macro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AssignMacroToFormControl.go" >}}
