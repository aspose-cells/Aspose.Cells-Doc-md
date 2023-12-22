---
title: Cambie el nombre de las columnas duplicadas automáticamente al exportar datos de la hoja de trabajo
type: docs
weight: 250
url: /es/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aprenda a cambiar el nombre de las columnas duplicadas automáticamente mientras exporta datos de la hoja de trabajo a través de Aspose.Cells for .NET API.
keywords: Rename duplicate columns while exporting worksheet data, Rename duplicate columns automatically while exporting  data to DataTable
---
##  **Posibles escenarios de uso**

 A veces, el usuario enfrenta el problema de columnas duplicadas al exportar datos de la hoja de trabajo a la tabla de datos. DataTable no puede tener columnas duplicadas, por lo que se debe cambiar el nombre de las columnas duplicadas antes de poder exportar los datos de la hoja de cálculo a la tabla de datos. Aspose.Cells puede cambiar el nombre de las columnas duplicadas automáticamente según la estrategia especificada por usted con[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) propiedad. Si especifica[**Cambiar nombre de estrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, las columnas cambiarán de nombre como columna1, columna2, columna3, etc. y si lo especifica[**Cambiar nombre de estrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, luego se cambiará el nombre de las columnas como columnaA, columnaB, columnaC, etc.

##  **Cambie el nombre de las columnas duplicadas automáticamente al exportar datos de la hoja de trabajo**

El siguiente código de muestra agrega algunos datos en las primeras tres columnas de la hoja de trabajo, pero todas las columnas tienen el mismo nombre, es decir, *Personas*. Luego exporta los datos de la hoja de trabajo a la tabla de datos especificando[**Cambiar nombre de estrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Estrategia de letras. Luego imprime los nombres de las columnas de la tabla de datos generada por Aspose.Cells. La siguiente captura de pantalla muestra la tabla de datos con los datos exportados en el visualizador. Como puede ver, las columnas duplicadas han cambiado de nombre a PersonasA, PersonasB, etc.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

##  **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior como referencia.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
