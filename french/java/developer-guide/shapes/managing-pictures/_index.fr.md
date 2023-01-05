---
title: Gestion des images
type: docs
weight: 10
url: /fr/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells permet aux développeurs d'ajouter des images aux feuilles de calcul lors de l'exécution. De plus, le positionnement de ces images peut être contrôlé au moment de l'exécution, ce qui est discuté plus en détail dans les sections à venir.

Aspose.Cells for Java ne prend en charge que les formats d'image : BMP, JPEG, PNG, GIF.

Les index utilisés dans les exemples commencent à 0.

{{% /alert %}}

## **Ajout d'images**

Ajouter des images à une feuille de calcul est très simple. Cela ne prend que quelques lignes de code.

 Appelez simplement le[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) méthode de la[**Des photos**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) collection (encapsulée dans le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objet). Le[**ajouter**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) prend les paramètres suivants :

- **Index de la ligne supérieure gauche**, l'index de la ligne supérieure gauche.
- **Index de la colonne en haut à gauche**, l'indice de la colonne supérieure gauche.
- **Nom du fichier image**, le nom du fichier image, complet avec le chemin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positionnement des images**

Les images peuvent être positionnées en utilisant Aspose.Cells comme suit :

- [Positionnement absolu](/cells/fr/java/managing-pictures/#absolute-positioning).

### **Positionnement absolu**

 Les développeurs peuvent positionner les images de manière absolue en utilisant le[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) et[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) méthodes de la[**Photo**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objet.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Sujets avancés**
- [Insérer une image liée à partir d'une adresse Web](/cells/fr/java/insert-a-linked-picture-from-web-address/)
- [Insérer une image basée sur la référence Cell](/cells/fr/java/insert-a-picture-based-on-cell-reference/)
- [Insérer une image Web à partir d'une URL dans une feuille de calcul Excel](/cells/fr/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
