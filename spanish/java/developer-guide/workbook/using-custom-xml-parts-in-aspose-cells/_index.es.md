---
title: Uso de elementos XML personalizados en Aspose.Cells
type: docs
weight: 570
url: /es/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

 Las partes XML personalizadas son los datos XML almacenados por diferentes aplicaciones como SharePoint, etc. dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no utiliza estos datos, por lo que no hay GUI para agregarlos. Puede ver estos datos cambiando la extensión de**.xlsx** en**.Código Postal** y luego abriéndolo usando**WinRAR** . Los datos están presentes dentro del**customXml** carpeta como se muestra en esta imagen.

![todo:imagen_alternativa_texto](using-custom-xml-parts-in-aspose-cells_1.png)

 Puede agregar partes XML personalizadas usando Aspose.Cells a través del[Libro de trabajo.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)) método.

{{% /alert %}} 
## **Uso de piezas Xml personalizadas en Aspose.Cells**
 El siguiente código de ejemplo hace uso de[Libro de trabajo.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) método y agrega el**Catálogo de libros Xml** y su nombre es**Librería**La siguiente imagen muestra el resultado de este código. Como puede ver, se agrega Book Catalog Xml dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:imagen_alternativa_texto](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Artículo relacionado**
{{% alert color="primary" %}} 

- [Adición de propiedades personalizadas visibles dentro del panel de información del documento](/cells/es/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
