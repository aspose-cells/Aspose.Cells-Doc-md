---
title: Données dans une forme non primitive avec Golang via C++
linktitle: Données dans une forme non primitive
type: docs
weight: 300
url: /fr/go-cpp/data-in-non-primitive-shape/
description: Accéder et manipuler les données dans des formes non primitives en utilisant Aspose.Cells avec Golang via C++.
---

## **Accès aux données d'une forme non primitive**

Parfois, vous avez besoin d'accéder aux données d'une forme qui n'est pas intégrée. Les formes intégrées sont appelées formes primitives; celles qui ne le sont pas sont appelées non primitives. Par exemple, vous pouvez définir vos propres formes en utilisant différentes lignes connectées par courbe.

## **Une forme non primitive**

Dans Aspose.Cells, les formes non primitives sont assignées au type [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). Vous pouvez vérifier leur type en utilisant la propriété [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

Accédez aux données de la forme en utilisant la propriété [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). Il renvoie tous les chemins connectés qui composent la forme non primitive. Ces chemins sont du type [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) qui contient une liste de tous les segments qui contiennent à leur tour les points de chaque segment.

|**Montre un exemple d'une forme non primitive**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
