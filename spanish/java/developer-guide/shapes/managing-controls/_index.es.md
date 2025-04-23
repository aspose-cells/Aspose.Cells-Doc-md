---
title: Gestionar controles
type: docs
weight: 120
url: /es/java/managing-controls/
---

## **Introducción**

Los desarrolladores pueden agregar diferentes objetos de dibujo, como cuadros de texto, casillas de verificación, botones de opción, cuadros combinados, etiquetas, botones, líneas, rectángulos, arcos, óvalos, selectores, barras de desplazamiento, cuadros de grupo, etc. Aspose.Cells proporciona el espacio de nombres de Aspose.Cells.Drawing que contiene todos los objetos de dibujo. Sin embargo, hay algunos objetos de dibujo o formas que aún no son compatibles. Cree estos objetos de dibujo en una hoja de cálculo de diseño utilizando Microsoft Excel y luego importe la hoja de cálculo de diseño a Aspose.Cells. Aspose.Cells le permite cargar estos objetos de dibujo desde una hoja de cálculo de diseño y escribirlos en un archivo generado.

## **Agregar control de cuadro de texto a la hoja de cálculo**

Una forma de destacar información importante en un informe es utilizando un cuadro de texto. Por ejemplo, añadir texto para resaltar el nombre de la empresa o indicar la región geográfica con las mayores ventas, etc. Aspose.Cells proporciona la clase TextBoxes, utilizada para añadir un nuevo cuadro de texto a la colección. Hay otra clase, [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), que representa un cuadro de texto utilizado para definir todos los tipos de ajustes. Tiene algunos miembros importantes:

- El método [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) devuelve un objeto [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) utilizado para ajustar el contenido del cuadro de texto.
- El método [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) especifica el tipo de colocación.
- El método [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) especifica los atributos de fuente.
- El método [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink-java.lang.String-) agrega un hipervínculo al cuadro de texto.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) devuelve un objeto [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) utilizado para establecer el formato de relleno para el cuadro de texto.
- La propiedad [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) devuelve el objeto [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) utilizado generalmente para el estilo y peso de la línea del cuadro de texto.
- El método [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) especifica el texto de entrada para el cuadro de texto.

El siguiente ejemplo crea dos cuadros de texto en la primera hoja de cálculo del libro. El primer cuadro de texto está bien decorado con diferentes ajustes de formato. El segundo es simple.

El siguiente resultado se genera al ejecutar el código:

**Se crean dos cuadros de texto en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipular Controles de Cuadro de Texto en las Hojas de Cálculo del Diseñador**

Aspose.Cells también le permite acceder a los cuadros de texto en las hojas de cálculo de diseño y manipularlos. Utilice la propiedad [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) para obtener la colección de cuadros de texto en la hoja.

El siguiente ejemplo utiliza el archivo de Microsoft Excel – tsttextboxes.xls – que creamos en el ejemplo anterior. Obtiene las cadenas de texto de los dos cuadros de texto y cambia el texto del segundo cuadro de texto para guardar el archivo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Agregar Control de Casilla de Verificación a la Hoja de Cálculo**

Las casillas de verificación son útiles si desea proporcionar una forma para que un usuario elija entre dos opciones, como verdadero o falso; sí o no. Aspose.Cells le permite usar casillas de verificación en hojas de cálculo. Por ejemplo, es posible que haya desarrollado una hoja de cálculo de proyección financiera en la que pueda tener en cuenta una adquisición particular o no. En este caso, es posible que desee colocar una casilla de verificación en la parte superior de la hoja de cálculo. Luego puede vincular el estado de esta casilla de verificación a otra celda, para que si la casilla de verificación está seleccionada, el valor de la celda sea Verdadero; si no está seleccionada, el valor de la celda será Falso.

### **Usar Microsoft Excel**

Para colocar un control de casilla de verificación en su hoja de cálculo, siga estos pasos:

