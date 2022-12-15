---
title: Gestión de controles
type: docs
weight: 150
url: /es/net/managing-controls/
---
## **Introducción**

Los desarrolladores pueden agregar diferentes objetos de dibujo, como cuadros de texto, casillas de verificación, botones de opción, cuadros combinados, etiquetas, botones, líneas, rectángulos, arcos, óvalos, botones giratorios, barras de desplazamiento, cuadros de grupo, etc. Aspose.Cells proporciona el espacio de nombres Aspose.Cells.Drawing que contiene todos los objetos de dibujo. Sin embargo, hay algunos objetos de dibujo o formas que aún no son compatibles. Cree estos objetos de dibujo en una hoja de cálculo de diseñador usando Microsoft Excel y luego importe la hoja de cálculo de diseñador a Aspose.Cells. Aspose.Cells le permite cargar estos objetos de dibujo desde una hoja de cálculo de diseñador y escribirlos en un archivo generado.

## **Adición de un control de cuadro de texto a una hoja de cálculo**

 Una forma de resaltar la información importante en un informe es utilizar un cuadro de texto. Por ejemplo, agregue texto para resaltar el nombre de la empresa o para indicar la región geográfica con las ventas más altas, etc. Aspose.Cells proporciona la[**Colección TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) class, que se usa para agregar un nuevo cuadro de texto a la colección. Hay otra clase,[**Caja de texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), que representa un cuadro de texto utilizado para definir todo tipo de configuraciones. Tiene algunos miembros importantes:

-  los[**Marco de texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) propiedad devuelve un[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) objeto utilizado para ajustar el contenido del cuadro de texto.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propiedad especifica el tipo de ubicación.
-  los[**Fuente**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) La propiedad especifica los atributos de la fuente.
-  los[**Agregar hipervínculo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) El método agrega un hipervínculo para el cuadro de texto.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) propiedad devuelve un[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) objeto utilizado para establecer el formato de relleno para el cuadro de texto.
-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) propiedad devuelve el[**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) objeto generalmente utilizado para el estilo y el peso de la línea del cuadro de texto.
-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propiedad especifica el texto de entrada para el cuadro de texto.

El siguiente ejemplo crea dos cuadros de texto en la primera hoja de trabajo del libro. El primer cuadro de texto está bien equipado con diferentes configuraciones de formato. La segunda es sencilla.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipulación de controles de cuadro de texto en hojas de cálculo de Designer**

 Aspose.Cells también le permite acceder a cuadros de texto en las hojas de trabajo del diseñador y manipularlos. Utilizar el[**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) propiedad para obtener la colección de cuadros de texto en la hoja.

El siguiente ejemplo usa el archivo de Excel Microsoft que creamos en el ejemplo anterior. Obtiene las cadenas de texto de los dos cuadros de texto y cambia el texto del segundo cuadro de texto para guardar el archivo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Adición de un control de casilla de verificación a una hoja de cálculo**

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

 Aspose.Cells proporciona el[**Colección CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) class, que se utiliza para agregar una nueva casilla de verificación a la colección. Hay otra clase,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), que representa una casilla de verificación. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propiedad especifica una celda que está vinculada a la casilla de verificación.
-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propiedad especifica la cadena de texto asociada con la casilla de verificación. Es la etiqueta de la casilla de verificación.
-  los[**Valor**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) La propiedad especifica si la casilla de verificación está marcada o no.

El siguiente ejemplo muestra cómo agregar una casilla de verificación a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Agregar control de botón de radio a la hoja de trabajo**

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

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**Agregar botón de radio**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , que se utiliza para agregar un control de botón de opción a una hoja de cálculo. El método devuelve un[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) objeto. La clase[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) representa un botón de opción. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propiedad especifica una celda que está vinculada al botón de opción.
-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)La propiedad especifica la cadena de texto asociada con el botón de opción. Es la etiqueta del botón de opción.
-  los[**Está chequeado**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) La propiedad especifica si el botón de radio está marcado o no.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La propiedad especifica el formato de relleno del botón de opción.
-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propiedad especifica los estilos de formato de línea del botón de opción.

