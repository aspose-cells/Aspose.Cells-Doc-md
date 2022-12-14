---
title: Buscar o buscar datos
type: docs
weight: 50
url: /es/net/find-or-search-data/
---
{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contiene datos específicos.

{{% /alert %}}

## **Encontrar Cells que contiene datos especificados**

### **Usando Microsoft Excel**

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contiene datos específicos. Si selecciona**Editar** desde el**Encontrar** menú en Microsoft Excel, verá un cuadro de diálogo donde puede especificar el valor de búsqueda.

Aquí, buscamos el valor "Naranjas". Aspose.Cells también permite a los desarrolladores encontrar celdas en la hoja de trabajo que contienen valores específicos.

### **Usando Aspose.Cells**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona un[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección que representa todas las celdas de la hoja de trabajo. los[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)collection proporciona varios métodos para encontrar celdas en una hoja de cálculo que contiene datos especificados por el usuario. Algunos de estos métodos se analizan a continuación con más detalle.

{{% alert color="primary" %}}

Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados para buscar.

{{% /alert %}}

## **Encontrar Cells que contiene una fórmula**

 Los desarrolladores pueden encontrar una fórmula específica en la hoja de trabajo llamando al[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método. Típicamente, el[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)El método acepta tres parámetros:

- **Objeto:**El objeto a buscar. El tipo debe ser int,double,DateTime,string,bool.
- **Celda anterior:**Celda anterior con el mismo objeto. Este parámetro se puede establecer en nulo si se busca desde el principio.
- FindOptions: Opciones para encontrar el objeto requerido.

Los siguientes ejemplos usan datos de hojas de trabajo para practicar métodos de búsqueda:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingFormula-1.cs" >}}

## **Búsqueda de datos o fórmulas mediante FindOptions**

 Es posible encontrar valores especificados usando el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método con varios[**BuscarOpciones**](https://reference.aspose.com/cells/net/aspose.cells/findoptions) . Típicamente, el[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index)método acepta los siguientes parámetros:

- **Valor de búsqueda**, el dato o valor a buscar.
- **celda anterior**, la última celda que contenía el mismo valor. Este parámetro se puede establecer en nulo cuando se busca desde el principio.
- **Buscar opciones**, las opciones de búsqueda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingDataOrFormulasUsingFindOptions-1.cs" >}}

## **Encontrar Cells que contiene un valor o número de cadena especificado**

 Es posible encontrar valores de cadena especificados llamando al mismo[**Encontrar**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/find/index) método que se encuentra en el[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) colección con varios[**BuscarOpciones**](https://reference.aspose.com/cells/net/aspose.cells/findoptions).

 Especifica el[**FindOptions.LookInType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookintype) y[**FindOptions.LookAtType**](https://reference.aspose.com/cells/net/aspose.cells/findoptions/properties/lookattype)propiedades. El siguiente código de ejemplo ilustra cómo usar estas propiedades para encontrar celdas con varios números de cadenas al mismo tiempo.**comienzo** o en el**centro** o en el**final** de la cadena de la celda.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-Find-FindingCellsContainingStringValueOrNumber-1.cs" >}}

## **Temas avanzados**
- [Encuentra Cells con estilo específico](/cells/es/net/find-cells-with-specific-style/)
- [Averigüe si el valor de la celda comienza con comillas simples](/cells/es/net/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Buscar datos usando valores originales](/cells/es/net/search-data-using-original-values/)
