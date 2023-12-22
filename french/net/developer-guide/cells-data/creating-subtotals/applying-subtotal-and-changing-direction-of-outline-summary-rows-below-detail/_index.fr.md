---
title: Application du sous-total et modification de la direction des lignes récapitulatives du plan sous les détails
type: docs
weight: 100
url: /fr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Découvrez comment appliquer le sous-total et modifier la direction des lignes récapitulatives du plan ci-dessous les détails en utilisant le Aspose.Cells for .NET API.
keywords: Apply subtotal, Add subtotal, change direction of outline summary Rows below Detail, change direction of outline summary Columns to right of Detail, Create subtotal and change direction of outline summary Rows below Detail
---
{{% alert color="primary" %}}

Cet article explique comment appliquer le sous-total aux données et modifier la direction des lignes récapitulatives sous les détails.

 Vous pouvez appliquer un sous-total aux données en utilisant[**Feuille de calcul.Cells.Sous-total()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) méthode. Il prend les paramètres suivants.

- **ZoneCellule** - La plage sur laquelle appliquer le sous-total
- **Par groupe** - Le champ par lequel regrouper, sous forme de décalage entier de base zéro
- **Fonction** - La fonction sous-total.
- **Liste totale** Un tableau de décalages de champs de base zéro, indiquant les champs auxquels les sous-totaux sont ajoutés.
- **Remplacer** - Indique si remplacer les sous-totaux actuels
- **Sauts de page** - Indique si ajouter un saut de page entre les groupes
- **Résumé ci-dessousDonnées** - Indique si vous ajoutez un résumé sous les données.

 Vous pouvez également contrôler la direction du contour**Les lignes récapitulatives ci-dessous détaillent** comme indiqué dans la capture d'écran suivante en utilisant la propriété Worksheet.Outline.SummaryRowBelow. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant**Données > Plan > Paramètres**

![tâche : image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

##  Images des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple de code ci-dessous qui contient des données dans les colonnes A et B.

![tâche : image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par l'exemple de code. Comme vous pouvez le constater, le sous-total a été appliqué à la plage A2:B11 et la direction du contour correspond aux lignes récapitulatives situées sous les détails.

![tâche : image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Code C# pour appliquer le sous-total et modifier la direction des lignes récapitulatives du plan

Voici l'exemple de code pour obtenir le résultat comme indiqué ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
