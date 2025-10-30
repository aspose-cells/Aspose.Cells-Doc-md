---  
title: Establecer fórmulas de matriz dinámica con C++  
description: Cómo usar la biblioteca Aspose.Cells para calcular fórmulas de matriz dinámica en Microsoft Excel con C++.  
keywords: Fórmulas de Matriz Dinámica, Fórmulas de Matriz Dinámica en Excel, Establecer fórmulas de matriz dinámica, Cálculo de fórmulas de matriz dinámica, operar fórmulas de matriz dinámica de Excel.  
type: docs  
weight: 70  
url: /es/cpp/calculation-of-dynamic-array-formulas/  
---  

## **¿Qué es la Fórmula de Matriz de Excel?**  
En Excel, una fórmula de matriz es un tipo especial de fórmula que le permite realizar cálculos en matrices de datos en lugar de celdas individuales. Las fórmulas de matriz se pueden utilizar para realizar cálculos complejos, manipular datos y resolver problemas específicos de manera eficiente. Se ingresan de manera diferente a las fórmulas regulares y a menudo requieren el uso de Ctrl + Mayús + Entrar.  

Aquí hay algunos puntos clave sobre las fórmulas de matriz en Excel:  
1. **Sintaxis:**  
Las fórmulas de matriz se escriben como fórmulas regulares pero involucran operaciones en matrices de valores. Se encierran entre llaves { } para indicar que son fórmulas de matriz. Sin embargo, no es necesario escribir estas llaves; Excel las añade automáticamente cuando se ingresa la fórmula correctamente.  
1. **Ingresar fórmulas de matriz:**  
Para ingresar una fórmula de matriz, escribe la fórmula en la barra de fórmulas. En lugar de pulsar Enter para finalizar, pulsa Ctrl + Shift + Enter. Esto indica a Excel que es una fórmula de matriz. Cuando se ingresa correctamente, Excel muestra la fórmula dentro de llaves en la barra de fórmulas para indicar que es una fórmula de matriz.  
1. **Casos de uso:**  
Las fórmulas de matriz son útiles para realizar cálculos en múltiples celdas o rangos simultáneamente. Se pueden utilizar para cálculos matemáticos avanzados, operaciones condicionales, filtrado de datos y más.  
1. **Beneficios:**  
Las fórmulas de matriz le permiten realizar cálculos complejos en una sola fórmula, lo que puede mejorar la eficiencia y simplificar sus hojas de cálculo. Pueden manejar conjuntos de datos grandes y realizar cálculos que de lo contrario requerirían múltiples pasos intermedios.  
1. **Limitaciones:**  
Las fórmulas de matriz pueden ser más difíciles de entender y solucionar problemas que las fórmulas regulares. Pueden ralentizar el rendimiento de la hoja de cálculo, especialmente si se usan extensivamente o con conjuntos de datos grandes.  
1. **Ejemplos:**  
Sumar los valores en un rango: **{=SUMA(A1:A5*B1:B5)}**  
Encontrar el valor máximo en un rango: **{=MAX(A1:A5+B1:B5)}**  
<br><image src="1.png" width="70%" />  
<br>  
Recuerda que las fórmulas de matriz deben utilizarse con precaución, y es importante entender cómo funcionan antes de implementarlas en tus hojas de cálculo. Pueden ser herramientas poderosas para el análisis y manipulación de datos en Excel.  

## **¿Qué es la Fórmula de Matriz Dinámica de Excel?**  
Las fórmulas de matriz dinámica son una nueva característica introducida en Excel 365 y Excel 2021. Te permiten trabajar con matrices de datos de forma más fluida y eficiente en comparación con las fórmulas de matriz tradicionales. Las fórmulas de matriz dinámica desbordan automáticamente los resultados en celdas adyacentes, eliminando la necesidad de Ctrl + Shift + Enter y permitiendo una manipulación más fácil de los datos.  

