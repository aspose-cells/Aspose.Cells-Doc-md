---  
title: Configuración de fórmulas de matriz dinámica con Node.js a través de C++  
linktitle: Establecimiento de Fórmulas de Matriz Dinámica  
description: Cómo usar la biblioteca Aspose.Cells para calcular fórmulas de matriz dinámica en Excel usando Node.js a través de C++. Carga, calcula y guarda archivos de Excel fácilmente.  
keywords: Fórmulas de matriz dinámica, Fórmulas de matriz dinámica en Excel, Establecer fórmulas de matriz dinámica Node.js a través de C++, Cálculo de fórmulas de matriz dinámica Node.js a través de C++, operar fórmulas de matriz dinámica de Excel.  
type: docs  
weight: 70  
url: /es/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **¿Qué es la Fórmula de Matriz de Excel?**  
En Excel, una fórmula de matriz es un tipo especial de fórmula que le permite realizar cálculos en matrices de datos en lugar de celdas individuales. Las fórmulas de matriz se pueden utilizar para realizar cálculos complejos, manipular datos y resolver problemas específicos de manera eficiente. Se ingresan de manera diferente a las fórmulas regulares y a menudo requieren el uso de Ctrl + Mayús + Entrar.

Aquí hay algunos puntos clave sobre las fórmulas de matriz en Excel:  
1. Sintaxis:  
<br>  
Las fórmulas de matriz se escriben como fórmulas regulares pero involucran operaciones en matrices de valores. Se encierran entre llaves { } para indicar que son fórmulas de matriz. Sin embargo, no es necesario escribir estas llaves; Excel las añade automáticamente cuando se ingresa la fórmula correctamente.  
2. Entrada de Matriz:  
<br>  
Para ingresar una fórmula de matriz, escribe la fórmula en la barra de fórmulas. En lugar de pulsar Enter para finalizar, pulsa Ctrl + Shift + Enter. Esto indica a Excel que es una fórmula de matriz. Cuando se ingresa correctamente, Excel muestra la fórmula dentro de llaves en la barra de fórmulas para indicar que es una fórmula de matriz.  
3. Casos de uso:  
<br>  
Las fórmulas de matriz son útiles para realizar cálculos en múltiples celdas o rangos simultáneamente. Se pueden utilizar para cálculos matemáticos avanzados, operaciones condicionales, filtrado de datos y más.  
4. Beneficios:  
<br>  
Las fórmulas de matriz le permiten realizar cálculos complejos en una sola fórmula, lo que puede mejorar la eficiencia y simplificar sus hojas de cálculo. Pueden manejar conjuntos de datos grandes y realizar cálculos que de lo contrario requerirían múltiples pasos intermedios.  
5. Limitaciones:  
<br>  
Las fórmulas de matriz pueden ser más difíciles de entender y solucionar problemas que las fórmulas regulares. Pueden ralentizar el rendimiento de la hoja de cálculo, especialmente si se usan extensivamente o con conjuntos de datos grandes.  
6. Ejemplos:  
<br>  
Sumar los valores en un rango: **{=SUMA(A1:A5*B1:B5)}**  
<br>  
Encontrar el valor máximo en un rango: **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Recuerda que las fórmulas de matriz deben utilizarse con precaución, y es importante entender cómo funcionan antes de implementarlas en tus hojas de cálculo. Pueden ser herramientas poderosas para el análisis y manipulación de datos en Excel.

## **¿Qué es la Fórmula de Matriz Dinámica de Excel?**  
Las fórmulas de matriz dinámica son una nueva característica introducida en Excel 365 y Excel 2021. Te permiten trabajar con matrices de datos de forma más fluida y eficiente en comparación con las fórmulas de matriz tradicionales. Las fórmulas de matriz dinámica desbordan automáticamente los resultados en celdas adyacentes, eliminando la necesidad de Ctrl + Shift + Enter y permitiendo una manipulación más fácil de los datos.

