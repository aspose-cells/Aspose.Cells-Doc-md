---
title: Gestionar controles
type: docs
weight: 150
url: /es/python-net/managing-controls/
---

## **Introducción**

Los desarrolladores pueden agregar diferentes objetos de dibujo, como cuadros de texto, casillas de verificación, botones de opción, cuadros combinados, etiquetas, botones, líneas, rectángulos, arcos, óvalos,spinner, barras de desplazamiento, cuadros de agrupamiento, etc. Aspose.Cells para Python via .NET proporciona el espacio de nombres Aspose.Cells.Drawing, que contiene todos los objetos de dibujo. Sin embargo, hay algunos objetos de dibujo o formas que aún no son compatibles. Crea estos objetos en un archivo de Excel de diseñador usando Microsoft Excel y luego importa el archivo de diseñador a Aspose.Cells. Aspose.Cells para Python via .NET permite cargar estos objetos de dibujo desde un archivo de diseñador y escribirlos en un archivo generado.

## **Adición de un control de cuadro de texto a una hoja de cálculo**

Una forma de resaltar información importante en un informe es usar un cuadro de texto. Por ejemplo, agregar texto para resaltar el nombre de la empresa o indicar la región geográfica con las mayores ventas, etc. Aspose.Cells para Python via .NET ofrece la clase [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection), utilizada para agregar un nuevo cuadro de texto a la colección. Existe otra clase, [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox), que representa un cuadro de texto utilizado para definir todo tipo de configuraciones. Tiene algunos miembros importantes:

