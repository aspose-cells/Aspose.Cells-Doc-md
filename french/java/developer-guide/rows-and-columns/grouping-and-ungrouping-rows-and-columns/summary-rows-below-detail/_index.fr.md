---
title: Application du sous-total et modification de la direction des lignes récapitulatives du plan sous le détail
type: docs
weight: 100
url: /fr/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---
{{% alert color="primary" %}}

Cet article explique comment appliquer le sous-total aux données et changer la direction des lignes de résumé du plan sous le détail.

 Vous pouvez appliquer le sous-total aux données à l'aide de[**Feuille de calcul.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])) méthode. Il prend les paramètres suivants.

- **ZoneCellule** - La plage sur laquelle appliquer le sous-total
- **Par groupe** - Le champ à regrouper, sous la forme d'un décalage d'entier de base zéro
- **Fonction** - La fonction de sous-total.
- **TotalListe** - Un tableau de décalages de champ de base zéro, indiquant les champs auxquels les sous-totaux sont ajoutés.
- **Remplacer** - Indique si remplacer les sous-totaux actuels
- **Sauts de page** - Indique si ajouter un saut de page entre les groupes
- **SummaryBelowData** - Indique si ajouter un résumé sous les données.

 En outre, vous pouvez contrôler la direction du contour**Lignes récapitulatives sous les détails** comme indiqué dans la capture d'écran suivante en utilisant[**Feuille de calcul.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) propriété. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant**Données > Plan > Paramètres**

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Exemple

### Captures d'écran comparant les fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple de code ci-dessous qui contient des données dans les colonnes A et B.

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par l'exemple de code. Comme vous pouvez le voir, le sous-total a été appliqué à la plage**A2:B11** et la direction du contour correspond aux lignes récapitulatives sous les détails.

![tâche : image_autre_texte](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Java code pour appliquer le sous-total et changer la direction des lignes de résumé du plan sous les détails

Voici l'exemple de code pour obtenir la sortie comme indiqué ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
