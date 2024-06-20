---
title: Renombrar columnas duplicadas automáticamente al exportar datos de hoja de cálculo
type: docs
weight: 250
url: /es/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
description: Aprenda cómo renombrar columnas duplicadas automáticamente al exportar datos de hoja de cálculo a través de la API Aspose.Cells for .NET.
keywords: Renombrar columnas duplicadas al exportar datos de hoja de cálculo, renombrar columnas duplicadas automáticamente al exportar datos a DataTable
---

## **Escenarios de uso posibles**

A veces el usuario se enfrenta a un problema de columnas duplicadas al exportar datos de la hoja de cálculo a la tabla de datos. DataTable no puede tener columnas duplicadas, por lo que las columnas duplicadas deben ser renombradas antes de poder exportar los datos de la hoja de cálculo a la tabla de datos. Aspose.Cells puede renombrar automáticamente las columnas duplicadas según la estrategia especificada por usted con la propiedad [**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy). Si especifica [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Digit, las columnas se renombrarán como column1, column2, column3, etc. y si especifica [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, entonces las columnas se renombrarán como columnaA, columnaB, columnaC, etc.

## **Renombrar columnas duplicadas automáticamente al exportar datos de la hoja de cálculo**

El siguiente código de muestra agrega algunos datos en las tres primeras columnas de la hoja de cálculo, pero todas las columnas tienen el mismo nombre, es decir, *People*. Luego exporta los datos de la hoja de cálculo a la tabla de datos especificando la estrategia [**RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter. Luego imprime los nombres de las columnas de la tabla de datos generada por Aspose.Cells. La siguiente captura de pantalla muestra la tabla de datos con los datos exportados en el visualizador. Como puede ver, las columnas duplicadas han sido renombradas a PeopleA, PeopleB, etc.

![todo:image_alt_text](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior como referencia.

{{< highlight java >}}

People

PeopleA

PeopleB

{{< /highlight >}}
