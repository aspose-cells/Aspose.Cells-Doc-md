---
title: Usar elementos XML personalizados en Aspose.Cells
type: docs
weight: 390
url: /es/net/use-custom-xml-parts-in-aspose-cells/
---
## Uso de elementos XML personalizados en Aspose.Cells

Las partes XML personalizadas son los datos XML almacenados por diferentes aplicaciones como SharePoint, etc. dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no utiliza estos datos, por lo que no hay GUI para agregarlos. Puede ver estos datos cambiando la extensión de**.xlsx** en**.Código Postal** y luego abriéndolo usando**WinZip** . También puede abrir el archivo ZIP usando cualquier utilidad zip Windows de tercera parte, como WinRAR o WinZip, etc. Los datos están presentes dentro del**customXml** carpeta.

 Puede agregar partes XML personalizadas usando Aspose.Cells a través del[**Libro de trabajo.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)método.

 El siguiente código de ejemplo hace uso de[**Libro de trabajo.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) método y agrega el**Catálogo de libros XML** y su nombre es**Librería**. La siguiente imagen muestra el resultado de este código. Como puede ver, el XML del catálogo de libros se agrega dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:imagen_alternativa_texto](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:imagen_alternativa_texto](use-custom-xml-parts-in-aspose-cells_2.png)

## C# código para usar partes XML personalizadas

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Artículo relacionado

- [Adición de propiedades personalizadas visibles dentro del panel de información del documento](/cells/es/net/adding-custom-properties-visible-inside-document-information-panel/)
