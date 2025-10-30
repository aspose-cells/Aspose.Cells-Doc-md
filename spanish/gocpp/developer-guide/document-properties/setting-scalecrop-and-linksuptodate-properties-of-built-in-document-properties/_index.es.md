---
title: Configurar las propiedades ScaleCrop y LinksUpToDate de las propiedades incorporadas del documento con Golang a través de C++
linktitle: Establecer propiedades ScaleCrop y LinksUpToDate
type: docs
weight: 320
url: /es/go-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aprende cómo establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
[GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) y [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) son dos propiedades extendidas incorporadas en el formato OpenXml. El propósito de estas propiedades es:

## **1) ScaleCrop**
Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en **TRUE** para habilitar el escalado de la miniatura del documento para la visualización. Establezca este elemento en **FALSE** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajusten a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.

## **2) LinksUpToDate**
Este elemento indica si los hipervínculos en un documento están actualizados. Establezca este elemento en **TRUE** para indicar que los hipervínculos están actualizados. Establezca este elemento en **FALSE** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.

## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Establecer propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas**
El siguiente código de ejemplo establece las propiedades extendidas incorporadas [GetScaleCrop()](https://reference.aspose.com/cells/go-cpp/builtindocumentpropertycollection/getscalecrop/) y [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) del libro de trabajo. Por favor, revisa el archivo de Excel de salida generado con este código, cambia su extensión a .zip, extrae su contenido y visualiza el archivo app.xml como se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingScalecropAndLinksuptodatePropertiesOfBuiltInDocumentProperties.go" >}}
