---
title: Manipular Rango Nombrado en un Libro de Trabajo
type: docs
weight: 90
url: /es/cpp/manipulate-named-range-in-a-workbook/
---

## **Escenarios de uso posibles**
Aspose.Cells admite la manipulación de rangos nombrados existentes. Todos los rangos nombrados existentes se pueden acceder desde la colección [Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/). Una vez que acceda al rango nombrado, puede cambiar sus varios métodos, por ejemplo, [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) y [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Manipular Rango con Nombre en un Libro de Trabajo**
El siguiente código de ejemplo lee el primer rango con nombre dentro del [archivo de Excel fuente](23167008.xlsx) e imprime sus propiedades [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) y [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) en la consola. Después de eso, modifica la propiedad `RefersTo` y guarda el [archivo de Excel de salida](23167009.xlsx).
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Salida de la consola**
La siguiente salida en consola imprime los valores de los miembros [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) y [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) del *Rango con Nombre* existente en el código anterior.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
