---
title: Appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
type: docs
weight: 100
url: /fr/java/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
---

{{% alert color="primary" %}}

Cet article expliquera comment appliquer un sous-total aux données et changer la direction des lignes de synthèse du contour en dessous du détail.

Vous pouvez appliquer un sous-total aux données en utilisant la méthode [**Worksheet.Cells.subtotal()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#subtotal(com.aspose.cells.CellArea,%20int,%20int,%20int[])). Elle prend les paramètres suivants.

- **CellArea** - la plage sur laquelle appliquer le sous-total
- **GroupBy** - le champ à regrouper, en tant que décalage entier indexé à partir de zéro
- **Function** - la fonction de sous-total
- **TotalList** - un tableau de décalages de champ indexés à partir de zéro, indiquant les champs auxquels les sous-totaux sont ajoutés
- **Replace** - Indique s'il faut remplacer les sous-totaux actuels
- **Sauts de page** - Indique s'il faut ajouter un saut de page entre les groupes
- **RésuméSousDonnées** - Indique s'il faut ajouter un résumé sous les données.

De plus, vous pouvez contrôler la direction des **lignes de résumé sous les détails** comme indiqué dans la capture d'écran suivante en utilisant la propriété [**Worksheet.getOutline().SummaryRowBelow**](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow). Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant **Données > Contour > Paramètres**

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Exemple

### Captures d'écran comparant les fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous, qui contient des données dans les colonnes A et B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel généré par le code d'exemple. Comme vous pouvez le constater, un sous-total a été appliqué à la plage **A2:B11** et la direction de la bordure est des lignes de synthèse en dessous des détails.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

### Code Java pour appliquer un sous-total et changer la direction des lignes de synthèse en dessous des détails

Voici le code d'exemple pour obtenir le résultat tel que montré ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ApplyingSubtotal-1.java" >}}
