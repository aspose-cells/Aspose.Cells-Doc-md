---
title: Conversión
type: docs
weight: 30
url: /es/net/conversion/
---

Una característica única de Aspose.Cells que proporciona flexibilidad en las conversiones de versiones sin afectar el trabajo.
SaveFormat es una enumeración que puede convertir documentos en las extensiones que se muestran a continuación en la tabla.

| **Nombre de Miembro** | **Valor** | **Descripción** |
| :- | :- | :- |
|CSV |1 | Representa un archivo CSV. |
|Xlsx |6 | Representa un archivo xlsx. |
|Xlsm |7 | Representa un archivo xlsm que habilita macros. |
|Xltx |8 | Representa un archivo xltx. |
|Xltm |9 | Representa un archivo xltm que habilita macros. |
|TabDelimited |11 | Representa un archivo de texto delimitado por tabulaciones. |
|Html |12 | Representa un archivo html. |
|MHtml |17 | Representa un archivo mhtml. |
|ODS |14 | Representa un archivo ods. |
|Excel97To2003 |5 | Representa un archivo xls de Excel97-2003. |
|SpreadsheetML |15 | Representa un archivo xml de Excel 2003.
|Xlsb |16 | Representa un archivo xlsb. |
|Auto |0 | Si se guarda el archivo en el disco, el formato del archivo debe coincidir con la extensión del nombre del archivo. <br> Si se guarda el archivo en el flujo, el formato del archivo es xlsx. |
|Unknown |255 | Representa un formato no reconocido, no se puede guardar. |
|Pdf |13 | Representa un archivo Pdf. |
|XPS |20 | Representa un archivo XPS. |
|TIFF |21 | Representa un archivo TIFF. |
|SVG |22 | Representa un archivo SVG. |
|Dif |30 | Formato de Intercambio de Datos. |
A continuación se muestra un fragmento de código que muestra la conversión de xls a xlsx, también se puede hacer viceversa.

{{< highlight csharp >}}

 Workbook workbook = new Workbook("Sample.xls");

workbook.Save("Converted.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}
## **Descargar Código de Ejemplo**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Conversion%20between%20Excel%20Formats%20%28Aspose.Cells%29.zip)
