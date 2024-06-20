---
title: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 140
url: /es/net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrar Proyecto VBA al cargar un libro de Excel en C#**

Algunos archivos .xlsm/.xslb tienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos datos (meta) al abrir este tipo de libros. Es posible que necesite controlar esto a través de [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) cuando realmente solo necesite extraer nombres de hojas para un gran número de libros, evitando este contenido innecesario. Este filtro se proporciona mediante la introducción de una nueva opción, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Código de muestra**

El siguiente código de muestra carga un libro de trabajo de manera que solo VBA está filtrado. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
