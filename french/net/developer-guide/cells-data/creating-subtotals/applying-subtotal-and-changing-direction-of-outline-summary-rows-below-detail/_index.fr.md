---
title: Appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
type: docs
weight: 100
url: /fr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Apprenez comment appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail à l aide de l API Aspose.Cells for .NET.
keywords: Appliquer un sous total, ajouter un sous total, changer la direction des lignes de synthèse du contour en dessous du détail, changer la direction des colonnes de synthèse du contour à droite du détail, créer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
---

{{% alert color="primary" %}}

Cet article expliquera comment appliquer un sous-total aux données et changer la direction des lignes de synthèse du contour en dessous du détail.

Vous pouvez appliquer un sous-total aux données en utilisant la méthode [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index). Elle prend les paramètres suivants.

- **CellArea** - la plage sur laquelle appliquer le sous-total
- **GroupBy** - le champ à regrouper, en tant que décalage entier indexé à partir de zéro
- **Function** - la fonction de sous-total
- **TotalList** - un tableau de décalages de champ indexés à partir de zéro, indiquant les champs auxquels les sous-totaux sont ajoutés
- **Replace** - Indique s'il faut remplacer les sous-totaux actuels
- **SautsDePage** - Indique s'il faut ajouter un saut de page entre les groupes
- **RésuméSousDonnées** - Indique s'il faut ajouter un résumé sous les données.

De plus, vous pouvez contrôler la direction des lignes de résumé avec détail **ci-dessous** comme indiqué dans la capture d'écran suivante en utilisant la propriété Worksheet.Outline.SummaryRowBelow. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant **Données > Plan > Paramètres**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Images des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous, qui contient des données dans les colonnes A et B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code d'exemple. Comme vous pouvez le constater, un sous-total a été appliqué à la plage A2:B11 et la direction de la synthèse est les lignes de résumé ci-dessous le détail.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Code C# pour appliquer un sous-total et changer la direction des lignes de synthèse

Voici le code d'exemple pour obtenir le résultat tel que montré ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
