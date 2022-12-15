---
title: Gestión de controles
type: docs
weight: 120
url: /es/java/managing-controls/
---
## **Introducción**

Los desarrolladores pueden agregar diferentes objetos de dibujo, como cuadros de texto, casillas de verificación, botones de opción, cuadros combinados, etiquetas, botones, líneas, rectángulos, arcos, óvalos, botones giratorios, barras de desplazamiento, cuadros de grupo, etc. Aspose.Cells proporciona el espacio de nombres Aspose.Cells.Drawing que contiene todos los objetos de dibujo. Sin embargo, hay algunos objetos de dibujo o formas que aún no son compatibles. Cree estos objetos de dibujo en una hoja de cálculo de diseñador usando Microsoft Excel y luego importe la hoja de cálculo de diseñador a Aspose.Cells. Aspose.Cells le permite cargar estos objetos de dibujo desde una hoja de cálculo de diseñador y escribirlos en un archivo generado.

## **Agregar control de cuadro de texto a la hoja de trabajo**

Una forma de resaltar la información importante en un informe es utilizar un cuadro de texto. Por ejemplo, agregue texto para resaltar el nombre de la empresa o para indicar la región geográfica con las ventas más altas, etc. Aspose.Cells proporciona la clase TextBoxes, que se usa para agregar un nuevo cuadro de texto a la colección. Hay otra clase,[**Caja de texto**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), que representa un cuadro de texto utilizado para definir todo tipo de configuraciones. Tiene algunos miembros importantes:

-  los[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) método devuelve un[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) objeto utilizado para ajustar el contenido del cuadro de texto.
-  los[**establecerColocación**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) El método especifica el tipo de ubicación.
-  los[**establecer fuente**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) El método especifica los atributos de la fuente.
-  los[**añadir hipervínculo**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) agrega un hipervínculo para el cuadro de texto.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) devoluciones de propiedad[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) objeto utilizado para establecer el formato de relleno para el cuadro de texto.
-  los[**formato de línea**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) propiedad devuelve el[**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) objeto generalmente utilizado para el estilo y el peso de la línea del cuadro de texto.
-  los[**establecerTexto**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text)El método especifica el texto de entrada para el cuadro de texto.

El siguiente ejemplo crea dos cuadros de texto en la primera hoja de trabajo del libro. El primer cuadro de texto está bien equipado con diferentes configuraciones de formato. La segunda es sencilla.

La siguiente salida se genera al ejecutar el código:

**Se crean dos cuadros de texto en la hoja de cálculo.** 

![todo:imagen_alternativa_texto](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulación de controles de cuadro de texto en las hojas de cálculo del diseñador**

 Aspose.Cells también le permite acceder a cuadros de texto en las hojas de trabajo del diseñador y manipularlos. Utilizar el[**Hoja de trabajo.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) propiedad para obtener la colección de cuadros de texto en la hoja.

El siguiente ejemplo utiliza el archivo de Excel Microsoft, tsttextboxes.xls, que creamos en el ejemplo anterior. Obtiene las cadenas de texto de los dos cuadros de texto y cambia el texto del segundo cuadro de texto para guardar el archivo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Adición del control CheckBox a la hoja de trabajo**

Las casillas de verificación son útiles si desea proporcionar una forma para que un usuario elija entre dos opciones, como verdadero o falso; si o no. Aspose.Cells le permite usar casillas de verificación en las hojas de trabajo. Por ejemplo, es posible que haya desarrollado una hoja de trabajo de proyección financiera en la que puede dar cuenta de una adquisición en particular o no. En este caso, es posible que desee colocar una casilla de verificación en la parte superior de la hoja de trabajo. Luego puede vincular el estado de esta casilla de verificación a otra celda, de modo que si la casilla de verificación está seleccionada, el valor de la celda es Verdadero; si no se selecciona, el valor de la celda es Falso.

### **Usando Microsoft Excel**

Para colocar un control de casilla de verificación en su hoja de trabajo, siga estos pasos:

1. Asegúrese de que se muestra la barra de herramientas Formularios.
1.  Haga clic en el**casilla de verificación** en la barra de herramientas Formularios.
1. En el área de su hoja de trabajo, haga clic y arrastre para definir el rectángulo que contendrá la casilla de verificación y la etiqueta al lado de la casilla de verificación.
1. Una vez que se coloca la casilla de verificación, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1.  En el**Cell Enlace**campo, especifique la dirección de la celda a la que debe vincularse esta casilla de verificación.
1.  Haga clic en**OK**.

### **Usando Aspose.Cells**

 Aspose.Cells proporciona el[**Colección CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) class, que se utiliza para agregar una nueva casilla de verificación a la colección. Hay otra clase,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), que representa una casilla de verificación. Tiene algunos miembros importantes:

