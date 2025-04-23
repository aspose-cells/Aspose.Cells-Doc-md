---
title: Gestión de controles con C++
linktitle: Gestionar controles
type: docs
weight: 150
url: /es/cpp/managing-controls/
description: Aprende cómo agregar y gestionar varios controles como líneas, rectángulos, arcos, óvalos, spinners, barras de desplazamiento y cuadros de grupo en hojas de cálculo usando Aspose.Cells con C++.
---

## **Introducción**

Los desarrolladores pueden agregar diferentes objetos de dibujo como cuadros de texto, casillas de verificación, botones de radio, cuadros combinados, etiquetas, botones, líneas, rectángulos, arcos, óvalos, spinners, barras de desplazamiento, cuadros de grupo, etc. Aspose.Cells proporciona el espacio de nombres `Aspose::Cells::Drawing` que contiene todos los objetos de dibujo. Sin embargo, hay algunos objetos o formas de dibujo que aún no son soportados. Cree estos objetos en un libro de Excel de diseño y luego importe ese libro a Aspose.Cells. Aspose.Cells le permite cargar estos objetos de dibujo desde un libro de diseño y escribirlos en un archivo generado.

## **Adición de un control de cuadro de texto a una hoja de cálculo**

Una forma de resaltar información importante en un informe es utilizar un cuadro de texto. Por ejemplo, agregar texto para resaltar el nombre de la empresa o indicar la región geográfica con las ventas más altas, etc. Aspose.Cells proporciona la clase [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/), utilizada para agregar un nuevo cuadro de texto a la colección. Hay otra clase, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), que representa un cuadro de texto utilizado para definir todo tipo de ajustes. Tiene algunos miembros importantes:

- La propiedad [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el tipo de colocación.
- La propiedad [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) especifica los atributos de fuente.
- El método [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) agrega un hipervínculo al cuadro de texto.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) devuelve un objeto [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) utilizado para establecer el formato de relleno para el cuadro de texto.
- La propiedad [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) devuelve el objeto [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) utilizado generalmente para el estilo y peso de la línea del cuadro de texto.
- La propiedad [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica el texto de entrada para el cuadro de texto.

El siguiente ejemplo crea dos cuadros de texto en la primera hoja de cálculo del libro. El primer cuadro de texto está bien decorado con diferentes ajustes de formato. El segundo es simple.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Manipulación de controles de cuadro de texto en hojas de cálculo de diseño**

Aspose.Cells también le permite acceder a los cuadros de texto en las hojas de cálculo de diseño y manipularlos. Utilice la propiedad [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) para obtener la colección de cuadros de texto en la hoja.

El siguiente ejemplo utiliza el archivo de Microsoft Excel que creamos en el ejemplo anterior. Obtiene las cadenas de texto de los dos cuadros de texto y cambia el texto del segundo cuadro de texto para guardar el archivo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Adición de un control de casilla de verificación a una hoja de cálculo**

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

Aspose.Cells proporciona la clase [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), que se utiliza para agregar un nuevo cuadro de verificación a la colección. También hay otra clase, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), que representa un cuadro de verificación. Tiene algunos miembros importantes:

