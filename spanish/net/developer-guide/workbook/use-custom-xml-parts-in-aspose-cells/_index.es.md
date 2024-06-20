---
title: Usar Partes XML Personalizadas en Aspose.Cells
type: docs
weight: 390
url: /es/net/use-custom-xml-parts-in-aspose-cells/
---

## Usando Partes XML Personalizadas en Aspose.Cells

Las Partes XML Personalizadas son los datos XML que son almacenados por diferentes aplicaciones como SharePoint, etc. dentro del archivo de Excel. Estos datos son consumidos por diferentes aplicaciones que los necesitan. Microsoft Excel no hace uso de estos datos, por lo que no hay una interfaz gráfica para agregarlos. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y luego abriéndolos con **WinZip**. También puedes abrir el archivo ZIP usando cualquier utilidad de compresión de Windows de terceros como WinRAR o WinZip, etc. Los datos están presentes dentro de la carpeta **customXml**.

Puedes agregar partes XML personalizadas usando Aspose.Cells a través del método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index).

El siguiente código de muestra hace uso del método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) y agrega el **Catálogo de Libros XML** y su nombre es **Librería**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el Catálogo de Libros XML se agrega dentro del nodo Librería que es el nombre de esta propiedad.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Código C# para usar partes XML personalizadas

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## Artículo Relacionado

- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/net/adding-custom-properties-visible-inside-document-information-panel/)
