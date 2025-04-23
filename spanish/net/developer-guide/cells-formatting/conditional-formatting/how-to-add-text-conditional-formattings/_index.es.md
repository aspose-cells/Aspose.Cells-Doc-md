---
title: Cómo agregar formato condicional de texto
description: Cómo usar la biblioteca Aspose.Cells en C# para aplicar formato condicional de texto. Al ajustar estos criterios, tienes mayor control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional de texto, C#, Condicional, Formato
type: docs
weight: 70
url: /es/net/how-to-add-text-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar formato condicional basado en texto en hojas de cálculo es útil para resaltar celdas que cumplen con criterios textuales específicos. Esto puede mejorar el análisis de datos y facilitar la búsqueda de información clave en un conjunto de datos grande. Aquí algunas razones para usar formato condicional de texto:

1. Resaltar Texto Específico: Puedes aplicar formato en función de palabras, frases o caracteres específicos. Por ejemplo, quizás quieras resaltar todas las celdas que contienen la palabra "Urgente" o "Completado" para diferenciar tareas en un proyecto fácilmente.
1. Identificar patrones o tendencias: Si trabajas con categorías o estados (como "Alto", "Medio", "Bajo"), el formato condicional de texto puede distinguir visualmente entre ellos, facilitando el seguimiento del progreso o priorización de tareas.
1. Alertas de errores o entrada de datos: El formato de texto puede marcar entradas inconsistentes o erróneas, como palabras mal escritas, texto incompleto o valores incorrectos. Esto es especialmente útil en conjuntos de datos con mucha entrada textual.
1. Mejora de la legibilidad: Codificar por colores el texto o cambiar su estilo (negrita, cursiva, etc.) ayuda a que la información importante destaque, mejorando la legibilidad general de tu hoja.
1. Retroalimentación dinámica: Puedes establecer reglas que ajusten automáticamente el formato cuando el texto coincida con ciertas condiciones. Esto significa que no tienes que actualizar manualmente el formato a medida que cambian los datos.

En esencia, el formato condicional de texto te ayuda a detectar rápidamente información relevante, errores y tendencias, convirtiéndolo en una herramienta poderosa para gestionar e interpretar datos textuales.

## **Cómo agregar formato condicional de texto usando Excel**
Para agregar formato condicional basado en texto en Excel, sigue estos pasos:

1. Selecciona el rango de celdas: Resalta las celdas donde deseas aplicar el formato condicional.
1. Abre el menú de Formato condicional: Ve a la pestaña Inicio en la cinta de opciones de Excel. Haz clic en Formato condicional en el grupo "Estilos".
1. Elige "Nueva regla": Desde el menú desplegable, selecciona Nueva regla.
1. Selecciona "Formatear solo celdas que contengan": En el cuadro de diálogo Nueva regla de formato, elige Formatear solo celdas que contengan en la sección "Seleccionar un tipo de regla".
1. Establece los criterios de la regla: En la sección "Formatear celdas con", elige Texto específico en el menú desplegable. Selecciona si contiene, empieza con o termina con, dependiendo de la condición que deseas aplicar. Ingresa el texto que quieres formatear (por ejemplo, una palabra específica como "Urgente" o "Completado").
1. Elige el formato: Haz clic en el botón de Formato. En el cuadro de diálogo de Formato de celdas, puedes seleccionar el color de fuente, color de relleno u otras opciones de formato que prefieras.
1. Aplica la regla: Una vez que hayas establecido el formato deseado, haz clic en Aceptar para aplicar la regla. Haz clic en Aceptar nuevamente en el cuadro de diálogo Nueva regla de formato para cerrarlo.
1. Ver los resultados: Las celdas que contienen el texto especificado tendrán ahora el formato aplicado, facilitando la identificación de la información relevante.


## **Cómo agregar formato condicional de texto usando Aspose.Cells for .NET**

Aspose.Cells admite completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en las celdas en tiempo de ejecución. Estos ejemplos demuestran un ejercicio de formatos condicionales avanzados incluyendo BeginsWith, ContainsBlank, ContainsText, etc.

### **Formate la celda cuando el valor comience con texto especificado**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **Formate la celda cuando el valor contenga en blanco**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Formate la celda cuando el valor contenga errores**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Formate la celda cuando el valor contenga texto especificado**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Formate la celda cuando el valor contenga valores duplicados**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Formate la celda cuando el valor termine con texto especificado**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Formate la celda cuando el valor no contenga en blanco**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Formate la celda cuando el valor no contenga errores**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Formate la celda cuando el valor no contenga texto especificado**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Formate la celda cuando el valor contenga valores únicos**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
