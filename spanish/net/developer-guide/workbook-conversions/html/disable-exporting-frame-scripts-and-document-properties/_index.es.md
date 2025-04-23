---
title: Desactivar la Exportación de Scripts de Marco y Propiedades del Documento
type: docs
weight: 310
url: /es/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells exporta scripts de marco y propiedades del documento al convertir un libro de trabajo a HTML. La versión 8.6.0 de Aspose.Cells for .NET introduce una opción que te permite desactivar opcionalmente la exportación de scripts de marco y propiedades del documento. Por favor usa la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties para desactivar la exportación.

{{% /alert %}}

## **Desactivar la exportación de scripts de marco y propiedades del documento**

El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
