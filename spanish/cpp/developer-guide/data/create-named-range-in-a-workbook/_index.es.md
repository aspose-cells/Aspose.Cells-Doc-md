---
title: Crear rango con nombre en un libro de trabajo
type: docs
weight: 60
url: /es/cpp/create-named-range-in-a-workbook/
---
## **Posibles escenarios de uso**
 Aspose.Cells admite la creación de un rango con nombre. Hay diferentes formas de crear un rango con nombre. Una de las formas más sencillas es crear primero[IRango](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) objeto y luego establezca su nombre usando[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) método. Puede ver todos los rangos con nombre dentro de su archivo de Excel a través de Microsoft Excel*Administrador de nombres*interfaz.
## **Crear rango con nombre en un libro de trabajo**
 El siguiente código de ejemplo explica cómo crear un*Rango con nombre* vía Aspose.Cells. Una vez, el*Rango con nombre* se crea, es visible dentro de la[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) recopilación. Por favor vea el[archivo de salida de Excel](23167006.xlsx) generado por el código para una referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Salida de consola**
 La siguiente salida de la consola imprime los valores de[ObtenerTextoCompleto](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) y `GetRefersTo` métodos del creado*Rango con nombre*en el código anterior.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
