---
title: Créer des plages nommées au niveau du classeur (Global) et de la feuille de calcul
type: docs
weight: 10
url: /fr/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux portées différentes : le classeur (également appelé portée globale) et la feuille de calcul.

- Les plages nommées avec une portée de classeur peuvent être accédées à partir de n'importe quelle feuille de calcul au sein de ce classeur en utilisant simplement son nom.
- Les plages nommées avec une portée de feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elle a été créée.

Aspose.Cells fournit la même fonctionnalité que Microsoft Excel pour ajouter des plages nommées au niveau du classeur et de la feuille de calcul. Lors de la création d'une plage nommée au niveau de la feuille de calcul, la référence à la feuille de calcul doit être utilisée dans la plage nommée pour la spécifier comme une plage nommée au niveau de la feuille de calcul.

{{% /alert %}}

Les extraits de code suivants montrent comment créer des plages nommées au niveau du classeur et de la feuille de calcul en utilisant la classe [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range).

## **Ajout d'une plage nommée avec une portée de classeur**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Ajout d'une plage nommée avec une portée de feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
