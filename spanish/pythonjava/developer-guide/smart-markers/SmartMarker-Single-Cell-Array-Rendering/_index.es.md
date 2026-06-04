---
title: Renderizado de Array en Celda Única con SmartMarker | Aspose.Cells Python via Java
description: Aprenda a renderizar datos de array en una sola celda usando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Python via Java.
keywords: Aspose.Cells, biblioteca Python via Java, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, array de celda única, renderizado de array, plantilla
type: docs
weight: 195
url: /es/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells admite el renderizado de datos de array en una sola celda a través de Smart Markers. Al usar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos del array dentro de una sola celda, proporcionando un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente característica basada en plantillas que le permite poblar dinámicamente datos en hojas de cálculo utilizando expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.

Por defecto, cuando un Smart Marker hace referencia a una propiedad de array (por ejemplo, `&=DataSource.Numbers`), el motor expande el array y coloca cada elemento en una celda adyacente separada, ya sea horizontalmente a lo largo de una fila o verticalmente en una columna. Si bien este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría renderizar todo el array en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta Smart Marker, abordan exactamente este requisito. Le permiten mantener diseños de informes compactos y predecibles mientras trabaja de forma nativa con orígenes de datos de arrays.

## **Por Qué Se Necesita Esta Función**

### **Comportamiento Predeterminado de Expansión de Arrays**

Cuando un Smart Marker hace referencia a una propiedad de array, Aspose.Cells expande el array en varias celdas por defecto. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando otro contenido de la plantilla hacia afuera y potencialmente rompiendo diseños de informes cuidadosamente diseñados.

### **Limitaciones de los Casos de Uso**

Hay muchos escenarios prácticos donde el comportamiento de expansión predeterminado no es deseable:

- **Informes estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de tags, etiquetas o palabras clave** que necesitan mostrarse como valores separados por comas o pipes dentro de una sola celda.
- **Fichas de filtro o indicadores de estado** que agrupan múltiples valores en un solo lugar para mejorar la legibilidad.
- **Pipelines posteriores** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un valor consolidado único por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no pueden tolerar arrays que se extienden a través de varias celdas.

### **El Espacio que Llena**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar datos en Python, uniendo arrays en cadenas delimitadas antes de vincularlos al diseñador de libros de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la Función**

Usar los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos del array se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee: coma, punto y coma, guion, pipe, nueva línea o cualquier texto personalizado.
- **Formato impulsado por plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta Smart Marker.
- **Informes más limpios**: Los datos del array ya no empujan el contenido vecino de la plantilla a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de datos que se pueda unir con un delimitador.
- **Compatibilidad hacia atrás**: Cuando se omiten los atributos, se preserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo Usar Esta Función**

### **Sintaxis del Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de array en el origen de datos enlazado.
- `arrayasSingle=true` — indica al motor que renderice todo el array en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador colocado entre los elementos del array. El valor es un literal de cadena; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier literal de cadena, incluyendo delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nueva línea. Si el array está vacío, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de Trabajo Paso a Paso**

El siguiente flujo de trabajo describe cómo renderizar un array en una sola celda usando Smart Markers.

1. **Prepare el origen de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva un array. La propiedad puede devolver `string[]`, `int[]` o cualquier otro tipo de array compatible.
2. **Cree un libro de trabajo de diseño**: Cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda Smart Marker que haga referencia a la propiedad de array con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia del WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño y vincule su origen de datos usando el método `set_data_source`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.process()` para expandir los Smart Markers y poblar el libro de trabajo con datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo compatible.

### **Ejemplo de Código 1 — Renderizado Básico de Array de Cadenas**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

class Product:
    def __init__(self, tags):
        self._tags = tags
    
    def getTags(self):
        return self._tags

product = Product(["C#", "Aspose", "SmartMarker", "Excel"])

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Tags")
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = WorkbookDesigner()
designer.setWorkbook(workbook)
designer.setDataSource("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")

jpype.shutdownJVM()
```

### **Ejemplo de Código 2 — Array Numérico con Delimitador Personalizado**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook

# Definir la clase Student
class Student:
    def __init__(self):
        self.Scores = []

student = Student()
student.Scores = [95, 88, 76, 100, 67]

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

worksheet.getCells().get("A1").putValue("Scores")
worksheet.getCells().get("A2").putValue(" - ".join(str(s) for s in student.Scores))

workbook.save("output_numericArray.xlsx")

jpype.shutdownJVM()
```

### **Ejemplo de Código 3 — Comparación del Comportamiento Predeterminado vs. ArrayAsSingle**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, WorkbookDesigner

# Define la fuente de datos como un diccionario (equivalente a la clase Order)
order = {"Items": ["Apple", "Banana", "Cherry", "Date"]}

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Sección 1: Marcador inteligente predeterminado - valores distribuidos horizontalmente en las celdas
cells.get("A1").putValue("Default Spreading Behavior:")
cells.get("A2").putValue("&=Order.Items")

# Sección 2: Nueva renderización de una sola celda usando arrayasSingle y extraDelimiter
cells.get("A4").putValue("Single Cell Rendering (arrayasSingle=true):")
cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")")

# Vincular la fuente de datos y procesar los Marcadores Inteligentes
designer = WorkbookDesigner(workbook)
designer.setDataSource("Order", order)
designer.process()

# Guardar el libro de trabajo resultante
workbook.save("output_comparison.xlsx")

jpype.shutdownJVM()
```

### **Notas y Mejores Prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor de `extraDelimiter` se trata como un literal de cadena; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de celda única; cualquier otro valor vuelve al comportamiento de expansión predeterminado.
- Si el array está vacío o es nulo, la celda se deja vacía (o contiene una cadena en blanco según el tipo de datos).
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en arrays.
- Para salida separada por nueva línea, puede usar `\n` o la constante de nueva línea de la plataforma como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga suficiente ancho para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente en las celdas adyacentes según el formato.

## **Artículos Relacionados**

- [Smart Markers](/cells/es/python-java/smart-markers/)

{{< app/cells/assistant language="python" >}}