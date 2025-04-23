---
title: Eliminar espacios redundantes después de un salto de línea al importar HTML
type: docs
weight: 620
url: /es/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Utilice la propiedad [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) y establezca **true** para eliminar todos los espacios redundantes que vienen después de la etiqueta de salto de línea. De forma predeterminada, esta propiedad es **false** y los espacios redundantes se conservan en los archivos de Excel de salida.

{{% /alert %}} 
## **Efecto de establecer la propiedad HtmlLoadOptions.DeleteRedundantSpaces en falso y verdadero**
La siguiente captura de pantalla muestra el efecto de establecer esta propiedad en **false** y **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Eliminar espacios redundantes después de salto de línea al importar HTML**
El siguiente código de ejemplo muestra el uso de la propiedad [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces). Por favor, establézcalo como **true** o **false** para obtener la salida como se muestra en la captura de pantalla anterior.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
