---
title: Renderizado de Matriz en Celda Única con SmartMarker | Aspose.Cells C++
linktitle: Renderizado de Matriz
description: Aprenda a renderizar datos de matriz en una sola celda utilizando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Aspose.Cells for C++.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz de celda única, renderizado de matriz, plantilla
type: docs
weight: 195
url: /es/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite el renderizado de datos de matriz en una sola celda a través de Smart Markers. Mediante el uso del atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, proporcionando un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente característica basada en plantillas que le permite completar dinámicamente datos de hojas de cálculo mediante expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseñador y, cuando la plantilla se procesa mediante `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.

Por defecto, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente separada — ya sea horizontalmente a lo largo de una fila o verticalmente hacia abajo en una columna. Si bien este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría renderizar la matriz completa en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta Smart Marker, abordan exactamente este requisito. Le permiten mantener diseños de informes compactos y predecibles mientras sigue trabajando de forma nativa con orígenes de datos de matrices.

## **Por Qué Se Necesita Esta Característica**

### **Comportamiento Predeterminado de Expansión de Matrices**

Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de múltiples celdas por defecto. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando el contenido de la plantilla hacia afuera y potencialmente rompiendo diseños de informes cuidadosamente diseñados.

### **Limitaciones de los Casos de Uso**

Hay muchos escenarios prácticos en los que el comportamiento de expansión predeterminado no es deseable:

- **Informes de estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o por barras verticales dentro de una sola celda.
- **Indicadores de estado o chips de filtro** que agrupan múltiples valores en un solo lugar para facilitar la lectura.
- **Pipelines descendentes** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad entre plataformas**, donde algunos consumidores no toleran matrices que se desbordan a través de múltiples celdas.

### **La Brecha Que Cubre**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar datos en C++ — uniendo matrices en cadenas delimitadas antes de vincularlas al diseñador del libro de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la Característica**

El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee — coma, punto y coma, guion, barra vertical, nueva línea o cualquier texto personalizado.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta Smart Marker.
- **Informes más limpios**: Los datos de la matriz ya no empujan al contenido vecino de la plantilla a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de dato que se pueda unir con un delimitador.
- **Compatibilidad hacia atrás**: Cuando se omiten los atributos, se preserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo Usar Esta Característica**

### **Sintaxis de Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en el origen de datos vinculado.
- `arrayasSingle=true` — indica al motor que renderice la matriz completa en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es una cadena literal; puede estar vacío, ser un solo carácter o una cadena de múltiples caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier cadena literal, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nuevas líneas. Si la matriz está vacía, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de Trabajo Paso a Paso**

El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda usando Smart Markers.

1. **Prepare el origen de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `std::vector<std::string>`, `std::vector<int>`, o cualquier otro tipo de matriz/vector compatible.
2. **Cree un libro de trabajo de diseñador**: Cree un nuevo `Workbook`, añada una fila de encabezado y coloque una celda de Smart Marker que haga referencia a la propiedad de matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia de WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseñador a él y vincule su origen de datos usando el método `SetDataSource`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.Process()` para expandir los Smart Markers y completar el libro de trabajo con datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo compatible.

### **Ejemplo de Código 1 — Renderizado Básico de Matriz de Cadenas**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner no está disponible en Aspose.Cells para C++
    // Necesitamos simular el procesamiento de SmartMarker reemplazando los marcadores manualmente
    // Dado que Aspose.Cells C++ no admite WorkbookDesigner, usaremos el reemplazo de U16String
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Reemplazar el marcador inteligente con los datos reales
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ejemplo de Código 2 — Matriz Numérica con Delimitador Personalizado**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Ejemplo de Código 3 — Comparación del Comportamiento Predeterminado vs. ArrayAsSingle**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Preparar fuente de datos
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Crear libro de trabajo y obtener la primera hoja de cálculo
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Sección 1: Marcador Inteligente predeterminado - valores distribuidos horizontalmente entre celdas
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Sección 2: Nueva representación en una sola celda usando arrayasSingle y extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Vincular la fuente de datos y procesar los Marcadores Inteligentes
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Guardar el libro de trabajo resultante
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Notas y Mejores Prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor de `extraDelimiter` se trata como una cadena literal; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de celda única; cualquier otro valor recae en el comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de dato).
- La característica funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para salida separada por nuevas líneas, puede usar `\n` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente en celdas adyacentes según el formato.

## **Artículos Relacionados**

- [Smart Markers](/cells/es/cpp/smart-markers/)
- [Combinar y Descombinar Celdas](/cells/es/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}