---
title: Steuerelemente mit C++ verwalten
linktitle: Steuerelemente verwalten
type: docs
weight: 150
url: /de/cpp/managing-controls/
description: Erfahren Sie, wie Sie mit Aspose.Cells in C++ verschiedene Steuerelemente wie Linien, Rechtecke, Bögen, Ellipsen, Spinner, Bildlaufleisten und Gruppenkästen in Arbeitsblättern hinzufügen und verwalten.
---

## **Einführung**

Entwickler können verschiedene Zeichenobjekte wie Textfelder, Kontrollkästchen, Optionsfelder, Komboboxen, Labels, Buttons, Linien, Rechtecke, Bögen, Ellipsen, Spinner, Bildlaufleisten, Gruppenkästen usw. erstellen. Aspose.Cells bietet den Namespace `Aspose::Cells::Drawing`, der alle Zeichenobjekte enthält. Es gibt jedoch einige Zeichenobjekte oder Formen, die noch nicht unterstützt werden. Erstellen Sie diese Zeichenobjekte in einer Designer-Tabellenkalkulation mit Microsoft Excel und importieren Sie die Designer-Datei in Aspose.Cells. Aspose.Cells ermöglicht es, diese Zeichenobjekte aus einer Designer-Tabellenkalkulation zu laden und in eine generierte Datei zu schreiben.

## **Hinzufügen einer Textfeldsteuerung zu einem Arbeitsblatt**

Eine Möglichkeit, wichtige Informationen in einem Bericht zu betonen, besteht darin, ein Textfeld zu verwenden. Fügen Sie beispielsweise Text hinzu, um den Firmennamen hervorzuheben oder die geografische Region mit den höchsten Umsätzen anzuzeigen usw. Aspose.Cells bietet die [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/)-Klasse, die verwendet wird, um ein neues Textfeld zur Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), die ein Textfeld zum Definieren aller Arten von Einstellungen repräsentiert. Sie hat einige wichtige Elemente:

- Die [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)-Eigenschaft gibt den Platzierungstyp an.
- Die [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/)-Eigenschaft gibt die Schriftattributen an.
- Die Methode [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) fügt dem Textfeld einen Hyperlink hinzu.
- Die [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)-Eigenschaft gibt ein [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/)-Objekt zurück, das verwendet wird, um das Füllformat für das Textfeld festzulegen.
- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) gibt normalerweise das [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/)-Objekt zurück, das zur Formatierung und Gewichtung der Textfeldlinie verwendet wird.
- Die [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/)-Eigenschaft gibt den Eingabetext für das Textfeld an.

Im folgenden Beispiel werden zwei Textfelder im ersten Arbeitsblatt der Arbeitsmappe erstellt. Das erste Textfeld ist gut ausgestattet mit verschiedenen Formatierungseinstellungen. Das zweite ist einfach gehalten.

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

## **Bearbeiten von Textfeldsteuerungen in Designer-Arbeitsmappen**

Aspose.Cells ermöglicht es Ihnen auch, auf Textfelder in den Designer-Arbeitsblättern zuzugreifen und diese zu manipulieren. Verwenden Sie die Eigenschaft [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), um die Textfelder-Sammlung im Blatt zu erhalten.

Im folgenden Beispiel wird die Microsoft Excel-Datei verwendet, die wir im obigen Beispiel erstellt haben. Es ruft die Textzeichenfolgen der beiden Textfelder ab und ändert den Text des zweiten Textfelds, um die Datei zu speichern.

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

## **Hinzufügen einer Kontrollkästchensteuerung zu einem Arbeitsblatt**

