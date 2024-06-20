---
title: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/net/detect-hyperlink-type/
description: Aprenda a detectar el tipo de hipervínculo a través de la API Aspose.Cells for .NET.
keywords: Detectar el tipo de hipervínculo, Obtener el tipo de hipervínculo
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externos, referencias de celda, rutas de archivo, etc. Aspose.Cells admite la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos están representados por la enumeración [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). La enumeración [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype) tiene los siguientes miembros.

- Externo: Enlace externo
- RutaArchivo: Ruta local y completa a archivos/carpetas.
- CorreoElectrónico: Correo electrónico
- ReferenciaCelda: Enlace a celda o rango nombrado.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink) proporciona una propiedad [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) con un tipo de retorno de [**TargetModeType**](https://reference.aspose.com/cells/net/aspose.cells/targetmodetype). El siguiente fragmento de código demuestra el uso de la propiedad [**LinkType**](https://reference.aspose.com/cells/net/aspose.cells/hyperlink/properties/linktype) utilizando este [archivo de Excel fuente](94896195.xlsx).

### Código Fuente

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-DetectLinkTypes-1.cs" >}}

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