- La propiedad [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda que está vinculada al cuadro de verificación.
- La propiedad [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica la cadena de texto asociada con el cuadro de verificación. Es la etiqueta del cuadro de verificación.
- La propiedad [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) especifica si el cuadro de verificación está marcado o no.

El siguiente ejemplo muestra cómo agregar un cuadro de verificación a la hoja de cálculo.

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

### **Usar Aspose.Cells**

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) ofrece un método llamado [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), que se usa para agregar un control de botón de opción a una hoja de cálculo. El método devuelve un objeto [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/). La clase [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) representa un botón de opción. Tiene algunos miembros importantes:

- La propiedad [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda vinculada al botón de opción.
- La propiedad [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica la cadena de texto asociada al botón de opción. Es la etiqueta del botón de opción.
- La propiedad [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) especifica si el botón de opción está marcado o no.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) especifica el formato de relleno del botón de opción.
- La propiedad [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) especifica los estilos de formato de línea del botón de opción.

El siguiente ejemplo muestra cómo agregar botones de opción a una hoja de cálculo. El ejemplo agrega tres botones de opción que representan grupos de edad.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();

    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);


    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

La clase [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), que se utiliza para agregar un control de cuadro combinado a una hoja de cálculo. El método devuelve un objeto [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/). La clase [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) representa un cuadro combinado. Tiene algunos miembros importantes:

- La propiedad [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda que está vinculada al cuadro combinado.
- La propiedad [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) especifica el rango de celdas de la hoja de cálculo utilizadas para rellenar el cuadro combinado.
- La propiedad [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) especifica el número de líneas de lista que se muestran en la parte desplegable de un cuadro combinado.
- La propiedad [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) indica si el cuadro combinado tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Agregando un control de etiqueta a una hoja de cálculo**

Las etiquetas son una forma de proporcionar información a los usuarios sobre el contenido de una hoja de cálculo. Aspose.Cells permite agregar y manipular etiquetas en una hoja de cálculo. La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), que se utiliza para agregar un control de etiqueta a la hoja de cálculo. El método devuelve un objeto [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). La clase [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) representa una etiqueta en la hoja de cálculo. Tiene algunos miembros importantes:

- El método [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica una cadena de título de la etiqueta.
- El método [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que la etiqueta está unida a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar una etiqueta a la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), que se utiliza para agregar un control de lista a una hoja de cálculo. El método devuelve un objeto [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/). La clase [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) representa un cuadro de lista. Tiene algunos miembros importantes:

- El método [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda que está vinculada al cuadro de lista.
- El método [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) especifica el rango de celdas de la hoja de cálculo usadas para rellenar el cuadro de lista.
- El método [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) especifica el modo de selección del cuadro de lista.
- El método [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) indica si el cuadro de lista tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un cuadro de lista a la hoja de cálculo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), utilizado para agregar un control de botón a la hoja de cálculo. El método devuelve un objeto [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/). La clase [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) representa un botón. Tiene algunos miembros importantes:

- La propiedad [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica la leyenda del botón.
- La propiedad [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) especifica los atributos de fuente para la etiqueta del control de botón.
- La propiedad [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que el botón se conecta a las celdas en la hoja de cálculo.
- La propiedad [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) agrega un hipervínculo para el control de botón. Al hacer clic en el botón, se navegará a la URL relacionada.

El siguiente ejemplo muestra cómo agregar un botón a la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Agregar control de línea a la hoja de cálculo**

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haga clic en **formas automáticas**, apunte a **líneas** y seleccione el estilo de línea que desee.
1. Arrastre para dibujar la línea.
1. Haz uno o ambos de los siguientes:
   1. Para restringir la línea para dibujar en ángulos de 15 grados desde su punto de partida, mantenga presionada la tecla MAYÚS mientras arrastra.
   1. Para alargar la línea en direcciones opuestas desde el primer punto final, mantenga presionada la tecla CTRL mientras arrastra.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) ofrece un método llamado [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), que se usa para agregar una forma de línea a la hoja de cálculo. El método devuelve un objeto [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/). La clase [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) representa una línea. Tiene algunos miembros importantes:

- El método [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) especifica el formato de una línea.
- El método [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que la línea está conectada a las celdas en la hoja de cálculo.

El siguiente ejemplo muestra cómo agregar líneas a la hoja de cálculo. Crea tres líneas con diferentes estilos.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Agregar una cabeza de flecha a una línea**

Aspose.Cells también te permite dibujar líneas de flecha. Es posible agregar una cabeza de flecha a una línea y dar formato a la línea. Por ejemplo, puedes cambiar el color de la línea o especificar el grosor y estilo de la línea.

El siguiente ejemplo muestra cómo agregar una cabeza de flecha a una línea.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Agregar control de rectángulo a una hoja de cálculo**

Aspose.Cells te permite dibujar formas de rectángulo en tus hojas de cálculo. Puedes crear un rectángulo, un cuadrado, etc. También puedes formatear el color de relleno y el borde de la forma. Por ejemplo, puedes cambiar el color del rectángulo, establecer el color de sombreado, especificar el grosor y el estilo del rectángulo según tus necesidades.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Rectángulo**.
1. Arrastra para dibujar el rectángulo.
1. Haz uno o ambos de los siguientes:
   1. Para restringir el rectángulo y dibujar un cuadrado desde su punto de inicio, mantén presionada la tecla SHIFT mientras arrastras.
   1. Para dibujar un rectángulo desde un punto central, mantén presionada la tecla CTRL mientras arrastras.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), que se usa para agregar una forma de rectángulo a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/). La clase [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) representa un rectángulo. Tiene algunos miembros importantes:

- La propiedad [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) especifica los atributos del formato de línea de un rectángulo.
- La propiedad [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que el rectángulo está conectado a las celdas en la hoja de cálculo.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) especifica los estilos de formato de relleno de un rectángulo.

El siguiente ejemplo muestra cómo agregar un rectángulo a la hoja de cálculo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Añadir control de arco a la hoja de cálculo**

Aspose.Cells te permite dibujar formas de arco en tus hojas de cálculo. Puedes crear arcos simples y rellenos. Puedes formatear el color de relleno y el borde de la forma. Por ejemplo, puedes especificar/cambiar el color del arco, establecer el color de sombreado, especificar el grosor y estilo de la forma según tus necesidades.

### **Usar Microsoft Excel**

1. En la barra de herramientas **Dibujo**, haz clic en **Arco** en **Autoformas**.
1. Arrastra para dibujar el arco.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), que se usa para agregar una forma de arco a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/). La clase [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) representa un arco. Tiene algunos miembros importantes:

