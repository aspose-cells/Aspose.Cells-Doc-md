---
title: Buscar o buscar datos
type: docs
weight: 50
url: /es/net/find-or-search-data/
description: Aprenda a buscar celdas en una hoja de trabajo que contenga datos específicos a través de Aspose.Cells for .NET API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios buscar celdas en una hoja de cálculo que contiene datos específicos.

{{% /alert %}}

##  **Hallazgo Cells que contiene datos especificados**

###  **Usando Microsoft Excel**

 Microsoft Excel permite a los usuarios buscar celdas en una hoja de cálculo que contiene datos específicos. Si seleccionas**Editar** desde el**Encontrar** menú en Microsoft Excel, verá un cuadro de diálogo donde puede especificar el valor de búsqueda.

Aquí buscamos el valor "Naranjas". Aspose.Cells también permite a los desarrolladores buscar celdas en la hoja de trabajo que contengan valores específicos.

###  **Usando Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo Excel Microsoft. El[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de cálculo del archivo Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. El[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección que representa todas las celdas de la hoja de trabajo. El[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)La colección proporciona varios métodos para buscar celdas en una hoja de trabajo que contiene datos especificados por el usuario. Algunos de estos métodos se analizan a continuación con más detalle.

{{% alert color="primary" %}}

Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados para buscar.

{{% /alert %}}

##  **Encontrar Cells que contiene una fórmula**

 Los desarrolladores pueden encontrar una fórmula específica en la hoja de trabajo llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método. Normalmente, el[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)El método acepta tres parámetros:

- **Objeto:**El objeto a buscar. El tipo debe ser int,double,DateTime,string,bool.
- **Celda anterior:**Celda anterior con el mismo objeto. Este parámetro se puede establecer en nulo si se busca desde el principio.
- FindOptions: Opciones para encontrar el objeto requerido.

Los siguientes ejemplos utilizan datos de hojas de trabajo para practicar métodos de búsqueda:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

##  **Encontrar datos o fórmulas usando FindOptions**

 Es posible encontrar valores específicos utilizando el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método con varios[**Buscar opciones**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Normalmente, el[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)El método acepta los siguientes parámetros:

- *Valor de búsqueda**, el dato o valor a buscar.
- *Celda anterior**, la última celda que contenía el mismo valor. Este parámetro se puede establecer en nulo cuando se busca desde el principio.
- *Buscar opciones**, las opciones de búsqueda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

##  **Encontrar Cells que contiene un valor o número de cadena especificado**

 Es posible encontrar valores de cadena específicos llamando al mismo[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método encontrado en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección con varios[**Buscar opciones**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Especifica el[**BuscarOpciones.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) y[**BuscarOpciones.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype) propiedades. El siguiente código de ejemplo ilustra cómo utilizar estas propiedades para buscar celdas con varios números de cadenas en el**comienzo** o en el**centro** o en el**fin** de la cadena de la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

##  **Temas avanzados**
- [Encuentre Cells con estilo específico](/cells/es/net/find-cells-with-specific-style/)
- [Encuentre si el valor de la celda comienza con comillas simples](/cells/es/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Buscar datos utilizando valores originales](/cells/es/net/search-data-using-original-values/)
