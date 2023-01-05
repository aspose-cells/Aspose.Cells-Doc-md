---
title: Función de marcadores inteligentes en Aspose.Cells
type: docs
weight: 30
url: /es/net/smart-markers-feature-in-aspose-cells/
---
**Marcadores inteligentes** se utilizan para que Aspose.Cells sepa qué información colocar en una hoja de cálculo de Microsoft diseñador de Excel. Los marcadores inteligentes le permiten crear plantillas que contienen solo información y formato específicos.
## **Diseñador de hojas de cálculo y marcadores inteligentes**
Las hojas de cálculo de Designer son archivos estándar de Excel que contienen formato visual, fórmulas y marcadores inteligentes. Pueden contener marcadores inteligentes que hacen referencia a una o más fuentes de datos, como información de un proyecto e información de contactos relacionados. Los marcadores inteligentes se escriben en las celdas donde desea la información.

Todos los marcadores inteligentes comienzan con &=. Un ejemplo de marcador de datos es &=Party.FullName. Si el marcador de datos da como resultado más de un elemento, por ejemplo, una fila completa, las siguientes filas se mueven hacia abajo automáticamente para dejar espacio para toda la información nueva. Por lo tanto, los subtotales y los totales se pueden colocar en la fila inmediatamente después del marcador de datos para realizar cálculos basados en los datos insertados. Para realizar cálculos en las filas insertadas, utilice fórmulas dinámicas.

 Los marcadores inteligentes consisten en la**fuente de datos** y**nombre del campo**piezas para la mayoría de la información. También se puede pasar información especial con variables y matrices de variables. Las variables siempre llenan solo una celda, mientras que las matrices de variables pueden llenar varias. Solo use un marcador de datos por celda. Los marcadores inteligentes no utilizados se eliminan.

El marcador inteligente también puede contener parámetros. Los parámetros le permiten modificar cómo se distribuirá la información. Se agregan al final del marcador inteligente entre paréntesis como una lista separada por comas.
### **Opciones de marcador inteligente**
- &=FuenteDeDatos.NombreDeCampo
- &=Fuente de datos.Nombre de campo
- &=$NombreVariable
- &=$VariableArray
- &==Fórmula dinámica
- &=&=Fórmula dinámica repetida
### **Parámetros**
Se permiten los siguientes parámetros:

- noadd: no agregue filas adicionales para ajustar los datos.
- skip:n - Saltar n número de filas para cada fila de datos.
- ascending:n o descending:n - Ordenar datos en marcadores inteligentes. Si n es 1, entonces la columna es la primera clave del clasificador. Los datos se ordenan después de procesar la fuente de datos. Por ejemplo &=Tabla1.Campo3(ascendente:1).
- horizontal: escriba los datos de izquierda a derecha, en lugar de arriba a abajo.
- numérico: convertir texto en número si es posible. Solo se admite en la versión .NET.
- shift - Desplace hacia abajo o hacia la derecha, creando filas o columnas adicionales para ajustar los datos. El parámetro shift funciona de la misma manera que en Microsoft Excel. Por ejemplo, en MS Excel, cuando selecciona un rango de celdas, haga clic con el botón derecho y seleccione Insertar y especifique desplazar celdas hacia abajo, desplazar celdas hacia la derecha y otras opciones. En resumen, el parámetro de desplazamiento cumple la misma función para marcadores inteligentes verticales/normales (de arriba a abajo) u horizontales (de izquierda a derecha).
- copystyle: copia el estilo de la celda base en todas las celdas de esa columna.

 Los parametros**no agregar** y skip se pueden combinar para insertar datos en filas alternas. Debido a que la plantilla se procesa de abajo hacia arriba, debe agregar noadd en la primera fila para evitar que se inserten filas adicionales antes de la fila alternativa.

Esta sección incluye los siguientes temas

- [Agrupación de datos en Aspose.Cells](/cells/es/net/grouping-data-in-aspose-cells/)
- [Marcadores de imagen en Aspose.Cells](/cells/es/net/image-markers-in-aspose-cells/)
- [Uso de tipos anónimos u objetos personalizados en Aspose.Cells](/cells/es/net/using-anonymous-types-or-custom-objects-in-aspose-cells/)
- [Uso de objetos anidados en Aspose.Cells](/cells/es/net/using-nested-objects-in-aspose-cells/)