- La propiedad [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) especifica los atributos del formato de línea de una forma de arco.
- La propiedad [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que se adjunta el arco a las celdas en la hoja de cálculo.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) especifica los estilos de formato de relleno de la forma.
- La propiedad [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) especifica el índice de la fila de la esquina inferior derecha.
La propiedad [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas de arco a la hoja de cálculo. El ejemplo crea dos formas de arco: una está rellena y la otra es simple.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Agregar Control Oval a una Hoja de Cálculo**

Aspose.Cells le permite dibujar formas ovaladas en las hojas de cálculo. Cree formas ovaladas simples y rellenas y formatee el color de relleno y el color de la línea de borde del control. Por ejemplo, puede especificar/cambiar el color del óvalo, configurar el color de sombreado, especificar el peso y el estilo de la forma.

### **Usar Microsoft Excel**

- En la barra de herramientas *Dibujo*, haga clic en *Óvalo*.
- Arrastre para dibujar el óvalo.
- Haga uno o ambos de los siguientes:
- Para limitar el óvalo y dibujar un círculo desde su punto de inicio, mantenga presionada la tecla MAYÚS mientras arrastra.
- Para dibujar un óvalo desde un punto central, mantenga presionada la tecla CTRL mientras arrastra.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), que se utiliza para agregar una forma ovalada a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/). La clase [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) representa una forma ovalada. Tiene algunos miembros importantes:

