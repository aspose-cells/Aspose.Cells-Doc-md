---
title: Funcionalidad de Marcadores Inteligentes
type: docs
weight: 30
url: /es/net/smart-markers-feature/
---

**Los marcadores inteligentes** se utilizan para que Aspose.Cells sepa qué información colocar en una hoja de cálculo de diseño de Microsoft Excel. Los marcadores inteligentes le permiten crear plantillas que contienen solo información específica y formato.
## **Hoja de cálculo de diseño y Marcadores inteligentes**
Las hojas de cálculo de diseño son archivos Excel estándar que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de un marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, entonces las filas subsiguientes son movidas hacia abajo automáticamente para dar espacio a toda la nueva información. De esta forma, los subtotales y totales pueden colocarse en la fila inmediatamente después del marcador de datos para realizar cálculos basados en la información insertada. Para realizar cálculos en las filas insertadas, se utilizan fórmulas dinámicas.

Los marcadores inteligentes consisten en las partes de **fuente de datos** y **nombre del campo** para la mayoría de la información. También se puede enviar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Utilice solo un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

Un marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se va a organizar la información. Se añaden al final del marcador inteligente entre paréntesis como una lista separada por comas.
### **Opciones de Marcador Inteligente**
- &=DataSource.FieldName
- &=Data Source.Field Name
- &=$VariableName
- &=$VariableArray
- &==DynamicFormula
- &=&=RepeatDynamicFormula
### **Parámetros**
Se permiten los siguientes parámetros:

- noadd - No agregar filas adicionales para ajustar datos.
- skip:n - Omitir n número de filas por cada fila de datos.
- ascending:n o descending:n - Ordenar datos en los marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del ordenador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo, &=Table1.Field3(ascending:1).
- horizontal - Escribir datos de izquierda a derecha, en lugar de arriba hacia abajo.
- numérico - Convertir texto en número si es posible. Solo compatible con la versión .NET.
- shift - Desplazar hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro shift funciona de la misma manera que en Microsoft Excel. Por ejemplo, en MS Excel, cuando seleccionas un rango de celdas, haces clic derecho, seleccionas Insertar y especificas desplazar celdas hacia abajo, desplazar celdas hacia la derecha y otras opciones. En resumen, el parámetro shift cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- copystyle - Copiar el estilo de la celda base a todas las celdas en esa columna.

Los parámetros **noadd** y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debes agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.
