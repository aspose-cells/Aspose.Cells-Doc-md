---
title: Actualiser les valeurs des formes liées
type: docs
weight: 3200
url: /fr/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est liée à une cellule. Dans Microsoft Excel, la modification de la valeur de la cellule liée modifie également la valeur de la forme liée. Cela fonctionne également très bien avec Aspose.Cells si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous souhaitez enregistrer votre classeur au format PDF ou HTML, vous devrez appeler[**Feuille de calcul.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) méthode pour actualiser la valeur de la forme liée.

{{% /alert %}}

## Exemple

 La capture d'écran suivante montre le fichier Excel source utilisé dans l'exemple de code ci-dessous. Il a une image liée liée aux cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells puis appeler[**Feuille de calcul.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)méthode pour actualiser la valeur de l'image et l'enregistrer au format PDF.

![tâche : image_autre_texte](refresh-values-of-linked-shapes_1.jpg)

Vous pouvez télécharger le[fichier Excel source](95584291.xlsx) et le[sortie PDF](95584292.pdf) à partir des liens donnés.

### Code C# pour actualiser les valeurs des formes liées

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
