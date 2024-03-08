---
title: Configuración de fórmulas de matriz dinámica
description: Cómo utilizar la biblioteca Aspose.Cells para calcular fórmulas de matriz dinámica en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar el método proporcionado por Aspose.Cells para calcular la fórmula de matriz dinámica y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /es/net/calculation-of-dynamic-array-formulas/
---
##  **¿Qué es la fórmula matricial de Excel?**
En Excel, una fórmula matricial es un tipo especial de fórmula que le permite realizar cálculos en matrices de datos en lugar de celdas individuales. Las fórmulas matriciales se pueden utilizar para realizar cálculos complejos, manipular datos y resolver problemas específicos de manera eficiente. Se ingresan de manera diferente a las fórmulas normales y, a menudo, requieren el uso de Ctrl + Shift + Enter.

A continuación se presentan algunos puntos clave sobre las fórmulas matriciales en Excel:
1. Sintaxis:
<br>
Las fórmulas matriciales se escriben como fórmulas normales, pero implican operaciones con matrices de valores. Están encerrados entre llaves { } para indicar que son fórmulas matriciales. Sin embargo, usted no escribe estas llaves usted mismo; Excel los agrega automáticamente cuando ingresa la fórmula correctamente.
1. Ingresando fórmulas de matriz:
<br>
Para ingresar una fórmula matricial, escriba la fórmula en la barra de fórmulas. En lugar de presionar Enter para finalizar, presione Ctrl + Shift + Enter. Esto le dice a Excel que es una fórmula matricial. Cuando se ingresa correctamente, Excel muestra la fórmula entre llaves en la barra de fórmulas para indicar que es una fórmula matricial.
1. Casos de uso:
<br>
Las fórmulas matrices son útiles para realizar cálculos en varias celdas o rangos simultáneamente. Se pueden utilizar para cálculos matemáticos avanzados, operaciones condicionales, filtrado de datos y más.
1. Beneficios:
<br>
Las fórmulas matriciales le permiten realizar cálculos complejos en una sola fórmula, lo que puede mejorar la eficiencia y simplificar sus hojas de trabajo. Pueden manejar grandes conjuntos de datos y realizar cálculos que de otro modo requerirían múltiples pasos intermedios.
1. Limitaciones:
<br>
Las fórmulas matriciales pueden ser más difíciles de entender y solucionar problemas que las fórmulas normales. Pueden ralentizar el rendimiento de las hojas de cálculo, especialmente si se utilizan de forma intensiva o con grandes conjuntos de datos.
1. Ejemplos:
<br>
 Sumando los valores en un rango:**{=SUM(A1:A5*B1:B5)}**
