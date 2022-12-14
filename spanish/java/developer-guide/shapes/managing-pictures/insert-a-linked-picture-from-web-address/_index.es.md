---
title: Insertar una imagen vinculada desde una dirección web
type: docs
weight: 50
url: /es/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

A veces es necesario insertar una imagen de la web (http://) en una hoja de trabajo. Para hacerlo, especifique la URL de la imagen y la imagen se descargará cada vez que se abra la hoja de cálculo en Microsoft Excel. La imagen no está incrustada físicamente en el documento de Excel, sino que apunta a un recurso web.

{{% /alert %}}

## **Insertar una imagen vinculada desde una dirección web**

### **Usando Microsoft Excel**

En Microsoft Excel (por ejemplo 2007):

1.  Haga clic en el**Insertar** menú y seleccione**Imagen**.

![todo:imagen_alternativa_texto](insert-a-linked-picture-from-web-address_1.png)

1.  Especifique la dirección web de la imagen en el cuadro de diálogo Insertar imagen.

![todo:imagen_alternativa_texto](insert-a-linked-picture-from-web-address_2.png)

Se inserta la imagen.

![todo:imagen_alternativa_texto](insert-a-linked-picture-from-web-address_3.png)

### **Usando Aspose.Cells for Java**

 Aspose.Cells for Java admite agregar una imagen vinculada utilizando el método[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 El método devuelve un[**Imagen**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objeto.

El siguiente ejemplo muestra cómo agregar una imagen vinculada desde una dirección web a una hoja de trabajo.

Después de ejecutar el código, el archivo de Excel generado contiene una imagen vinculada en la primera hoja de trabajo.

**El archivo de salida** 

![todo:imagen_alternativa_texto](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