- La propiedad [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) especifica los atributos del formato de línea de una forma ovalada.
- La propiedad [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) especifica el [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la forma en que el óvalo está adjunto a las celdas en la hoja de cálculo.
- La propiedad [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) especifica los estilos de formato de relleno de la forma.
- La propiedad [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) especifica el índice de la fila de la esquina inferior derecha.
La propiedad [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) especifica el índice de la columna de la esquina inferior derecha.

El siguiente ejemplo muestra cómo agregar formas ovaladas a la hoja de cálculo. El ejemplo crea dos formas ovaladas: una es una elipse rellena y la otra es un círculo simple.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Agregar control de spinner a la hoja de cálculo**

Un control de spinner es un cuadro de texto adjunto a un botón (llamado un botón de giro) que consiste en una flecha hacia arriba y una flecha hacia abajo en las que haces clic para cambiar incrementalmente el valor en el cuadro de texto. Al utilizar controles de giró, puedes ver cómo los cambios de entrada en tu modelo financiero alterarán las salidas del modelo. Puedes adjuntar un botón de giro a una celda de entrada específica. Mientras haces clic en la flecha hacia arriba o hacia abajo en el botón de giro, el valor entero en la celda de entrada objetivo aumenta o disminuye. *Aspose.Cells* te permite crear spinners en tus hojas de cálculo.

### **Usar Microsoft Excel**

Para colocar un control de spinner en tu hoja de cálculo:

- Asegúrate de que la barra de herramientas *Formularios* esté visible.
- Haz clic en la herramienta *Spinner*.
- En la zona de tu hoja de cálculo, haz clic y arrastra para definir el rectángulo que contendrá el spinner.
- Una vez que el spinner esté colocado en la hoja de cálculo, haz clic derecho en el control y haz clic en *Formato de control* y especifica los valores máximo, mínimo e incrementales.
- En el campo *Vínculo a celda*, especifica la dirección de la celda a la que debe estar vinculado este control de spinner.
- Haz clic en *Aceptar*.

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), que se utiliza para agregar un control de spinner a una hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/). La clase [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) representa un control de spinner. Tiene algunos miembros importantes:

- La propiedad [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda que está vinculada al control de spinner.
- La propiedad [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) especifica el valor máximo del rango del control de spinner.
- La propiedad [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) especifica el valor mínimo del rango del control de spinner.
- La propiedad [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) especifica la cantidad de valor por la que se incrementa un spinner al desplazarse una línea.
- La propiedad [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) indica si el control de spinner tiene un sombreado en 3D.
- La propiedad [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) especifica el valor actual del control de spinner.

El siguiente ejemplo muestra cómo agregar un cuadro combinado a la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), que se utiliza para agregar un control de barra de desplazamiento a la hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/). La clase [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) representa una barra de desplazamiento. Tiene algunos miembros importantes:

- La propiedad [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) especifica una celda que está vinculada a la barra de desplazamiento.
- La propiedad [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) especifica el valor máximo para el rango de la barra de desplazamiento.
- La propiedad [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) especifica el valor mínimo para el rango de la barra de desplazamiento.
- La propiedad [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) especifica la cantidad de valor por la cual se incrementa una barra de desplazamiento al desplazar una línea.
- La propiedad [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) indica si la barra de desplazamiento tiene sombreado en 3D.
- La propiedad [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) especifica el valor actual de la barra de desplazamiento.
- La propiedad [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) especifica cuánto se incrementará el valor actual si hace clic dentro de la barra de desplazamiento en cualquiera de los lados de la caja de desplazamiento.

El siguiente ejemplo muestra cómo agregar una barra de desplazamiento a la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

### **Usar Aspose.Cells**

La clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) proporciona un método llamado [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), que se utiliza para agregar un control de cuadro de grupo a la hoja de cálculo. El método devuelve un objeto [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/). Además, el método [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) de la clase [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) agrupa las formas, toma un array [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) como parámetro y devuelve un objeto [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/). La clase [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) representa un cuadro de grupo. Tiene algunos miembros importantes:

- La propiedad [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) especifica la cadena de título del cuadro de grupo.
- La propiedad [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) indica si el cuadro de grupo tiene sombreado en 3D.

El siguiente ejemplo muestra cómo agregar un grupo y agrupar los controles en la hoja de cálculo.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Temas avanzados**
- [Agregar controles ActiveX usando Aspose.Cells](/cells/es/cpp/add-activex-controls-using-aspose-cells/)
- [Eliminar control ActiveX](/cells/es/cpp/remove-activex-control/)
- [Actualizar control ActiveX ComboBox](/cells/es/cpp/update-activex-combobox-control/)
