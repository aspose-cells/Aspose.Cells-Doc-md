---
title: Problema de Tabla Dinámica
type: docs
weight: 50
url: /es/net/pivot-table-issue/
---

## **Síntoma**
"Intenté abrir el archivo de Excel generado desde el botón "Abrir" de Internet Explorer. El Excel ha sido generado leyendo una plantilla de Excel. Mientras hago clic en el botón Abrir se abre y al mismo tiempo aparece un mensaje de error que dice "No se puede abrir el archivo de origen de la Tabla Dinámica.....".

Pero cuando guardo el archivo de Excel generado usando el botón "Guardar" y lo abro desde la vía guardada se abre correctamente sin errores. "
### **Solución**
Aspose.Cells establece el formato de datos de la tabla dinámica y obliga a MS Excel a crear el informe de la tabla dinámica y otras tareas de cálculo basadas en la fuente de datos al abrirse el libro de trabajo en MS Excel. Por lo tanto, se debe usar **SaveType.OpenInBrowser** en lugar de usar **SaveType.OpenInExcel**. Una de las muchas razones es que al usar la opción OpenInExcel al guardar el archivo generado en MS Excel en tiempo de ejecución al usar el botón "Abrir" del cuadro de diálogo de descarga, MS Excel no puede analizar los datos del Libro para generar el informe de la tabla dinámica. Esto se debe a un problema con el nombre de archivo, es la rutina de IE ya que agrega algo como "[1]" para convertirlo en "nombreDeArchivo"+ "[1]"+ ".xls" al nombre original y por lo tanto nada tiene que ver con Aspose.Cells. (es decir.... siempre agrega "[1]" para convertir "nombreDeArchivo"+ "[1]"+ ".xls" y no como nombreDeArchivo.xls). En resumen, si un archivo contiene tabla dinámica, no se puede abrir usando la opción SaveType OpenInExcel y esto se aplicará tanto si creas el archivo desde cero como si usas cualquier archivo de plantilla para los datos de origen para crear el informe de tabla dinámica. Por lo tanto, se debe usar la opción SaveType OpenInBrowser si el archivo tiene datos de tabla dinámica para crear el informe de tabla dinámica.

Debes cambiar tu código y actualizar a SaveType.OpenInBrowser si estás usando el método Workbook.Save()

O modifica tu código para usar "en línea" si estás utilizando la opción "adjunto" en tu código. es decir.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
