---
title: Mostrar y ocultar elementos
type: docs
weight: 60
url: /es/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells permite al usuario mostrar y ocultar elementos de un libro de trabajo, incluidas hojas de trabajo, filas, columnas, pestañas, barras de desplazamiento, líneas de cuadrícula,

{{% /alert %}}

## **Mostrar y ocultar una hoja de trabajo**

 Un archivo de Excel puede tener una o más hojas de trabajo. Cada vez que creamos un archivo de Excel, agregamos hojas de trabajo al archivo de Excel en el que trabajamos. Cada hoja de trabajo en un archivo de Excel es independiente de la otra hoja de trabajo al tener sus propios datos y configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de trabajo y otras visibles en el archivo de Excel para su propio interés. Asi que,**Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de trabajo en sus archivos de Excel.

**Controlando la Visibilidad de las Hojas de Trabajo:**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel.[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)que permite acceder a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar una hoja de cálculo. Pero, para controlar la visibilidad de una hoja de trabajo, los desarrolladores pueden usar[**conjuntoVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

### **Hacer una hoja de trabajo visible**

 Los desarrolladores pueden hacer que una hoja de trabajo sea visible pasando**verdadero** como parámetro de la[**conjuntoVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

### **Ocultar una hoja de trabajo**

 Los desarrolladores pueden ocultar una hoja de trabajo pasando**falso** como parámetro de la[**conjuntoVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) metodo de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

**Ejemplo:**

 A continuación se muestra un ejemplo completo que demuestra el uso de[**setVisible(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) método de[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class para ocultar la primera hoja de cálculo del archivo de Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Hoja de trabajo - Antes de la modificación:**

 En la captura de pantalla a continuación, puede ver que**Libro1.xls** El archivo contiene tres hojas de trabajo:**Hoja1** , **Hoja2** y**Hoja3** .

![todo:imagen_alternativa_texto](show-and-hide-elements_1.png)

**Figura:** Vista de hoja de trabajo antes de cualquier modificación

**Hoja de trabajo: después de ejecutar el código de ejemplo:**

**Libro1.xls** El archivo se abre con el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase y luego la primera hoja de trabajo del**Libro1.xls** el archivo se hace oculto. El archivo modificado se guarda como**salida.xls**archivo cuya vista pictórica se muestra a continuación:

![todo:imagen_alternativa_texto](show-and-hide-elements_2.png)

**Figura:** Vista de hoja de trabajo después de la modificación

**Configuración del tipo de visibilidad**

 También puede ocultar las hojas de trabajo de una manera especial. Esta característica puede ocultar la hoja de trabajo para que la única forma de hacerla visible nuevamente sea dando[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) como valor de parámetro para el[**establecer tipo de visibilidad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) en el código (se debe tener en cuenta aquí, el usuario no puede hacer que el objeto sea visible en MS Excel directamente usando sus opciones de menú). Los usuarios también pueden utilizar[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) método para verificar si una hoja de trabajo está marcada como VeryHidden o no.

## **Mostrar u ocultar pestañas**

Si observa detenidamente la parte inferior de un archivo de Excel Microsoft, verá una serie de controles. Éstos incluyen:

- Pestañas de hoja.
- Botones de desplazamiento de pestañas.

Las pestañas de hoja representan las hojas de trabajo en el archivo de Excel. Haga clic en cualquier pestaña para cambiar a esa hoja de trabajo. Cuantas más hojas de trabajo haya en el libro de trabajo, más pestañas de hojas habrá. Si el archivo de Excel tiene una buena cantidad de hojas de trabajo, necesita botones para navegar por ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de las hojas.

**Fichas de hojas y botones de desplazamiento de fichas**

![todo:imagen_alternativa_texto](show-and-hide-elements_3.png)

Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de las hojas y los botones de desplazamiento de las pestañas en los archivos de Excel.

**Controlando la visibilidad de las pestañas:**
 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel.

### **Ocultar pestañas**

 Ocultar pestañas en un archivo de Excel configurando el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase'[**getSettings().setShowTabs(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Hacer pestañas visibles**

 Haz que las pestañas sean visibles con el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase'[**getSettings().setShowTabs(verdadero)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) método.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Ejemplo de código completo:**

A continuación se muestra un ejemplo completo que abre un archivo de Excel (libro1.xls), oculta sus pestañas y guarda el archivo modificado como salida.xls.

Puede ver que el archivo Book1.xls contiene pestañas en la siguiente figura. Después de ejecutar el código de ejemplo, las pestañas se ocultan, como puede ver en la captura de pantalla del archivo output.xls a continuación.

**book1.xls: archivo de Excel antes de cualquier modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_4.png)

**output.xls: archivo de Excel después de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Mostrar y ocultar filas y columnas**

Todas las hojas de trabajo en un archivo de Excel se componen de celdas que se organizan en filas y columnas. Todas las filas y columnas tienen valores únicos que se utilizan para identificarlas y para identificar celdas individuales. Por ejemplo, las filas están numeradas (1, 2, 3, 4, etc.) y las columnas están ordenadas alfabéticamente (A, B, C, D, etc.). Los valores de fila y columna se muestran en los encabezados. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de estos encabezados de fila y columna.

**Controlando la Visibilidad de las Hojas de Trabajo:**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en un archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)clase. La clase Worksheet proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para controlar la visibilidad de los encabezados de fila y columna, use la clase Worksheet[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) método.

### **Ocultar encabezados de fila/columna**

 Oculte los encabezados de fila y columna con el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setRowColumnHeadersVisible(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) método.

### **Hacer visibles los encabezados de fila/columna**

 Haga que los encabezados de fila y columna sean visibles usando el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setRowColumnHeadersVisible(verdadero)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) método.

 A continuación se proporciona un ejemplo completo que demuestra cómo utilizar el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setRowColumnHeadersVisible(falso)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) método para ocultar los encabezados de fila y columna de la primera hoja de cálculo de un archivo de Excel.

