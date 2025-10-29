---
title: Actualiser les valeurs des formes liées
type: docs
weight: 3200
url: /fr/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Parfois, vous avez une forme liée dans votre fichier Excel qui est reliée à une certaine cellule. Dans Microsoft Excel, changer la valeur de la cellule liée modifie aussi la valeur de la forme liée. Cela fonctionne aussi avec Aspose.Cells pour Python via .NET si vous souhaitez enregistrer votre classeur au format XLS ou XLSX. Cependant, si vous voulez enregistrer votre classeur en format PDF ou HTML, vous devrez appeler la méthode [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) pour rafraîchir la valeur de la forme liée.

{{% /alert %}}

## Exemple

La capture d'écran suivante montre le fichier Excel source utilisé dans le code d'exemple ci-dessous. Il possède une image liée à des cellules A1 à E4. Nous allons changer la valeur de la cellule B4 avec Aspose.Cells pour Python via .NET, puis appeler la méthode [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) pour rafraîchir la valeur de l’image et l’enregistrer au format PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Vous pouvez télécharger le fichier Excel source et le PDF final à partir des liens donnés.

### Code C# pour rafraîchir les valeurs des formes liées

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
