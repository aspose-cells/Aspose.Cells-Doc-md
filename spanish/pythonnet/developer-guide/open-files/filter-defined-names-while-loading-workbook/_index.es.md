---
title: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/python-net/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET permite filtrar o eliminar nombres definidos presentes dentro del libro. Usa [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) para cargar nombres definidos y ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) para eliminarlos al cargar el libro. Ten en cuenta que, si eliminas nombres definidos, las fórmulas dentro del libro podrían fallar.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de muestra carga el [archivo de Excel de muestra](61767860.xlsx) que tiene una fórmula en la celda **C1** que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Como estamos usando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) para eliminar los nombres definidos al cargar el libro de trabajo, la fórmula en la celda C1 en el [archivo de Excel de salida](61767861.xlsx) se rompe y se ve *#NAME?* en su lugar. Consulte la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

