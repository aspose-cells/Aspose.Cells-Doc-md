---
title: Deshabilitar la exportación de secuencias de comandos de fotogramas y propiedades de documentos
type: docs
weight: 310
url: /es/net/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}}

Aspose.Cells exporta secuencias de comandos de marcos y propiedades de documentos al convertir un libro de trabajo en HTML. La versión 8.6.0 de Aspose.Cells for .NET presenta una opción que le permite deshabilitar opcionalmente la exportación de scripts de marcos y propiedades de documentos. Utilice la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties para deshabilitar la exportación.

{{% /alert %}}

## **Deshabilitar la exportación de secuencias de comandos de fotogramas y propiedades de documentos**

El siguiente código de ejemplo le permite deshabilitar la exportación de secuencias de comandos de marcos y propiedades de documentos. Una vez que convierta un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