Puntos clave sobre las fórmulas de matriz dinámica en Excel:  
1. **Desbordamiento automático:**  
Las fórmulas de matriz dinámica desbordan automáticamente los resultados en celdas adyacentes según el tamaño de los datos de salida. Esto significa que no necesitas seleccionar un rango de celdas antes de ingresar la fórmula o usar Ctrl + Shift + Enter para confirmar la fórmula.  
1. **Entrada en una sola celda:**  
Las fórmulas de matriz dinámica se ingresan en una sola celda, y Excel llena automáticamente las celdas adyacentes con los resultados. Esto facilita la gestión y comprensión de las fórmulas, ya que solo necesitas ingresar la fórmula una vez.  
1. **Nuevas funciones:**  
Las fórmulas de matriz dinámica introducen nuevas funciones que pueden manejar matrices de forma nativa, como **FILTRAR**, **ORDENAR**, **ÚNICO**, **SECUENCIA**, **ORDENARPOR** y **MATRIZALEATORIA**. Estas funciones pueden devolver múltiples valores o manipular matrices directamente, simplificando cálculos complejos.  
1. **Manejo flexible del rango:**  
Las fórmulas de matriz dinámica ajustan el tamaño del rango desbordado dinámicamente según el tamaño de los datos de entrada o la operación realizada. Esta flexibilidad permite un uso más eficiente del espacio de la hoja de cálculo y simplifica la creación de fórmulas.  
1. **Mejor rendimiento:**  
Las fórmulas de matriz dinámica pueden mejorar el rendimiento en comparación con las fórmulas de matriz tradicionales, especialmente al trabajar con conjuntos de datos grandes o cálculos complejos.  
1. **Compatibilidad:**  
Las fórmulas de matriz dinámica están disponibles en Excel 365 y Excel 2021. Es posible que no sean compatibles con versiones anteriores de Excel.  
1. **Ejemplos de fórmulas de matriz dinámicas:**  
**FILTER**: Devuelve una serie de valores que cumplen con criterios específicos.  
**SORT**: Ordena los valores en un rango o serie.  
**UNIQUE**: Devuelve valores únicos de una lista o rango.  
**SEQUENCE**: Genera una secuencia de números o fechas.  
**RANDARRAY**: Genera una serie de números aleatorios.  
<br><image src="2.png" width="70%" />  
<br>  
Las fórmulas de matriz dinámica ofrecen capacidades poderosas para la manipulación y análisis de datos en Excel, facilitando el trabajo con matrices de datos y realizando cálculos complejos de manera eficiente.  

## **¿Cuál es la diferencia entre Fórmulas de Array y Fórmulas de Array Dinámicas en Excel?**  
En Excel, tanto las fórmulas de matriz como las fórmulas de matriz dinámicas se utilizan para realizar cálculos en múltiples valores simultáneamente, pero tienen algunas diferencias en términos de funcionalidad y cómo se implementan.  

### **Características de las Fórmulas de Array**  
1. Las fórmulas de matriz son fórmulas tradicionales en Excel que pueden realizar cálculos en matrices de datos.  
1. Se ingresan presionando Ctrl + Shift + Enter después de escribir la fórmula, lo que le indica a Excel que es una fórmula de matriz.  
1. Las fórmulas de matriz tienen limitaciones en cuanto a su capacidad de desbordar resultados en celdas adyacentes. Normalmente devuelven un solo resultado, aunque ese resultado puede ser un arreglo de celdas.  
1. Han existido por mucho tiempo y son compatibles con todas las versiones de Excel.  

### **Características de las Fórmulas de Array Dinámicas**  
1. Las fórmulas de array dinámicas son una nueva característica introducida en Excel 365 (suscripción a Office 365) y Excel 2021.  
1. Automáticamente derraman resultados en celdas adyacentes basándose en el tamaño de los datos de entrada o en el cálculo de la fórmula.  
1. Las fórmulas de array dinámicas no requieren presionar Ctrl + Shift + Enter; simplemente escribe la fórmula en una celda y Excel llena automáticamente las celdas adyacentes con los resultados.  
1. Estas fórmulas tienen la capacidad de devolver múltiples resultados (un rango de celdas) directamente sin necesidad de una fórmula de matriz o Ctrl + Shift + Enter.  
1. Tienen nuevas funciones como **FILTER**, **SORT**, **UNIQUE**, etc., que pueden manejar matrices de forma nativa y devolver resultados en un formato de matriz dinámica.  
En resumen, las fórmulas de array dinámicas son una forma más moderna y conveniente de trabajar con matrices en Excel, proporcionando un derrame automático de resultados y simplificando el proceso de trabajar con matrices en comparación con las fórmulas de array tradicionales. Sin embargo, solo están disponibles en las versiones más nuevas de Excel que admiten matrices dinámicas.  

