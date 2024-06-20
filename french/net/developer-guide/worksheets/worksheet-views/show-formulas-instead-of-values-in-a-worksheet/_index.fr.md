---
title: Afficher les formules au lieu des valeurs dans une feuille de calcul
type: docs
weight: 20
url: /fr/net/show-formulas-instead-of-values-in-a-worksheet/
description: Cet article fournit un code d exemple pour utiliser l API C# ou la bibliothèque .NET pour afficher de manière programmée des formules plutôt que des valeurs dans une feuille de calcul Excel ou un classeur.
---

{{% alert color="primary" %}}

Il est possible d'afficher des formules au lieu des valeurs calculées dans Microsoft Excel en utilisant l'option **Afficher les formules** de l'onglet **Formules**. Lorsque les formules sont affichées, Microsoft Excel affiche les formules dans la feuille de calcul. Vous pouvez obtenir le même résultat en utilisant Aspose.Cells.

{{% /alert %}}

Aspose.Cells fournit une propriété [**Worksheet.ShowFormulas**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/showformulas). Définissez-la sur **true** pour demander à Microsoft Excel d'afficher des formules.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ShowFormulasInsteadOfValues-1.cs" >}}
