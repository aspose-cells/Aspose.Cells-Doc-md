---
title: Appliquer un sous total et changer la direction des lignes de synthèse du contour en dessous du détail
type: docs
weight: 100
url: /fr/python-net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/
description: Apprenez comment appliquer un sous total et changer la direction des lignes de synthèse sous le détail en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Appliquer un sous total, Ajouter un sous total, changer la direction des lignes de synthèse sous le détail, changer la direction des colonnes de synthèse sous le détail, Créer un sous total et changer la direction des lignes de synthèse sous le détail
---

{{% alert color="primary" %}}

Cet article expliquera comment appliquer un sous-total aux données et changer la direction des lignes de synthèse du contour en dessous du détail.

Vous pouvez appliquer un sous-total aux données en utilisant la méthode [**Worksheet.cells.subtotal()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/subtotal/#aspose.cells.CellArea-int-aspose.cells.ConsolidationFunction-list-bool-bool-bool). Elle prend les paramètres suivants.

- **ca** - La plage sur laquelle appliquer le sous-total
- **group_by** - Le champ à regrouper, en tant que décalage entier basé sur zéro
- **function** - La fonction de sous-total
- **total_list** - Un tableau de décalages de champ basés sur zéro, indiquant les champs auxquels les sous-totaux sont ajoutés
- **replace** - Indique s'il faut remplacer les sous-totaux actuels
- **page_breaks** - Indique s'il faut ajouter un saut de page entre les groupes
- **summary_below_data** - Indique si ajouter un résumé sous les données.

De plus, vous pouvez contrôler la direction des lignes de résumé avec détail **ci-dessous** comme indiqué dans la capture d'écran suivante en utilisant la propriété Worksheet.Outline.SummaryRowBelow. Vous pouvez ouvrir ce paramètre dans Microsoft Excel en utilisant **Données > Plan > Paramètres**

![todo:image_alt_text](1.png)

{{% /alert %}}

## **Images des fichiers sources et de sortie**

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous, qui contient des données dans les colonnes A et B.

![todo:image_alt_text](2.png)

La capture d'écran suivante montre le fichier Excel de sortie généré par le code d'exemple. Comme vous pouvez le constater, un sous-total a été appliqué à la plage A2:B11 et la direction de la synthèse est les lignes de résumé ci-dessous le détail.

![todo:image_alt_text](3.png)

## **Code Python pour appliquer un sous-total et changer la direction des lignes de résumé de la bordure**

Voici le code d'exemple pour obtenir le résultat tel que montré ci-dessus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyingSubtotalChangeSummaryDirection-1.py" >}}
