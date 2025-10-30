---
title: Agregar propiedades personalizadas visibles en el panel de información del documento con Golang a través de C++
linktitle: Agregar Propiedades Personalizadas visibles dentro del Panel de Información del Documento
type: docs
weight: 300
url: /es/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aprenda cómo agregar propiedades personalizadas visibles en el panel de información del documento usando Aspose.Cells con Golang a través de C++
---

## **Agregar propiedades personalizadas visibles dentro del Panel de información del documento**

Aspose.Cells se puede utilizar para agregar propiedades personalizadas dentro del objeto del libro que son visibles dentro del Panel de Información del Documento. Puede abrir el Panel de Información del Documento en Microsoft Excel usando los comandos del menú Archivo > Información > Propiedades > Mostrar panel de documentos.

Utilice el método [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) para agregar una propiedad personalizada que será visible en el Panel de Información del Documento.

El siguiente ejemplo de código añade dos propiedades personalizadas. La primera propiedad no tiene ningún tipo y la segunda tiene un tipo como DateTime. Cuando abras el archivo de Excel generado por este código, verás estas dos propiedades dentro del Panel de Información del Documento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **Artículo Relacionado**

{{% alert color="primary" %}}

- [Usar Partes de XML Personalizadas en Aspose.Cells](/cells/es/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
