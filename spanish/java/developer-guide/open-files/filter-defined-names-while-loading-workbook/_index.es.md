---
title: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/java/filter-defined-names-while-loading-workbook/
---
## **Posibles escenarios de uso**

Aspose.Cells le permite filtrar o eliminar nombres definidos presentes dentro del libro de trabajo. Por favor use[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)para cargar nombres definidos y usar ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)para eliminarlos mientras se carga el libro de trabajo. Tenga en cuenta que si eliminará los nombres definidos, las fórmulas dentro del libro de trabajo pueden romperse.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](61767873.xlsx)que tiene una fórmula en la celda C1 que contiene los nombres definidos, es decir*=SUMA(MiNombre1, MiNombre2)*. Ya que estamos usando ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)para eliminar los nombres definidos al cargar el libro, la fórmula en la celda C1 en[archivo de salida de Excel](61767872.xlsx)se rompe y ves*#NAME?*en cambio. Consulte la siguiente captura de pantalla que muestra el efecto del código en el archivo de muestra de Excel.

![todo:imagen_alternativa_texto](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
