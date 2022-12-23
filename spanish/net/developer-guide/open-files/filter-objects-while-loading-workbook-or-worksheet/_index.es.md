---
title: Filtrar objetos al cargar el libro de trabajo o la hoja de trabajo
type: docs
weight: 330
url: /es/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Posibles escenarios de uso**
Por favor use[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)propiedad al filtrar datos del libro de trabajo. Pero si desea filtrar datos de hojas de trabajo individuales, tendrá que anular el[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)método. Proporcione el valor apropiado de la[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)enumeración al crear o trabajar con[Cargarfiltro](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 Él[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)enumeración tiene los siguientes valores posibles.

- Todos
- Configuración del libro
- Celda en blanco
- CellBool
- CellData
- error de celda
- CellNumeric
- Cadena de celdas
- valor de celda
- Gráfico
- Formato condicional
- Validación de datos
- Nombres definidos
- Propiedades del documento
- Fórmula
- hipervínculos
- MergedArea
- Tabla dinámica
- Ajustes
- Forma
- SheetData
- Configuración de hoja
- Estructura
- Estilo
- Mesa
- VBA
- XmlMapa
## **Filtrar objetos al cargar el libro de trabajo**
 El siguiente código de ejemplo ilustra cómo filtrar gráficos del libro. Por favor, checa el[ejemplo de archivo de Excel](5115258.xlsx) utilizado en este código y el[salida PDF](5115257.pdf)generada por ella. Como puede ver en el resultado PDF, todos los gráficos se han filtrado del libro de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtrar objetos al cargar la hoja de trabajo**
 El siguiente código de ejemplo carga el[archivo fuente excel](5115255.xlsx) y filtra los siguientes datos de sus hojas de trabajo usando un filtro personalizado.

- Filtra gráficos de la hoja de trabajo denominada NoCharts.
- Filtra las formas de la hoja de trabajo denominada NoShapes.
- Filtra el formato condicional de la hoja de trabajo denominada NoConditionalFormatting.

 Una vez, carga el[archivo fuente excel](5115255.xlsx) con un filtro personalizado, toma las imágenes de todas las hojas de trabajo una por una. Aquí están las imágenes de salida para su referencia. Como puede ver, la primera imagen no tiene gráficos, la segunda imagen no tiene formas y la tercera imagen no tiene formato condicional.

- [NoGráficos.png](5115254.png)
- [Sin Formas.png](5115256.png)
- [Sin formato condicional.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Así es como se usa la clase CustomLoadFilter según los nombres de las hojas de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