1. Asegúrese de que aparezca la barra de herramientas de formularios.
1. Haga clic en la herramienta **Cuadro de verificación** en la barra de herramientas de Formularios.
1. En el área de su hoja de cálculo, haga clic y arrastre para definir el rectángulo que contendrá el cuadro de verificación y la etiqueta junto al cuadro de verificación.
1. Una vez que se coloque el cuadro de verificación, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1. En el campo **Vínculo de celda**, especifique la dirección de la celda a la que debe estar vinculado este cuadro de verificación.
1. Haz clic en **Aceptar**.

### **Usar Aspose.Cells**

Aspose.Cells proporciona la clase [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection), que se utiliza para agregar un nuevo cuadro de verificación a la colección. También hay otra clase, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), que representa un cuadro de verificación. Tiene algunos miembros importantes:

- El método [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) especifica una celda vinculada a la casilla de verificación.
- El método [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) especifica la cadena de texto asociada con la casilla de verificación. Es la etiqueta de la casilla de verificación.
- El método [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) especifica si la casilla de verificación está marcada o no.

El siguiente ejemplo muestra cómo agregar una casilla de verificación a la hoja de cálculo. El resultado a continuación se genera después de ejecutar el código.

**Se agrega una casilla de verificación en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Agregando Control de Botón de Opción a la Hoja de Cálculo**

Un botón de opción, o un botón de opción, es un control hecho de un cuadro redondo. El usuario toma su decisión seleccionando el cuadro redondo. Un botón de opción generalmente, si no siempre, está acompañado por otros. Estos botones de opción aparecen y se comportan como un grupo. El usuario decide qué botón es válido seleccionando solo uno de ellos. Cuando el usuario hace clic en un botón, se llena. Cuando se selecciona un botón en el grupo, los botones del mismo grupo están vacíos.

### **Usar Microsoft Excel**

Para colocar un control de botón de opción en su hoja de cálculo, siga estos pasos:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haga clic en la herramienta **Botón de opción**.
1. En la hoja de cálculo, haga clic y arrastre para definir el rectángulo que contendrá el botón de opción y la etiqueta junto al botón de opción.
1. Una vez que se coloca el botón de opción en la hoja de cálculo, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1. En el campo **Vínculo de celda**, especifique la dirección de la celda a la que debe estar vinculado este botón de opción.
1. Haz clic en **Aceptar**.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape que se puede utilizar para agregar un control de botón de opción a una hoja de cálculo. El método puede devolver un objeto RadioButton. La clase RadioButton representa un botón de opción. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al botón de opción.
- El método setText especifica la cadena de texto asociada con el botón de opción. Es la etiqueta del botón de opción.
- La propiedad Checked especifica si el botón de opción está seleccionado o no.
- El método setFillFormat especifica el formato de relleno del botón de opción.
- El método setLineFormat especifica los estilos de formato de línea del botón de opción.

El siguiente ejemplo muestra cómo agregar botones de opción a una hoja de cálculo. El ejemplo agrega tres botones de opción que representan grupos de edad. El siguiente resultado se generaría después de ejecutar el código.

**Se agregan algunos botones de opción en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

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

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se puede utilizar para agregar un control de cuadro combinado a la hoja de cálculo. El método puede devolver un objeto ComboBox. La clase ComboBox representa un cuadro combinado. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al cuadro combinado.
- El método setInputRange especifica el rango de celdas de la hoja de cálculo utilizado para rellenar el cuadro combinado.
- El método setDropDownLines especifica el número de líneas de lista que se muestran en la parte desplegable de un cuadro combinado.
- El método setShadow indica si el cuadro combinado tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo. El siguiente resultado se genera al ejecutar el código.

**Se agrega un cuadro combinado en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Agregando un control de etiqueta a una hoja de cálculo**

Las etiquetas sirven para proporcionar a los usuarios información sobre el contenido de una hoja de cálculo. Aspose.Cells permite agregar y manipular etiquetas en una hoja de cálculo. La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar un control de etiqueta a la hoja de cálculo. El método devuelve un objeto Label. La clase Label representa una etiqueta en la hoja de cálculo. Tiene algunos miembros importantes:

