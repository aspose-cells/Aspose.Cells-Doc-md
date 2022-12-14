---
title: Créer des plages nommées d'étendue de classeur (global) et de feuille de calcul
type: docs
weight: 10
url: /fr/java/create-workbook-global-and-worksheet-scoped-named-ranges/
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de définir des plages nommées avec deux étendues différentes : classeur (également appelé étendue globale) et feuille de calcul.

- Les plages nommées avec une étendue de classeur sont accessibles à partir de n'importe quelle feuille de calcul de ce classeur en utilisant simplement son nom.
- Les plages nommées étendues à la feuille de calcul sont accessibles avec la référence de la feuille de calcul particulière dans laquelle elles ont été créées.

Aspose.Cells fournit la même fonctionnalité que Microsoft Excel pour l'ajout de plages nommées de classeur et de feuille de calcul. Lors de la création d'une plage nommée de portée de feuille de calcul, la référence de feuille de calcul doit être utilisée dans la plage nommée pour la spécifier en tant que plage nommée de portée de feuille de calcul.

{{% /alert %}}

 Les exemples de code suivants montrent comment créer des plages de noms délimitées par des classeurs et des feuilles de calcul à l'aide de la propriété[**Intervalle**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) classer.

## **Ajout d'une plage nommée avec l'étendue du classeur**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorkbookScope-AddNamedRangeWithWorkbookScope.java" >}}

## **Ajout d'une plage nommée avec l'étendue de la feuille de calcul**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddNamedRangeWithWorksheetScope-AddNamedRangeWithWorkbookScope.java" >}}
