---
title: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 450
url: /es/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A veces necesitas insertar una imagen desde la web (http://) en una hoja de cálculo. Para hacerlo, especifica la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no se incrusta físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Usar Microsoft Excel**

En Microsoft Excel (por ejemplo, 2007):

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.
1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen.

## **Usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET soporta agregar una imagen vinculada usando [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