- El método setText especifica la cadena de la etiqueta.
- El método setPlacement especifica el PlacementType, la forma en que la etiqueta está adjunta a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar una etiqueta a la hoja de cálculo. El siguiente resultado se genera al ejecutar el código.

**Se agrega una etiqueta en la hoja de cálculo**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

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

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar un control de lista a una hoja de cálculo. El método devuelve un objeto ListBox. La clase ListBox representa un cuadro de lista. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al cuadro de lista.
- El método setInputRange especifica el rango de celdas de la hoja de cálculo utilizado para rellenar el cuadro de lista.
- El método setSelectionType especifica el modo de selección del cuadro de lista.
- El método setShadow indica si el cuadro de lista tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de lista a la hoja de cálculo. El siguiente resultado se genera al ejecutar el código.

**Se agrega un cuadro de lista en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Agregando Control de Botón a una Hoja de Cálculo**

Los botones son útiles para realizar algunas acciones. A veces, es útil asignar un Macro de VBA al botón o asignar un hipervínculo para abrir una página web.

### **Usar Microsoft Excel**

Para colocar un control de botón en tu hoja de cálculo:

1. Asegúrate de que la barra de herramientas **Formularios** esté visible.
1. Haz clic en la herramienta **Botón**.
1. En el área de tu hoja de cálculo, haz clic y arrastra para definir el rectángulo que contendrá el botón.
1. Una vez que el cuadro de lista esté colocado en la hoja de cálculo, haz clic derecho sobre el control y selecciona **Formato de control**, luego especifica un Macro de VBA y atributos relacionados con fuente, alineación, tamaño, margen, etc.
1. Haz clic en **Aceptar**.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar un control de botón a la hoja de cálculo. El método puede devolver un objeto Button. La clase Button representa un botón. Tiene algunos miembros importantes:

- El método setText especifica el título del botón.
- El método setPlacement especifica el PlacementType, la forma en que el botón está adjunto a las celdas en la hoja de trabajo.
- El método addHyperlink agrega un hipervínculo para el control del botón. Al hacer clic en el botón, navegará a la URL relacionada.

El siguiente ejemplo muestra cómo agregar un botón a la hoja de cálculo. La salida generada al ejecutar el código es la siguiente

**Se agrega un botón en la hoja de cálculo**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Agregar control de línea a una hoja de cálculo**

Aspose.Cells le permite dibujar autoshapes en sus hojas de cálculo. Puede crear una línea con facilidad. También se le permite dar formato a la línea. Por ejemplo, puede cambiar el color de la línea, especificar el peso y estilo de la línea según sus necesidades.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haga clic en **formas automáticas**, apunte a **líneas** y seleccione el estilo de línea que desee.
1. Arrastre para dibujar la línea.
1. Haz uno o ambos de los siguientes:
   1. Para restringir la línea para dibujar en ángulos de 15 grados desde su punto de partida, mantenga presionada la tecla MAYÚS mientras arrastra.
   1. Para alargar la línea en direcciones opuestas desde el primer punto final, mantenga presionada la tecla CTRL mientras arrastra.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar una forma de línea a la hoja de cálculo. El método puede devolver un objeto LineShape. La clase LineShape representa una línea. Tiene algunos miembros importantes:

- El método setDashStyle especifica el formato de una línea.
- El método setPlacement especifica el tipo de PlacementType, la forma en que la línea se adjunta a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar líneas a la hoja de cálculo. Crea tres líneas con diferentes estilos. La siguiente salida se genera después de ejecutar el código

**Se agregan algunas líneas en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Agregar una punta de flecha a una línea**

Aspose.Cells también te permite dibujar líneas de flecha. Es posible agregar una cabeza de flecha a una línea y dar formato a la línea. Por ejemplo, puedes cambiar el color de la línea o especificar el grosor y estilo de la línea.

El siguiente ejemplo muestra cómo agregar una punta de flecha a una línea. La siguiente salida se genera al ejecutar el código.

**Se agrega una línea con punta de flecha en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Agregar control de rectángulo a una hoja de cálculo**