-  los[**establecerCeldaEnlazada**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) El método especifica una celda que está vinculada a la casilla de verificación.
-  los[**establecerTexto**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) El método especifica la cadena de texto asociada con la casilla de verificación. Es la etiqueta de la casilla de verificación.
-  los[**valor ajustado**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) El método especifica si la casilla de verificación está marcada o no.

El siguiente ejemplo muestra cómo agregar una casilla de verificación a la hoja de trabajo. El siguiente resultado se genera después de ejecutar el código.

**Se agrega un CheckBox en la hoja de trabajo** 

![todo:imagen_alternativa_texto](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Adición del control RadioButton a la hoja de trabajo**

Un botón de radio, o un botón de opción, es un control hecho de una caja redonda. El usuario toma su decisión seleccionando la casilla redonda. Un botón de opción suele ir acompañado, si no siempre, de otros. Dichos botones de radio aparecen y se comportan como un grupo. El usuario decide qué botón es válido seleccionando sólo uno de ellos. Cuando el usuario hace clic en un botón, se llena. Cuando se selecciona un botón en el grupo, los botones del mismo grupo están vacíos.

### **Usando Microsoft Excel**

Para colocar un control Botón de radio en su hoja de trabajo, siga estos pasos:

1.  Asegúrate que**formularios** se muestra la barra de herramientas.
1.  Haga clic en el**Botón de opción** herramienta.
1. En la hoja de trabajo, haga clic y arrastre para definir el rectángulo que contendrá el botón de opción y la etiqueta al lado del botón de opción.
1. Una vez que el botón de radio se coloca en la hoja de trabajo, mueva el cursor del mouse al área de la etiqueta y cambie la etiqueta.
1.  En el**Cell Enlace** campo, especifique la dirección de la celda a la que debe vincularse este botón de opción.
1.  Hacer clic**OK**.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class proporciona un método llamado addShape que se puede usar para agregar un control de botón de radio a una hoja de trabajo. El método puede devolver un objeto RadioButton. La clase RadioButton representa un botón de opción. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al botón de opción.
- El método setText especifica la cadena de texto asociada con el botón de opción. Es la etiqueta del botón de opción.
- La propiedad Checked especifica si el botón de radio está marcado o no.
- El método setFillFormat especifica el formato de relleno del botón de opción.
- El método setLineFormat especifica los estilos de formato de línea del botón de opción.

El siguiente ejemplo muestra cómo agregar botones de opción a una hoja de cálculo. El ejemplo agrega tres botones de radio que representan grupos de edad. El siguiente resultado se generaría después de ejecutar el código.

**Algunos botones de radio se agregan en la hoja de trabajo** 

![todo:imagen_alternativa_texto](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Agregar control de cuadro combinado a una hoja de trabajo**

Para facilitar la entrada de datos, o para limitar las entradas a ciertos elementos que defina, puede crear un cuadro combinado o una lista desplegable de entradas válidas que se compila a partir de celdas en otras partes de la hoja de trabajo. Cuando crea una lista desplegable para una celda, muestra una flecha junto a esa celda. Para ingresar información en esa celda, haga clic en la flecha y luego haga clic en la entrada que desee.

### **Usando Microsoft Excel**

Para colocar un control de cuadro combinado en su hoja de cálculo, siga estos pasos:

1.  Asegúrate que**formularios** se muestra la barra de herramientas.
1.  Haga clic en el**Caja combo** herramienta.
1. En el área de su hoja de trabajo, haga clic y arrastre para definir el rectángulo que contendrá el cuadro combinado.
1.  Una vez que el cuadro combinado se coloca en la hoja de cálculo, haga clic con el botón derecho en el control para hacer clic en**Control de formato** y especifique el rango de entrada.
1.  En el**Cell Enlace** campo, especifique la dirección de la celda a la que debe vincularse este cuadro combinado.
1.  Haga clic en**OK**.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class proporciona un método llamado addShape, que se puede usar para agregar un control de cuadro combinado a la hoja de cálculo. El método puede devolver el objeto ComboBox. La clase ComboBox representa un cuadro combinado. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al cuadro combinado.
- El método setInputRange especifica el rango de celdas de la hoja de cálculo que se usa para llenar el cuadro combinado.
- El método setDropDownLines especifica el número de líneas de lista que se muestran en la parte desplegable de un cuadro combinado.
- El método setShadow indica si el cuadro combinado tiene sombreado 3D.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo. El siguiente resultado se genera al ejecutar el código.

**Se agrega un cuadro combinado en la hoja de trabajo** 

![todo:imagen_alternativa_texto](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Adición de control de etiquetas a una hoja de trabajo**

 Las etiquetas son un medio para dar a los usuarios información sobre el contenido de una hoja de cálculo. Aspose.Cells permite agregar y manipular etiquetas en una hoja de trabajo. los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class proporciona un método llamado addShape, que se usa para agregar un control de etiqueta a la hoja de trabajo. El método devuelve un objeto Label. La clase Label representa una etiqueta en la hoja de trabajo. Tiene algunos miembros importantes:

- El método setText especifica la cadena de título de una etiqueta.
- El método setPlacement especifica PlacementType, la forma en que la etiqueta se adjunta a las celdas de la hoja de trabajo.

El siguiente ejemplo muestra cómo agregar una etiqueta a la hoja de trabajo. El siguiente resultado se genera al ejecutar el código.

**Se agrega una etiqueta en la hoja de trabajo.**

![todo:imagen_alternativa_texto](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Agregar control de cuadro de lista a una hoja de trabajo**

Un control de cuadro de lista crea un control de lista que permite la selección de uno o varios elementos.

### **Usando Microsoft Excel**

Para colocar un control de cuadro de lista en una hoja de cálculo:

1.  Asegúrate que**formularios** se muestra la barra de herramientas.
1.  Haga clic en el**Cuadro de lista** herramienta.
1. En el área de su hoja de trabajo, haga clic y arrastre para definir el rectángulo que contendrá el cuadro de lista.
1.  Una vez que el cuadro de lista se coloca en la hoja de trabajo, haga clic con el botón derecho en el control para hacer clic en**Control de formato** y especifique el rango de entrada.
1.  En el**Cell Enlace**campo, especifique la dirección de la celda a la que se debe vincular este cuadro de lista y establezca el atributo de tipo de selección (Único, Múltiple, Extender)
1.  Hacer clic**OK**.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class proporciona un método denominado addShape, que se utiliza para agregar un control de cuadro de lista a una hoja de trabajo. El método devuelve un objeto ListBox. La clase ListBox representa un cuadro de lista. Tiene algunos miembros importantes:

- El método setLinkedCell especifica una celda que está vinculada al cuadro de lista.
- El método setInputRange especifica el rango de celdas de la hoja de cálculo que se usa para llenar el cuadro de lista.
- El método setSelectionType especifica el modo de selección del cuadro de lista.
- El método setShadow indica si el cuadro de lista tiene sombreado 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de lista a la hoja de trabajo. El siguiente resultado se genera al ejecutar el código.

**Se agrega un cuadro de lista en la hoja de trabajo.** 

![todo:imagen_alternativa_texto](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Agregar control de botón a una hoja de trabajo**

Los botones son útiles para realizar algunas acciones. A veces, es útil asignar una macro de VBA al botón o asignar un hipervínculo para abrir una página web.

### **Usando Microsoft Excel**

Para colocar un control de botón en su hoja de cálculo:

1.  Asegúrate que**formularios** se muestra la barra de herramientas.
1.  Haga clic en el**Botón** herramienta.
1. En el área de su hoja de trabajo, haga clic y arrastre para definir el rectángulo que contendrá el botón.
1.  Una vez que el cuadro de lista se coloca en la hoja de trabajo, haga clic derecho en el control y seleccione**Control de formato**, luego especifique una macro de VBA y los atributos relacionados con la fuente, la alineación, el tamaño, el margen, etc.
1.  Haga clic en**OK**.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class proporciona un método llamado addShape, que se usa para agregar un control de botón a la hoja de trabajo. El método puede devolver un objeto Button. La clase Button representa un botón. Tiene algunos miembros importantes:

- El método setText especifica el título del botón.
- El método setPlacement especifica PlacementType, la forma en que el botón se adjunta a las celdas de la hoja de trabajo.
- El método addHyperlink agrega un hipervínculo para el control de botón. Al hacer clic en el botón se navegará a la URL relacionada.

El siguiente ejemplo muestra cómo agregar un botón a la hoja de trabajo. El siguiente resultado se genera al ejecutar el código

**Se agrega un botón en la hoja de trabajo.**

![todo:imagen_alternativa_texto](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Adición de control de línea a una hoja de trabajo**

Aspose.Cells le permite dibujar autoformas en sus hojas de trabajo. Puede crear una línea con facilidad. También puede formatear la línea. Por ejemplo, puede cambiar el color de la línea, especificar el grosor y el estilo de la línea según sus necesidades.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Autoformas** , apunta a**Líneas**y seleccione el estilo de línea que desee.
1. Arrastre para dibujar la línea.
1. Haga uno o ambos de los siguientes:
 1. Para restringir la línea para que se dibuje en ángulos de 15 grados desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
 1. Para alargar la línea en direcciones opuestas desde el primer punto final, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)class proporciona un método llamado addShape, que se usa para agregar una forma de línea a la hoja de cálculo. El método puede devolver un objeto LineShape. La clase LineShape representa una línea. Tiene algunos miembros importantes:

- El método setDashStyle especifica el formato de una línea.
- El método setPlacement especifica PlacementType, la forma en que la línea se adjunta a las celdas de la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar líneas a la hoja de cálculo. Crea tres líneas con diferentes estilos. El siguiente resultado se genera después de ejecutar el código.

**Se agregan algunas líneas en la hoja de trabajo.** 

![todo:imagen_alternativa_texto](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Agregar una punta de flecha a una línea**

Aspose.Cells también le permite dibujar líneas de flecha. Es posible agregar una punta de flecha a una línea y formatear la línea. Por ejemplo, puede cambiar el color de la línea o especificar el grosor y el estilo de la línea.

El siguiente ejemplo muestra cómo agregar una punta de flecha a una línea. El siguiente resultado se genera al ejecutar el código.

**Se agrega una línea con punta de flecha en la hoja de trabajo** 

![todo:imagen_alternativa_texto](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Agregar control de rectángulo a una hoja de trabajo**

Aspose.Cells le permite dibujar formas rectangulares en sus hojas de trabajo. Puede crear un rectángulo, un cuadrado, etc. También puede formatear el color de relleno y el color de la línea del borde del control. Por ejemplo, puede cambiar el color del rectángulo, establecer el color del sombreado, especificar el grosor y el estilo del rectángulo según sus necesidades.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Rectángulo**.
1. Arrastre para dibujar el rectángulo.
1. Haga uno o ambos de los siguientes:
 1. Para restringir el rectángulo para que dibuje un cuadrado desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
 1. Para dibujar un rectángulo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class proporciona un método llamado addShape, que se usa para agregar una forma de rectángulo a una hoja de cálculo. El método puede devolver un objeto RectangleShape. La clase RectangleShape representa un rectángulo. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de un rectángulo.
- El método setPlacement especifica PlacementType, la forma en que el rectángulo se adjunta a las celdas de la hoja de cálculo.
- La propiedad FillFormat especifica los estilos de formato de relleno de un rectángulo.

El siguiente ejemplo muestra cómo agregar un rectángulo a la hoja de trabajo. El siguiente resultado se genera al ejecutar el código.

**Se agrega un rectángulo en la hoja de cálculo.** 

![todo:imagen_alternativa_texto](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Agregar control de arco a la hoja de trabajo**

Aspose.Cells le permite dibujar formas de arco en sus hojas de trabajo. Puede crear arcos simples y rellenos. Se le permite formatear el color de relleno y el color de la línea del borde del control. Por ejemplo, puede especificar/cambiar el color del arco, establecer el color del sombreado, especificar el peso y el estilo de la forma según sus necesidades.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Arco** en el**Autoformas**.
1. Arrastre para dibujar el arco.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class proporciona un método llamado addShape, que se usa para agregar una forma de arco a la hoja de trabajo. El método puede devolver un objeto ArcShape. La clase ArcShape representa un arco. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de una forma de arco.
- El método setPlacement especifica PlacementType, la forma en que el arco se adjunta a las celdas de la hoja de trabajo.
- La propiedad FillFormat especifica los estilos de formato de relleno de la forma.

El siguiente ejemplo muestra cómo agregar formas de arco a la hoja de cálculo. El ejemplo crea dos formas de arco: una está llena y la otra es simple. El siguiente resultado se genera al ejecutar el código

**Se agregan dos formas de arco a la hoja de trabajo.** 

![todo:imagen_alternativa_texto](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Adición de control ovalado a una hoja de trabajo**

Aspose.Cells le permite dibujar formas ovaladas en hojas de trabajo. Cree formas ovaladas simples y rellenas y formatee el color de relleno y el color de la línea del borde del control. Por ejemplo, puede especificar/cambiar el color del óvalo, establecer el color del sombreado, especificar el peso y el estilo de la forma.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Oval** .
1. Arrastra para dibujar el óvalo.
1. Haga uno o ambos de los siguientes:
 1. Para restringir el óvalo para que dibuje un círculo desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
1. Para dibujar un óvalo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) class proporciona un método llamado addShape, que se usa para agregar una forma ovalada a una hoja de cálculo. El método puede devolver un objeto Oval. La clase Oval representa una forma ovalada. Tiene algunos miembros importantes:

- El método setLineFormat especifica los atributos de formato de línea de una forma ovalada.
-  El método setPlacement especifica el**Tipo de ubicación** , la forma en que el óvalo se une a las celdas de la hoja de cálculo.
- La propiedad FillFormat especifica los estilos de formato de relleno de la forma.

El siguiente ejemplo muestra cómo agregar formas ovaladas a la hoja de cálculo. El ejemplo crea dos formas ovaladas: una es un óvalo relleno y la otra es un círculo simple. El siguiente resultado se genera al ejecutar el código.

**Se agregan dos formas ovaladas en la hoja de trabajo.** 

![todo:imagen_alternativa_texto](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Temas avanzados**
- [Agregue controles ActiveX usando Aspose.Cells](/cells/es/java/add-activex-controls-using-aspose-cells/)
- [Eliminar control ActiveX](/cells/es/java/remove-activex-control/)
