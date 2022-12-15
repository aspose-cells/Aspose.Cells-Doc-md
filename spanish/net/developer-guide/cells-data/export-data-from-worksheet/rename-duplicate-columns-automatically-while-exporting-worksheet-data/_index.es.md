---
title: Cambie el nombre de las columnas duplicadas automáticamente al exportar datos de la hoja de trabajo
type: docs
weight: 250
url: /es/net/rename-duplicate-columns-automatically-while-exporting-worksheet-data/
---
## **Posibles escenarios de uso**

 veces, el usuario enfrenta un problema de columnas duplicadas al exportar datos de la hoja de trabajo a la tabla de datos. DataTable no puede tener columnas duplicadas, por lo que se debe cambiar el nombre de las columnas duplicadas antes de poder exportar los datos de la hoja de cálculo a la tabla de datos. Aspose.Cells puede cambiar el nombre de las columnas duplicadas automáticamente de acuerdo con la estrategia especificada por usted con[**ExportTableOptions.RenameStrategy**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/renamestrategy) propiedad. si especificas[**RenombrarEstrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy) .Digit, las columnas se renombrarán como columna1, columna2, columna3, etc. y si especifica[**RenombrarEstrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Letter, luego las columnas se renombrarán como columnaA, columnaB, columnaC, etc.

## **Cambie el nombre de las columnas duplicadas automáticamente al exportar datos de la hoja de trabajo**

 El siguiente código de ejemplo agrega algunos datos en las tres primeras columnas de la hoja de trabajo, pero todas las columnas tienen el mismo nombre, es decir*Gente* . Luego exporta los datos de la hoja de trabajo a la tabla de datos especificando[**RenombrarEstrategia**](https://reference.aspose.com/cells/net/aspose.cells/renamestrategy).Estrategia de cartas. Luego imprime los nombres de las columnas de la tabla de datos generada por Aspose.Cells. La siguiente captura de pantalla muestra la tabla de datos con los datos exportados en el visualizador. Como puede ver, las columnas duplicadas se han renombrado como PeopleA, PeopleB, etc.

![todo:imagen_alternativa_texto](rename-duplicate-columns-automatically-while-exporting-worksheet-data_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-RenameDuplicateColumnsAutomaticallyWhileExportingWorksheetData.cs" >}}

## **Salida de consola**

Aquí está la salida de la consola del código de muestra anterior como referencia.

{{< highlight "java" >}}

People

PeopleA

PeopleB

{{< /highlight >}}
