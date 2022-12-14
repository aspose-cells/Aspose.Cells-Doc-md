---
title: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 450
url: /es/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

A veces es necesario insertar una imagen de la web (http://) en una hoja de trabajo. Para hacerlo, especifique la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no está incrustada físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Usando Microsoft Excel**

En Microsoft Excel (por ejemplo 2007):

1.  Haga clic en el**Insertar** menú y seleccione**Imagen**.
1. Especifique la dirección web de la imagen en el cuadro de diálogo Insertar imagen.

## **Usando Aspose.Cells for .NET**

 Aspose.Cells for .NET admite agregar una imagen vinculada usando el[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . El método devuelve un[**Imagen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objeto.

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
