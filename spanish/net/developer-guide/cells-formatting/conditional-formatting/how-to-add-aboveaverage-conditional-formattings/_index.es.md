---
title: Cómo agregar formateo condicional de valores por encima del promedio
description: Cómo usar la biblioteca Aspose.Cells en C# para aplicar formateo condicional de valores por encima del promedio. Ajustando estos criterios, tienes más control sobre la apariencia y presentación de las celdas.
keywords: Aspose.Cells, Formato condicional de por encima del promedio, C#, Condicional, Formato
type: docs
weight: 70
url: /es/net/how-to-add-above-average-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar formato condicional de por encima del promedio en herramientas como Microsoft Excel o Google Sheets es una manera rápida y visual de resaltar datos destacados—específicamente, valores que son mayores que el promedio en un rango. Aquí las razones para usarlo:
1. Detectar tendencias rápidamente: Te ayuda a identificar instantáneamente valores de alto rendimiento sin calcular manualmente los promedios o escanear números.
1. Simplificar análisis de datos: No necesitas calcular ni ingresar fórmulas, es una forma automática de aplicar formato basado en lógica, ahorrando tiempo.
1. Mejorar el atractivo visual: La codificación por colores ayuda a que tu hoja de cálculo sea más fácil de leer y visualmente más atractiva, especialmente durante presentaciones.
1. Apoyar la toma de decisiones: Identificar rápidamente valores por encima del promedio puede orientar acciones, como recompensar a los que rinden alto o investigar por qué ciertos productos superan a otros.

## **Cómo agregar formateo condicional de por encima del promedio usando Excel**
Para agregar formateo condicional de por encima del promedio en Excel, así es como puedes hacerlo paso a paso:

1. Selecciona el rango de celdas al que deseas aplicar el formato. Por ejemplo: A1:A20.
1. Ve a la pestaña Inicio en la cinta de opciones.
1. Haz clic en Formato condicional en el grupo Estilos.
1. Pasa el cursor sobre Reglas superiores/inferiores.
1. Haz clic en Por encima del promedio...
1. En el cuadro de diálogo que aparece: Detectará automáticamente "Formatar celdas que están POR ENCIMA del media." Puedes cambiar el estilo de formato haciendo clic en la flecha hacia abajo junto a (por ejemplo, elegir un color de relleno o formato personalizado).
1. Haz clic en Aceptar. Todas las celdas en tu rango seleccionado que estén por encima del promedio de ese rango serán resaltadas.


## **Cómo agregar formateo condicional de por encima del promedio usando Aspose.Cells for .NET**

Aspose.Cells admite completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en las celdas en tiempo de ejecución. Este ejemplo demuestra un ejercicio para el formato condicional de Superiores a Promedio con diferentes conjuntos de atributos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-AboveAverage.cs" >}}

{{< app/cells/assistant language="csharp" >}}