<br>
 Encontrar el valor máximo en un rango:**{=MÁX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

Recuerde que las fórmulas matriciales deben usarse con prudencia y es importante comprender cómo funcionan antes de implementarlas en sus hojas de trabajo. Pueden ser herramientas poderosas para el análisis y manipulación de datos en Excel.

##  **¿Qué es la fórmula de matriz dinámica de Excel?**
Las fórmulas de matriz dinámica son una nueva característica introducida en Excel 365 y Excel 2021. Le permiten trabajar con matrices de datos de manera más fluida y eficiente en comparación con las fórmulas de matriz tradicionales. Las fórmulas de matriz dinámica distribuyen automáticamente los resultados en las celdas vecinas, lo que elimina la necesidad de Ctrl + Shift + Enter y permite una manipulación más sencilla de los datos.

Puntos clave sobre las fórmulas de matriz dinámica en Excel:
1. Derrame automático:
<br>
Las fórmulas de matriz dinámica distribuyen automáticamente los resultados en celdas adyacentes según el tamaño de los datos de salida. Esto significa que no necesita seleccionar un rango de celdas antes de ingresar la fórmula o usar Ctrl + Shift + Enter para confirmar la fórmula.
1. Entrada única-Cell:
<br>
Las fórmulas de matriz dinámica se ingresan en una sola celda y Excel completa automáticamente las celdas vecinas con los resultados. Esto hace que sea más fácil administrar y comprender las fórmulas, ya que solo necesita ingresar la fórmula una vez.
1. Nuevas funciones:
<br>
Las fórmulas de matriz dinámica introducen nuevas funciones que pueden manejar matrices de forma nativa, como *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** y *RANDARRAY**. Estas funciones pueden devolver múltiples valores o manipular matrices directamente, simplificando cálculos complejos.
1. Manejo de rango flexible:
<br>
Las fórmulas de matriz dinámica ajustan dinámicamente el tamaño del rango derramado en función del tamaño de los datos de entrada o del cálculo realizado. Esta flexibilidad permite un uso más eficiente del espacio de la hoja de cálculo y simplifica la creación de fórmulas.
1. Desempeño mejorado:
<br>
Las fórmulas de matriz dinámica pueden mejorar el rendimiento en comparación con las fórmulas de matriz tradicionales, especialmente cuando se trabaja con grandes conjuntos de datos o cálculos complejos.
1. Compatibilidad:
<br>
Las fórmulas de matriz dinámica están disponibles en Excel 365 y Excel 2021. Es posible que no sean compatibles con versiones anteriores de Excel.
1. Ejemplos de fórmulas de matriz dinámica:
<br>
*FILTRO**: Devuelve una matriz de valores que cumplen con los criterios especificados.
<br>
*ORDENAR**: Ordena los valores en un rango o matriz.
<br>
*ÚNICO**: Devuelve valores únicos de una lista o rango.
<br>
*SECUENCIA**: Genera una secuencia de números o fechas.
<br>
*RANDARRAY**: Genera una matriz de números aleatorios.
<br>
<image src="2.png" width="70%" />
<br>

Las fórmulas de matriz dinámica ofrecen potentes capacidades para la manipulación y el análisis de datos en Excel, lo que facilita el trabajo con matrices de datos y la realización de cálculos complejos de manera eficiente.

##  **¿Cuál es la diferencia entre fórmulas de matriz y fórmulas de matriz dinámicas en Excel?**
En Excel, tanto las fórmulas matriciales como las fórmulas matriciales dinámicas se utilizan para realizar cálculos sobre múltiples valores simultáneamente, pero tienen algunas diferencias en términos de funcionalidad y forma de implementarlas.

###  **Funciones de fórmulas de matriz**
1. Las fórmulas matriciales son fórmulas tradicionales en Excel que pueden realizar cálculos en matrices de datos.
1. Se ingresan presionando Ctrl + Shift + Enter después de escribir la fórmula, lo que le dice a Excel que es una fórmula matricial.
1. Las fórmulas de matriz tienen limitaciones en términos de su capacidad para distribuir resultados en celdas adyacentes. Por lo general, devuelven un 1. único resultado, aunque ese resultado podría ser una matriz de celdas.
1. Existen desde hace mucho tiempo y son compatibles con todas las versiones de Excel.

###  **Funciones de fórmulas de matriz dinámica**
1. Las fórmulas de matriz dinámica son una nueva característica introducida en Excel 365 (suscripción a Office 365) y Excel 2021.
1. Automáticamente distribuyen los resultados en celdas adyacentes según el tamaño de los datos de entrada o el cálculo de la fórmula.
1. Las fórmulas de matriz dinámica no requieren presionar Ctrl + Shift + Enter; simplemente escriba la fórmula en una celda y Excel completará automáticamente las celdas adyacentes con los resultados.
1. Estas fórmulas tienen la capacidad de devolver múltiples resultados (un rango de celdas) directamente sin la necesidad de una fórmula matricial o Ctrl + Shift + Enter.
1. Tienen nuevas funciones como *FILTER**, *SORT**, *UNIQUE**, etc., que pueden manejar matrices de forma nativa y devolver resultados en un formato de matriz dinámica.
En resumen, las fórmulas de matrices dinámicas son una forma más moderna y conveniente de trabajar con matrices en Excel, ya que proporcionan resultados automáticos y simplifican el proceso de trabajo con matrices en comparación con las fórmulas de matrices tradicionales. Sin embargo, sólo están disponibles en las versiones más recientes de Excel que admiten matrices dinámicas.

##  **Cómo configurar y calcular fórmulas de matriz dinámica en Excel**
 La configuración de fórmulas de matriz dinámica en Excel implica el uso de funciones específicas que están diseñadas para trabajar con matrices de datos y permitir que los resultados se extiendan automáticamente a las celdas vecinas.

Aquí hay una guía paso a paso para configurar fórmulas de matriz dinámica:
1. Seleccione el Cell:
<br>
Elija la celda donde desea que aparezcan los resultados de la fórmula de matriz dinámica. Las fórmulas de matriz dinámica distribuyen los resultados en celdas adyacentes, así que asegúrese de que haya suficiente espacio para la salida dividida.
1. Ingrese la fórmula:
<br>
 Escriba la fórmula de matriz dinámica en la barra de fórmulas de la celda seleccionada. Utilice una de las funciones de matriz dinámica disponibles en Excel 365 y Excel 2021, como *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** o *RANDARRAY**.
<br>
Por ejemplo, puede utilizar la función FILTRO para filtrar una lista de datos según criterios específicos: *=FILTRO(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Presione Entrar:
<br>
Después de escribir la fórmula, simplemente presione Enter en su teclado. A diferencia de las fórmulas matriciales tradicionales, no es necesario presionar Ctrl + Shift + Enter.
1. Observe el rango derramado:
<br>
Excel derrama automáticamente los resultados de la fórmula en las celdas vecinas. El rango extendido se ajusta dinámicamente según el tamaño de los datos de salida o el cálculo realizado por la fórmula. Excel resalta el rango derramado con un borde y un icono de flecha diagonal para indicar que contiene datos derramados.
1. Interactuar con el rango derramado:
<br>
Puede interactuar con el rango derramado como cualquier otro rango de celdas en Excel. Utilice el rango derramado en otras fórmulas, realice cálculos en él, formatéelo o haga referencia a él en gráficos o tablas.
1. Actualiza la fórmula:
<br>
Si necesita modificar la fórmula de matriz dinámica, simplemente edite la fórmula en la celda original donde se ingresó.
Después de editar, presione Enter nuevamente para confirmar los cambios. Excel actualizará automáticamente el rango derramado si es necesario.
1. Limpiar el rango derramado:
<br>
Si desea borrar los datos derramados, puede eliminar la fórmula de la celda original. Excel también borrará el rango derramado. Alternativamente, puede eliminar el rango derramado directamente seleccionándolo y presionando la tecla Eliminar.
<br>

Si sigue estos pasos, puede configurar fórmulas de matriz dinámica en Excel para analizar y manipular matrices de datos de manera eficiente, lo que permite realizar análisis de datos y tareas de generación de informes más fáciles.

##  **Cómo configurar y actualizar fórmulas de matriz dinámica usando Aspose.Cells**
 Consulte el siguiente código de muestra que carga el[archivo de Excel de muestra](dynamicArrayFormula.xlsx) que contiene algunos datos ficticios. Después de cargar el archivo, llame al[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) función para establecer la fórmula de matriz dinámica y[Libro de trabajo.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) función para actualizar las fórmulas de matriz dinámica antes de llamar al cálculo de la fórmula y, finalmente, guardar el libro como[archivo de salida de Excel](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

La instantánea de salida:
<br>
<image src="4.png" width="70%" />