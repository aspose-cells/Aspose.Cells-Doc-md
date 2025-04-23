---
title: Desactivar la Exportación de Scripts de Marco y Propiedades del Documento
type: docs
weight: 410
url: /es/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells exporta scripts de marco y propiedades del documento al convertir un libro de trabajo en HTML. La versión 8.6.0 de Aspose.Cells for Java introduce una opción que le permite desactivar opcionalmente la exportación de scripts de marco y propiedades del documento. Utilice la propiedad [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) para deshabilitar la exportación.

{{% /alert %}} 
## **Desactivar la exportación de scripts de marco y propiedades del documento**
El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

Aquí hay un código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
{{< app/cells/assistant language="java" >}}
