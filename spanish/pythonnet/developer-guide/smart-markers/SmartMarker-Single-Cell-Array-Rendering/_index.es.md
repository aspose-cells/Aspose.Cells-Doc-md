---
title: Renderizado de matriz de celda única SmartMarker | Aspose.Cells for Python via .NET
linktitle: Renderizado de matriz de celda única SmartMarker | Aspose.Cells
description: Aprenda a renderizar datos de matriz en una sola celda utilizando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, biblioteca de Python via .NET, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz de celda única, renderizado de matriz, plantilla
type: docs
weight: 195
url: /es/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la renderización de datos de matriz en una sola celda a través de Smart Markers. Al utilizar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, proporcionando un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente función basada en plantillas que le permite llenar dinámicamente datos de hojas de cálculo usando expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.

Por defecto, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente separada, ya sea horizontalmente a lo largo de una fila o verticalmente por una columna. Si bien este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría renderizar toda la matriz en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta Smart Marker, abordan exactamente este requisito. Le permiten mantener diseños de informes compactos y predecibles mientras trabaja de forma nativa con orígenes de datos de matrices.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de expansión de matriz**

Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando el contenido de la plantilla hacia afuera y potencialmente rompiendo diseños de informes cuidadosamente diseñados.

### **Limitaciones de los casos de uso**

Hay muchos escenarios prácticos donde el comportamiento de expansión predeterminado no es deseable:

- **Informes de estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o por pipes dentro de una sola celda.
- **Indicadores de chips de filtro o estado** que agrupan varios valores en un solo lugar para facilitar la lectura.
- **Pipelines posteriores** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no toleran matrices que se extienden a través de varias celdas.

### **La brecha que llena**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar datos en Python, uniendo matrices en cadenas delimitadas antes de enlazarlas al diseñador de libros de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la función**

El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee: coma, punto y coma, guion, pipe, nueva línea o cualquier texto personalizado.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta Smart Marker.
- **Informes más limpios**: Los datos de la matriz ya no empujan el contenido de la plantilla vecina a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de dato que se pueda unir con un delimitador.
- **Compatibilidad con versiones anteriores**: Cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo usar esta función**

### **Sintaxis del Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en el origen de datos enlazado.
- `arrayasSingle=true` — indica al motor que renderice toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es una cadena literal; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier cadena literal, incluyendo delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nueva línea. Si la matriz está vacía, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda usando Smart Markers.

1. **Preparar el origen de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `list[str]`, `list[int]` o cualquier otro tipo de matriz compatible.
2. **Crear un libro de trabajo de diseño**: Cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda Smart Marker que haga referencia a la propiedad de la matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Instanciar el WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño a él y enlace su origen de datos usando el método `set_data_source`.
4. **Procesar los marcadores**: Llame al método `WorkbookDesigner.process()` para expandir los Smart Markers y llenar el libro de trabajo con datos reales.
5. **Guardar el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo compatible.

### **Ejemplo de código 1 — Renderizado básico de matriz de cadenas**

```python
class Product:
    def __init__(self):
        self.Tags = []

product = Product()
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Tags")
worksheet.cells["A2"].put_value("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")")

designer = ac.WorkbookDesigner()
designer.workbook = workbook
designer.set_data_source("Product", product)
designer.process()

workbook.save("output_arraySingle.xlsx")
```

### **Ejemplo de código 2 — Matriz numérica con delimitador personalizado**

```python
class Student:
    def __init__(self):
        self.scores = []


student = Student()
student.scores = [95, 88, 76, 100, 67]

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Scores")
worksheet.cells["A2"].put_value(" - ".join(str(s) for s in student.scores))

workbook.save("output_numericArray.xlsx")
```

### **Ejemplo de código 3 — Comparación del comportamiento predeterminado frente a ArrayAsSingle**

```python
class Order:
    def __init__(self, items):
        self._items = items

    @property
    def Items(self):
        return self._items

    @Items.setter
    def Items(self, value):
        self._items = value

order = Order(["Apple", "Banana", "Cherry", "Date"])

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# Sección 1: Marcador Inteligente Predeterminado - valores distribuidos horizontalmente en las celdas
cells["A1"].put_value("Default Spreading Behavior:")
cells["A2"].put_value("&=Order.Items")

# Sección 2: Nueva renderización de celda única usando arrayasSingle y extraDelimiter
cells["A4"].put_value("Single Cell Rendering (arrayasSingle=true):")
cells["A5"].put_value('&=Order.Items(arrayasSingle=true, extraDelimiter="; ")')

# Vincular la fuente de datos y procesar Marcadores Inteligentes
designer = ac.WorkbookDesigner(workbook)
designer.set_data_source("Order", order)
designer.process()

# Guardar el libro de trabajo resultante
workbook.save("output_comparison.xlsx")
```

### **Notas y mejores prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor de `extraDelimiter` se trata como una cadena literal; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`True` / `False`). Solo `True` activa el comportamiento de celda única; cualquier otro valor vuelve al comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de datos).
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para salida separada por nueva línea, puede usar `\n` o `os.linesep` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga el ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente a las celdas adyacentes según el formato.

## **Artículos relacionados**

- [Smart Markers](/cells/es/python-net/smart-markers/)
- [Combinar y separar celdas](/cells/es/python-net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="python" >}}