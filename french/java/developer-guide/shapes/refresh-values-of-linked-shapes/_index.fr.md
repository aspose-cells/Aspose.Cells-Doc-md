---
title: Actualiser les valeurs des formes liées
type: docs
weight: 3000
url: /fr/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, changer la valeur de la cellule liée change également la valeur de la forme liée. Cela fonctionne également parfaitement avec Aspose.Cells si vous voulez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous voulez enregistrer votre classeur au format PDF ou HTML, alors vous devrez appeler la méthode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) pour actualiser la valeur de la forme liée.

{{% /alert %}}

## Exemple

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous. Il a une image liée **Picture 1** liée à la cellule A1. Nous changerons la valeur de la cellule A1 avec Aspose.Cells et puis appeler la méthode [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) pour actualiser la valeur de **Picture 1** et l'enregistrer au format PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Vous pouvez télécharger le [fichier Excel source](5472956.xlsx) et le [fichier PDF de sortie](5472955.pdf) des liens donnés.

### Code Java pour actualiser les valeurs des formes liées

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
