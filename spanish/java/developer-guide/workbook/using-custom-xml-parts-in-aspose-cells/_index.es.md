---
title: Usar Partes XML Personalizadas en Aspose.Cells
type: docs
weight: 570
url: /es/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

Las Partes XML Personalizadas son los datos XML que son almacenados por diferentes aplicaciones como SharePoint, etc. dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no hace uso de estos datos, por lo que no hay una GUI para agregarlos. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y luego abriéndolos con **WinRAR**. Los datos están presentes dentro de la carpeta **customXml** como se muestra en esta imagen.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Puedes agregar partes XML personalizadas usando Aspose.Cells a través del método [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-)

{{% /alert %}} 
## **Usar Partes XML Personalizadas en Aspose.Cells**
El siguiente código de ejemplo hace uso del método [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) y agrega el **Catálogo de Libros XML** cuyo nombre es **LibroTienda**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el Catálogo de Libros XML se agrega dentro del nodo LibroTienda, que es el nombre de esta propiedad.

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **Artículo Relacionado**
{{% alert color="primary" %}} 

- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
