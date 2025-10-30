---
title: Detectar el tipo de hipervínculo con Golang a través de C++
linktitle: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/go-cpp/detect-hyperlink-type/
description: Aprende cómo detectar el tipo de hiper enlace a través de la API Aspose.Cells for C++.
keywords: Detectar el tipo de hipervínculo, Obtener el tipo de hipervínculo
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externos, referencias de celda, rutas de archivo, etc. Aspose.Cells admite la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos están representados por la enumeración [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/). La enumeración [**TargetModeType**](https://reference.aspose.com/cells/go-cpp/targetmodetype/) tiene los siguientes miembros.

- Externo: Enlace externo
- RutaArchivo: Ruta local y completa a archivos/carpetas.
- CorreoElectrónico: Correo electrónico
- ReferenciaCelda: Enlace a celda o rango nombrado.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/go-cpp/hyperlink/) proporciona una propiedad [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) con un tipo de retorno de [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/). El siguiente fragmento de código demuestra el uso de la propiedad [**LinkType**](https://reference.aspose.com/cells/go-cpp/hyperlink/getlinktype/) utilizando este [archivo de Excel fuente](94896195.xlsx).

### Código Fuente

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType.go" >}}
El siguiente es el resultado generado por el fragmento de código dado anteriormente.

### Salida en Consola
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetectHyperlinkType-1.go" >}}
