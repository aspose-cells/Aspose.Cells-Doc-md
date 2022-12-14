---
title: Gestion des images
type: docs
weight: 10
url: /fr/net/managing-pictures/
---
Aspose.Cells permet aux développeurs d'ajouter des images aux feuilles de calcul lors de l'exécution. De plus, le positionnement de ces images peut être contrôlé au moment de l'exécution, ce qui est discuté plus en détail dans les sections à venir.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très simple. Cela ne prend que quelques lignes de code :
 Appelez simplement le[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) méthode de la[**Des photos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) collection (encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objet). La[**Ajouter**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)méthode prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne en haut à gauche**, l'indice de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Images de positionnement**

Il existe deux manières possibles de contrôler le positionnement des images à l'aide du Aspose.Cells :

- Positionnement proportionnel : définissez une position proportionnelle à la hauteur et à la largeur de la ligne.
- Positionnement absolu : définissez la position exacte sur la page où l'image sera insérée, par exemple, 40 pixels à gauche et 20 pixels en dessous du bord de la cellule.

### **Positionnement proportionnel**

 Les développeurs peuvent positionner les images proportionnellement à la hauteur des lignes et à la largeur des colonnes à l'aide de l'outil[**SupérieurDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) et[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) propriétés de la[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objet. UN[**Image**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) l'objet peut être obtenu auprès du[**Des photos**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)collection en transmettant son index d'images. Cet exemple place une image dans la cellule F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Positionnement absolu**

 Les développeurs peuvent également positionner les images de manière absolue en utilisant le[**La gauche**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) et[**Haut**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) propriétés de la[**Image**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objet. Cet exemple place une image dans la cellule F6, à 60 pixels de la gauche et 10 pixels du haut de la cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Insertion d'une image basée sur la référence Cell**

Aspose.Cells vous permet d'afficher le contenu d'une cellule de feuille de calcul dans une forme d'image. Vous pouvez lier l'image à la cellule qui contient les données que vous souhaitez afficher. Étant donné que la cellule ou la plage de cellules est liée à l'objet graphique, les modifications que vous apportez aux données de cette cellule ou plage de cellules apparaissent automatiquement dans l'objet graphique.

 Ajoutez une image à la feuille de calcul en appelant le[**Ajouter une image**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) méthode de la[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) collection (encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objet). Spécifiez la plage de cellules à l'aide de la[**Formule**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attribut de la[**Image**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Sujets avancés**
- [Ajouter un ensemble d'icônes conditionnelles avec le texte Cell](/cells/fr/net/add-conditional-icons-set-with-the-cell-text/)
- [Insérer une image liée à partir d'une adresse Web](/cells/fr/net/insert-a-linked-picture-from-web-address/)
- [Insérer une image basée sur la référence Cell](/cells/fr/net/insert-a-picture-based-on-cell-reference/)
- [Charger une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

