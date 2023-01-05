---
title: Manipular rango con nombre en un libro de trabajo
type: docs
weight: 90
url: /es/cpp/manipulate-named-range-in-a-workbook/
---
## **Posibles escenarios de uso**
 Aspose.Cells admite la manipulación de rangos con nombre existentes. Se puede acceder a todos los rangos con nombre existentes desde[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) recopilación. Una vez que acceda al rango con nombre, puede cambiar sus diversos métodos, por ejemplo[ObtenerTextoCompleto](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)y[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Manipular rango con nombre en un libro de trabajo**
 El siguiente código de muestra lee el primer rango con nombre dentro del[archivo fuente excel](23167008.xlsx) e imprime su[Texto completo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)y[Se refiere a](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) propiedades en la consola. Después de eso, modifica la propiedad `RefersTo` y guarda el[archivo de salida de Excel](23167009.xlsx).
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Salida de consola**
 La siguiente salida de la consola imprime los valores de[Texto completo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)y[Se refiere a](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) miembros de los existentes*Rango con nombre*en el código anterior.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