Kontrollkästen sind praktisch, wenn Sie dem Benutzer eine Auswahl zwischen zwei Optionen ermöglichen möchten, beispielsweise true oder false; Ja oder Nein. Aspose.Cells ermöglicht es Ihnen, Kontrollkästchen in Arbeitsblättern zu verwenden. Beispielsweise könnten Sie ein Finanzprognose-Arbeitsblatt entwickelt haben, in dem Sie entweder eine bestimmte Akquisition berücksichtigen können oder nicht. In diesem Fall möchten Sie möglicherweise ein Kontrollkästchen oben auf dem Arbeitsblatt platzieren. Sie können dann den Status dieses Kontrollkästchens mit einer anderen Zelle verknüpfen, sodass, wenn das Kontrollkästchen ausgewählt ist, der Wert der Zelle wahr ist; wenn es nicht ausgewählt ist, ist der Wert der Zelle falsch.

### **Verwendung von Microsoft Excel**

Um ein Kontrollkästchen-Steuerelement in Ihr Arbeitsblatt zu platzieren, befolgen Sie diese Schritte:

1. Stellen Sie sicher, dass die Formen-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Kontrollkästchen**-Symbol in der Symbolleiste Formulare.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Kontrollkästchen und das Label neben dem Kontrollkästchen enthält.
1. Sobald das Kontrollkästchen platziert ist, bewegen Sie den Mauszeiger in den Etikettenbereich und ändern Sie das Etikett.
1. Geben Sie im Feld **Zellenbezug** die Adresse der Zelle an, mit der dieses Kontrollkästchen verknüpft sein soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Aspose.Cells bietet die Klasse [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), die verwendet wird, um ein neues Kontrollkästchen der Sammlung hinzuzufügen. Es gibt eine weitere Klasse, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), die ein Kontrollkästchen darstellt. Es hat einige wichtige Elemente:

- Die Eigenschaft [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) gibt eine Zelle an, die mit dem Kontrollkästchen verknüpft ist.
- Die Eigenschaft [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) gibt den Textstring an, der mit dem Kontrollkästchen verbunden ist. Es ist die Beschriftung des Kontrollkästchens.
- Die Eigenschaft [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) gibt an, ob das Kontrollkästchen aktiviert ist oder nicht.

Das folgende Beispiel zeigt, wie ein Kontrollkästchen dem Arbeitsblatt hinzugefügt wird.

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

## **Radio Button Steuerelement dem Arbeitsblatt hinzufügen**

Ein Optionsfeld oder Kontrollkästchen ist ein Steuerelement in Form eines runden Kastens. Der Benutzer trifft seine Entscheidung, indem er den runden Kasten auswählt. Ein Optionsfeld ist normalerweise, wenn nicht immer, von anderen begleitet. Solche Optionsfelder erscheinen und verhalten sich als Gruppe. Der Benutzer entscheidet, welcher Schaltfläche gültig ist, indem er nur eine davon auswählt. Wenn der Benutzer eine Schaltfläche anklickt, wird sie gefüllt. Wenn eine Schaltfläche in der Gruppe ausgewählt ist, sind die Schaltflächen derselben Gruppe leer.

### **Verwendung von Microsoft Excel**

So platzieren Sie ein Optionsfeldsteuerelement in Ihrem Arbeitsblatt:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf die Schaltfläche **Optionsfeld**.
1. Klicken und ziehen Sie im Arbeitsblatt, um das Rechteck zu definieren, in dem das Optionsfeld und das daneben stehende Etikett platziert werden sollen.
1. Sobald das Optionsfeld im Arbeitsblatt platziert ist, bewegen Sie den Mauszeiger in den Etikettenbereich und ändern das Etikett.
1. Geben Sie im Feld **Zellverknüpfung** die Adresse der Zelle an, mit der dieses Optionsfeld verbunden werden soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), mit der ein Optionsfeld zu einem Arbeitsblatt hinzugefügt werden kann. Die Methode gibt ein [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/)-Objekt zurück. Die Klasse [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) repräsentiert eine Optionsschaltfläche. Sie verfügt über einige wichtige Mitglieder:

