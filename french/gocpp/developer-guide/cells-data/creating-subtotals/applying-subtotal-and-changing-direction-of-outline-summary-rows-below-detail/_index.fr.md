---
title: Application des sous totaux et changement de direction des lignes de résumé de contour sous Détail avec Golang via C++
linktitle: Appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
type: docs
weight: 100
url: /fr/go-cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Apprenez comment appliquer le sous total et changer la direction des lignes de résumé de la contours sous le détail en utilisant l API Aspose.Cells for C++.
keywords: Appliquer un sous total, ajouter un sous total, changer la direction des lignes de synthèse du contour en dessous du détail, changer la direction des colonnes de synthèse du contour à droite du détail, créer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
---

{{% alert color="primary" %}}

 Cet article expliquera comment appliquer le Sous-total aux données et changer la direction des lignes de résumé de la contours sous le détail.

Vous pouvez appliquer le Sous-total aux données en utilisant la méthode [**Worksheet.Cells.Subtotal()**](https://reference.aspose.com/cells/go-cpp/cells/subtotal_cellarea_int_consolidationfunction_int32array/). Elle prend les paramètres suivants :

- **CellArea** - la plage sur laquelle appliquer le sous-total
- **GroupBy** - le champ à regrouper, en tant que décalage entier indexé à partir de zéro
- **Function** - la fonction de sous-total
- **TotalList** - un tableau de décalages de champ indexés à partir de zéro, indiquant les champs auxquels les sous-totaux sont ajoutés
- **Remplacer** - Indique si les sous-totaux actuels doivent être remplacés
- **Sauts de page** - Indique si une rupture de page doit être ajoutée entre les groupes
- **Résumé sous les données** - Indique si un résumé doit être ajouté en dessous des données.

De plus, vous pouvez contrôler la direction des lignes de résumé **en dessous du détail** en utilisant la propriété `Worksheet.Outline.SummaryRowBelow`. Vous pouvez ouvrir ce paramètre dans Microsoft Excel via **Données > Plan > Paramètres**.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_1.png)

{{% /alert %}}

## Images des fichiers source et de sortie

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous, qui contient des données dans les colonnes A et B.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code d'exemple. Comme vous pouvez le constater, un sous-total a été appliqué à la plage A2:B11 et la direction de la synthèse est les lignes de résumé ci-dessous le détail.

![todo:image_alt_text](applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail_3.png)

## Code C++ pour appliquer le sous-total et changer la direction des lignes de résumé du contour

Voici le code d'exemple pour obtenir le résultat tel que montré ci-dessus.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyingSubtotalAndChangingDirectionOfOutlineSummaryRowsBelowDetail.go" >}}