La siguiente captura de pantalla muestra que Book1.xls contiene tres hojas de trabajo: Sheet1, Sheet2 y Sheet3. Cada hoja de trabajo muestra encabezados de fila y columna.

**Book1.xls: hoja de trabajo antes de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_6.png)

 Book1.xls se abre usando el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' y los encabezados de fila y columna en la primera hoja de trabajo están ocultos. El archivo modificado se guarda como salida.xls.

**Vista de hoja de trabajo después de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Mostrar y ocultar barras de desplazamiento**

Las barras de desplazamiento son muy utilizadas para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de trabajo. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en archivos de Excel.

**Controlando la visibilidad de las barras de desplazamiento:**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel.[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Pero, para controlar la visibilidad de las barras de desplazamiento en el archivo de Excel, los desarrolladores pueden usar[**establecerVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) métodos de la[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase.

### **Ocultar barras de desplazamiento**

 Oculte las barras de desplazamiento configurando el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase'[**establecerVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) métodos para**falso**.

### **Haciendo visibles las barras de desplazamiento**

 Haga que las barras de desplazamiento sean visibles configurando la clase Workbook'[**establecerVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) o[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) métodos para**verdadero**.

**Ejemplo de código completo:**

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como salida.xls.

La siguiente captura de pantalla muestra el archivo Book1.xls que contiene ambas barras de desplazamiento. El archivo modificado se guarda como archivo de salida.xls, también se muestra a continuación.

**Book1.xls: archivo de Excel antes de cualquier modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_8.png)

**output.xls: archivo de Excel después de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Mostrar y ocultar líneas de cuadrícula**

Todas las hojas de cálculo de Excel Microsoft tienen líneas de cuadrícula de forma predeterminada. Ayudan a delinear las celdas, de modo que es fácil ingresar datos en celdas particulares. Las líneas de cuadrícula nos permiten ver una hoja de trabajo como una colección de celdas, donde cada celda es fácilmente identificable.

Aspose.Cells también le permite controlar la visibilidad de las líneas de cuadrícula.

### **Control de la visibilidad de las líneas de cuadrícula**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la clase contiene un[**Colección de hojas de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) que permite el acceso a cada hoja de trabajo en el archivo.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase. los[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para controlar la visibilidad de las líneas de cuadrícula, utilice el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) método.

#### **Hacer visibles las líneas de cuadrícula**

 Para hacer visibles las líneas de cuadrícula, use el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) método.

#### **Ocultar líneas de cuadrícula**

 Oculte las líneas de cuadrícula con el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) método.

{{% alert color="primary" %}}

Las líneas de cuadrícula se aplican a toda la hoja. Para 'ocultar' líneas de cuadrícula en una sección de una hoja de trabajo, use[formato de borde](/cells/es/java/create-table-by-using-border-lines-for-a-range/) para establecer los bordes en un color que se mezcle con el esquema de color de la hoja.

{{% /alert %}}

**Ejemplo: Ocultar líneas de cuadrícula en una hoja de trabajo en particular**

 El siguiente ejemplo demuestra el uso de la[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) método para ocultar las líneas de cuadrícula de la primera hoja de cálculo de un archivo de Excel.

La siguiente captura de pantalla muestra que el archivo Book1.xls contiene tres hojas de trabajo: Sheet1, Sheet2 y Sheet3. Todas estas hojas de trabajo tienen líneas de cuadrícula.

**Vista de hoja de trabajo antes de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_10.png)

 El archivo Book1.xls se abre con el[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) clase y luego se ocultan las líneas de cuadrícula de la primera hoja de trabajo. El archivo modificado se guarda como archivo de salida.xls.

**Vista de hoja de trabajo después de la modificación**

![todo:imagen_alternativa_texto](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Artículos relacionados**

{{% alert color="primary" %}}

- [Funciones de configuración de página](/cells/es/java/page-setup-features/).
- [Agregar bordes a las celdas para crear una tabla](/cells/es/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
