---
title: Actualiser les valeurs des formes liées
type: docs
weight: 3000
url: /fr/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, la modification de la valeur de la cellule liée modifie également la valeur de la forme liée. Cela fonctionne également très bien avec Aspose.Cells si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous souhaitez enregistrer votre classeur au format PDF ou HTML, vous devrez appeler[**Feuille de calcul.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) pour actualiser la valeur de la forme liée.

{{% /alert %}}

## Exemple

 La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple de code ci-dessous. Il a un lien**Image 1** lié à la cellule A1. Nous allons changer la valeur de la cellule A1 avec Aspose.Cells puis appeler[**Feuille de calcul.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) méthode pour actualiser la valeur de**Image 1** et enregistrez-le au format PDF.

![tâche : image_autre_texte](refresh-values-of-linked-shapes_1.png)

Vous pouvez télécharger le[fichier Excel source](5472956.xlsx) et le[sortie PDF](5472955.pdf) à partir des liens donnés.

### Code Java pour actualiser les valeurs des formes liées

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
