---
title: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 450
url: /es/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A veces necesitas insertar una imagen desde la web (http://) en una hoja de cálculo. Para hacerlo, especifica la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no se incrusta físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Usar Microsoft Excel**

En Microsoft Excel (por ejemplo, 2007):

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.
1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen.

## **Usando Aspose.Cells for .NET**

Aspose.Cells for .NET admite agregar una imagen vinculada usando el [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