Puntos clave sobre las fórmulas de matriz dinámica en Excel:  
1. Desbordamiento Automático:  
<br>  
Las fórmulas de matriz dinámica desbordan automáticamente los resultados en celdas adyacentes según el tamaño de los datos de salida. Esto significa que no necesitas seleccionar un rango de celdas antes de ingresar la fórmula o usar Ctrl + Shift + Enter para confirmar la fórmula.  
2. Entrada en una sola celda:  
<br>  
Las fórmulas de matriz dinámica se ingresan en una sola celda, y Excel llena automáticamente las celdas adyacentes con los resultados. Esto facilita la gestión y comprensión de las fórmulas, ya que solo necesitas ingresar la fórmula una vez.  
3. Nuevas funciones:  
<br>  
Las fórmulas de matriz dinámica introducen nuevas funciones que pueden manejar matrices de forma nativa, como **FILTRAR**, **ORDENAR**, **ÚNICO**, **SECUENCIA**, **ORDENARPOR** y **MATRIZALEATORIA**. Estas funciones pueden devolver múltiples valores o manipular matrices directamente, simplificando cálculos complejos.  
4. Manejo de rangos flexible:  
<br>  
Las fórmulas de matriz dinámica ajustan el tamaño del rango desbordado dinámicamente según el tamaño de los datos de entrada o la operación realizada. Esta flexibilidad permite un uso más eficiente del espacio de la hoja de cálculo y simplifica la creación de fórmulas.  
5. Mejor rendimiento:  
<br>  
Las fórmulas de matriz dinámica pueden mejorar el rendimiento en comparación con las fórmulas de matriz tradicionales, especialmente al trabajar con conjuntos de datos grandes o cálculos complejos.  
6. Compatibilidad:  
<br>  
Las fórmulas de matriz dinámica están disponibles en Excel 365 y Excel 2021. Es posible que no sean compatibles con versiones anteriores de Excel.  
7. Ejemplos de fórmulas de matriz dinámica:  
<br>  
**FILTER**: Devuelve una serie de valores que cumplen con criterios específicos.  
<br>  
**SORT**: Ordena los valores en un rango o serie.  
<br>  
**UNIQUE**: Devuelve valores únicos de una lista o rango.  
<br>  
**SEQUENCE**: Genera una secuencia de números o fechas.  
<br>  
**RANDARRAY**: Genera una serie de números aleatorios.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Las fórmulas de matriz dinámica ofrecen capacidades poderosas para la manipulación y análisis de datos en Excel, facilitando el trabajo con matrices de datos y realizando cálculos complejos de manera eficiente.

## **¿Cuál es la diferencia entre Fórmulas de Array y Fórmulas de Array Dinámicas en Excel?**  
En Excel, tanto las fórmulas de matriz como las fórmulas de matriz dinámicas se utilizan para realizar cálculos en múltiples valores simultáneamente, pero tienen algunas diferencias en términos de funcionalidad y cómo se implementan.

### **Características de las Fórmulas de Array**  
1. Las fórmulas de matriz son fórmulas tradicionales en Excel que pueden realizar cálculos en matrices de datos.  
2. Se ingresan presionando Ctrl + Shift + Enter después de escribir la fórmula, lo que indica a Excel que es una fórmula de matriz.  
3. Las fórmulas de matriz tienen limitaciones en cuanto a su capacidad para volcar resultados en celdas adyacentes. Normalmente devuelven un solo resultado, aunque ese resultado podría ser un array de celdas.  
4. Han existido durante mucho tiempo y son compatibles con todas las versiones de Excel.

### **Características de las Fórmulas de Array Dinámicas**  
1. Las fórmulas de array dinámicas son una nueva característica introducida en Excel 365 (suscripción a Office 365) y Excel 2021.  
2. Automáticamente vuelcan los resultados en celdas adyacentes según el tamaño de los datos de entrada o el cálculo de la fórmula.  
3. Las fórmulas de matriz dinámica no requieren presionar Ctrl + Shift + Enter; simplemente escribe la fórmula en una celda, y Excel llena automáticamente las celdas adyacentes con los resultados.  
4. Estas fórmulas tienen la capacidad de devolver múltiples resultados (un rango de celdas) directamente, sin necesidad de una fórmula de matriz o Ctrl + Shift + Enter.  
5. Tienen funciones nuevas como **FILTER**, **SORT**, **UNIQUE**, etc., que pueden manejar matrices de forma nativa y devolver resultados en formato de matriz dinámica.  
En resumen, las fórmulas de array dinámicas son una forma más moderna y conveniente de trabajar con matrices en Excel, proporcionando un derrame automático de resultados y simplificando el proceso de trabajar con matrices en comparación con las fórmulas de array tradicionales. Sin embargo, solo están disponibles en las versiones más nuevas de Excel que admiten matrices dinámicas.

