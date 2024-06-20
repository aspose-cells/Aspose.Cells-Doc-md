---
title: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 500
url: /es/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cells se puede utilizar para agregar propiedades personalizadas dentro del objeto del libro que son visibles dentro del Panel de Información del Documento. Puede abrir el Panel de Información del Documento en Microsoft Excel usando los comandos del menú Archivo > Información > Propiedades > Mostrar panel de documentos.

Por favor utiliza el método [**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo agrega dos propiedades personalizadas. La primera propiedad es sin ningún tipo y la segunda propiedad tiene un tipo como DateTime. Una vez que abra el archivo de Excel de salida generado por este código, verá estas dos propiedades dentro del Panel de Información del Documento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes XML Personalizadas en Aspose.Cells](/cells/es/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
