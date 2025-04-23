---
title: Desactivar la Exportación de Scripts de Marco y Propiedades del Documento
type: docs
weight: 310
url: /es/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET exporta scripts de marco y propiedades del documento al convertir un libro en HTML. La versión 8.6.0 de Aspose.Cells para Python via .NET introduce una opción que permite deshabilitar opcionalmente la exportación de scripts de marco y propiedades del documento. Usa la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties para desactivar la exportación.

{{% /alert %}}

## **Desactivar la exportación de scripts de marco y propiedades del documento**

El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
