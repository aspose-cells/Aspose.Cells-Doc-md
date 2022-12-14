---
title: Conversión
type: docs
weight: 30
url: /es/net/conversion/
---
Aspose.Cells característica única que brinda flexibilidad en las conversiones de versión sin afectar el trabajo.
SaveFormat es una enumeración que puede convertir documentos en las extensiones que se indican a continuación en la tabla.

|**Nombre de miembro** |**Valor** |**Descripción** |
|:- |:- |:- |
| CSV|1 | Representa un archivo CSV.|
| xlsx|6 | Representa un archivo xlsx.|
| xlsm|7 | Representa un archivo xlsm que habilita macros.|
| xltx|8 | Representa un archivo xltx.|
| xltm|9 | Representa un archivo xltm que habilita macros.|
| Delimitado por tabulaciones|11 | Representa un archivo de texto delimitado por tabuladores.|
| html|12 | Representa un archivo html.|
| MHtml|17 | Representa un archivo mhtml.|
| SAO|14 | Representa un archivo ods.|
| Excel97To2003|5 | Representa un archivo xls Excel97-2003.|
| Hoja de cálculoML|15 | Representa un archivo xml de Excel 2003.|
| xlsb|16 | Representa un archivo xlsb.|
| Auto|0 |Si guarda el archivo en el disco, el formato del archivo se corresponde con la extensión del nombre del archivo.<br> Si guarda el archivo en la secuencia, el formato de archivo es xlsx.|
| Desconocido|255 | Representa un formato no reconocido, no se puede guardar.|
| pdf|13 | Representa un archivo PDF.|
| XPS|20 | Representa un archivo XPS.|
| PELEA|21 | Representa un archivo TIFF.|
| SVG|22 | Representa un archivo SVG.|
| diferencia|30 | Formato de intercambio de datos.|
A continuación se muestra un fragmento de código que muestra la conversión de xls a xlsx, también puede hacerlo al revés

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Descargar código de muestra**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
