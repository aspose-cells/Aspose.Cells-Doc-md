---
title: Gestion des images
type: docs
weight: 10
url: /fr/python-net/managing-pictures/
---

Aspose.Cells pour Python via .NET permet aux développeurs d'ajouter des images aux feuilles de calcul à l'exécution. De plus, le positionnement de ces images peut être contrôlé en temps réel, ce qui est expliqué plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :
Il suffit d’appeler la méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) de la collection [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (encapsulée dans l’objet [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). La méthode [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Positionnement des images**

Il existe deux méthodes possibles pour contrôler le positionnement des images en utilisant Aspose.Cells pour Python via .NET :

- Positionnement proportionnel: définir une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement proportionnel : définir une position proportionnelle à la hauteur et à la largeur de la ligne.

### **Positionnement proportionnel**

Les développeurs peuvent positionner les images proportionnellement à la hauteur de la ligne et à la largeur de la colonne en utilisant les propriétés [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) et [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) de l'objet [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Un objet [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) peut être obtenu à partir de la collection [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) en passant son indice d'image. Cet exemple place une image dans la cellule F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Positionnement Absolu**

Les développeurs peuvent également positionner les images absolument en utilisant les propriétés [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) et [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) de l'objet [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Cet exemple place une image dans la cellule F6, à 60 pixels de la gauche et à 10 pixels du haut de la cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Insérer une image basée sur la référence de cellule**

Aspose.Cells pour Python via .NET vous permet d'afficher le contenu d'une cellule de la feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule contenant les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, toute modification apportée aux données de cette cellule ou plage de cellules apparaît automatiquement dans l'objet graphique.

Ajoutez une image à la feuille de calcul en appelant la méthode [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) de l'objet [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse web](/cells/fr/python-net/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/python-net/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
