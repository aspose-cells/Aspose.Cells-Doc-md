---
title: Manipular el rango con nombre en un libro de trabajo
type: docs
weight: 90
url: /es/cpp/manipulate-named-range-in-a-workbook/
---
##  **Posibles escenarios de uso**
 Aspose.Cells admite la manipulación de rangos con nombre existentes. Se puede acceder a todos los rangos con nombre existentes desde[Libro de trabajo.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) recopilación. Una vez que acceda al rango nombrado, puede cambiar sus diversos métodos, por ejemplo[Obtener texto completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)y[Obtener referencias a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Manipular el rango con nombre en un libro de trabajo**
 El siguiente código de muestra lee el primer rango con nombre dentro del[archivo excel fuente](23167008.xlsx) e imprime su[Texto completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)y[Se refiere a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) propiedades en la consola. Después de eso, modifica la propiedad `RefersTo` y guarda el[archivo de excel de salida](23167009.xlsx).
##  **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Salida de consola**
 La siguiente salida de consola imprime los valores de[Texto completo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)y[Se refiere a](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) miembros de la existente*Rango con nombre*en el código anterior.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
