---
title: Filtre el proyecto VBA mientras carga un libro de trabajo
type: docs
weight: 140
url: /es/net/filter-vba-project-while-loading-a-workbook/
---
## **Filtre el proyecto VBA mientras carga un libro de Excel en C#**

Algunos archivos .xlsm/.xslb tienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos (meta) datos al abrir dichos libros de trabajo. Sin embargo, es posible que necesite controlar esto.[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) cuando realmente solo necesita extraer los nombres de las hojas para una gran cantidad de libros de trabajo, omitiendo así ese contenido innecesario. Este filtro se proporciona introduciendo una nueva opción,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Código de muestra**

El siguiente código de ejemplo carga un libro de trabajo de modo que solo se filtra VBA. Se puede descargar un archivo de muestra para probar esta característica desde el siguiente enlace:

[muestraMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
