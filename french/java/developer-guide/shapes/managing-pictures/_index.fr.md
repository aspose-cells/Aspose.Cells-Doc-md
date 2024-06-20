---
title: Gestion des images
type: docs
weight: 10
url: /fr/java/managing-pictures/
---

Aspose.Cells permet aux développeurs d'ajouter des images à des feuilles de calcul en cours d'exécution. De plus, le positionnement de ces images peut être contrôlé en cours d'exécution, ce qui est discuté plus en détail dans les sections suivantes.

Cet article explique comment ajouter des images et comment insérer une image qui montre le contenu de certaines cellules.

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très facile. Cela ne prend que quelques lignes de code.

Il suffit d'appeler la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) de la collection [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). La méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne supérieure gauche**, l'index de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positionnement des images**

Les images peuvent être positionnées à l'aide d'Aspose.Cells comme suit :

- [Positionnement Absolu](/cells/fr/java/managing-pictures/#absolute-positioning).

### **Positionnement Absolu**

Les développeurs peuvent positionner les images de manière absolue en utilisant les méthodes [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) et [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) de l'objet [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Sujets avancés**
- [Insérer une image liée à partir d'une adresse web](/cells/fr/java/insert-a-linked-picture-from-web-address/)
- [Insérer une image en fonction de la référence de la cellule](/cells/fr/java/insert-a-picture-based-on-cell-reference/)
- [Insérer une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
