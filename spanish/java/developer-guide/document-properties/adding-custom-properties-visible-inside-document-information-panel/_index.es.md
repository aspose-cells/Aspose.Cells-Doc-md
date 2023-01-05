---
title: Adición de propiedades personalizadas visibles dentro del panel de información del documento
type: docs
weight: 500
url: /es/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

Aspose.Cells se puede usar para agregar propiedades personalizadas dentro del objeto del libro de trabajo que son visibles dentro del Panel de información del documento. Puede abrir el Panel de información del documento en Microsoft Excel usando los comandos de menú Archivo > Información > Propiedades > Mostrar panel del documento.

 Por favor use[**Libro de trabajo.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) método para agregar una propiedad personalizada que será visible en el Panel de información del documento

{{% /alert %}}

## **Ejemplo**

El siguiente código de ejemplo agrega dos propiedades personalizadas. La primera propiedad no tiene ningún tipo y la segunda propiedad tiene un tipo como DateTime. Una vez, abrirá el archivo de salida de Excel generado por este código, verá estas dos propiedades dentro del Panel de información del documento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **Artículo relacionado**

{{% alert color="primary" %}}

- [Uso de elementos XML personalizados en Aspose.Cells](/cells/es/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
