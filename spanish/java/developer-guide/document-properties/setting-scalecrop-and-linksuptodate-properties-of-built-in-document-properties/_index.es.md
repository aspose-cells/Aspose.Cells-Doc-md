---
title: Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado
type: docs
weight: 1050
url: /es/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **Posibles escenarios de uso**
[EscalaCultivo](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) y[Enlaces actualizados](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate)son dos propiedades de documento incorporadas extendidas definidas dentro del formato OpenXml. El propósito de estas propiedades son los siguientes
## **1) Recorte de escala**
 Este elemento indica el modo de visualización de la miniatura del documento. Establezca este elemento en**verdadero**para habilitar la escala de la miniatura del documento a la pantalla. Establezca este elemento en**falso** para habilitar el recorte de la miniatura del documento para mostrar solo las secciones que se ajustan a la pantalla.

Los valores posibles para este elemento están definidos por el tipo de datos booleano W3C XML Schema.
## **2) Enlaces actualizados**
 Este elemento indica si los hipervínculos de un documento están actualizados. Establezca este elemento en**verdadero** para indicar que los hipervínculos están actualizados. Establezca este elemento en**falso**para indicar que los hipervínculos están desactualizados.

Los valores posibles para este elemento están definidos por el tipo de datos booleano W3C XML Schema.
## **Captura de pantalla que muestra estas propiedades dentro del archivo app.xml**
![todo:imagen_alternativa_texto](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **Configuración de las propiedades ScaleCrop y LinksUpToDate de las propiedades del documento integrado**
 El siguiente código de ejemplo establece el[EscalaCultivo](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop)y[Enlaces actualizados](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) propiedades de documento incorporadas extendidas del libro de trabajo. Por favor, checa el[archivo de salida de Excel](5472494.xlsx) generado con este código, cambie su extensión a .zip y extraiga su contenido y vea el aap.xml como se muestra en la captura de pantalla anterior.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
