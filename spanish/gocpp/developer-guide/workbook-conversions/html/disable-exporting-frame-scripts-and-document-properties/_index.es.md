---
title: Desactivar exportación de scripts de marco y propiedades del documento con Golang vía C++
type: docs
weight: 310
url: /es/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Desactivar exportación de scripts de marco y propiedades del documento usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

Aspose.Cells exporta scripts de marco y propiedades de documento al convertir un libro de trabajo a HTML. La versión 8.6.0 de Aspose.Cells for C++ introduce una opción que permite desactivar opcionalmente la exportación de scripts de marco y propiedades de documento. Usa la propiedad HtmlSaveOptions.ExportFrameScriptsAndProperties para desactivar la exportación.

{{% /alert %}}

## **Desactivar la exportación de scripts de marco y propiedades del documento**

El siguiente código de muestra te permite desactivar la exportación de scripts de marco y propiedades del documento. Una vez que conviertas un libro de trabajo a HTML, el archivo de salida no contendrá ningún script de marco ni propiedades del documento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
