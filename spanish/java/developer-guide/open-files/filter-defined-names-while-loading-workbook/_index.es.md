---
title: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/java/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite filtrar o eliminar nombres definidos presentes en el libro de trabajo. Utilice [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) para cargar los nombres definidos y use ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) para eliminarlos al cargar el libro de trabajo. Tenga en cuenta que si elimina los nombres definidos, las fórmulas dentro del libro pueden romperse.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de muestra carga el archivo de Excel de muestra que contiene una fórmula en la celda C1 que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Dado que estamos utilizando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) para eliminar los nombres definidos al cargar el libro, la fórmula en la celda C1 en el archivo de Excel de salida se rompe y verá *#NAME?* en su lugar. Consulte la captura de pantalla siguiente que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
