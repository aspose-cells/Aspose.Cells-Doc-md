---
title: Données dans une forme non primitive
type: docs
weight: 500
url: /fr/java/data-in-non-primitive-shape/
---

## **Accès aux données d'une forme non primitive**

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.

## **Une forme non primitive**

Dans Aspose.Cells, les formes non primitives sont assignées au type [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE). Vous pouvez vérifier leur type en utilisant la méthode [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

Accédez aux données de forme en utilisant la méthode [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). Cela renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type ShapePath qui contient une liste de tous les segments qui contiennent à leur tour les points de chaque segment.

L'extrait de code suivant illustre l'utilisation de la méthode [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) pour accéder aux informations sur le chemin de la forme non primitive.

**Montre un exemple d'une forme non primitive** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
