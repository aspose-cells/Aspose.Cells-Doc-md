---
title: Establecimiento de las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas
type: docs
weight: 1050
url: /es/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Escenarios de uso posibles**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) y [LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) son dos propiedades de documento integradas extendidas definidas dentro del formato OpenXML. El propósito de estas propiedades es el siguiente
## **1) ScaleCrop**
Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en **verdadero** para habilitar el escalado de la miniatura del documento para la visualización. Establezca este elemento en **falso** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que encajan en la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **2) LinksUpToDate**
Este elemento indica si los hipervínculos en un documento están actualizados. Establezca este elemento en **verdadero** para indicar que los hipervínculos están actualizados. Establezca este elemento en **falso** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas**
El siguiente código de ejemplo establece las propiedades de documento integradas extendidas ScaleCrop y LinksUpToDate del libro de trabajo. Por favor, revise el archivo de Excel de salida (5472494.xlsx) generado con este código, cambie su extensión a .zip y extraiga su contenido y vea el aap.xml como se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
