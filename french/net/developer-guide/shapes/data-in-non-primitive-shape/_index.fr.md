---
title: Données sous forme non primitive
type: docs
weight: 300
url: /fr/net/data-in-non-primitive-shape/
---
## **Accès aux données de forme non primitive**

Parfois, vous devez accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives ; ceux qui ne le sont pas sont appelés non primitifs. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par des courbes.

## **Une forme non primitive**

 Dans Aspose.Cells, les formes non primitives sont affectées du type[**AutoShapeType.NotPrimitiveAutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . Vous pouvez vérifier leur type à l'aide de la[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)propriété.

 Accédez aux données de forme à l'aide de la[**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)propriété. Il renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type[**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)qui contient une liste de tous les segments qui à leur tour contiennent les points de chaque segment.

|**Montre un exemple de forme non primitive**|
|:- |
|![tâche : image_autre_texte](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
