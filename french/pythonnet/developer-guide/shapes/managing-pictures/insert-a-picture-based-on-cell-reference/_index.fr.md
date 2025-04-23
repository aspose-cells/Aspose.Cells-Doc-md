---
title: Insérer une image basée sur la référence de la cellule
type: docs
weight: 150
url: /fr/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Parfois, vous avez une image vide et souhaitez afficher des données ou du contenu dans l’image en définissant une référence de cellule dans la barre de formule. Aspose.Cells pour Python via .NET supporte cette fonctionnalité (Microsoft Excel 2010).

{{% /alert %}}

## Insertion d'une image basée sur la référence de la cellule

Aspose.Cells pour Python via .NET supporte l'affichage du contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l’image à la cellule contenant les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l’objet graphique, les modifications que vous apportez aux données de cette cellule ou plage de cellules apparaissent automatiquement dans l’objet graphique. Ajoutez une image à la feuille de calcul en appelant la méthode [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (encapsulée dans l’objet [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Spécifiez la plage de cellules en utilisant l’attribut [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) de l’objet [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

### Exemple de code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
