---
title: SpreadsheetML - XLSX, XML
type: docs
weight: 10
url: /es/net/spreadsheetml-xlsx-xml/
---

## **Acerca de SpreadsheetML**
SpreadsheetML es el nombre de una familia de formatos basados en XML para documentos de hojas de cálculo. Hay varias versiones de SpreadsheetML:

1. La versión 2003 de SpreadsheetML se introdujo en Microsoft Word 2003. SpreadsheetML fue un paso significativo de Microsoft hacia la apertura del formato de documento.
1. [Office Open XML](https://en.wikipedia.org/wiki/Office_Open_XML) (OOXML) es el nuevo formato basado en XML introducido en las aplicaciones de Microsoft Office 2007. Office Open XML es un formato contenedor para varios lenguajes de marcado basados en XML especializados. La versión 2007 de SpreadsheetML es el lenguaje de marcado utilizado por Microsoft Office Excel 2007 para almacenar sus documentos.
1. Microsoft Excel 2010 almacena documentos en la versión 2010 de SpreadsheetML según lo definido en el estándar actualizado de OOXML.
## **SpreadsheetML en Aspose.Cells**
Existen tres "versiones" de SpreadsheetML disponibles:

|**SpreadsheetML “Versión”**|**Estándar/Especificación Aplicable**|**Compatible en Aspose.Cells for .NET**|
| :- | :- | :- |
|Microsoft Excel 2003|[Microsoft Excel 2003 XML](https://en.wikipedia.org/wiki/Microsoft_Office_XML_formats)|Sí|
|Microsoft Excel 2007|[OOXML ECMA-376](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)|Sí|
|Microsoft Excel 2010|OOXML ISO/IEC DIS 29500|Sí|
|Microsoft Excel 2013|OOXML ISO/IEC DIS 29500|Sí|
Los documentos de OOXML SpreadsheetML más a menudo vienen en archivos XLSX, que son paquetes ZIP. Además de XLSX, Aspose.Cells brinda un amplio soporte para cargar, guardar y convertir documentos de SpreadsheetML. Esta implementación integral es posible porque Aspose.Cells fue diseñado teniendo en cuenta la estructura de los documentos de Microsoft Excel (y se sabe que SpreadsheetML imita la representación interna de los documentos de Microsoft Excel).
### **OOXML es abierto, ¿por qué usar Aspose.Cells?**
Es cierto que la tecnología Office Open XML hace posible construir aplicaciones de procesamiento y generación de documentos utilizando solo las clases XML sin depender de bibliotecas de terceros como Aspose.Cells. Sin embargo, creemos firmemente que sigue siendo muy beneficioso usar Aspose.Cells cuando se trata de documentos OOXML, en lugar de trabajar a través de XML u otras bibliotecas.

La especificación de OOXML tiene varias miles de páginas. Ser abierto y estándar no significa ser simple. Para procesar o generar documentos de OOXML correctamente, uno debe invertir en aprender bien el formato.

Además de hacer que sea más simple procesar y generar documentos válidos correctamente, Aspose.Cells proporciona las siguientes características importantes que no tendría al trabajar con archivos OOXML directamente a través de XML u otras bibliotecas de terceros:

- Conversiones de calidad entre muchos formatos de Excel populares, incluida la conversión a PDF, HTML, TIFF e impresión.
- Capacidad para construir documentos a partir de fragmentos, de uno o varios documentos, mientras se fusionan automáticamente datos mediante formato estilístico, gráficos y gráficos.
- Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable, DataColumn, DataGrid, DataView y DataReader o exportar datos para completar un DataTable o un Array con solo una línea de código.
- Motor de cálculo de fórmulas robusto que admite casi todas las funciones estándar y avanzadas de Microsoft Excel.

Considere el siguiente ejemplo. Algunas celdas contienen el texto “Hola Mundo” en negrita. Ahora imagine que necesita escribir un programa que busque todas las frases “Hola Mundo” en la hoja de cálculo y las reemplace por “Adiós Tierra”.
### **Un fragmento de un Documento de Office Open XML**
**XML**

{{< highlight csharp >}}

 <?xml version="1.0" encoding="UTF-8" standalone="yes" ?>

\- <worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">

  <dimension ref="A1:M184" />

\- <sheetViews>

\- <sheetView tabSelected="1" workbookViewId="0">

  <selection activeCell="H27" sqref="H27" />

  </sheetView>

  </sheetViews>

  <sheetFormatPr defaultRowHeight="15" />

\- <sheetData>

\- <row r="1" spans="1:7">

\- <c r="A1" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="11" spans="1:7">

\- <c r="D11" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="15" spans="1:7">

\- <c r="G15" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="21" spans="2:7">

\- <c r="G21" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="25" spans="2:7">

\- <c r="F25" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="31" spans="2:7">

\- <c r="B31" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="34" spans="6:13">

\- <c r="M34" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="38" spans="6:13">

\- <c r="F38" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="117" spans="8:8">

\- <c r="H117" s="1" t="s">

  <v>0</v>

  </c>

  </row>

\- <row r="184" spans="8:8">

\- <c r="H184" s="1" t="s">

  <v>0</v>

  </c>

  </row>

  </sheetData>

  <pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />

</worksheet>



{{< /highlight >}}


Implementar incluso una operación simple de buscar y reemplazar en un documento de Office Open XML es difícil. Nuestro consejo: recuerde que abierto y estándar no significa simple, y use Aspose.Cells.
{{< app/cells/assistant language="csharp" >}}
