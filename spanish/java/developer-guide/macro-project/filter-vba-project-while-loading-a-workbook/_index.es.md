---
title: Filtre el proyecto VBA mientras carga un libro de trabajo
type: docs
weight: 70
url: /es/java/filter-vba-project-while-loading-a-workbook/
---
## **Posibles escenarios de uso**
Algunos archivos .xlsm/.xslb tienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos (meta) datos al abrir dichos libros de trabajo. Es posible que deba controlar esto a través de LoadDataFilterOptions, cuando realmente solo necesita extraer los nombres de las hojas para una gran cantidad de libros de trabajo, por lo que se salta el contenido innecesario. Este filtro se proporciona mediante la introducción de la nueva opción LoadDataFilterOptions.VBA.
## **Código de muestra**
El siguiente código de ejemplo carga un libro de trabajo de modo que solo se filtra VBA. El archivo de muestra para probar esta función se puede descargar desde el siguiente enlace:

[muestraMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Establecer las opciones de carga, no queremos cargar VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(nuevo LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Cree un objeto de libro de trabajo a partir de un archivo de Excel de muestra usando las opciones de carga
Libro de trabajo book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Guardar la salida en formato pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