- Die Eigenschaft [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) gibt eine Zelle an, die mit dem Optionsfeld verknüpft ist.
- Die Eigenschaft [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) gibt den Textstring an, der mit dem Optionsfeld verbunden ist. Es ist die Beschriftung des Optionsfelds.
- Die Eigenschaft [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) gibt an, ob das Optionsfeld aktiviert ist oder nicht.
- Die Eigenschaft [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) gibt das Füllformat des Optionsfeldes an.
- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) gibt die Linienformatstile des Optionsfeldes an.

Das folgende Beispiel zeigt, wie Radio-Buttons einem Arbeitsblatt hinzugefügt werden. Das Beispiel fügt drei Radio-Buttons hinzu, die Altersgruppen repräsentieren.

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

## **Hinzufügen eines Kombinationsfeldsteuerelements zu einem Arbeitsblatt**

Um die Dateneingabe zu vereinfachen oder die Eingabe auf bestimmte von Ihnen definierte Elemente zu beschränken, können Sie eine Kombinationsfeld oder Dropdown-Liste der gültigen Eingaben erstellen, die aus Zellen an anderer Stelle im Arbeitsblatt zusammengestellt werden. Wenn Sie für eine Zelle eine Dropdown-Liste erstellen, wird ein Pfeil neben dieser Zelle angezeigt. Um Informationen in diese Zelle einzugeben, klicken Sie auf den Pfeil und dann auf den Eintrag, den Sie möchten.

### **Verwendung von Microsoft Excel**

Um ein Kombinationsfeld-Steuerelement in Ihrem Arbeitsblatt zu platzieren, befolgen Sie diese Schritte:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Kombinationsfeld**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Kombinationsfeld halten wird.
1. Sobald das Kombinationsfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement, um **Steuerelement formatieren** zu klicken und den Eingabebereich festzulegen.
1. Geben Sie im Feld **Zellverknüpfung** die Adresse der Zelle an, mit der dieses Kombinationsfeld verknüpft werden soll.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), mit der ein Combo-Box-Steuerlement einem Arbeitsblatt hinzugefügt werden kann. Die Methode gibt ein [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/)-Objekt zurück. Die Klasse [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) repräsentiert eine Combo-Box. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) gibt eine Zelle an, die mit der Combo-Box verknüpft ist.
- Die Eigenschaft [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) gibt den Arbeitsblattbereich der Zellen an, die die Combo-Box füllen.
- Die Eigenschaft [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) gibt die Anzahl der Listenzeilen an, die im Dropdown-Teil einer Combo-Box angezeigt werden.
- Die Eigenschaft [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) gibt an, ob die Combo-Box 3D-Schattierung aufweist.

Das folgende Beispiel zeigt, wie eine Combo-Box dem Arbeitsblatt hinzugefügt wird.

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

## **Hinzufügen eines Beschriftungssteuerelements zu einem Arbeitsblatt**

Labels sind eine Möglichkeit, Benutzern Informationen über den Inhalt eines Tabellenblatts zur Verfügung zu stellen. Aspose.Cells ermöglicht es, Labels einem Arbeitsblatt hinzuzufügen und zu manipulieren. Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), mit der ein Label-Steuerlement dem Arbeitsblatt hinzugefügt wird. Die Methode gibt ein [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/)-Objekt zurück. Die Klasse [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) repräsentiert ein Label im Arbeitsblatt. Sie hat einige wichtige Elemente:

- Die Methode [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) gibt einen Beschriftungszeichenfolge an.
- Die [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)-Methode gibt die [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) an, die Art und Weise, wie das Label an die Zellen im Arbeitsblatt angehängt ist.

Das folgende Beispiel zeigt, wie man einem Arbeitsblatt eine Beschriftung hinzufügt.

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

## **Hinzufügen eine Listfeld-Steuerung zu einem Arbeitsblatt**

Ein Listenfeld erstellt eine Liste-Steuerung, die die Auswahl eines einzelnen oder mehrerer Elemente ermöglicht.

### **Verwendung von Microsoft Excel**

