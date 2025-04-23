---
title: Cómo agregar formato condicional de períodos de tiempo
description: Cómo usar la biblioteca Aspose.Cells en C# para aplicar formato condicional de períodos de tiempo. Ajustando estos criterios, tienes más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional de períodos de tiempo, C#, Condicional, Formateo
type: docs
weight: 70
url: /es/net/how-to-add-time-periods-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar el formato condicional de períodos de tiempo en Excel es súper útil cuando trabajas con fechas: te ayuda a seguir y gestionar visualmente los datos basados en el tiempo rápidamente.
1. ideas instantáneas sobre datos basados en el tiempo: resalta rápidamente tareas de hoy, ventas del mes pasado, fechas límite próximas, citas de la próxima semana.
1. Mejor gestión del tiempo: te ayuda a mantenerte al día con las fechas de vencimiento, eventos o elementos que caducan. Ideal para cronogramas de proyectos, facturas o horarios.
1. Actualizaciones automáticas: se actualiza dinámicamente. Si cambia la fecha de hoy, Excel actualizará automáticamente el formato sin que hagas nada.

1. Claridad visual: hace que la información sensible al tiempo destaque usando colores o estilos en negrita, para que no se pase por alto.

## **Cómo agregar formato condicional de períodos de tiempo en Excel**
Así puedes agregar formato condicional de períodos de tiempo en Excel, muy útil para resaltar fechas como hoy, la semana pasada, el próximo mes, etc.

Pasos para agregar formato condicional de períodos de tiempo:
1. Selecciona el rango de celdas de fechas que quieres formatear. Ejemplo: A2:A50.
1. Ve a la pestaña Inicio en la cinta de opciones.
1. Haz clic en Formato condicional en el grupo Estilos.
1. Pasa el cursor sobre Reglas para resaltar celdas.
1. Haz clic en Ocurrencia de una fecha...
1. En la ventana de diálogo que aparece: Usa la lista desplegable para seleccionar un período de tiempo (Hoy, Ayer, Mañana, Últimos 7 días, La semana pasada, El próximo mes, etc.).
1. Elige el formato (por defecto es relleno rosa claro con texto rojo oscuro, o haz clic en Formato personalizado para elegir el tuyo).
1. Haz clic en Aceptar


## **Cómo agregar formato condicional de períodos de tiempo usando Aspose.Cells for .NET**

Aspose.Cells soporta completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en archivos XLSX en tiempo de ejecución. Este ejemplo demuestra un ejercicio para formato condicional de períodos de tiempo con diferentes conjuntos de atributos.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-TimePeriod.cs" >}}

{{< app/cells/assistant language="csharp" >}}
