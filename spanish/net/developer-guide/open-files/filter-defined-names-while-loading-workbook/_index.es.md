---
title: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/net/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite filtrar o eliminar nombres definidos presentes en el libro de trabajo. Utilice [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) para cargar los nombres definidos y use ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) para eliminarlos al cargar el libro de trabajo. Tenga en cuenta que si elimina los nombres definidos, las fórmulas dentro del libro pueden romperse.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de muestra carga el [archivo de Excel de muestra](61767860.xlsx) que tiene una fórmula en la celda **C1** que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Como estamos usando ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) para eliminar los nombres definidos al cargar el libro de trabajo, la fórmula en la celda C1 en el [archivo de Excel de salida](61767861.xlsx) se rompe y se ve *#NAME?* en su lugar. Consulte la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