Um eine Listfeld-Steuerung in einem Arbeitsblatt zu platzieren:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Listfeld**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das das Listenfeld halten wird.
1. Sobald das Listenfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf die Steuerung, um auf **Steuerelement formatieren** zu klicken und den Eingabebereich anzugeben.
1. Geben Sie im Feld **Zellenverknüpfung** die Adresse der Zelle an, mit der dieses Listenfeld verknüpft werden soll, und setzen Sie das Attribut für den Auswahltyp (Einzelauswahl, Mehrfachauswahl, Erweiterte Auswahl).
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), die dazu verwendet wird, ein Listenfeld-Steuerlement zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/)-Objekt zurück. Die Klasse [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) repräsentiert ein Listenfeld. Sie hat einige wichtige Elemente:

- Die [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/)-Methode gibt eine Zelle an, die mit dem Listenfeld verknüpft ist.
- Die [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/)-Methode gibt den Arbeitsblattbereich von Zellen an, die zur Befüllung des Listenfelds verwendet werden.
- Die [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/)-Methode gibt den Auswahmodus des Listenfelds an.
- Die [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/)-Methode zeigt an, ob das Listenfeld 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie man einem Arbeitsblatt ein Listenfeld hinzufügt.

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

## **Hinzufügen einer Schaltflächensteuerung zu einem Arbeitsblatt**

Schaltflächen sind nützlich, um Aktionen auszuführen. Manchmal ist es nützlich, einer Schaltfläche ein VBA-Makro zuzuweisen oder einen Hyperlink zuzuweisen, um eine Webseite zu öffnen.

### **Verwendung von Microsoft Excel**

Um eine Schaltflächensteuerung in Ihrem Arbeitsblatt zu platzieren:

1. Stellen Sie sicher, dass die **Formulare**-Symbolleiste angezeigt wird.
1. Klicken Sie auf das **Schaltflächen**-Werkzeug.
1. Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck zu definieren, das die Schaltfläche enthält.
1. Nachdem die Listenfeld im Arbeitsblatt platziert wurde, klicken Sie mit der rechten Maustaste auf die Steuerung und wählen Sie **Steuerung formatieren** aus, dann geben Sie ein VBA-Makro an und Attribute wie Schriftart, Ausrichtung, Größe, Rand usw. an.
1. Klicken Sie auf **OK**.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) enthält eine Methode namens [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), die verwendet wird, um eine Schaltflächensteuerung zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/)-Objekt zurück. Die Klasse [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) repräsentiert eine Schaltfläche. Sie verfügt über einige wichtige Elemente:

- Die Eigenschaft [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) gibt die Beschriftung der Schaltfläche an.
- Die Eigenschaft [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) gibt die Schriftattribute für das Label der Schaltflächensteuerung an.
- Die Eigenschaft [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) gibt die [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) an, wie die Schaltfläche an die Zellen im Arbeitsblatt angebracht ist.
- Die Eigenschaft [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) fügt eine Verknüpfung für die Schaltflächensteuerung hinzu. Durch Klicken auf die Schaltfläche wird zu der entsprechenden URL navigiert.

Das folgende Beispiel zeigt, wie Sie eine Schaltfläche zum Arbeitsblatt hinzufügen.

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

## **Hinzufügen einer Liniensteuerung zum Arbeitsblatt.**

### **Verwendung von Microsoft Excel**

1. Auf der **Zeichnen**-Symbolleiste klicken Sie auf **AutoFormen**, zeigen auf **Linien** und wählen den Linienstil aus, den Sie möchten.
1. Ziehen Sie, um die Linie zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Um die Linie auf 15-Grad-Winkel von ihrem Ausgangspunkt zu beschränken, halten Sie die UMSCHALTTASTE gedrückt, während Sie ziehen.
   1. Um die Linie in entgegengesetzte Richtungen vom ersten Endpunkt zu verlängern, halten Sie STRG gedrückt, während Sie ziehen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), mit der eine Linienform zum Arbeitsblatt hinzugefügt wird. Die Methode gibt ein [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/)-Objekt zurück. Die Klasse [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) repräsentiert eine Linie. Sie verfügt über einige wichtige Mitglieder:

