---
title: Gestion des images
type: docs
weight: 10
url: /fr/net/managing-pictures/
---

Aspose.Cells permet aux développeurs d'ajouter des images à des feuilles de calcul en cours d'exécution. De plus, le positionnement de ces images peut être contrôlé en cours d'exécution, ce qui est discuté plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Il suffit de quelques lignes de code :
Il suffit d’appeler la méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) de la collection [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (encapsulée dans l’objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). La méthode [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Positionnement des images**

Il existe deux façons possibles de contrôler le positionnement des images à l'aide d'Aspose.Cells :

- Positionnement proportionnel: définir une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement proportionnel : définir une position proportionnelle à la hauteur et à la largeur de la ligne.

### **Positionnement proportionnel**

Les développeurs peuvent positionner les images proportionnellement à la hauteur de la ligne et à la largeur de la colonne en utilisant les propriétés [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) et [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) de l'objet [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Un objet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) peut être obtenu à partir de la collection [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) en passant son indice d'image. Cet exemple place une image dans la cellule F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Positionnement Absolu**

Les développeurs peuvent également positionner les images absolument en utilisant les propriétés [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) et [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) de l'objet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Cet exemple place une image dans la cellule F6, à 60 pixels de la gauche et à 10 pixels du haut de la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Insérer une image basée sur la référence de cellule**

Aspose.Cells vous permet d'afficher le contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications apportées aux données dans cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique.

Ajoutez une image à la feuille de calcul en appelant la méthode [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) de la collection [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Spécifiez la plage de cellules en utilisant l'attribut [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) de l'objet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte de la cellule](/cells/fr/net/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse web](/cells/fr/net/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/net/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="csharp" >}}
