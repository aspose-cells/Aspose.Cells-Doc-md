---
title: Filtrar el proyecto VBA al cargar un libro de trabajo con Golang mediante C++
linktitle: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 140
url: /es/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Aprenda cómo filtrar proyectos VBA al cargar un libro de Excel usando Aspose.Cells con Golang mediante C++
---

## **Filtrar proyecto VBA al cargar un libro de Excel en C++**

Algunos archivos .xlsm/.xslb contienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos datos (meta) al abrir dichos libros. Es posible que necesite controlar esto mediante [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) cuando solo necesite extraer nombres de hojas para una gran cantidad de libros, omitiendo así contenido no necesario. Este filtro se proporciona mediante la introducción de una nueva opción, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Código de muestra**

El siguiente código de muestra carga un libro de trabajo de manera que solo VBA está filtrado. Se puede descargar un archivo de muestra para probar esta función desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