El siguiente ejemplo muestra cómo agregar botones de opción a una hoja de cálculo. El ejemplo agrega tres botones de radio que representan grupos de edad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

 los[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AñadirComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , que se usa para agregar un control de cuadro combinado a una hoja de trabajo. El método devuelve un[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) objeto. La clase[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) representa un cuadro combinado. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propiedad especifica una celda que está vinculada al cuadro combinado.
-  los[**Rango de entrada**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) La propiedad especifica el rango de celdas de la hoja de cálculo que se usa para llenar el cuadro combinado.
-  los[**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) La propiedad especifica el número de líneas de lista que se muestran en la parte desplegable de un cuadro combinado.
-  los[**Sombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) La propiedad indica si el cuadro combinado tiene sombreado 3D.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Adición de control de etiquetas a una hoja de trabajo**

 Las etiquetas son un medio para dar a los usuarios información sobre el contenido de una hoja de cálculo. Aspose.Cells permite agregar y manipular etiquetas en una hoja de trabajo. los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**Agregar etiqueta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , utilizado para agregar un control de etiqueta a la hoja de cálculo. El método devuelve un[**Etiqueta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) objeto. La clase[**Etiqueta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) representa una etiqueta en la hoja de cálculo. Tiene algunos miembros importantes:

-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) El método especifica la cadena de título de una etiqueta.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) método especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la forma en que la etiqueta se adjunta a las celdas de la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar una etiqueta a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , que se utiliza para agregar un control de cuadro de lista a una hoja de cálculo. El método devuelve un[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) objeto. La clase[**Cuadro de lista**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) representa un cuadro de lista. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) El método especifica una celda que está vinculada al cuadro de lista.
-  los[**Rango de entrada**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) El método especifica el rango de celdas de la hoja de trabajo utilizado para llenar el cuadro de lista.
-  los[**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)El método especifica el modo de selección del cuadro de lista.
-  los[**Sombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) El método indica si el cuadro de lista tiene sombreado 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de lista a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

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

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AñadirBotón**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , utilizado para agregar un control de botón a la hoja de trabajo. El método devuelve un[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) objeto. La clase[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) representa un botón. Tiene algunos miembros importantes:

-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) propiedad especifica el título del botón.
-  los[**Fuente**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) La propiedad especifica los atributos de fuente para la etiqueta del control de botón.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propiedad especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la forma en que el botón se adjunta a las celdas de la hoja de cálculo.
-  los[**Agregar hipervínculo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) La propiedad agrega un hipervínculo para el control de botón. Al hacer clic en el botón se navegará a la URL relacionada.

El siguiente ejemplo muestra cómo agregar un botón a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Adición de control de línea a la hoja de trabajo**

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Autoformas** , apunta a**Líneas**y seleccione el estilo de línea que desee.
1. Arrastre para dibujar la línea.
1. Haga uno o ambos de los siguientes:
 1. Para restringir la línea para que se dibuje en ángulos de 15 grados desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
 1. Para alargar la línea en direcciones opuestas desde el primer punto final, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**Añadir línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , que se utiliza para agregar una forma de línea a la hoja de cálculo. El método devuelve un[**LíneaForma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objeto. La clase[**LíneaForma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) representa una línea. Tiene algunos miembros importantes:

-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) El método especifica el formato de una línea.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) método especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)la forma en que la línea se une a las celdas de la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar líneas a la hoja de cálculo. Crea tres líneas con diferentes estilos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Agregar una punta de flecha a una línea**

Aspose.Cells también le permite dibujar líneas de flecha. Es posible agregar una punta de flecha a una línea y formatear la línea. Por ejemplo, puede cambiar el color de la línea o especificar el grosor y el estilo de la línea.

El siguiente ejemplo muestra cómo agregar una punta de flecha a una línea.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Agregar control de rectángulo a una hoja de trabajo**

