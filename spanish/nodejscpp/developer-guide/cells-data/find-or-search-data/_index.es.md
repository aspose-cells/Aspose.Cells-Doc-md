---  
title: Buscar datos
type: docs  
weight: 50  
url: /es/nodejs-cpp/find-or-search-data/  
description: Aprende cómo buscar o localizar celdas en una hoja de trabajo que contienen datos específicos mediante la API Aspose.Cells for Node.js via C++.  
keywords: Buscar datos en Node.js vía C++, Buscar datos en Node.js vía C++, Buscar celdas que contienen una fórmula en Node.js vía C++, Buscar celdas que contienen una fórmula en Node.js vía C++, Buscar datos o fórmulas usando FindOptions en Node.js vía C++, Buscar datos o fórmulas usando FindOptions en Node.js vía C++, Buscar o localizar celdas que contienen un valor de cadena o número especificado en Node.js vía C++, Buscar o localizar celdas que contienen datos específicos  
---  

{{% alert color="primary" %}}  
Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contienen datos específicos.  
{{% /alert %}}  

## **Encontrar celdas que contienen datos especificados**  

### **Usar Microsoft Excel**  

Microsoft Excel permite a los usuarios encontrar celdas en una hoja de trabajo que contienen datos específicos. Si seleccionas **Editar** en el menú **Buscar** en Microsoft Excel, verás un cuadro de diálogo donde puedes especificar el valor de búsqueda.  

Aquí, estamos buscando el valor "Naranjas". Aspose.Cells también permite a los desarrolladores encontrar celdas en la hoja de cálculo que contienen valores especificados.  

### **Usando Aspose.Cells for Node.js via C++**  

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contiene una colección [**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) proporciona una colección [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) que representa todas las celdas en la hoja de cálculo. La colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) ofrece varios métodos para buscar celdas en una hoja que contienen datos definidos por el usuario. Algunos de estos métodos se discuten a continuación en más detalle.  

{{% alert color="primary" %}}  
Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen los datos especificados.  
{{% /alert %}}  

## **Buscar celdas que contienen una fórmula**  

Los desarrolladores pueden encontrar una fórmula específica en la hoja llamando al método [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells). Por lo general, el método [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) acepta tres parámetros:  

- **Objeto:** El objeto a buscar. El tipo debe ser int, double, DateTime, string, bool.  
- **Celda anterior:** La celda anterior con el mismo objeto. Este parámetro puede establecerse a null si la búsqueda comienza desde el principio.  
- **FindOptions:** Opciones para encontrar el objeto requerido.  

Los ejemplos a continuación utilizan datos de hoja de cálculo para practicar los métodos de búsqueda:  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainFormula.js" >}}


## **Encontrar datos o fórmulas utilizando FindOptions**  

Es posible encontrar valores especificados usando el método [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-) de la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions). Por lo general, el método [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) acepta los siguientes parámetros:  

- **Valor de búsqueda**, los datos o valores a buscar.  
- **Celda anterior**, la última celda que contenía el mismo valor. Este parámetro puede establecerse en nulo al buscar desde el principio.  
- **Opciones de búsqueda**, las opciones de búsqueda.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindDataUsingFindOptions.js" >}}


## **Encontrar celdas que contengan un valor de cadena o número especificado**  

Es posible encontrar valores de cadena especificados llamando al mismo método [**find**](https://reference.aspose.com/cells/nodejs-cpp/cells/#find-object-cell-findoptions-) que se encuentra en la colección [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) con varios [**FindOptions**](https://reference.aspose.com/cells/nodejs-cpp/findoptions).  

Especifica las propiedades [**FindOptions.setLookInType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookInType-lookintype-) y [**FindOptions.setLookAtType**](https://reference.aspose.com/cells/nodejs-cpp/findoptions/#setLookAtType-lookattype-). El siguiente ejemplo de código ilustra cómo usar estas propiedades para buscar celdas con varias cadenas al **principio**, en el **centro** o al **final** de la cadena de la celda.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-FindCellsContainSpecifyString.js" >}}



## **Temas avanzados**  
- [Encontrar celdas con estilo específico](/cells/es/nodejs-cpp/find-cells-with-specific-style/)  
- [Encontrar si el valor de la celda comienza con una comilla simple](/cells/es/nodejs-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Buscar Datos usando Valores Originales](/cells/es/nodejs-cpp/search-data-using-original-values/)  