Aspose.Cells te permite dibujar formas de rectángulo en tus hojas de cálculo. Puedes crear un rectángulo, un cuadrado, etc. También puedes formatear el color de relleno y el borde de la forma. Por ejemplo, puedes cambiar el color del rectángulo, establecer el color de sombreado, especificar el grosor y el estilo del rectángulo según tus necesidades.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Rectángulo**.
1. Arrastra para dibujar el rectángulo.
1. Haz uno o ambos de los siguientes:
   1. Para restringir el rectángulo y dibujar un cuadrado desde su punto de inicio, mantén presionada la tecla SHIFT mientras arrastras.
   1. Para dibujar un rectángulo desde un punto central, mantén presionada la tecla CTRL mientras arrastras.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar una forma de rectángulo a una hoja de cálculo. El método puede devolver un objeto RectangleShape. La clase RectangleShape representa un rectángulo. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de un rectángulo.
- El método setPlacement especifica el PlacementType, la forma en que el rectángulo se adjunta a las celdas en la hoja de cálculo.
- La propiedad FillFormat especifica los estilos de formato de relleno de un rectángulo.

El siguiente ejemplo muestra cómo agregar un rectángulo a la hoja de cálculo. La siguiente salida se genera al ejecutar el código.

**Se agrega un rectángulo en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Añadir control de arco a la hoja de cálculo**

Aspose.Cells te permite dibujar formas de arco en tus hojas de cálculo. Puedes crear arcos simples y rellenos. Puedes formatear el color de relleno y el borde de la forma. Por ejemplo, puedes especificar/cambiar el color del arco, establecer el color de sombreado, especificar el grosor y estilo de la forma según tus necesidades.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Arco** en **Autoformas**.
1. Arrastra para dibujar el arco.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar una forma de arco a la hoja de cálculo. El método puede devolver un objeto ArcShape. La clase ArcShape representa un arco. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de una forma de arco.
- El método setPlacement especifica el PlacementType, la forma en que el arco se adjunta a las celdas en la hoja de cálculo.
- La propiedad FillFormat especifica los estilos de formato de relleno de la forma.

El siguiente ejemplo muestra cómo agregar formas de arco a la hoja de cálculo. El ejemplo crea dos formas de arco: una está rellena y la otra es simple. La siguiente salida se genera al ejecutar el código

**Se agregan dos formas de arco a la hoja de cálculo** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Agregar Control Oval a una Hoja de Cálculo**

Aspose.Cells le permite dibujar formas ovaladas en las hojas de cálculo. Cree formas ovaladas simples y rellenas y formatee el color de relleno y el color de la línea de borde del control. Por ejemplo, puede especificar/cambiar el color del óvalo, configurar el color de sombreado, especificar el peso y el estilo de la forma.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Óvalo**.
1. Arrastra para dibujar el óvalo.
1. Haz uno o ambos de los siguientes:
   1. Para restringir el óvalo y dibujar un círculo desde su punto de inicio, mantén presionada la tecla MAYÚS mientras lo arrastras.
   1. Para dibujar un óvalo desde un punto central, mantén presionada la tecla CTRL mientras lo arrastras.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) proporciona un método llamado addShape, que se utiliza para agregar una forma de óvalo a una hoja de cálculo. El método puede devolver un objeto Oval. La clase Oval representa una forma de óvalo. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de una forma de óvalo.
- El método setPlacement especifica el **PlacementType**, la forma en que el óvalo se adjunta a las celdas en la hoja de cálculo.
- La propiedad FillFormat especifica los estilos de formato de relleno de la forma.

El siguiente ejemplo muestra cómo agregar formas de óvalo a la hoja de cálculo. El ejemplo crea dos formas de óvalo: uno es un óvalo relleno y el otro es un simple círculo. La siguiente salida se genera al ejecutar el código

**Se agregan dos formas de óvalo en la hoja de cálculo** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Temas avanzados**
- [Agregar controles ActiveX usando Aspose.Cells](/cells/es/java/add-activex-controls-using-aspose-cells/)
- [Eliminar control ActiveX](/cells/es/java/remove-activex-control/)
{{< app/cells/assistant language="java" >}}
