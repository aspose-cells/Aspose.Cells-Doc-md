---
title: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/nodejs-cpp/detect-hyperlink-type/
description: Aprender cómo detectar el tipo de hipervínculo a través de la API Aspose.Cells for Node.js via C++.
keywords: Detectar tipo de hipervínculo Node.js vía C++, Detectar el tipo de hipervínculo Node.js vía C++, Obtener el tipo de hipervínculo Node.js vía C++
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externo, referencia de celda, ruta de archivo, etc. Aspose.Cells for Node.js via C++ soporta la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos son representados por la [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeración. La [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) Enumeración tiene los siguientes miembros.

- Externo: Enlace externo
- RutaArchivo: Ruta local y completa a archivos/carpetas.
- Email: Correo electrónico
- ReferenciaCelda: Enlace a celda o rango con nombre.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) proporciona un método [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) con un tipo de retorno [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). La siguiente porción de código demuestra el uso del método [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) usando este [archivo fuente de Excel](94896195.xlsx).

### Código Fuente

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


El siguiente es el resultado generado por el fragmento de código dado anteriormente.

### Salida en Consola
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
