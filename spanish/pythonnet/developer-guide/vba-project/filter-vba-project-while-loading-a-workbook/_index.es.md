---
title: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 140
url: /es/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrar proyecto VBA al cargar un libro de trabajo de Excel en Python**

Algunos archivos .xlsm/.xslb contienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells para Python via .NET cargará incondicionalmente estos datos (meta) al abrir tales libros de trabajo. Puede que necesite controlar esto mediante [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) si solo necesita extraer los nombres de las hojas para una gran cantidad de libros, saltándose dicho contenido no necesario. Este filtro se proporciona introduciendo una nueva opción, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **Código de muestra**

El siguiente código de muestra carga un libro de trabajo de manera que solo VBA está filtrado. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

