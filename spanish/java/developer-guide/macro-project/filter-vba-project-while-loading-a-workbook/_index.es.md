---
title: Filtrar proyecto VBA al cargar un libro de trabajo
type: docs
weight: 70
url: /es/java/filter-vba-project-while-loading-a-workbook/
---

## **Escenarios de uso posibles**
Algunos archivos .xlsm/.xslb tienen una cantidad extremadamente grande de macros (o macros muy, muy largas). Aspose.Cells cargará incondicionalmente estos datos (meta) al abrir dichos libros. Es posible que necesite controlar esto a través de LoadDataFilterOptions, cuando realmente solo necesita extraer nombres de hojas para un gran número de libros, evitando así ese contenido innecesario. Este filtro se proporciona al introducir la nueva opción LoadDataFilterOptions.VBA.
## **Código de muestra**
El siguiente código de muestra carga un libro de trabajo de tal manera que solo se filtra la VBA. El archivo de muestra para probar esta característica se puede descargar desde el siguiente enlace:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Establecer las opciones de carga, no queremos cargar la VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Crear objeto de libro de trabajo desde el archivo de Excel de muestra usando las opciones de carga
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Guardar la salida en formato pdf
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