Aspose.Cells le permite dibujar formas rectangulares en sus hojas de trabajo. Puede crear un rectángulo, un cuadrado, etc. También puede formatear el color de relleno y el color de la línea del borde del control. Por ejemplo, puede cambiar el color del rectángulo, establecer el color del sombreado, especificar el grosor y el estilo del rectángulo según sus necesidades.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Rectángulo**.
1. Arrastre para dibujar el rectángulo.
1. Haga uno o ambos de los siguientes:
 1. Para restringir el rectángulo para que dibuje un cuadrado desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
 1. Para dibujar un rectángulo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AñadirRectángulo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , que se utiliza para agregar una forma de rectángulo a una hoja de cálculo. El método vuelve[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objeto. La clase[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) representa un rectángulo. Tiene algunos miembros importantes:

-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propiedad especifica los atributos de formato de línea de un rectángulo.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propiedad especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la forma en que el rectángulo se une a las celdas de la hoja de cálculo.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La propiedad especifica los estilos de formato de relleno de un rectángulo.

El siguiente ejemplo muestra cómo agregar un rectángulo a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Agregar control de arco a la hoja de trabajo**

Aspose.Cells le permite dibujar formas de arco en sus hojas de trabajo. Puede crear arcos simples y rellenos. Se le permite formatear el color de relleno y el color de la línea del borde del control. Por ejemplo, puede especificar/cambiar el color del arco, establecer el color del sombreado, especificar el peso y el estilo de la forma según sus necesidades.

### **Usando Microsoft Excel**

1.  Sobre el**Dibujo** barra de herramientas, haga clic en**Arco** en el**Autoformas**.
1. Arrastre para dibujar el arco.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AgregarArco**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , que se utiliza para agregar una forma de arco a una hoja de trabajo. El método devuelve un[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) objeto. La clase[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) representa un arco. Tiene algunos miembros importantes:

-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propiedad especifica los atributos de formato de línea de una forma de arco.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propiedad especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la forma en que el arco se une a las celdas de la hoja de trabajo.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)La propiedad especifica los estilos de formato de relleno de la forma.
-  los[**FilaInferiorDerecha**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La propiedad especifica el índice de fila de la esquina inferior derecha.
-  los[**Columna inferior derecha**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La propiedad especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas de arco a la hoja de cálculo. El ejemplo crea dos formas de arco: una está llena y la otra es simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Adición de control ovalado a una hoja de trabajo**

Aspose.Cells le permite dibujar formas ovaladas en hojas de trabajo. Cree formas ovaladas simples y rellenas y formatee el color de relleno y el color de la línea del borde del control. Por ejemplo, puede especificar/cambiar el color del óvalo, establecer el color del sombreado, especificar el peso y el estilo de la forma.

### **Usando Microsoft Excel**

-  Sobre el*Dibujo* barra de herramientas, haga clic en*Oval*.
- Arrastra para dibujar el óvalo.
- Haga uno o ambos de los siguientes:
- Para restringir el óvalo para que dibuje un círculo desde su punto inicial, mantenga presionada la tecla MAYÚS mientras arrastra.
- Para dibujar un óvalo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AñadirOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , que se utiliza para agregar una forma ovalada a una hoja de cálculo. El método devuelve un[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) objeto. La clase[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) representa una forma ovalada. Tiene algunos miembros importantes:

-  los[**formato de línea**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propiedad especifica los atributos de formato de línea de una forma ovalada.
-  los[**Colocación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propiedad especifica el[**Tipo de ubicación**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la forma en que el óvalo se une a las celdas de la hoja de cálculo.
-  los[**Formato de relleno**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)La propiedad especifica los estilos de formato de relleno de la forma.
-  los[**FilaInferiorDerecha**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La propiedad especifica el índice de fila de la esquina inferior derecha.
-  los[**Columna inferior derecha**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La propiedad especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas ovaladas a la hoja de cálculo. El ejemplo crea dos formas ovaladas: una es un óvalo relleno y la otra es un círculo simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Agregar control giratorio a la hoja de trabajo**

 Un cuadro de número es un cuadro de texto adjunto a un botón (llamado botón de número) que consta de una flecha hacia arriba y una flecha hacia abajo en las que hace clic para cambiar gradualmente el valor en el cuadro de texto. Mediante el uso de cuadros de número, puede ver cómo los cambios de entrada en su modelo financiero alterarán los resultados del modelo. Puede adjuntar un botón giratorio a una celda de entrada específica. Mientras hace clic en la flecha hacia arriba o hacia abajo en el botón giratorio, el valor entero en la celda de entrada de destino aumenta o disminuye.*Aspose.Cells* le permite crear ruletas en sus hojas de trabajo.

### **Usando Microsoft Excel**

Para colocar un control de cuadro de número en su hoja de cálculo:

-  Asegúrate que*formularios* se muestra la barra de herramientas.
-  Haga clic en el*Hilandero* herramienta.
- En el área de su hoja de trabajo, haga clic y arrastre para definir el rectángulo que sostendrá la rueda giratoria.
-  Una vez que la ruleta se coloca en la hoja de trabajo, haga clic derecho en el control y haga clic en*Control de formato* y especificar los valores máximo, mínimo e incremental.
-  En el*Cell Enlace* campo, especifique la dirección de la celda a la que se debe vincular este cuadro de número.
-  Haga clic en*OK*.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AñadirSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) que se utiliza para agregar un control de cuadro numérico a una hoja de trabajo. El método devuelve un[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) objeto. La clase[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) representa una caja de giro. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propiedad especifica una celda que está vinculada al cuadro de número.
-  los[**máx.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) La propiedad especifica el valor máximo para el rango del cuadro numérico.
-  los[**mínimo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) La propiedad especifica el valor mínimo para el rango del cuadro numérico.
-  los[**Cambio incrementado**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) La propiedad especifica la cantidad de valor por la cual una rueda se incrementa en un desplazamiento de línea.
-  los[**Sombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) La propiedad indica si el cuadro de número tiene sombreado 3D.
-  los[**Valor actual**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) La propiedad especifica el valor actual del cuadro de número.

El siguiente ejemplo muestra cómo agregar un cuadro de número a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Agregar control de barra de desplazamiento a una hoja de trabajo**

Se utiliza un control de barra de desplazamiento para ayudar a seleccionar datos en una hoja de trabajo de manera similar a un control de cuadro de número. Al agregar el control a una hoja de cálculo y vincularlo a una celda, es posible devolver un valor numérico para la posición actual del control.

### **Usando Microsoft Excel**

- Para agregar una barra de desplazamiento en Excel 2003 y en versiones anteriores, haga clic en el*Barra de desplazamiento* botón en el*formularios* barra de herramientas y, a continuación, cree una barra de desplazamiento que cubra las celdas B2:B6 en altura y sea aproximadamente un cuarto del ancho de la columna.
-  Para agregar una barra de desplazamiento en Excel 2007, haga clic en el*Desarrollador* pestaña, haga clic*Insertar* y luego haga clic en*Barra de desplazamiento* en la sección Controles de formulario.
-  Haga clic con el botón derecho en la barra de desplazamiento y luego haga clic en*Control de formato*.
-  Escriba la siguiente información y haga clic en*OK*:
 - En el*Valor actual* caja, tipo 1.
 - En el*Valor mínimo* cuadro, escriba 1. Este valor restringe la parte superior de la barra de desplazamiento al primer elemento de la lista.
 - En el*Valor máximo* casilla, escriba 20. Este número especifica el número máximo de entradas en la lista.
 - En el*Cambio incrementado* cuadro, escriba 1. Este valor controla cuántos números incrementa el control de la barra de desplazamiento en el valor actual.
 - En el*Cambio de página* cuadro, escriba 5. Esta entrada controla cuánto se incrementará el valor actual si hace clic dentro de la barra de desplazamiento a cada lado del cuadro de desplazamiento.
 Para poner un valor numérico en la celda G1 (según el elemento seleccionado en la lista), escriba G1 en el*Cell enlace* caja.
- Haga clic en cualquier celda para que la barra de desplazamiento no se seleccione.

Cuando hace clic en el control hacia arriba o hacia abajo en la barra de desplazamiento, la celda G1 se actualiza a un número que indica el valor actual de la barra de desplazamiento más o menos el cambio incremental de la barra de desplazamiento.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**Añadir barra de desplazamiento**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , que se utiliza para agregar un control de barra de desplazamiento a la hoja de trabajo. El método devuelve un[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) objeto. La clase[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) representa una barra de desplazamiento. Tiene algunos miembros importantes:

-  los[**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propiedad especifica una celda que está vinculada a la barra de desplazamiento.
-  los[**máx.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) La propiedad especifica el valor máximo para el rango de la barra de desplazamiento.
-  los[**mínimo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) La propiedad especifica el valor mínimo para el rango de la barra de desplazamiento.
-  los[**Cambio incrementado**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) La propiedad especifica la cantidad de valor por la cual una barra de desplazamiento se incrementa un desplazamiento de línea.
-  los[**Sombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) La propiedad indica si la barra de desplazamiento tiene sombreado 3D.
-  los[**Valor actual**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) La propiedad especifica el valor actual de la barra de desplazamiento.
-  los[**Cambio de página**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)La propiedad especifica cuánto se incrementará el valor actual si hace clic dentro de la barra de desplazamiento a cada lado del cuadro de desplazamiento.

El siguiente ejemplo muestra cómo agregar una barra de desplazamiento a la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Agregar control GroupBox a controles de grupo en una hoja de trabajo**

A veces es necesario implementar botones de radio u otros controles que pertenecen a un determinado grupo, puede implementar mediante la inclusión de un cuadro de grupo o un control de rectángulo. Cualquiera de estos dos objetos serviría como delimitador del grupo. Después de agregar una de estas formas, puede agregar dos o más botones de radio u otros objetos de grupo.

### **Usando Microsoft Excel**

Para colocar un control de cuadro de grupo en su hoja de trabajo y colocar controles en él:

-  Para iniciar un formulario, en el menú principal, haga clic en*Vista* , seguido por*Barras de herramientas* y*formularios*.
-  Sobre el*formularios* barra de herramientas, haga clic en el*Cuadro de grupo* y dibuje un rectángulo en la hoja de trabajo.
- Escriba una cadena de título para el cuadro.
-  Sobre el*formularios* barra de herramientas, haga clic en*Botón de opción* y haga clic dentro del*Cuadro de grupo* justo debajo de la cadena de subtítulos.
-  Desde el*formularios* barra de herramientas de nuevo, haga clic en*Botón de opción* y haga clic dentro del*Cuadro de grupo*debajo del primer botón de opción.
-  Una vez más en el*formularios* barra de herramientas, haga clic en*Botón de opción* y haga clic dentro del*Cuadro de grupo* debajo del botón de opción anterior.

### **Usando Aspose.Cells**

 los[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase proporciona un método llamado[**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , que se utiliza para agregar un control de cuadro de grupo a la hoja de cálculo. El método devuelve un[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) objeto. Además, el[**Grupo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) metodo de la[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) clase agrupa las formas, se necesita un[**Forma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) array como parámetro y devuelve un[**GrupoForma**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) objeto. La clase[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) representa un cuadro de grupo. Tiene algunos miembros importantes:

-  los[**Texto**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propiedad especifica la cadena de título del cuadro de grupo.
-  los[**Sombra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) La propiedad indica si el cuadro de grupo tiene sombreado 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de grupo y agrupar los controles en la hoja de cálculo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Temas avanzados**
- [Agregue controles ActiveX usando Aspose.Cells](/cells/es/net/add-activex-controls-using-aspose-cells/)
- [Eliminar control ActiveX](/cells/es/net/remove-activex-control/)
- [Actualizar el control ActiveX ComboBox](/cells/es/net/update-activex-combobox-control/)
