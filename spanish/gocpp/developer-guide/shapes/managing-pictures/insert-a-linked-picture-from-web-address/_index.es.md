---
title: Insertar una Imagen Vinculada desde Dirección Web con Golang a través de C++
linktitle: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 450
url: /es/go-cpp/insert-a-linked-picture-from-web-address/
description: Aprende cómo insertar una imagen vinculada desde una dirección web en una hoja de trabajo usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces necesitas insertar una imagen desde la web (http://) en una hoja de cálculo. Para hacerlo, especifica la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no se incrusta físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Usar Microsoft Excel**

En Microsoft Excel (por ejemplo, 2007):

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.
1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen.

## **Usando Aspose.Cells for C++**

Aspose.Cells for C++ soporta agregar una imagen vinculada usando el método [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de trabajo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
