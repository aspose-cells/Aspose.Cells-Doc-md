---
title: Usar partes XML personalizadas en Aspose.Cells con Golang a través de C++
linktitle: Usar partes de XML personalizado
type: docs
weight: 390
url: /es/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aprende cómo usar partes XML personalizadas en archivos de Excel programáticamente con Aspose.Cells con Golang a través de C++
---

## Usando Partes XML Personalizadas en Aspose.Cells

Las partes de XML personalizadas son datos XML almacenados por diferentes aplicaciones como SharePoint dentro de un archivo de Excel. Estos datos son consumidos por varias aplicaciones que lo requieren. Microsoft Excel no utiliza estos datos, por lo que no hay interfaz gráfica para agregarlos. Puedes ver estos datos cambiando la extensión de **.xlsx** a **.zip** y abriéndolos con **WinZip**. También puedes abrir el archivo ZIP usando cualquier utilidad de compresión de Windows de terceros como WinRAR o WinZip. Los datos están presentes dentro de la carpeta **customXml**.

Puedes agregar partes XML personalizadas usando Aspose.Cells a través del método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/).

El siguiente código de ejemplo usa el método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) para agregar el **XML del Catálogo de Libros**, y su nombre es **BookStore**. La siguiente imagen muestra el resultado de este código. Como puedes ver, el XML del Catálogo de Libros se añadió dentro del nodo BookStore, que es el nombre de esta propiedad.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Código C++ para usar partes de XML personalizado

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## Artículo Relacionado

- [Agregar propiedades personalizadas visibles en el panel de información del documento](/cells/es/cpp/adding-custom-properties-visible-inside-document-information-panel/)
