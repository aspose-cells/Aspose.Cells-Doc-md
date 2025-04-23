---
title: Données dans une forme non primitive
type: docs
weight: 300
url: /fr/net/data-in-non-primitive-shape/
---

## **Accès aux données d'une forme non primitive**

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.

## **Une forme non primitive**

Dans Aspose.Cells, les formes non primitives sont assignées au type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). Vous pouvez vérifier leur type en utilisant la propriété [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

Accédez aux données de la forme en utilisant la propriété [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). Il renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) qui contient une liste de tous les segments qui contiennent à leur tour les points de chaque segment.

|**Montre un exemple d'une forme non primitive**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
