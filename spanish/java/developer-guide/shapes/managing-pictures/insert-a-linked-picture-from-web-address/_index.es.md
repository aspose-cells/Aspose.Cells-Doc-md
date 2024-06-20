---
title: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 50
url: /es/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

A veces necesitas insertar una imagen desde la web (http://) en una hoja de cálculo. Para hacerlo, especifica la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no se incrusta físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Insertar una imagen vinculada desde una dirección web**

### **Usar Microsoft Excel**

En Microsoft Excel (por ejemplo, 2007):

1. Haz clic en el menú **Insertar** y selecciona **Imagen**.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Especifica la dirección web de la imagen en el cuadro de diálogo Insertar Imagen. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

Se inserta la imagen.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Usando Aspose.Cells for Java**

Aspose.Cells for Java admite agregar una imagen vinculada utilizando el método [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

El método devuelve un objeto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de cálculo.

Después de ejecutar el código, el archivo de Excel generado contiene una imagen vinculada en la primera hoja de cálculo.

**El archivo de salida** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
