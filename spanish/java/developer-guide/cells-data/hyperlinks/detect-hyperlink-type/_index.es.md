---
title: Detectar tipo de hipervínculo
type: docs
weight: 180
url: /es/java/detect-hyperlink-type/
---
## **Detectar tipo de hipervínculo**

Un archivo de Excel puede tener diferentes tipos de hipervínculos como externo, referencia de celda, ruta de archivo, etc. Aspose.Cells admite la función para detectar el tipo de hipervínculo. Los tipos de hipervínculos están representados por el[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)Enumeración. los[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType)La enumeración tiene los siguientes miembros.

- [**EXTERNO**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EXTERNAL): Enlace externo
- [**RUTA DE ARCHIVO**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#FILE_PATH): Ruta local y completa a archivos\carpetas.
- [**EMAIL**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#EMAIL): Correo electrónico
- [**REFERENCIA_CELULAR**](https://reference.aspose.com/cells/java/com.aspose.cells/targetmodetype#CELL_REFERENCE): Enlace a celda o rango con nombre.

Para comprobar el tipo de hipervínculo, el[**Hipervínculo**](https://reference.aspose.com/cells/java/com.aspose.cells/Hyperlink) la clase proporciona un[**Tipo de vínculo**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType) propiedad con un tipo de retorno de[**TargetModeType**](https://reference.aspose.com/cells/java/com.aspose.cells/TargetModeType). El siguiente fragmento de código demuestra el uso de la[**Tipo de vínculo**](https://reference.aspose.com/cells/java/com.aspose.cells/hyperlink#LinkType)propiedad usando este[archivo fuente excel](LinkTypes.xlsx).

## Código fuente

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-DetectLinkTypes-1.java" >}}

El siguiente es el resultado generado por el fragmento de código dado anteriormente.

## Salida de consola
```
LinkTypes.xlsx: FILE_PATH </br>
C:\Windows\System32\cmd.exe: FILE_PATH </br>
C:\Program Files\Common Files: FILE_PATH </br>
'Test Sheet'!B2: CELL_REFERENCE </br>
FullPathExample: CELL_REFERENCE </br>
https://products.aspose.com/cells/ : EXTERNAL </br>
mailto:test@test.com?subject=TestLink: EMAIL
```