- Die Methode [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) gibt das Format einer Linie an.
- Die Methode [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) gibt die [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) an, wie die Linie an die Zellen im Arbeitsblatt angebracht ist.

Das folgende Beispiel zeigt, wie Sie Linien zum Arbeitsblatt hinzufügen. Es erstellt drei Linien mit unterschiedlichen Stilen.

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

### **Hinzufügen eines Pfeilkopfs zu einer Linie**

Aspose.Cells ermöglicht es auch, Pfeillinien zu zeichnen. Es ist möglich, einer Linie eine Pfeilspitze hinzuzufügen und die Linie zu formatieren. Sie können z.B. die Farbe der Linie ändern oder das Gewicht und den Stil der Linie festlegen.

Das folgende Beispiel zeigt, wie Sie einen Pfeilkopf zu einer Linie hinzufügen.

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

## **Hinzufügen einer Rechtecksteuerung zu einem Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Rechteckformen in Ihren Arbeitsblättern zu zeichnen. Sie können ein Rechteck, ein Quadrat usw. erstellen. Es ist auch möglich, die Füllfarbe und die Rahmenlinienfarbe der Steuerung zu formatieren. Sie können z.B. die Farbe des Rechtecks ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil des Rechtecks spezifizieren, wie Sie es benötigen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie auf der **Zeichnen**-Symbolleiste auf **Rechteck**.
1. Ziehen Sie, um das Rechteck zu zeichnen.
1. Führen Sie einen oder beide der folgenden Schritte aus:
   1. Halten Sie die UMSCHALTTASTE gedrückt, um das Rechteck zu zeichnen und so ein Quadrat von seinem Ausgangspunkt aus zu beschränken.
   1. Halten Sie STRG gedrückt, um ein Rechteck von einem Mittelpunkt aus zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) stellt eine Methode namens [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/) zur Verfügung, die dazu dient, eine Rechtecksform zu einem Arbeitsblatt hinzuzufügen. Diese Methode gibt ein [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) stellt ein Rechteck dar. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) legt die Linienformatattribute eines Rechtecks fest.
- Die Eigenschaft [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) legt das [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) fest, wie das Rechteck an die Zellen im Arbeitsblatt angefügt ist.
- Die Eigenschaft [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) legt die Füllformatstile eines Rechtecks fest.

Das folgende Beispiel zeigt, wie Sie ein Rechteck zum Arbeitsblatt hinzufügen.

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

## **Hinzufügen einer Bogensteuerung zum Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, Bogenformen in Ihren Arbeitsblättern zu zeichnen. Sie können einfache und gefüllte Bogen erstellen. Sie können die Füllfarbe und die Randlinienfarbe des Steuerelements formatieren. Sie können zum Beispiel die Farbe des Bogens festlegen/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form nach Bedarf festlegen.

### **Verwendung von Microsoft Excel**

1. Klicken Sie in der Symbolleiste **Zeichnen** auf **Bogen** in den **AutoFormen**.
1. Ziehen Sie, um den Bogen zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), die verwendet wird, um eine Bogenform zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) repräsentiert einen Bogen. Sie enthält einige wichtige Elemente:

- Die [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)-Eigenschaft gibt die Linienformatattribute einer Bogenform an.
- Die [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)-Eigenschaft gibt an, wie der Bogen an die Zellen im Arbeitsblatt angefügt ist.
- Die [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)-Eigenschaft gibt die Füllformatstile der Form an.
- Die [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/)-Eigenschaft gibt den Zeilenindex der rechten unteren Ecke an.
- Die [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/)-Eigenschaft gibt den Spaltenindex der rechten unteren Ecke an.

Das folgende Beispiel zeigt, wie Bogenformen zum Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei Bogenformen: eine ist gefüllt und die andere ist einfach.

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

