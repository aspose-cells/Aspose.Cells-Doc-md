---
title: Filtrar objetos al cargar un libro o hoja de trabajo con Golang a través de C++
linktitle: Filtrar objetos al cargar el libro o la hoja de trabajo
type: docs
weight: 330
url: /es/go-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aprenda cómo filtrar objetos como gráficos, formas y formato condicional al cargar libros de Excel o hojas de cálculo usando el Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
Por favor, utilice la propiedad [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) al filtrar datos del libro de trabajo. Pero si desea filtrar datos de hojas de trabajo individuales, entonces deberá anular el método [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). Proporcione un valor apropiado del enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) al crear o trabajar con [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

 El enumerador [LoadDataFilterOptions](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) tiene los siguientes valores posibles.

- Todo
- Configuraciones del libro
- Celda en blanco
- Celda booleana
- Datos de celda
- Error de celda
- Numérico de celda
- Cadena de celda
- Valor de celda
- Chart
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- Hipervínculos
- Área fusionada
- Tabla Dinámica
- Configuración
- Forma
- Datos de Hoja
- Configuraciones de Hoja
- Estructura
- Estilo
- Tabla
- VBA
- MapaXml

## **Objetos de Filtro al cargar el Libro**
El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, revise el [archivo de Excel de ejemplo](5115258.xlsx) utilizado en este código y el [PDF de salida](5115257.pdf) generado por él. Como se puede ver en el PDF de salida, todos los gráficos han sido filtrados fuera del libro.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet.go" >}}
## **Objetos de Filtro al cargar la Hoja de Trabajo**
El siguiente código de ejemplo carga el [archivo de Excel fuente](5115255.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra los gráficos de la hoja de trabajo llamada SinGráficos.
- Filtra las formas de la hoja de trabajo llamada SinFormas.
- Filtra el formato condicional de la hoja de trabajo llamada SinFormatoCondicional.

Una vez que carga el [archivo de Excel fuente](5115255.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas una por una. Aquí están las imágenes de salida para su referencia. Como se puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-1.go" >}}
Así es como se usa la clase CustomLoadFilter según los nombres de las hojas de cálculo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterObjectsWhileLoadingWorkbookOrWorksheet-2.go" >}}
