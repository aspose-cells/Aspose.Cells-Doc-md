---
title: Données sous forme non primitive
type: docs
weight: 500
url: /fr/java/data-in-non-primitive-shape/
---
## **Accès aux données de forme non primitive**

Parfois, vous devez accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives ; ceux qui ne le sont pas sont appelés non primitifs. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par des courbes.

## **Une forme non primitive**

Dans Aspose.Cells, les formes non primitives sont affectées du type[**Type de forme automatique.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . Vous pouvez vérifier leur type à l'aide de la[**Forme.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)méthode.

 Accédez aux données de forme à l'aide de la[**Forme.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)méthode. Il renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type ShapePath qui contient une liste de tous les segments qui à leur tour contiennent les points de chaque segment.

L'extrait de code suivant illustre l'utilisation de[**Forme.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)méthode pour accéder aux informations de chemin de forme non primitive.

**Montre un exemple de forme non primitive** 

![tâche : image_autre_texte](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
