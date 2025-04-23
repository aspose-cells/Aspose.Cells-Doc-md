---
title: Supprimer le tableau croisé dynamique d une feuille de calcul
type: docs
weight: 50
url: /fr/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells offre une fonctionnalité pour supprimer une table croisée dynamique d'une feuille de calcul. Vous pouvez supprimer la table croisée dynamique en utilisant l'objet de la table croisée dynamique ou la position de la table croisée dynamique. Veuillez utiliser la méthode [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) pour supprimer la table croisée dynamique à l'aide de l'objet de la table croisée dynamique et la méthode [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) pour supprimer un objet de la table croisée dynamique en utilisant sa position dans la collection de tables croisées dynamiques.

{{% /alert %}}

## **Exemple**

Le code d'exemple suivant supprime deux tables croisées dynamiques de la feuille de calcul. Tout d'abord, il supprime la table croisée dynamique en utilisant la méthode [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) puis il supprime la table croisée dynamique en utilisant la méthode [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
