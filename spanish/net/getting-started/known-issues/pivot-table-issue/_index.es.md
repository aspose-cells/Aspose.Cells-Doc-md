---
title: Problema de tabla dinámica
type: docs
weight: 50
url: /es/net/pivot-table-issue/
---
## **Síntoma**
"Intenté abrir el archivo de Excel generado desde el botón "Abrir" de IE. El Excel se generó al leer una plantilla de Excel. Mientras hago clic en el botón Abrir, se abre y al mismo tiempo aparece un mensaje de error que dice "No se puede abrir el archivo fuente de la tabla dinámica...".

Pero cuando guardo el archivo de Excel generado con el botón "Guardar" y lo abro desde el archivo desde la ruta guardada, se abre correctamente sin ningún error. "
### **Solución**
Aspose.Cells establece el formato de datos dinámicos y obliga a MS Excel a crear un informe de tabla dinámica y otras tareas de cálculo basadas en la fuente de datos cuando el libro de trabajo se abre en MS Excel. Así que uno debería usar**SaveType.OpenInBrowser** en lugar de usar**SaveType.OpenInExcel**Una de las muchas razones es cuando usa la opción OpenInExcel mientras guarda el archivo de salida generado en MS Excel en tiempo de ejecución usando el botón "Abrir" del cuadro de diálogo de descarga, MS Excel no pudo analizar los datos del Libro de trabajo para generar un informe de tabla dinámica. Esto se debe al problema del nombre de archivo. Es la rutina de IE, ya que agrega algo como "[1]" para convertirlo en "nombre de archivo"+ "[1]"+ ".xls" al nombre original y, por lo tanto, nada que hacer con Aspose.Cells. (es decir... siempre agrega "[1]" para hacer "fileName"+ "[1]"+ ".xls" y no como fileName.xls). En resumen, si un archivo contiene una tabla dinámica, no se puede abrir con la opción OpenInExcel SaveType y esto se aplicará a ambos, es decir, si crea el archivo desde cero o usa cualquier archivo de plantilla para datos de origen para crear un informe de tabla dinámica. Por lo tanto, debe usar la opción OpenInBrowser SaveType si el archivo tiene datos de tabla dinámica para crear un informe de tabla dinámica.

Debe cambiar su código y actualizar a SaveType.OpenInBrowser si está utilizando el método Workbook.Save()

O edite su código para usar "en línea" si está usando la opción "archivo adjunto" en su código. es decir



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
