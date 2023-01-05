---
title: Supprimer le tableau croisé dynamique d'une feuille de calcul
type: docs
weight: 50
url: /fr/java/delete-pivot-table-from-a-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells fournit une fonctionnalité pour supprimer ou supprimer un tableau croisé dynamique d'une feuille de calcul. Vous pouvez supprimer le tableau croisé dynamique à l'aide de l'objet tableau croisé dynamique ou de la position du tableau croisé dynamique. Veuillez utiliser le[**Feuille de calcul.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable) ) méthode pour supprimer le tableau croisé dynamique à l'aide de l'objet tableau croisé dynamique et[**Feuille de calcul.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)méthode pour supprimer un objet de tableau croisé dynamique en utilisant sa position à l'intérieur de la collection de tableaux croisés dynamiques.

{{% /alert %}}

## **Exemple**

 L'exemple de code suivant supprime deux tableaux croisés dynamiques de la feuille de calcul. Tout d'abord, il supprime le tableau croisé dynamique à l'aide de[**Feuille de calcul.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove(com.aspose.cells.PivotTable)) méthode, puis il supprime le tableau croisé dynamique à l'aide[**Feuille de calcul.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt(int)) méthode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
