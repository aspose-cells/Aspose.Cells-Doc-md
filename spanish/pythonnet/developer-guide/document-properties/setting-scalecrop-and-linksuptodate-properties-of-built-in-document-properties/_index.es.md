---
title: Establecimiento de las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento integradas
type: docs
weight: 320
url: /es/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **Escenarios de uso posibles**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) y [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) son dos propiedades extendidas incorporadas definidas dentro del formato OpenXml. El propósito de estas propiedades es el siguiente
## **1) ScaleCrop**
Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en **TRUE** para habilitar el escalado de la miniatura del documento para la visualización. Establezca este elemento en **FALSE** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajusten a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **2) LinksUpToDate**
Este elemento indica si los hipervínculos en un documento están actualizados. Establezca este elemento en **TRUE** para indicar que los hipervínculos están actualizados. Establezca este elemento en **FALSE** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano del esquema XML de W3C.
## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas**
El siguiente código de ejemplo establece las propiedades extendidas incorporadas [scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) y [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) del libro. Por favor, revisa el [archivo Excel generado](5115500.xlsx) con este código, cambia su extensión a .zip, extrae su contenido y visualiza el app.xml como se muestra en la captura de pantalla anterior.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
