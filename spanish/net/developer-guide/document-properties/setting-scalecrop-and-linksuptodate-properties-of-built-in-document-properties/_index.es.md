---
title: Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado
type: docs
weight: 320
url: /es/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Posibles escenarios de uso**
[EscalaCultivo](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) y[Enlaces actualizados](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)son dos propiedades de documento incorporadas extendidas definidas dentro del formato OpenXml. El propósito de estas propiedades son los siguientes
## **1) Recorte de escala**
 Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en**CIERTO** para habilitar la escala de la miniatura del documento a la pantalla. Establezca este elemento en**FALSO** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajustan a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano W3C XML Schema.
## **2) Enlaces actualizados**
 Este elemento indica si los hipervínculos de un documento están actualizados. Establezca este elemento en**CIERTO** para indicar que los hipervínculos están actualizados. Establezca este elemento en**FALSO** para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano W3C XML Schema.
## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:imagen_alternativa_texto](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado**
 El siguiente código de ejemplo establece el[EscalaCultivo](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop) y[Enlaces actualizados](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate) propiedades de documento incorporadas extendidas del libro de trabajo. Por favor, checa el[archivo de salida de Excel](5115500.xlsx)generado con este código, cambie su extensión a .zip y extraiga su contenido y vea el archivo app.xml como se muestra en la captura de pantalla anterior.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