- La propiedad [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) devuelve un objeto [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) utilizado para ajustar el contenido del cuadro de texto.
- La propiedad [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el tipo de colocación.
- La propiedad [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) especifica los atributos de fuente.
- El método [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) agrega un hipervínculo al cuadro de texto.
- La propiedad [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) devuelve un objeto [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) utilizado para establecer el formato de relleno para el cuadro de texto.
- La propiedad [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) devuelve el objeto [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) utilizado generalmente para el estilo y peso de la línea del cuadro de texto.
- La propiedad [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica el texto de entrada para el cuadro de texto.

El siguiente ejemplo crea dos cuadros de texto en la primera hoja de cálculo del libro. El primer cuadro de texto está bien decorado con diferentes ajustes de formato. El segundo es simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Manipulación de controles de cuadro de texto en hojas de cálculo de diseño**

Aspose.Cells para Python via .NET también permite acceder a los cuadros de texto en las hojas de trabajo del diseñador y manipularlos. Usa la propiedad [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) para obtener la colección de cuadros de texto en la hoja.

El siguiente ejemplo utiliza el archivo de Microsoft Excel que creamos en el ejemplo anterior. Obtiene las cadenas de texto de los dos cuadros de texto y cambia el texto del segundo cuadro de texto para guardar el archivo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Adición de un control de casilla de verificación a una hoja de cálculo**

Las casillas de verificación son útiles si quieres brindar a un usuario una forma de elegir entre dos opciones, como verdadero o falso; sí o no. Aspose.Cells para Python via .NET permite usar casillas de verificación en las hojas de trabajo. Por ejemplo, puede que hayas desarrollado una hoja de proyección financiera en la que puedes considerar una adquisición en particular o no. En este caso, es posible que desees colocar una casilla de verificación en la parte superior de la hoja. Luego, puedes vincular el estado de esta casilla a otra celda, de modo que si la casilla está marcada, el valor de la celda sea verdadero; si no está marcada, que sea falso.

### **Usar Microsoft Excel**

Para colocar un control de casilla de verificación en su hoja de cálculo, siga estos pasos:

1. Asegúrese de que aparezca la barra de herramientas de formularios.
1. Haga clic en la herramienta **Cuadro de verificación** en la barra de herramientas de Formularios.
1. En el área de su hoja de cálculo, haga clic y arrastre para definir el rectángulo que contendrá el cuadro de verificación y la etiqueta junto al cuadro de verificación.
1. Una vez que se coloque el cuadro de verificación, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1. En el campo **Vínculo de celda**, especifique la dirección de la celda a la que debe estar vinculado este cuadro de verificación.
1. Haz clic en **Aceptar**.

### **Usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET proporciona la clase [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection), que se usa para agregar una nueva casilla de verificación a la colección. Existe otra clase, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), que representa una casilla de verificación. Tiene algunos miembros importantes:

- La propiedad [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda que está vinculada al cuadro de verificación.
- La propiedad [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica la cadena de texto asociada con el cuadro de verificación. Es la etiqueta del cuadro de verificación.
- La propiedad [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) especifica si el cuadro de verificación está marcado o no.

El siguiente ejemplo muestra cómo agregar un cuadro de verificación a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

## **Agregar control de botón de opción a la hoja de cálculo**

Un botón de opción, o un botón de opción, es un control hecho de un cuadro redondo. El usuario toma su decisión seleccionando el cuadro redondo. Un botón de opción generalmente, si no siempre, está acompañado por otros. Estos botones de opción aparecen y se comportan como un grupo. El usuario decide qué botón es válido seleccionando solo uno de ellos. Cuando el usuario hace clic en un botón, se llena. Cuando se selecciona un botón en el grupo, los botones del mismo grupo están vacíos.

### **Usar Microsoft Excel**

Para colocar un control de botón de opción en su hoja de cálculo, siga estos pasos:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haga clic en la herramienta **Botón de opción**.
1. En la hoja de cálculo, haga clic y arrastre para definir el rectángulo que contendrá el botón de opción y la etiqueta junto al botón de opción.
1. Una vez que se coloca el botón de opción en la hoja de cálculo, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1. En el campo **Vínculo de celda**, especifique la dirección de la celda a la que debe estar vinculado este botón de opción.
1. Haz clic en **Aceptar**.

### **Usando Aspose.Cells para Python via .NET**

La clase [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button), que se utiliza para agregar un control de botón de opción a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton). La clase [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) representa un botón de opción. Tiene algunos miembros importantes:

- La propiedad [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda vinculada al botón de opción.
- La propiedad [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica la cadena de texto asociada al botón de opción. Es la etiqueta del botón de opción.
- La propiedad [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) especifica si el botón de opción está marcado o no.
- La propiedad [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) especifica el formato de relleno del botón de opción.
- La propiedad [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) especifica los estilos de formato de línea del botón de opción.

El siguiente ejemplo muestra cómo agregar botones de opción a una hoja de cálculo. El ejemplo agrega tres botones de opción que representan grupos de edad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

## **Agregando control de lista desplegable a una hoja de cálculo**

Para facilitar la entrada de datos, o para limitar las entradas a ciertos elementos que defina, puede crear una lista desplegable, o lista de entradas válidas que se compila a partir de celdas en otra parte de la hoja de cálculo. Cuando crea una lista desplegable para una celda, muestra una flecha junto a esa celda. Para introducir información en esa celda, haz clic en la flecha, y luego haz clic en la entrada que deseas.

### **Usar Microsoft Excel**

Para colocar un control de lista desplegable en tu hoja de cálculo, sigue estos pasos:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haz clic en la herramienta **Lista desplegable**.
1. En la área de tu hoja de cálculo, haz clic y arrastra para definir el rectángulo que contendrá la lista desplegable.
1. Una vez que la lista desplegable esté colocada en la hoja de cálculo, haz clic con el botón derecho en el control para hacer clic en **Control de formato** y especifica el rango de entrada.
1. En el campo **Vínculo de celda**, especifica la dirección de la celda a la que debe estar vinculada esta lista desplegable.
1. Haz clic en **Aceptar**.

### **Usando Aspose.Cells para Python via .NET**

La clase [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box), que se utiliza para agregar un control de cuadro combinado a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox). La clase [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) representa un cuadro combinado. Tiene algunos miembros importantes:

- La propiedad [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda que está vinculada al cuadro combinado.
- La propiedad [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) especifica el rango de celdas de la hoja de cálculo utilizadas para rellenar el cuadro combinado.
- La propiedad [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) especifica el número de líneas de lista que se muestran en la parte desplegable de un cuadro combinado.
- La propiedad [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) indica si el cuadro combinado tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Agregando un control de etiqueta a una hoja de cálculo**

Las etiquetas son un medio para brindar información a los usuarios sobre el contenido de una hoja de cálculo. Aspose.Cells para Python via .NET hace posible agregar y manipular etiquetas en una hoja de cálculo. La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label), que se usa para agregar un control de etiqueta a la hoja de cálculo. El método devuelve un objeto [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). La clase [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) representa una etiqueta en la hoja de cálculo. Tiene algunos miembros importantes:

- El método [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica una cadena de título de la etiqueta.
- El método [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que la etiqueta está unida a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar una etiqueta a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

## **Agregando un control de cuadro de lista a una hoja de cálculo**

Un control de cuadro de lista crea un control de lista que permite la selección de uno o varios elementos.

### **Usar Microsoft Excel**

Para colocar un control de cuadro de lista en una hoja de cálculo:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haga clic en la herramienta **Cuadro de lista**.
1. En el área de la hoja de cálculo, haga clic y arrastre para definir el rectángulo que contendrá el cuadro de lista.
1. Una vez que el cuadro de lista esté colocado en la hoja de cálculo, haga clic derecho en el control para hacer clic en **Formato de control** y especificar el rango de entrada.
1. En el campo **Vínculo de celda**, especifique la dirección de la celda a la que debe estar vinculado este cuadro de lista y establezca el atributo de tipo de selección (Simple, Múltiple, Extender).
1. Haz clic en **Aceptar**.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box), que se utiliza para agregar un control de lista a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox). La clase [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) representa un cuadro de lista. Tiene algunos miembros importantes:

- El método [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda que está vinculada al cuadro de lista.
- El método [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) especifica el rango de celdas de la hoja de cálculo usadas para rellenar el cuadro de lista.
- El método [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) especifica el modo de selección del cuadro de lista.
- El método [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) indica si el cuadro de lista tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de lista a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Agregando Control de Botón a una Hoja de Cálculo**

Los botones son útiles para realizar algunas acciones. A veces, es útil asignar un Macro de VBA al botón o asignar un hipervínculo para abrir una página web.

### **Usar Microsoft Excel**

Para colocar un control de botón en tu hoja de cálculo:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haz clic en la herramienta **Botón**.
1. En el área de tu hoja de cálculo, haz clic y arrastra para definir el rectángulo que contendrá el botón.
1. Una vez que el cuadro de lista esté colocado en la hoja de cálculo, haz clic derecho sobre el control y selecciona **Formato de control**, luego especifica un Macro de VBA y atributos relacionados con fuente, alineación, tamaño, margen, etc.
1. Haz clic en **Aceptar**.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button), utilizado para agregar un control de botón a la hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button). La clase [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) representa un botón. Tiene algunos miembros importantes:

- La propiedad [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica la leyenda del botón.
- La propiedad [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) especifica los atributos de fuente para la etiqueta del control de botón.
- La propiedad [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que el botón se conecta a las celdas en la hoja de cálculo.
- La propiedad [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) agrega un hipervínculo para el control de botón. Al hacer clic en el botón, se navegará a la URL relacionada.

El siguiente ejemplo muestra cómo agregar un botón a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Agregar control de línea a la hoja de cálculo**

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haga clic en **formas automáticas**, apunte a **líneas** y seleccione el estilo de línea que desee.
1. Arrastre para dibujar la línea.
1. Haz uno o ambos de los siguientes:
   1. Para restringir la línea para dibujar en ángulos de 15 grados desde su punto de partida, mantenga presionada la tecla MAYÚS mientras arrastra.
   1. Para alargar la línea en direcciones opuestas desde el primer punto final, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line), que se utiliza para agregar una forma de línea a la hoja de cálculo. El método devuelve un objeto [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape). La clase [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) representa una línea. Tiene algunos miembros importantes:

- El método [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) especifica el formato de una línea.
- El método [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que la línea está conectada a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar líneas a la hoja de cálculo. Crea tres líneas con diferentes estilos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Agregar una cabeza de flecha a una línea**

Aspose.Cells para Python via .NET también permite dibujar líneas de flechas. Es posible agregar una punta de flecha a una línea y formatear la línea. Por ejemplo, puedes cambiar el color de la línea, o especificar el peso y el estilo de la línea.

El siguiente ejemplo muestra cómo agregar una cabeza de flecha a una línea.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Agregar control de rectángulo a una hoja de cálculo**

Aspose.Cells para Python via .NET permite dibujar formas rectangulares en tus hojas de cálculo. Puedes crear un rectángulo, cuadrado, etc. También se permite formatear el color de relleno y el color de la línea del borde del control. Por ejemplo, puedes cambiar el color del rectángulo, establecer el color de sombreado, especificar el peso y el estilo del rectángulo según lo necesites.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Rectángulo**.
1. Arrastra para dibujar el rectángulo.
1. Haz uno o ambos de los siguientes:
   1. Para restringir el rectángulo y dibujar un cuadrado desde su punto de inicio, mantén presionada la tecla SHIFT mientras arrastras.
   1. Para dibujar un rectángulo desde un punto central, mantén presionada la tecla CTRL mientras arrastras.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle), que se usa para agregar una forma de rectángulo a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape). La clase [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) representa un rectángulo. Tiene algunos miembros importantes:

- La propiedad [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) especifica los atributos del formato de línea de un rectángulo.
- La propiedad [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que el rectángulo está conectado a las celdas en la hoja de cálculo.
- La propiedad [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) especifica los estilos de formato de relleno de un rectángulo.

El siguiente ejemplo muestra cómo agregar un rectángulo a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Añadir control de arco a la hoja de cálculo**

Aspose.Cells para Python via .NET permite dibujar formas de arco en las hojas de cálculo. Puedes crear arcos simples y rellenos. Se permite formatear el color de relleno y el color de la línea del borde de la forma. Por ejemplo, puedes especificar/cambiar el color del arco, establecer el color de sombreado, especificar el peso y el estilo de la forma según lo necesites.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Arco** en **Autoformas**.
1. Arrastra para dibujar el arco.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc), que se usa para agregar una forma de arco a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape). La clase [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) representa un arco. Tiene algunos miembros importantes:

- La propiedad [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) especifica los atributos del formato de línea de una forma de arco.
- La propiedad [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que se adjunta el arco a las celdas en la hoja de cálculo.
- La propiedad [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) especifica los estilos de formato de relleno de la forma.
- La propiedad [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) especifica el índice de la fila de la esquina inferior derecha.
La propiedad [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas de arco a la hoja de cálculo. El ejemplo crea dos formas de arco: una está rellena y la otra es simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Agregar Control Oval a una Hoja de Cálculo**

Aspose.Cells para Python via .NET permite dibujar formas ovaladas en las hojas de cálculo. Crear formas ovaladas simples y rellenas, y formatear el color de relleno y el color de la línea del borde de la forma. Por ejemplo, puedes especificar/cambiar el color de la elipse, establecer el color de sombreado, especificar el peso y el estilo de la forma.

### **Usar Microsoft Excel**

- En la barra de herramientas *Dibujo*, haga clic en *Óvalo*.
- Arrastre para dibujar el óvalo.
- Haga uno o ambos de los siguientes:
- Para limitar el óvalo y dibujar un círculo desde su punto de inicio, mantenga presionada la tecla MAYÚS mientras arrastra.
- Para dibujar un óvalo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval), que se utiliza para agregar una forma ovalada a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval). La clase [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) representa una forma ovalada. Tiene algunos miembros importantes:

- La propiedad [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) especifica los atributos del formato de línea de una forma ovalada.
- La propiedad [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) especifica el [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la forma en que el óvalo está adjunto a las celdas en la hoja de cálculo.
- La propiedad [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) especifica los estilos de formato de relleno de la forma.
- La propiedad [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) especifica el índice de la fila de la esquina inferior derecha.
La propiedad [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas ovaladas a la hoja de cálculo. El ejemplo crea dos formas ovaladas: una es una elipse rellena y la otra es un círculo simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Agregar control de spinner a la hoja de cálculo**

Un cuadro de desplazamiento (spin box) es un cuadro de texto adjunto a un botón (llamado botón de desplazamiento) que consta de una flecha hacia arriba y otra hacia abajo, que se hace clic para cambiar incrementalmente el valor en el cuadro de texto. Usando cuadros de desplazamiento, puedes ver cómo los cambios en la entrada afectarán los resultados en tu modelo financiero. Puedes adjuntar un botón de desplazamiento a una celda de entrada específica. Mientras haces clic en la flecha hacia arriba o hacia abajo en el botón de desplazamiento, el valor entero en la celda de entrada objetivo aumenta o disminuye. *Aspose.Cells para Python via .NET* permite crear spinners en tus hojas de cálculo.

### **Usar Microsoft Excel**

Para colocar un control de spinner en tu hoja de cálculo:

- Asegúrate de que la barra de herramientas *Formularios* esté visible.
- Haz clic en la herramienta *Spinner*.
- En la zona de tu hoja de cálculo, haz clic y arrastra para definir el rectángulo que contendrá el spinner.
- Una vez que el spinner esté colocado en la hoja de cálculo, haz clic derecho en el control y haz clic en *Formato de control* y especifica los valores máximo, mínimo e incrementales.
- En el campo *Vínculo a celda*, especifica la dirección de la celda a la que debe estar vinculado este control de spinner.
- Haz clic en *Aceptar*.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner), que se utiliza para agregar un control de spinner a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner). La clase [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) representa un control de spinner. Tiene algunos miembros importantes:

- La propiedad [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda que está vinculada al control de spinner.
- La propiedad [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) especifica el valor máximo del rango del control de spinner.
- La propiedad [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) especifica el valor mínimo del rango del control de spinner.
- La propiedad [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) especifica la cantidad de valor por la que se incrementa un spinner al desplazarse una línea.
- La propiedad [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) indica si el control de spinner tiene un sombreado en 3D.
- La propiedad [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) especifica el valor actual del control de spinner.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

## **Agregando control de barra de desplazamiento a una hoja de cálculo**

Un control de barra de desplazamiento se utiliza para ayudar a seleccionar datos en una hoja de cálculo de manera similar a un control de cuadro combinado. Al agregar el control a una hoja de cálculo y vincularlo a una celda, es posible devolver un valor numérico para la posición actual del control.

### **Usar Microsoft Excel**

- Para agregar una barra de desplazamiento en Excel 2003 y en versiones anteriores, haga clic en el botón *Barra de desplazamiento* en la barra de herramientas *Formularios*, y luego cree una barra de desplazamiento que cubra las celdas B2:B6 en altura y sea aproximadamente un cuarto del ancho de la columna.
- Para agregar una barra de desplazamiento en Excel 2007, haga clic en la pestaña *Desarrollador*, haga clic en *Insertar*, y luego haga clic en *Barra de desplazamiento* en la sección Controles de formulario.
- Haga clic con el botón derecho en la barra de desplazamiento, y luego haga clic en *Formato de control*.
- Escriba la siguiente información y haga clic en *Aceptar*:
  - En el cuadro de *Valor actual*, escriba 1.
  - En el cuadro de *Valor mínimo*, escriba 1. Este valor restringe el tope de la barra de desplazamiento al primer elemento de la lista.
  - En el cuadro de *Valor máximo*, escriba 20. Este número especifica el número máximo de entradas en la lista.
  - En el cuadro de *Cambio incremental*, escriba 1. Este valor controla cuántos números incrementa el control de la barra de desplazamiento el valor actual.
  - En el cuadro de *Cambio de página*, escriba 5. Esta entrada controla cuánto se incrementará el valor actual si hace clic dentro de la barra de desplazamiento en cualquiera de los lados de la caja de desplazamiento.
  - Para poner un valor numérico en la celda G1 (dependiendo de qué elemento esté seleccionado en la lista), escriba G1 en el cuadro de *Vínculo a celda*.
- Haga clic en cualquier celda para que la barra de desplazamiento no esté seleccionada.

Cuando hace clic en el control hacia arriba o hacia abajo en la barra de desplazamiento, la celda G1 se actualiza a un número que indica el valor actual de la barra de desplazamiento más o menos el cambio incremental de la barra de desplazamiento.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar), que se utiliza para agregar un control de barra de desplazamiento a la hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar). La clase [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) representa una barra de desplazamiento. Tiene algunos miembros importantes:

- La propiedad [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) especifica una celda que está vinculada a la barra de desplazamiento.
- La propiedad [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) especifica el valor máximo para el rango de la barra de desplazamiento.
- La propiedad [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) especifica el valor mínimo para el rango de la barra de desplazamiento.
- La propiedad [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) especifica la cantidad de valor por la cual se incrementa una barra de desplazamiento al desplazar una línea.
- La propiedad [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) indica si la barra de desplazamiento tiene sombreado en 3D.
- La propiedad [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) especifica el valor actual de la barra de desplazamiento.
- La propiedad [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) especifica cuánto se incrementará el valor actual si hace clic dentro de la barra de desplazamiento en cualquiera de los lados de la caja de desplazamiento.

El siguiente ejemplo muestra cómo agregar una barra de desplazamiento a la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

## **Agregar un control de cuadro del grupo a los controles de grupo en una hoja de cálculo.**

A veces es necesario implementar botones de opción u otros controles que pertenecen a un cierto grupo, se pueden implementar incluyendo un cuadro de grupo o un control de rectángulo. Cualquiera de estos dos objetos serviría como delimitador del grupo. Después de agregar una de estas formas, puede agregar dos o más botones de opción u otros objetos de grupo.

### **Usar Microsoft Excel**

Para colocar un control de cuadro del grupo en su hoja de cálculo y colocar controles en él:

- Para iniciar un formulario, en el menú principal, haga clic en *Ver*, seguido de *Barras de herramientas* y *Formularios*.
- En la barra de herramientas *Formularios*, haga clic en el *Cuadro de grupo* y dibuje un rectángulo en la hoja de cálculo.
- Escriba una cadena de título para el cuadro.
- En la barra de herramientas *Formularios*, haga clic en *Botón de opción* y haga clic dentro del *Cuadro de grupo* justo debajo de la cadena de título.
- Desde la barra de herramientas *Formularios* nuevamente, haga clic en *Botón de opción* y haga clic dentro del *Cuadro de grupo* debajo del primer botón de opción.
- Una vez más, en la barra de herramientas *Formularios*, haga clic en *Botón de opción* y haga clic dentro del *Cuadro de grupo* debajo del botón de opción anterior.

### **Usando Aspose.Cells para Python via .NET**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) proporciona un método llamado [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box), que se utiliza para agregar un control de cuadro de grupo a la hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox). Además, el método [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) de la clase [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) agrupa las formas, toma un array [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) como parámetro y devuelve un objeto [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape). La clase [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) representa un cuadro de grupo. Tiene algunos miembros importantes:

- La propiedad [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) especifica la cadena de título del cuadro de grupo.
- La propiedad [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) indica si el cuadro de grupo tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un grupo y agrupar los controles en la hoja de cálculo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Temas avanzados**
- [Agregar controles ActiveX](/cells/es/python-net/add-activex-controls-using-aspose-cells/)
- [Eliminar control ActiveX](/cells/es/python-net/remove-activex-control/)
- [Actualizar control ActiveX ComboBox](/cells/es/python-net/update-activex-combobox-control/)
