---
title: Representación de matrices en una sola celda con SmartMarker | Aspose.Cells for Python via .NET
description: Aprenda a representar datos de matrices en una sola celda mediante los atributos `arrayassingle` y `arraydelimiter` de marcadores inteligentes en Aspose.Cells for Python via .NET.
linktitle: Representación de matrices en una sola celda | Aspose.Cells
url: /es/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, biblioteca de Python mediante .NET, hoja de cálculo, marcadores inteligentes, arrayassingle, arraydelimiter, matriz de una sola celda, representación de matrices, plantilla
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells puede representar un origen de datos de tipo matriz en una sola celda mediante marcadores inteligentes. El atributo `arrayassingle` desactiva la expansión predeterminada elemento por elemento, y el atributo `arraydelimiter` selecciona el separador que se coloca entre los elementos combinados: una coma de forma predeterminada o cualquier carácter individual o cadena de varios caracteres entre comillas que se especifique.
{{% /alert %}}

## **Introducción**

Los marcadores inteligentes de Aspose.Cells son una función basada en plantillas que rellena dinámicamente los datos de hojas de cálculo mediante expresiones de marcador como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando `WorkbookDesigner` procesa la plantilla, los marcadores se sustituyen por los valores del origen de datos proporcionado.
De forma predeterminada, cuando un marcador inteligente hace referencia a un campo de matriz (por ejemplo, `&=Product.Tags` vinculado a una lista de cuatro valores), el motor expande la matriz y coloca cada elemento en su propia celda, distribuyendo los valores verticalmente hacia abajo en la columna situada bajo el marcador. Aunque este comportamiento resulta práctico en muchos escenarios, hay situaciones en las que conviene representar toda la matriz en una sola celda, concatenando los elementos y separándolos con el delimitador que se elija.
Los atributos `arrayassingle` y `arraydelimiter`, escritos dentro de los paréntesis de un marcador inteligente en forma `name:value`, cubren exactamente esta necesidad. Permiten mantener los diseños de informes compactos y predecibles mientras siguen funcionando de forma nativa con orígenes de datos de tipo matriz.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de expansión de matrices**

Cuando un marcador inteligente hace referencia a un campo de matriz, Aspose.Cells expande la matriz en varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` que utiliza una lista con cuatro valores coloca cada valor en su propia celda debajo del marcador, desplazando el resto del contenido de la plantilla y posiblemente alterando diseños de informe cuidadosamente definidos.

### **Limitaciones de los casos de uso**

Existen muchos escenarios prácticos en los que no conviene el comportamiento predeterminado de expansión:
- **Informes de tipo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Chips de filtro o indicadores de estado** que agrupan varios valores en un mismo lugar para facilitar la lectura.
- **Flujos de trabajo posteriores** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no pueden tolerar matrices que se extienden por varias celdas.

### **La brecha que cubre**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en Python: unir las listas en cadenas delimitadas antes de vincularlas al `WorkbookDesigner`. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `arrayassingle` y `arraydelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio marcador inteligente.

## **Ventajas de la función**

El uso de los atributos `arrayassingle` y `arraydelimiter` en los marcadores inteligentes ofrece varias ventajas:
- **Contención en una sola celda**: Todos los elementos de la matriz se representan en exactamente una celda, lo que mantiene los diseños compactos y predecibles.
- **Control del delimitador personalizado**: Especifique el separador que prefiera: una coma de forma predeterminada, un punto y coma, un guion, una barra vertical o una cadena de varios caracteres entre comillas como `" | "`.
- **Formato basado en plantillas**: No se necesita código adicional para preprocesar los datos; las reglas de formato se definen dentro de la etiqueta del marcador inteligente.
- **Informes más limpios**: Los datos de tipo matriz ya no desplazan el contenido contiguo de la plantilla a distintas filas o columnas.
- **Tipos de datos versátiles**: Funciona con listas de cadenas y listas numéricas proporcionadas como filas JSON.
- **Retrocompatibilidad**: Cuando se omiten los atributos, se conserva el comportamiento original de expansión, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo utilizar esta función**

### **Sintaxis de los marcadores inteligentes**

Los atributos `arrayassingle` y `arraydelimiter` utilizan la gramática de atributos `name:value` de Aspose.Cells dentro de los paréntesis de un marcador inteligente estándar. La sintaxis general es:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

