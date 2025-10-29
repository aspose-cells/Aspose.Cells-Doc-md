---
title: Données dans une forme non primitive
type: docs
weight: 300
url: /fr/python-net/data-in-non-primitive-shape/
description: Cet article montre des données dans une forme non primitive à travers l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Données dans une forme non primitive en Python, Comment accéder aux données d une forme non primitive en Python.
---

## **Accès aux données d'une forme non primitive**

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.

## **Une forme non primitive**

Dans Aspose.Cells pour Python via .NET, les formes non primitives se voient attribuer le type [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). Vous pouvez vérifier leur type en utilisant la propriété [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type).

Accédez aux données de la forme en utilisant la propriété [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). Il renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) qui contient une liste de tous les segments qui contiennent à leur tour les points de chaque segment.

|**Montre un exemple d'une forme non primitive**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
