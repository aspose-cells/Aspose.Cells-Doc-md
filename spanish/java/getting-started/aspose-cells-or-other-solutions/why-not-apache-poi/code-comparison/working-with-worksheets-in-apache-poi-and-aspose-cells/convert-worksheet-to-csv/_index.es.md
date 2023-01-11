﻿---
title: Convertir hoja de trabajo a CSV
type: docs
weight: 30
url: /es/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - Convertir hoja de trabajo a CSV**
Si los desarrolladores necesitan guardar sus archivos en alguna ubicación de almacenamiento, simplemente pueden especificar el nombre del archivo (con su ruta de almacenamiento completa) y el formato de archivo deseado (usando el**Tipo de formato de archivo**enumeración) mientras llama al**ahorrar**método de**Libro de trabajo**objeto.

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF y XSSF - Convertir hoja de trabajo a CSV**
El siguiente código muestra cómo la hoja de trabajo se puede convertir a CSV usando Apache POI HSSF y XSSF API en comparación con Aspose.Cells Java API.

**Java**

{{< highlight "java" >}}

 /**

\* Un procesador rudimentario XLSX -> CSV modelado en el

\* Programa de muestra POI XLS2CSVmra de Nick Burch de la

\* paquete org.apache.poi.hssf.eventusermodel.examples.

\* A diferencia de la versión HSSF, esta ignora por completo

\* filas faltantes.

\* <p/>

\* Las hojas de datos se leen usando un analizador SAX para mantener la

\* huella de memoria relativamente pequeña, por lo que debería ser

\* capaz de leer libros de trabajo enormes. La tabla de estilos y

\* la tabla de cadenas compartidas debe mantenerse en la memoria. Él

\* se utiliza la clase de tabla de estilos de puntos de interés estándar, pero

La clase \* (solo lectura) se usa para la tabla de cadenas compartida

\* porque el POI SharedStringsTable estándar crece mucho

\* rápidamente con el número de cadenas únicas.

\* <p/>

\* Gracias a Eric Smith por un parche que soluciona un problema

\* activado por celdas con múltiples elementos "t", que es

\* cómo Excel representa diferentes formatos (p. ej., una palabra

\* simple y una palabra en negrita).

\*

\* @autor Chris Lott

*/

public class ApacheXLSX2CSV {