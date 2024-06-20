---
title: Mostrar y ocultar elementos
type: docs
weight: 60
url: /es/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells permite al usuario mostrar u ocultar elementos de un libro de trabajo incluyendo hojas de cálculo, filas, columnas, pestañas, barras de desplazamiento, líneas de cuadrícula,

{{% /alert %}}

## **Mostrar y ocultar una hoja de cálculo**

Un archivo de Excel puede tener una o más hojas de cálculo. Siempre que creamos un archivo de Excel, agregamos hojas de cálculo al archivo de Excel en el que trabajamos. Cada hoja de cálculo en un archivo de Excel es independiente de las demás hojas de cálculo al tener sus propios datos, configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de cálculo y mostrar otras en el archivo de Excel por su propio interés. Entonces, **Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de cálculo en sus archivos de Excel.

**Controlar la visibilidad de las hojas de cálculo:**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar una hoja de cálculo. Sin embargo, para controlar la visibilidad de una hoja de cálculo, los desarrolladores pueden usar el método [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Hacer visible una hoja de cálculo**

Los desarrolladores pueden hacer una hoja de cálculo visible pasando **true** como parámetro al método [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Ocultar una hoja de trabajo**

Los desarrolladores pueden ocultar una hoja de cálculo pasando **false** como parámetro al método [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

**Ejemplo:**

A continuación se muestra un ejemplo completo que demuestra el uso del método [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) para ocultar la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Hoja de cálculo - Antes de la modificación:**

En la captura de pantalla a continuación, puedes ver que el archivo **Book1.xls** contiene tres hojas de cálculo: **Hoja1**, **Hoja2** y **Hoja3**.

![todo:image_alt_text](show-and-hide-elements_1.png)

**Figura:** Vista de la hoja de cálculo antes de cualquier modificación

**Hoja de cálculo - Después de ejecutar el código de ejemplo:**

El archivo **Book1.xls** se abre usando la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y luego se hace oculta la primera hoja de cálculo del archivo **Book1.xls**. El archivo modificado se guarda como **output.xls** cuya vista pictórica se muestra a continuación:

![todo:image_alt_text](show-and-hide-elements_2.png)

**Figura:** Vista de la hoja de cálculo después de la modificación

**Establecer VisibilityType**

También puedes ocultar las hojas de cálculo de una manera especial. Esta característica puede ocultar la hoja de cálculo de modo que la única forma de hacerla visible de nuevo es dando [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) como valor de parámetro para el método [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) en el código (se debe señalar aquí que los usuarios no pueden hacer visible el objeto en MS Excel directamente utilizando sus opciones de menú). Los usuarios también pueden utilizar el método [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) para comprobar si una hoja de cálculo está marcada como Muy oculta o no.

## **Mostrar u ocultar pestañas**

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:

- Pestañas de hojas.
- Botones de desplazamiento de pestañas.

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.

**Pestañas de hojas y botones de desplazamiento de pestañas**

![todo:image_alt_text](show-and-hide-elements_3.png)

Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de hojas y los botones de desplazamiento en archivos de Excel.

**Controlar la visibilidad de las pestañas:**
Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel.

### **Ocultar pestañas**

Oculta las pestañas en un archivo de Excel configurando el método [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Hacer pestañas visibles**

Haz visibles las pestañas con el método [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Ejemplo de código completo:**

A continuación se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls.

Puedes ver que el archivo Book1.xls contiene pestañas en la figura de abajo. Después de ejecutar el código de ejemplo, las pestañas están ocultas, como se puede ver en la captura de pantalla del archivo output.xls de abajo.

**book1.xls: Archivo de Excel antes de cualquier modificación**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: Archivo de Excel después de la modificación**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Mostrar y ocultar filas y columnas**

Todas las hojas de cálculo en un archivo de Excel están compuestas por celdas que se organizan en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas, así como para identificar celdas individuales. Por ejemplo, las filas están numeradas – 1, 2, 3, 4, etc. – y las columnas están ordenadas alfabéticamente – A, B, C, D, etc. Los valores de fila y columna se muestran en los encabezados. Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

**Controlar la visibilidad de las hojas de cálculo:**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de cálculo en un archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase Worksheet proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para controlar la visibilidad de los encabezados de fila y columna, utiliza el método [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la clase Worksheet.

### **Ocultar encabezados de filas/columnas**

Ocultar encabezados de fila y columna mediante el método [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Hacer visibles los encabezados de fila/columna**

Hacer visibles los encabezados de fila y columna mediante el método [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

A continuación se muestra un ejemplo completo que demuestra cómo utilizar el método [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) para ocultar los encabezados de fila y columna de la primera hoja de cálculo de un archivo de Excel.

La captura de pantalla a continuación muestra que Book1.xls contiene tres hojas de cálculo: Sheet1, Sheet2 y Sheet3. Cada hoja de cálculo muestra los encabezados de fila y columna.

**Book1.xls: hoja de cálculo antes de la modificación**

![todo:image_alt_text](show-and-hide-elements_6.png)

Se abre Book1.xls utilizando la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y se ocultan los encabezados de fila y columna de la primera hoja de cálculo. El archivo modificado se guarda como output.xls.

**Vista de la hoja de cálculo después de la modificación**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento son muy útiles para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de cálculo. Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en los archivos de Excel.

**Controlar la visibilidad de las barras de desplazamiento:**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Sin embargo, para controlar la visibilidad de las barras de desplazamiento en el archivo de Excel, los desarrolladores pueden utilizar los métodos [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) y [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

### **Ocultar Barras de Desplazamiento**

Ocultar barras de desplazamiento estableciendo los métodos [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) en **false**.

### **Hacer visibles las Barras de Desplazamiento**

Hacer visibles las barras de desplazamiento estableciendo los métodos [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la clase Workbook en **true**.

**Ejemplo de código completo:**

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.

La captura de pantalla siguiente muestra el archivo Book1.xls que contiene ambas barras de desplazamiento. El archivo modificado se guarda como archivo output.xls, también se muestra a continuación.

**Book1.xls: Archivo de Excel antes de cualquier modificación**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: Archivo de Excel después de la modificación**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Mostrar y ocultar las cuadrículas**

Todas las hojas de cálculo de Microsoft Excel tienen líneas de cuadrícula de forma predeterminada. Ayudan a delimitar las celdas, de modo que sea fácil introducir datos en celdas específicas. Las líneas de cuadrícula nos permiten ver una hoja de cálculo como una colección de celdas, donde cada celda es fácilmente identificable.

Aspose.Cells también te permite controlar la visibilidad de las líneas de cuadrícula.

### **Controlar la visibilidad de las líneas de cuadrícula**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite acceder a cada hoja de cálculo en el archivo.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) proporciona una amplia variedad de propiedades y métodos para gestionar hojas de cálculo. Para controlar la visibilidad de las líneas de cuadrícula, utiliza el método [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Hacer visible las líneas de cuadrícula**

Para hacer visibles las líneas de cuadrícula, utiliza el método [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) .

#### **Ocultar líneas de cuadrícula**

Oculta las líneas de cuadrícula utilizando el método [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{% alert color="primary" %}}

Las líneas de cuadrícula se aplican a toda la hoja. Para 'ocultar' las líneas de cuadrícula en una sección de una hoja de cálculo, utiliza [formato de borde](/cells/es/java/create-table-by-using-border-lines-for-a-range/) para establecer los bordes a un color que se mezcle con el esquema de color de la hoja.

{{% /alert %}}

**Ejemplo: Ocultar líneas de cuadrícula en una hoja de cálculo en particular**

El ejemplo a continuación demuestra el uso del método [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) para ocultar las líneas de cuadrícula de la primera hoja de cálculo de un archivo de Excel.

La captura de pantalla a continuación muestra que el archivo Book1.xls contiene tres hojas de cálculo: Sheet1, Sheet2 y Sheet3. Todas estas hojas de cálculo tienen líneas de cuadrícula.

**Vista de la hoja de cálculo antes de la modificación**

![todo:image_alt_text](show-and-hide-elements_10.png)

El archivo Book1.xls se abre usando la clase [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) y luego se ocultan las líneas de cuadrícula de la primera hoja de cálculo. El archivo modificado se guarda como archivo output.xls.

**Vista de la hoja de cálculo después de la modificación**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Artículos relacionados**

{{% alert color="primary" %}}

- [Funciones de configuración de página](/cells/es/java/page-setup-features/).
- [Agregar bordes a celdas para crear una tabla](/cells/es/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
