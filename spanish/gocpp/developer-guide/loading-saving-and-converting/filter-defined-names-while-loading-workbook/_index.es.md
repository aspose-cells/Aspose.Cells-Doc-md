---
title: Filtrar nombres definidos al cargar el libro de trabajo
type: docs
weight: 50
url: /es/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite filtrar o eliminar nombres definidos presentes dentro del libro. Por favor, usa [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) para cargar nombres definidos durante la carga del libro. Ten en cuenta que, si eliminas los nombres definidos, las fórmulas dentro del libro pueden dejar de funcionar.

## **Filtrar nombres definidos al cargar el libro de trabajo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767860.xlsx), que tiene una fórmula en la celda **C1** que contiene los nombres definidos, es decir, *=SUM(MyName1, MyName2)*. Dado que estamos usando ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) para eliminar los nombres definidos durante la carga del libro, la fórmula en la celda C1 del [archivo de Excel de salida](61767861.xlsx) se rompe y muestra *#NAME?*. Por favor, vea la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