## **Ovale Steuerung zu einem Arbeitsblatt hinzufügen**

Mit Aspose.Cells können Sie ovale Formen in Arbeitsblättern zeichnen. Erstellen Sie einfache und gefüllte ovale Formen und formatieren Sie die Füllfarbe und die Randlinienfarbe des Steuerelements. Sie können zum Beispiel die Farbe des Ovals spezifizieren/ändern, die Schattierungsfarbe festlegen, das Gewicht und den Stil der Form festlegen.

### **Verwendung von Microsoft Excel**

- Klicken Sie auf der *Zeichnen*-Symbolleiste auf *Oval*.
- Ziehen Sie, um das Oval zu zeichnen.
- Führen Sie eine oder beide der folgenden Aktionen aus:
- Halten Sie beim Ziehen die UMSCHALTTASTE gedrückt, um das Oval zu einem Kreis von seinem Startpunkt zu beschränken.
- Halten Sie beim Ziehen die STRG-TASTE gedrückt, um ein Oval von einem Mittelpunkt aus zu zeichnen.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), die verwendet wird, um eine ovale Form zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) repräsentiert eine ovale Form. Sie enthält einige wichtige Elemente:

- Die [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/)-Eigenschaft gibt die Linienformatattribute einer ovalen Form an.
- Die [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/)-Eigenschaft gibt an, wie das Oval an die Zellen im Arbeitsblatt angefügt ist.
- Die [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/)-Eigenschaft gibt die Füllformatstile der Form an.
- Die [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/)-Eigenschaft gibt den Zeilenindex der rechten unteren Ecke an.
- Die [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/)-Eigenschaft gibt den Spaltenindex der rechten unteren Ecke an.

Das folgende Beispiel zeigt, wie ovale Formen zum Arbeitsblatt hinzugefügt werden. Das Beispiel erstellt zwei ovale Formen: eine gefüllte ovale Form und eine einfache Kreisform.

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

## **Hinzufügen von Spinner Control zum Arbeitsblatt**

Ein Drehfeld ist ein Textfeld, das mit einer Schaltfläche (einem Drehfeld) verbunden ist, bestehend aus einem Aufwärts- und einem Abwärtspfeil, den Sie anklicken, um den Wert im Textfeld inkrementell zu ändern. Durch Verwendung von Drehfeldern können Sie sehen, wie sich Eingaben auf Ihr Finanzmodell auf die Modellausgaben auswirken. Sie können ein Drehfeld an eine bestimmte Eingabezelle anhängen. Wenn Sie den Aufwärts- oder Abwärtspfeil am Drehfeld anklicken, wird der ganze Zahlenwert in der Ziel-Eingabezelle erhöht oder verringert. *Aspose.Cells* ermöglicht es Ihnen, Drehfelder in Ihren Arbeitsblättern zu erstellen.

### **Verwendung von Microsoft Excel**

Um ein Drehfeldsteuerelement in Ihrem Arbeitsblatt zu platzieren:

- Stellen Sie sicher, dass die *Formulare* Symbolleiste angezeigt wird.
- Klicken Sie auf das *Spinner* Werkzeug.
- Klicken und ziehen Sie im Arbeitsblattbereich, um das Rechteck festzulegen, das das Drehfeld halten wird.
- Sobald das Drehfeld im Arbeitsblatt platziert ist, klicken Sie mit der rechten Maustaste auf das Steuerelement und klicken Sie auf *Steuerelement formatieren* und geben Sie die maximalen, minimalen und inkrementellen Werte an.
- Geben Sie im Feld *Zellenverknüpfung* die Adresse der Zelle an, mit der dieses Drehfeld verknüpft sein soll.
- Klicken Sie auf *OK*.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), die verwendet wird, um ein Drehfeldsteuerelement zu einem Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) stellt ein Drehfeld dar. Sie hat einige wichtige Elemente:

- Die Eigenschaft [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) gibt eine Zelle an, die mit dem Drehfeld verknüpft ist.
- Die Eigenschaft [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) gibt den maximalen Wert für den Drehfeldbereich an.
- Die Eigenschaft [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) gibt den minimalen Wert für den Drehfeldbereich an.
- Die Eigenschaft [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) gibt den Wertbetrag an, um den ein Spinner eine Zeilenverschiebung inkrementiert.
- Die Eigenschaft [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) gibt an, ob das Drehfeld eine 3D-Schattierung aufweist.
- Die Eigenschaft [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) gibt den aktuellen Wert des Drehfelds an.

Das folgende Beispiel zeigt, wie ein Drehfeld zum Arbeitsblatt hinzugefügt wird.

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

## **Hinzufügen von Bildlaufleistensteuerelement zum Arbeitsblatt**

Ein Bildlaufleistensteuerelement wird verwendet, um Daten auf einem Arbeitsblatt in ähnlicher Weise wie ein Drehfeldsteuerelement auszuwählen. Durch Hinzufügen des Steuerelements zu einem Arbeitsblatt und Verknüpfen mit einer Zelle ist es möglich, einen numerischen Wert für die aktuelle Position des Steuerelements zurückzugeben.

### **Verwendung von Microsoft Excel**

- Um eine Bildlaufleiste in Excel 2003 und in früheren Versionen hinzuzufügen, klicken Sie auf die *Bildlaufleiste* Schaltfläche in der *Formular*-Symbolleiste und erstellen Sie dann eine Bildlaufleiste, die die Zellen B2:B6 in der Höhe abdeckt und etwa ein Viertel der Breite der Spalte ist.
- Um eine Bildlaufleiste in Excel 2007 hinzuzufügen, klicken Sie auf die *Entwickler* Registerkarte, klicken Sie auf *Einfügen* und dann auf *Bildlaufleiste* im Bereich Formularsteuerelemente.
- Klicken Sie mit der rechten Maustaste auf die Bildlaufleiste und wählen Sie dann *Steuerung formatieren*.
- Geben Sie die folgenden Informationen ein und klicken Sie auf *OK*:
  - Geben Sie im Feld *Aktueller Wert* 1 ein.
  - Geben Sie im Feld *Minimalwert* 1 ein. Dieser Wert beschränkt die obere Position der Bildlaufleiste auf den ersten Eintrag in der Liste.
  - Geben Sie im Feld *Maximalwert* 20 ein. Diese Zahl gibt die maximale Anzahl von Einträgen in der Liste an.
  - Geben Sie im Feld *Inkrementeller Wechsel* 1 ein. Dieser Wert steuert, wie viele Zahlen das Bildlaufleiste Steuerelement den aktuellen Wert inkrementiert.
  - Geben Sie im Feld *Seitenwechsel* 5 ein. Dieser Eintrag steuert, wie viel der aktuelle Wert inkrementiert wird, wenn Sie innerhalb der Bildlaufleiste auf einer Seite des Schiebereglers klicken.
  - Geben Sie zur Eingabe eines Zahlenwerts in Zelle G1 (abhängig davon, welches Element in der Liste ausgewählt ist), G1 in das *Zellen verknüpfen* Feld ein.
- Klicken Sie auf eine Zelle, sodass die Bildlaufleiste nicht ausgewählt ist.

Wenn Sie auf die Auf- oder Ab-Steuerung auf der Bildlaufleiste klicken, wird die Zelle G1 auf einen Wert aktualisiert, der den aktuellen Wert der Bildlaufleiste plus oder minus dem inkrementellen Wechsel der Bildlaufleiste angibt.

### **Verwendung von Aspose.Cells**

Die [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) Klasse bietet eine Methode mit dem Namen [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), die verwendet wird, um ein Bildlaufleiste-Steuerelement zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) stellt eine Bildlaufleiste dar. Sie hat einige wichtige Elemente:

