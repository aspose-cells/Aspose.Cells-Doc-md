---
title: Buscar datos
type: docs
weight: 120
url: /es/java/find-or-search-data/
---

{{% alert color="primary" %}} 

En Microsoft Excel, los usuarios pueden buscar celdas que contienen datos específicos. Por ejemplo, haciendo clic en **Editar** y luego en **Buscar** se abre el cuadro de diálogo de búsqueda. Los usuarios ingresan un valor y hacen clic en **Aceptar** para buscarlo. Excel resalta los campos coincidentes.

**Usar el cuadro de diálogo Buscar para encontrar celdas que contienen un valor específico** 

![todo:image_alt_text](find-or-search-data_1.png)

En este ejemplo, el valor de búsqueda es "Naranjas".

Aspose.Cells permite a los desarrolladores buscar a través de las celdas en una hoja de cálculo para encontrar aquellas que contienen un valor dado.

{{% /alert %}} 
## **Buscar celdas que contengan datos específicos**
Aspose.Cells proporciona una clase, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), que representa un archivo de Excel. La clase [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contiene [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), una colección que permite acceder a cada una de las hojas de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

La clase [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) proporciona [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), una colección que representa todas las celdas en la hoja de cálculo. La colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) proporciona varios métodos para encontrar celdas en una hoja de cálculo que contienen datos especificados por el usuario. Algunos de estos métodos se discuten a continuación con más detalle.

Todos los métodos de búsqueda devuelven las referencias de las celdas que contienen el valor de búsqueda especificado.
## **Buscar que Contienen una Fórmula**
Los desarrolladores pueden buscar una fórmula específica en la hoja de cálculo llamando al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/). Configurando [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) en [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) y pasándolo como parámetro al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells/).

Por lo general, el método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) acepta dos o más parámetros:

- Objeto a buscar: representa un objeto que se necesita encontrar en la hoja de cálculo.
- La celda previa: representa la celda previa con la misma fórmula. Este parámetro puede establecerse en nulo al buscar desde el principio.
- Opciones de búsqueda: representa los criterios de búsqueda. En los ejemplos a continuación, se utiliza la siguiente información de la hoja de cálculo para practicar los métodos de búsqueda:

**Datos de muestra de la hoja de cálculo** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Búsqueda de Cadenas**
Buscar celdas que contengan un valor de cadena es fácil y flexible. Existen diferentes formas de búsqueda, por ejemplo, buscar celdas que contengan cadenas que comiencen con un carácter particular o conjunto de caracteres.
### **Búsqueda de Cadenas que Comienzan con Caracteres Específicos**
Para buscar el primer carácter en una cadena, llama al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), configura [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START-WITH) y pásalo como parámetro al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Búsqueda de Cadenas que Terminan con Caracteres Específicos**
Aspose.Cells también puede encontrar cadenas que terminan con caracteres específicos. Para buscar los últimos caracteres en una cadena, llama al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-) de la colección [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), configura [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END-WITH) y pásalo como parámetro al método [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find-java.lang.Object-com.aspose.cells.Cell-).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Búsqueda con Expresiones Regulares: la Función de RegEx**
Una expresión regular ofrece un medio conciso y flexible de hacer coincidir (especificar y reconocer) cadenas de texto, como caracteres particulares, palabras o patrones.

Por ejemplo, el patrón de expresión regular abc-*~~xyz~~ coincide con las cadenas "abc-123-xyz", "abc-985-xyz" y "abc-pony-xyz". * es un comodín, por lo que el patrón coincide con cualquier cadena que comience con "abc" y termine con "-xyz", independientemente de qué caracteres haya en el medio.

Aspose.Cells le permite buscar con expresiones regulares.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Temas avanzados**
- [Buscar celdas con estilo específico](/cells/es/java/find-cells-with-specific-style/)
- [Buscar Datos usando Valores Originales](/cells/es/java/search-data-using-original-values/)
{{< app/cells/assistant language="java" >}}
