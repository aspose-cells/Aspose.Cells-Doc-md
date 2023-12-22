---
title: Crear rango con nombre en un libro de trabajo
type: docs
weight: 60
url: /es/cpp/create-named-range-in-a-workbook/
---
##  **Posibles escenarios de uso**
 Aspose.Cells admite la creación de un rango con nombre. Hay diferentes formas de crear un rango con nombre. Una de las formas más sencillas es crear primero[Rango](https://reference.aspose.com/cells/cpp/aspose.cells/range) objeto y luego establezca su nombre usando[Rango.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) método. Puede ver todos los rangos con nombre dentro de su archivo de Excel a través de Microsoft Excel*Administrador de nombres*interfaz.
##  **Crear rango con nombre en un libro de trabajo**
 El siguiente código de muestra explica cómo crear un*Rango con nombre* vía Aspose.Cells. Una vez, el*Rango con nombre* se crea, es visible dentro del[Libro de trabajo.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) recopilación. Por favor vea el[archivo de excel de salida](23167006.xlsx) generado por el código como referencia.
##  **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Salida de consola**
 La siguiente salida de consola imprime los valores de[Obtener texto completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) y[Obtener referencias a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) métodos de lo creado*Rango con nombre*en el código anterior.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
