---
title: Crear Rango Nombrado en un Libro de Trabajo
type: docs
weight: 60
url: /es/cpp/create-named-range-in-a-workbook/
---

## **Escenarios de uso posibles**
Aspose.Cells admite la creación de un rango nombrado. Hay diferentes formas de crear un rango nombrado. Una de las formas más simples es primero crear un objeto [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) y luego establecer su nombre usando el método [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). Puede ver todos los rangos nombrados dentro de su archivo de Excel a través de la interfaz del *Gestor de Nombres* de Microsoft Excel.
## **Crear Rango Nombrado en un Libro de Trabajo**
El siguiente código de ejemplo explica cómo crear un *Rango Nombrado* a través de Aspose.Cells. Una vez creado el *Rango Nombrado*, es visible dentro de la colección [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames). Por favor vea el archivo de Excel de salida generado por el código para su referencia.
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Salida de la consola**
La siguiente salida de consola imprime los valores de los métodos [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) y [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) del *Rango Nombrado* creado en el código anterior.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