- Die [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) Eigenschaft gibt eine Zelle an, die mit der Bildlaufleiste verknüpft ist.
- Die [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) Eigenschaft gibt den maximalen Wert für den Bereich der Bildlaufleiste an.
- Die [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) Eigenschaft gibt den minimalen Wert für den Bereich der Bildlaufleiste an.
- Die [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) Eigenschaft gibt den Wert an, um den eine Bildlaufleiste pro Zeilenwechsel inkrementiert wird.
- Die [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) Eigenschaft gibt an, ob die Bildlaufleiste eine 3D-Schattierung hat.
- Die [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) Eigenschaft gibt den aktuellen Wert der Bildlaufleiste an.
- Die [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) Eigenschaft gibt an, um wie viel der aktuelle Wert inkrementiert wird, wenn Sie innerhalb der Bildlaufleiste auf einer Seite des Schiebereglers klicken.

Das folgende Beispiel zeigt, wie Sie eine Bildlaufleiste zum Arbeitsblatt hinzufügen können.

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

## **Hinzufügen von GroupBox-Steuerelementen zu Gruppensteuerungen in einem Arbeitsblatt**

Manchmal müssen Sie Kontrollkästchen oder andere Steuerelemente implementieren, die zu einer bestimmten Gruppe gehören. Dies können Sie erreichen, indem Sie entweder ein Gruppenfeld oder ein Rechteck-Steuerelement einbeziehen. Eines dieser beiden Objekte dient dann als Begrenzung der Gruppe. Nach dem Hinzufügen einer dieser Formen können Sie dann zwei oder mehr Optionsfelder oder andere Gruppenobjekte hinzufügen.

### **Verwendung von Microsoft Excel**

Um ein Gruppenfeldsteuerelement in Ihr Arbeitsblatt einzufügen und Steuerelemente darin zu platzieren:

- Um ein Formular zu starten, klicken Sie im Hauptmenü auf *Ansicht*, gefolgt von *Symbolleisten* und *Formularen*.
- Auf der *Formulare*-Symbolleiste klicken Sie auf die *Gruppenfeld*-Schaltfläche und zeichnen ein Rechteck auf dem Arbeitsblatt.
- Geben Sie einen Beschriftungsstring für das Feld ein.
- Klicken Sie auf der *Formulare*-Symbolleiste auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* direkt unter dem Beschriftungsstring.
- Klicken Sie erneut auf der *Formulare*-Symbolleiste auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* unter dem ersten Optionsfeld.
- Noch einmal auf der *Formulare*-Symbolleiste klicken Sie auf *Optionsfeld* und klicken Sie innerhalb des *Gruppenfelds* unter dem vorherigen Optionsfeld.

### **Verwendung von Aspose.Cells**

Die Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) bietet eine Methode namens [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), die verwendet wird, um ein Gruppenfeld-Steuerelement zum Arbeitsblatt hinzuzufügen. Die Methode gibt ein [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/)-Objekt zurück. Außerdem gruppiert die Methode [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) der Klasse [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) die Formen. Sie nimmt ein [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/)-Array als Parameter und gibt ein [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/)-Objekt zurück. Die Klasse [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) repräsentiert ein Gruppenfeld. Sie verfügt über einige wichtige Mitglieder:

- Die Eigenschaft [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) gibt den Beschriftungsstring des Gruppenfelds an.
- Die Eigenschaft [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) gibt an, ob das Gruppenfeld eine 3D-Schattierung hat.

Das folgende Beispiel zeigt, wie Sie ein Gruppenfeld hinzufügen und die Steuerelemente im Arbeitsblatt gruppieren.

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

## **Erweiterte Themen**
- [AktiveX-Steuerelemente mit Aspose.Cells hinzufügen](/cells/de/cpp/add-activex-controls-using-aspose-cells/)
- [AktiveX-Steuerung entfernen](/cells/de/cpp/remove-activex-control/)
- [Aktualisieren Sie das ActiveX-ComboBox-Steuerelement](/cells/de/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