## **Cómo configurar y calcular fórmulas de matrices dinámicas en Excel**  
Configurar fórmulas de matrices dinámicas en Excel implica usar funciones específicas diseñadas para trabajar con arrays de datos y permitir que los resultados se derramen automáticamente en celdas adyacentes. 

Aquí tienes una guía paso a paso para configurar fórmulas de matrices dinámicas:  
1. Selecciona la celda:  
<br>  
Elige la celda donde deseas que aparezcan los resultados de la fórmula de matriz dinámica. Las fórmulas de matrices dinámicas desbordan los resultados en celdas adyacentes, así que asegúrate de que haya suficiente espacio para la salida derramada.  
2. Ingresa la Fórmula:  
<br>  
Escribe la fórmula de matriz dinámica en la barra de fórmulas de la celda seleccionada. Usa una de las funciones de matriz dinámica disponibles en Excel 365 y Excel 2021, como **FILTRAR**, **ORDENAR**, **ÚNICO**, **SECUENCIA**, **ORDENAR.POR**, o **MATRIZALEATORIA**.  
<br>  
Por ejemplo, podrías usar la función FILTRAR para filtrar una lista de datos en base a criterios específicos: **=FILTRAR(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Presiona Enter:  
<br>  
Después de escribir la fórmula, simplemente presiona Enter en tu teclado. A diferencia de las fórmulas de matriz tradicionales, no necesitas presionar Ctrl + Mayús + Entrar.  
4. Observa el Rango Desbordado:  
<br>  
Excel derrama automáticamente los resultados de la fórmula en celdas adyacentes. El rango derramado se ajusta dinámicamente en base al tamaño de los datos de salida o la cálculo realizado por la fórmula. Excel resalta el rango derramado con un borde y un icono de flecha diagonal para indicar que contiene datos derramados.  
5. Interactúa con el Rango Desbordado:  
<br>  
Puedes interactuar con el rango derramado como lo harías con cualquier otro rango de celdas en Excel. Utiliza el rango derramado en otras fórmulas, realiza cálculos en él, formatealo o haz referencia a él en gráficos o tablas.  
6. Actualiza la Fórmula:  
<br>  
Si necesitas modificar la fórmula de matriz dinámica, simplemente edita la fórmula en la celda original donde fue ingresada. Después de editar, presiona Enter nuevamente para confirmar los cambios. Excel actualizará automáticamente el rango desbordado si es necesario.  
7. Limpieza del Rango Desbordado:  
<br>  
Si deseas limpiar los datos derramados, puedes eliminar la fórmula de la celda original. Excel también limpiará el rango derramado. Alternativamente, puedes eliminar el rango derramado directamente seleccionándolo y presionando la tecla Suprimir.  
<br>  

Siguiendo estos pasos, puedes configurar fórmulas de matrices dinámicas en Excel para analizar y manipular arrays de datos de manera eficiente, lo que facilita las tareas de análisis de datos e informes.

## **Cómo configurar y actualizar fórmulas de array dinámicas utilizando Aspose.Cells**  
Por favor, vea el siguiente código de ejemplo que carga el [archivo Excel de ejemplo](dynamicArrayFormula.xlsx) que contiene algunos datos ficticios. Después de cargar el archivo, llame a la función [Cell.setDynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setDynamicArrayFormula-string-formulaparseoptions-boolean-) para establecer una fórmula de matriz dinámica y a la función [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/nodejs-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) para actualizar las fórmulas de matriz dinámica antes de llamar al cálculo de la fórmula y, finalmente, guardar el libro como [archivo Excel de salida](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

La instantánea de salida:  
<br>  
<image src="4.png" width="70%" />  

{{< app/cells/assistant language="nodejs-cpp" >}}
