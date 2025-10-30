---
title: Detectar tipo de hipervínculo
type: docs
weight: 160
url: /es/python-net/detect-hyperlink-type/
description: Aprende cómo detectar el tipo de hipervínculo a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Detectar el tipo de hipervínculo en Python, Detectar el tipo de hipervínculo en Python, Obtener el tipo de hipervínculo en Python.
---

## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externos, de referencia a celdas, de ruta de archivo, etc. Aspose.Cells para Python via .NET admite la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos están representados por la enumeración [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). La enumeración [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype) tiene los siguientes miembros.

- EXTERNO: Enlace externo
- RUTA_ARCHIVO: Ruta local y completa de archivos o carpetas.
- EMAIL: Correo electrónico
- REFERENCIA_CELDA: Enlace a celda o rango nombrado.

Para verificar el tipo de hipervínculo, la clase [**Hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink) proporciona una propiedad [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) con un tipo de retorno de [**TargetModeType**](https://reference.aspose.com/cells/python-net/aspose.cells/targetmodetype). El siguiente fragmento de código demuestra el uso de la propiedad [**link_type**](https://reference.aspose.com/cells/python-net/aspose.cells/hyperlink/link_type/) utilizando este [archivo de Excel fuente](94896195.xlsx).

### Código Fuente

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DetectLinkTypes-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
