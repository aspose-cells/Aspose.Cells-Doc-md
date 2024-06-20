---
title: Establecimiento de las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas
type: docs
weight: 320
url: /es/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Escenarios de uso posibles**
[ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) y [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) son dos propiedades de documento integradas extendidas definidas en el formato OpenXml. El propósito de estas propiedades es el siguiente
## **1) ScaleCrop**
Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en **TRUE** para habilitar el escalado de la miniatura del documento para la visualización. Establezca este elemento en **FALSE** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajusten a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **2) LinksUpToDate**
Este elemento indica si los hipervínculos en un documento están actualizados. Establezca este elemento en **TRUE** para indicar que los hipervínculos están actualizados. Establezca este elemento en **FALSE** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas**
El siguiente código de muestra establece las propiedades de documento integradas [ScaleCrop](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) y [LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) extendidas del libro de trabajo. Consulte el [archivo de Excel de salida](5115500.xlsx) generado con este código, cambie su extensión a .zip y extraiga su contenido y vea el archivo app.xml como se muestra en la captura de pantalla anterior.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
