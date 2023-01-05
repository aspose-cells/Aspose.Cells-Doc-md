---
title: Application du sous-total et modification de la direction des lignes récapitulatives du plan sous le détail
type: docs
weight: 100
url: /fr/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Cet article explique comment appliquer le sous-total aux données et changer la direction des lignes de résumé du plan sous le détail.

 Vous pouvez appliquer le sous-total aux données à l'aide de[**Feuille de travail.Cells.Sous-total()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) méthode. Il prend les paramètres suivants.

- **ZoneCellule** La plage sur laquelle appliquer le sous-total
- **Par groupe** - Le champ à regrouper, sous la forme d'un décalage d'entier de base zéro
- **Une fonction** - La fonction de sous-total.
- **TotalListe** - Un tableau de décalages de champ de base zéro, indiquant les champs auxquels les sous-totaux sont ajoutés.
- **Remplacer** - Indique si remplacer les sous-totaux actuels
- **Sauts de page** - Indique si ajouter un saut de page entre les groupes
- **SummaryBelowData** - Indique si ajouter un résumé sous les données.

 En outre, vous pouvez contrôler la direction du contour**Lignes récapitulatives sous les détails** comme indiqué dans la capture d'écran suivante à l'aide de la propriété Worksheet.Outline.SummaryRowBelow. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant**Données > Plan > Paramètres**

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Images des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple de code ci-dessous qui contient des données dans les colonnes A et B.

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par l'exemple de code. Comme vous pouvez le constater, le sous-total a été appliqué à la plage A2 : B11 et la direction du contour correspond aux lignes récapitulatives sous les détails.

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Code C# pour appliquer le sous-total et modifier la direction des lignes récapitulatives du plan

Voici l'exemple de code pour obtenir la sortie comme indiqué ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ApplyingSubtotalChangeSummaryDirection-1.cs" >}}