## **Cómo configurar y calcular fórmulas de matrices dinámicas en Excel**  
Configurar fórmulas de matrices dinámicas en Excel implica usar funciones específicas diseñadas para trabajar con arrays de datos y permitir que los resultados se derramen automáticamente en celdas adyacentes.  

Aquí tienes una guía paso a paso para configurar fórmulas de matrices dinámicas:  
1. **Seleccionar la celda:**  
Elige la celda donde deseas que aparezcan los resultados de la fórmula de matriz dinámica. Las fórmulas de matrices dinámicas desbordan los resultados en celdas adyacentes, así que asegúrate de que haya suficiente espacio para la salida derramada.  
1. **Ingresar la fórmula:**  
Escribe la fórmula de matriz dinámica en la barra de fórmulas de la celda seleccionada. Usa una de las funciones de matriz dinámica disponibles en Excel 365 y Excel 2021, como **FILTRAR**, **ORDENAR**, **ÚNICO**, **SECUENCIA**, **ORDENAR.POR**, o **MATRIZALEATORIA**.  
Por ejemplo, podrías usar la función FILTRAR para filtrar una lista de datos en base a criterios específicos: **=FILTRAR(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br><image src="3.png" width="70%" />  
<br>  
1. **Presionar Enter:**  
Después de escribir la fórmula, simplemente presiona Enter en tu teclado. A diferencia de las fórmulas de matriz tradicionales, no necesitas presionar Ctrl + Mayús + Entrar.  
1. **Observar el rango desbordado:**  
Excel derrama automáticamente los resultados de la fórmula en celdas adyacentes. El rango derramado se ajusta dinámicamente en base al tamaño de los datos de salida o la cálculo realizado por la fórmula. Excel resalta el rango derramado con un borde y un icono de flecha diagonal para indicar que contiene datos derramados.  
1. **Interactuar con el rango desbordado:**  
Puedes interactuar con el rango derramado como lo harías con cualquier otro rango de celdas en Excel. Utiliza el rango derramado en otras fórmulas, realiza cálculos en él, formatealo o haz referencia a él en gráficos o tablas.  
1. **Actualizar la fórmula:**  
Si necesitas modificar la fórmula de matriz dinámica, simplemente edita la fórmula en la celda original donde fue ingresada.  
Después de editar, presiona Enter nuevamente para confirmar los cambios. Excel actualizará automáticamente el rango derramado si es necesario.  
1. **Limpiar el rango desbordado:**  
Si deseas limpiar los datos derramados, puedes eliminar la fórmula de la celda original. Excel también limpiará el rango derramado. Alternativamente, puedes eliminar el rango derramado directamente seleccionándolo y presionando la tecla Suprimir.  
<br>  
Siguiendo estos pasos, puedes configurar fórmulas de matrices dinámicas en Excel para analizar y manipular arrays de datos de manera eficiente, lo que facilita las tareas de análisis de datos e informes.  

## **Cómo configurar y actualizar fórmulas de array dinámicas utilizando Aspose.Cells**  
Por favor, vea el siguiente ejemplo de código que carga el [archivo Excel de muestra](dynamicArrayFormula.xlsx) que contiene algunos datos falsos. Después de cargar el archivo, llame a la función [Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula) para establecer fórmulas de matriz dinámica y a la función [Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) para actualizar las fórmulas de matriz dinámica antes de llamar al cálculo de fórmulas, y finalmente guardar el libro como [archivo Excel de salida](out.xlsx).  

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook(u"dynamicArrayFormula.xlsx");

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Getting the F16 
    Cell f16 = ws.GetCells().Get(u"F16");

    // Set dynamic array formula
    FormulaParseOptions formulaParseOptions;
    f16.SetDynamicArrayFormula(u"=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", formulaParseOptions, false);

    // Refresh the dynamic array formulas
    workbook.RefreshDynamicArrayFormulas(true);

    workbook.CalculateFormula();
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```  

La instantánea de salida:  
<br><image src="4.png" width="70%" />  
{{< app/cells/assistant language="cpp" >}}
