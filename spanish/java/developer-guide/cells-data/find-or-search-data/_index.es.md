---
title: Buscar o buscar datos
type: docs
weight: 120
url: /es/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 En Microsoft Excel, los usuarios pueden buscar celdas que contengan datos específicos. Por ejemplo, hacer clic en**Editar** y luego**Encontrar** abre el cuadro de diálogo Buscar. Los usuarios ingresan un valor y hacen clic**DE ACUERDO** para buscarlo Excel resalta los campos coincidentes.

**Uso del cuadro de diálogo Buscar para buscar celdas que contengan un valor específico** 

![todo:imagen_alternativa_texto](find-or-search-data_1.png)

En este ejemplo, el valor de búsqueda es "Naranjas".

Aspose.Cells permite a los desarrolladores buscar en las celdas de una hoja de trabajo para encontrar las que contienen un valor determinado.

{{% /alert %}} 
## **Encontrar Cells que contiene datos específicos**
 Aspose.Cells proporciona una clase,[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , que representa un archivo de Excel. Él[Libro de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la clase contiene[Colección de hojas de trabajo](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , una colección que permite acceder a cada una de las hojas de trabajo del archivo de Excel. Una hoja de trabajo está representada por el[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)clase.

 Él[Hoja de cálculo](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) clase proporciona[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , una colección que representa todas las celdas de la hoja de cálculo.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection proporciona varios métodos para buscar celdas en una hoja de trabajo que contienen datos especificados por el usuario. Algunos de estos métodos se analizan a continuación con más detalle.

Todos los métodos de búsqueda devuelven las referencias de celda para cualquier celda que contenga el valor de búsqueda especificado.
## **Encontrar que contiene una fórmula**
 Los desarrolladores pueden encontrar una fórmula específica en la hoja de trabajo llamando al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ) método, configurando el[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) a[LookInType.FÓRMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) pasándolo como parámetro al[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) método.

 Típicamente, el[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) el método acepta dos o más parámetros:

- Objeto a buscar: representa un objeto que se necesita encontrar en la hoja de trabajo.
- El anterior Cell: representa la celda anterior con la misma fórmula. Este parámetro se puede establecer en nulo cuando se busca desde el principio.
- Opciones de búsqueda: representa los criterios de búsqueda. En los ejemplos a continuación, los siguientes datos de la hoja de trabajo se utilizan para practicar la búsqueda de métodos:

**Datos de la hoja de trabajo de muestra** 

![todo:imagen_alternativa_texto](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Buscando cadenas**
La búsqueda de celdas que contienen un valor de cadena es fácil y flexible. Hay diferentes formas de buscar, por ejemplo, busque celdas que contengan cadenas que comiencen con un carácter o conjunto de caracteres en particular.
### **Búsqueda de cadenas que comienzan con caracteres específicos**
 Para buscar el primer carácter de una cadena, llame al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), configure el[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)pasarlo como parámetro al[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Búsqueda de cadenas que terminan con caracteres específicos**
 Aspose.Cells también puede encontrar cadenas que terminan con caracteres específicos. Para buscar los últimos caracteres de una cadena, llame al[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) colección[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), configure el[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) a[MirarTipo.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)pasarlo como parámetro al[encontrar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Búsqueda con expresiones regulares: la función RegEx**
Una expresión regular proporciona un medio flexible y conciso para hacer coincidir (especificar y reconocer) cadenas de texto, como caracteres, palabras o patrones particulares.

Por ejemplo, el patrón de expresión regular abc-* ~~xyz~~ coincide con las cadenas "abc-123-xyz", "abc-985-xyz" y "abc-pony-xyz".* es un comodín, por lo que el patrón coincide con cualquier cadena que comience con "abc" y termine con "-xyz", independientemente de los caracteres que se encuentren en el medio.

Aspose.Cells le permite buscar con expresiones regulares.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Temas avanzados**
- [Encuentra celdas con un estilo específico](/cells/es/java/find-cells-with-specific-style/)
- [Buscar datos usando valores originales](/cells/es/java/search-data-using-original-values/)