El marcador está compuesto por las siguientes partes:
- `&=DataSource.ArrayField` — el marcador inteligente estándar que hace referencia al campo de matriz del origen de datos vinculado.
- `arrayassingle:true` — indica al motor que represente toda la matriz en una sola celda en lugar de expandir sus elementos.
- `arraydelimiter:;` — es opcional; define el separador que se coloca entre los elementos de la matriz. Si se omite, se utiliza una coma.

{{% alert color="warning" %}}
Escriba los atributos en forma `name:value` (con dos puntos, no un signo igual) y separe varios atributos con una coma **sin espacios**. Un espacio después de la coma desplaza el valor analizado un carácter: `(arrayassingle:true, arraydelimiter:;)` combinaría los elementos con el separador incorrecto `:;` en lugar de `;`.
{{% /alert %}}

### **Formas del delimitador**

- Un carácter individual se escribe directamente después de los dos puntos: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separador de varios caracteres se escribe entre comillas dobles: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo representar una matriz en una sola celda mediante marcadores inteligentes.
1. **Prepare el origen de datos**: Organice cada registro como un objeto JSON cuyo campo contenga una matriz, por ejemplo `{"Tags": ["C#", "Aspose"]}`. Las instancias sencillas de clases de Python, los diccionarios y las listas que se pasan a `set_data_source` no vinculan campos de matriz en esta plataforma; las filas JSON son el formato tabular admitido.
2. **Cree un libro de trabajo de diseño**: Cree un `Workbook` nuevo, añada una fila de encabezado y coloque en una celda un marcador inteligente que haga referencia al campo de matriz con el atributo `arrayassingle` (y `arraydelimiter` cuando necesite un separador personalizado).
3. **Cree una instancia de `WorkbookDesigner`**: Cree un `WorkbookDesigner` alrededor del libro de trabajo y adjunte sus filas JSON con `set_json_data_source`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.process()` para expandir los marcadores inteligentes y rellenar el libro de trabajo con los datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo admitido.

### **Ejemplo de código 1: representación de una matriz de cadenas básica**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

El ejemplo imprime el valor combinado de toda la matriz. Las cuatro etiquetas se colocan en una sola celda, separadas por la coma predeterminada:

```
C#,Aspose,SmartMarker,Excel
```

### **Ejemplo de código 2: matriz numérica con un delimitador personalizado**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

Los números JSON se combinan exactamente igual que las cadenas: cada elemento conserva su representación numérica sin formato:

```
95-88-76-100-67
```

### **Ejemplo de código 3: comparación entre la representación predeterminada y la de una sola celda**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

El marcador predeterminado llena una celda por cada elemento a lo largo de la columna B, mientras que el marcador `arrayassingle` concentra la misma matriz en una sola celda de la columna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notas y prácticas recomendadas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `arrayassingle` y `arraydelimiter`:
- Los valores de los atributos usan la forma `name:value`. No se reconoce una forma con signo igual, como `arrayassingle=true`, y el sistema recurre silenciosamente al comportamiento predeterminado de expansión.
- Separe los atributos con una coma y sin espacios; un espacio después de la coma desplaza un carácter el valor del delimitador (consulte la advertencia anterior).
- El valor de `arraydelimiter` puede ser un carácter individual escrito directamente después de los dos puntos o una cadena de varios caracteres entre comillas dobles.
- Cuando se omite `arraydelimiter`, los elementos se combinan con una coma.
- Proporcione los campos de matriz mediante objetos de fila de `set_json_data_source`. Los objetos Python sencillos y los diccionarios que se pasan a `set_data_source` no se vinculan en esta plataforma, y un `ICellsDataTable` personalizado cuya columna devuelve una lista de Python representa el texto del contenedor de la lista en lugar de combinar sus elementos.
- Los números JSON conservan su forma de entero sin formato en la salida combinada.

## **Artículos relacionados**
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Python via .NET](/cells/es/python-net/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Python via .NET](/cells/es/python-net/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una tabla dinámica](/cells/es/python-net/change-page-field-layout/)
- [Convertir minigráficos a imagen y HTML en Aspose.Cells for Python via .NET](/cells/es/python-net/convert-sparkline-to-image-and-html/)
- [Conversión de Excel a formato OFD](/cells/es/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}