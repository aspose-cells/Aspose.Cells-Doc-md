---
title: Hantera kontroller med C++
linktitle: Hantering av kontroller
type: docs
weight: 150
url: /sv/cpp/managing-controls/
description: Lär dig hur man lägger till och hanterar olika kontroller som linjer, rektanglar, bågar, ovaler, spinners, rullningslister och gruppboxar i kalkblad med Aspose.Cells och C++.
---

## **Introduktion**

Utvecklare kan lägga till olika ritobjekt som textrutor, kryssrutor, radioknappar, comboboxar, etiketter, knappar, linjer, rektanglar, bågar, ovaler, spinners, rullningslister, gruppboxar etc. Aspose.Cells tillhandahåller `Aspose::Cells::Drawing`-namnrymden som innehåller alla ritobjekt. Det finns dock några ritobjekt eller former som ännu inte stöds. Skapa dessa ritobjekt i ett designer-kalkblad med Microsoft Excel och importera sedan designer-kalkbladet till Aspose.Cells. Aspose.Cells tillåter att du laddar dessa ritobjekt från designer-kalkblad och skriver dem till en genererad fil.

## **Lägga till textruta-kontroll till ett arbetsblad**

Ett sätt att betona viktig information i en rapport är att använda en textruta. Till exempel lägg till text för att framhäva företagsnamnet eller indikera den geografiska regionen med högst försäljning etc. Aspose.Cells tillhandahåller [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/) klassen, använd för att lägga till en ny textruta till samlingen. Det finns en annan klass, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), som representerar en textruta som används för att definiera alla typer av inställningar. Den har några viktiga medlemmar:

- [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) -egenskapen specificerar placeringstypen.
- [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) -egenskapen specificerar teckensnittattributen.
- Metoden [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) lägger till en hyperlänk för textrutan.
- [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) -egenskapen returnerar ett [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/)-objekt som används för att ställa in fyllningsformatet för textrutan.
- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) returnerar [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/)-objekt som vanligtvis används för stil och tjocklek på textrutans linje.
- [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) -egenskapen specificerar den inmatade texten för textrutan.

I det följande exemplet skapas två textrutor i den första arbetsbladet i arbetsboken. Den första textrutan är välordnad med olika formatinställningar. Den andra är enkel.

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

## **Manipulera textrute-kontroller i designer- kalkylblad**

Aspose.Cells låter dig också komma åt textrutor i designkalkylbladen och manipulera dem. Använd egenskapen [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) för att få textrutor samlingen i arket.

Följande exempel använder Microsoft Excel-filen som vi skapade i det ovanstående exemplet. Det hämtar textsträngarna för de två textrutorna och ändrar texten i den andra textrutan för att spara filen.

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

## **Lägger till kontrollrutan för kryssruta i en arbetsbok**

Kryssrutor är användbara om du vill ge användaren ett sätt att välja mellan två alternativ, som sant eller falskt; ja eller nej. Aspose.Cells låter dig använda kryssrutor i kalkylblad. Till exempel kan du ha utvecklat ett ekonomiskt prognoskalkylblad där du antingen kan räkna med förvärvet eller inte. I detta fall vill du placera en kryssruta längst upp på kalkylbladet. Du kan sedan koppla statusen för denna kryssruta till en annan cell, så att om kryssrutan är markerad är värdet i cellen Sant; om den inte är markerad är värdet i cellen Falskt.

### **Använda Microsoft Excel**

För att placera en kryssruta i ditt kalkylblad, följ dessa steg:

1. Se till att formulär verktygsfältet visas.
1. Klicka på verktyget **Kryssruta** på formulär verktygsfältet.
1. I ditt arbetsbladsområde klickar du och drar för att definiera rektangeln som kommer att hålla kryssrutan och etiketten bredvid kryssrutan.
1. När kryssrutan är placerad, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna kryssruta ska länkas till.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Aspose.Cells tillhandahåller klassen [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), som används för att lägga till en ny kryssruta i samlingen. Det finns en annan klass, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), som representerar en kryssruta. Den har några viktiga medlemmar:

- Egenskapen [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är länkad till kryssrutan.
- Egenskapen [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specificerar den textsträng som är associerad med kryssrutan. Det är etiketten för kryssrutan.
- Egenskapen [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) specificerar om kryssrutan är markerad eller inte.

Följande exempel visar hur man lägger till en kryssruta i arbetsboken.

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

## **Lägger till alternativknappsstyrning till arbetsboken**

En radioknapp eller en alternativknapp är en kontroll gjord av en rund ruta. Användaren fattar sitt beslut genom att välja den runda rutan. En radioknapp åtföljs vanligtvis, om inte alltid, av andra. Sådana radioknappar visas och beter sig som en grupp. Användaren bestämmer vilken knapp som är giltig genom att endast välja en av dem. När användaren klickar på en knapp fylls den i. När en knapp i gruppen är vald är knapparna i samma grupp tomma.

### **Använda Microsoft Excel**

Följ dessa steg för att placera en radioknappskontroll i ditt arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget **Alternativknapp**.
1. I arbetsbladet klickar du och drar för att definiera rektangeln som kommer att hålla alternativknappen och etiketten bredvid alternativknappen.
1. När radioknappen är placerad i arbetsbladet, flytta muspekaren till etikettområdet och ändra etiketten.
1. I fältet Cell Link specificerar du adressen för den cell som denna radioknapp ska länkas till.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)-klassen erbjuder en metod som heter [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), vilken används för att lägga till en radioknappskontroll till ett kalkblad. Metoden returnerar ett [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/)-objekt. Klassen [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) representerar ett alternativknapp. Den har några viktiga medlemmar:

- Egenskapen [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är länkad till alternativknappen.
- Egenskapen [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specificerar den textsträng som är associerad med alternativknappen. Det är etiketten för alternativknappen.
- Egenskapen [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) specificerar om alternativknappen är markerad eller inte.
- Egenskapen [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specificerar fill formatet för alternativknappen.
- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specificerar linjeformatet för optionsknappen.

Följande exempel visar hur man lägger till alternativknappar i en arbetsbok. Exemplet lägger till tre alternativknappar som representerar åldersgrupper.

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

## **Lägga till Combobox-kontroll i ett arbetsblad**

För att underlätta inmatning av data eller begränsa inmatningar till vissa objekt som du definierar kan du skapa en combobox eller en nedrullningslista med giltiga inmatningar som är samlade från celler någon annanstans på arbetsbladet. När du skapar en nedrullningslista för en cell visas en pil bredvid den cellen. För att ange information i den cellen klickar du på pilen och klickar sedan på den post som du vill ha.

### **Använda Microsoft Excel**

Följ dessa steg för att placera en combobox-kontroll i ditt arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget för **Kombinationsruta**.
1. I området för din arbetsblad, klicka och dra för att definiera rektangeln som kommer att hålla kombinationsrutan.
1. När kombinationsrutan är placerad i arbetsbladet, högerklicka på kontrollen för att klicka på **Formatkontroll** och ange inmatningsintervallet.
1. I fältet för **Cell Länk**, ange adressen för cellen till vilken denna kombinationsruta ska länkas.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), vilket används för att lägga till en combo box-kontroll till ett arbetsblad. Metoden returnerar ett [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/)-objekt. Klassen [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) representerar en combo box. Den har några viktiga medlemmar:

- Egenskapen [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är länkad till combo boxen.
- Egenskapen [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) specificerar arbetsbokens område av celler som används för att fylla combo boxen.
- Egenskapen [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) specificerar antalet listrader som visas i nedrullningsdelen av en combo box.
- Egenskapen [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) indikerar om combo boxen har 3D-skuggning.

Följande exempel visar hur man lägger till en combo box i arbetsbladet.

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

## **Lägga till etikettkontroll i ett arbetsblad**

Etiketter är ett sätt att ge användarna information om ett kalkylblads innehåll. Aspose.Cells gör det möjligt att lägga till och manipulera etiketter i ett arbetsblad. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), som används för att lägga till en etikett-kontroll i arbetsbladet. Metoden returnerar ett [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/)-objekt. Klassen [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) representerar en etikett i arbetsbladet. Den har några viktiga medlemmar:

- Metoden [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specificerar en etiketts bildtext.
- Metoden [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specificerar [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), det sätt som etiketten är fäst vid cellerna i arbetsbladet.

Följande exempel visar hur man lägger till en etikett i arbetsbladet.

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

## **Lägga till en listrutekontroll i ett arbetsblad**

En listrutekontroll skapar en listkontroll som tillåter enkel eller flervals. artikelval.

### **Använda Microsoft Excel**

För att placera en listrutekontroll i ett arbetsblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på verktyget för **Listrute**.
1. I ditt arbetsbladsområde, klicka och dra för att definiera rektangeln som kommer att hålla listrutan.
1. När listrutan är placerad i arbetsbladet, högerklicka på kontrollen för att klicka på **Formatkontroll** och ange inmatningsintervallet.
1. I fältet för **Cell Länk**, ange adressen för cellen till vilken denna listruta ska länkas och ange attributet för valtyp (Enkel, Multi, Utöka).
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), vilket används för att lägga till en list box-kontroll i ett arbetsblad. Metoden returnerar ett [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/)-objekt. Klassen [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) representerar en listbox. Den har några viktiga medlemmar:

- Metoden [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är länkad till listboxen.
- Metoden [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) anger kalkylbladintervall av celler som används för att fylla listrutan.
- Metoden [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) anger urvalsläge för listrutan.
- Metoden [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) indikerar om listrutan har 3D-skuggning.

Följande exempel visar hur man lägger till en listruta i kalkylbladet.

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

## **Lägga till knappkontroll i ett kalkylblad**

Knappar är användbara för att utföra vissa åtgärder. Ibland är det användbart att tilldela en VBA-makro till knappen eller tilldela en hyperlänk för att öppna en webbsida.

### **Använda Microsoft Excel**

För att placera en knappkontroll i ditt kalkylblad:

1. Se till att **Formulär** verktygsfältet visas.
1. Klicka på **Knapp**-verktyget.
1. I ditt kalkylbladsområde klicka och dra för att definiera rektangeln som kommer att innehålla knappen.
1. När listrutan väl är placerad i kalkylbladet, högerklicka på kontrollen och välj **Formatera kontroll**, ange sedan en VBA-makro och attributrelaterad font, justering, storlek, marginal etc.
1. Klicka på **OK**.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod med namnet [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), som används för att lägga till en knappkontroll i kalkylbladet. Metoden returnerar ett [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) objekt. Klassen [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) representerar en knapp. Den har några viktiga medlemmar:

- Egenskapen [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) anger knappens text.
- Egenskapen [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) anger teckensnittsattribut för etiketten på knappkontrollen.
- Egenskapen [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) anger [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), sättet knappen är kopplad till cellerna i kalkylbladet.
- Egenskapen [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) lägger till en hyperlänk för knappkontrollen. Genom att klicka på knappen navigeras till relaterad URL.

Följande exempel visar hur man lägger till en knapp i kalkylbladet.

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

## **Lägga Till Linjekontroll i Kalkylbladet**

### **Använda Microsoft Excel**

1. På **Ritning** verktygsfältet, klicka på **Autoshapes**, peka på **Linjer** och välj linjestilen du vill ha.
1. Dra för att rita linjen.
1. Gör en eller båda av följande:
   1. För att begränsa linjen att rita vid 15-graders vinklar från dess startpunkt, håll ner SKIFT när du drar.
   1. För att förlänga linjen i motsatta riktningar från första ändpunkten, håll ner CTRL när du drar.

### **Använda Aspose.Cells**

[**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/)-klassen tillhandahåller en metod som heter [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), vilken används för att lägga till en linjeform till kalkbladet. Metoden returnerar ett [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/)-objekt. Klassen [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) representerar en linje. Den har några viktiga medlemmar:

- Metoden [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) anger formatet för en linje.
- Metoden [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) anger [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), sättet linjen är kopplad till cellerna i kalkylbladet.

Följande exempel visar hur man lägger till linjer i kalkylbladet. Det skapar tre linjer med olika stilar.

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

### **Lägga Till en Pilkontroll till en Linje**

Aspose.Cells låter dig också rita pilrakningar. Det är möjligt att lägga till en pilspets på en linje och formatera linjen. Till exempel kan du ändra färgen på linjen eller ange linjens vikt och stil.

Det följande exemplet visar hur du lägger till en pilspets på en linje.

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

## **Lägga till rektangelkontroll i ett arbetsblad**

Aspose.Cells låter dig rita rektangelformar i dina arbetsblad. Du kan skapa en rektangel, kvadrat etc. Du har också möjlighet att formatera fyllningsfärgen och kantlinjens färg för kontrollen. Till exempel kan du ändra färgen på rektangeln, ange skuggningsfärg, specificera vikten och stilen på rektangeln enligt ditt behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Rektangel**.
1. Dra för att rita rektangeln.
1. Gör en eller båda av följande:
   1. För att begränsa rektangeln för att rita en kvadrat från dess startpunkt, håll ned SKIFT när du drar.
   1. För att rita en rektangel från en mittpunkt, håll ned CTRL när du drar.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), som används för att lägga till en rektangelform på ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) objekt. Klassen [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) representerar en rektangel. Den har några viktiga medlemmar:

- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) anger linjeformatattribut för en rektangel.
- Egenskapen [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) anger [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), sättet rektangeln är ansluten till cellerna i arbetsbladet.
- Egenskapen [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) anger fyllningsformatstilar för en rektangel.

Det följande exemplet visar hur du lägger till en rektangel i arbetsbladet.

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

## **Lägga till bågekontroll till arbetsbladet**

Aspose.Cells låter dig rita bågformer i dina arbetsblad. Du kan skapa enkla och fyllda bågar. Du har möjlighet att formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Till exempel kan du specificera/ändra färgen på bågen, ange skuggningsfärg, specificera vikten och stilen på formen enligt ditt behov.

### **Använda Microsoft Excel**

1. På verktygsfältet **Ritningar** klickar du på **Båge** i **AutoShapes**.
1. Dra för att rita bågen.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), som används för att lägga till en bågform på ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) objekt. Klassen [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) representerar en båge. Den har några viktiga medlemmar:

- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) anger linjeformatattribut för en bågform.
- Egenskapen [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) anger [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), sättet bågen är ansluten till cellerna i arbetsbladet.
- Egenskapen [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specificerar fyllnadformatstilar för formen.
- Egenskapen [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) specificerar den nedre högra hörnradsindex.
- Egenskapen [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) specificerar den nedre högra hörnkolumnindex.

Det följande exemplet visar hur du lägger till bågformer i arbetsbladet. Exemplet skapar två bågformer: en är fylld och den andra är enkel.

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

## **Lägga till ovalkontroll i ett arbetsblad**

Aspose.Cells låter dig rita ovala former i arbetsblad. Skapa enkla och fyllda ovala former och formatera fyllningsfärgen och kantlinjefärgen för kontrollen. Till exempel kan du specificera/ändra färgen på ovalen, ange skuggningsfärg, specificera vikten och stilen på formen enligt ditt behov.

### **Använda Microsoft Excel**

- På *Rita*-verktygsfältet klickar du på *Oval*.
- Dra för att rita ovalen.
- Gör en eller båda följande:
- För att begränsa ovalen och rita en cirkel från dess startpunkt, håll ned SKIFT när du drar.
- För att rita en oval från en mittpunkt, håll ner CTRL när du drar.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), som används för att lägga till en oval form i en arbetsbok. Metoden returnerar ett [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) objekt. Klassen [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) representerar en oval form. Det har några viktiga medlemmar:

- Egenskapen [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) specificerar linjeformatattributen för en oval form.
- Egenskapen [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) specificerar [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), sättet som ovalen är kopplad till cellerna i arbetsboken.
- Egenskapen [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) specificerar fyllnadformatstilar för formen.
- Egenskapen [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) specificerar den nedre högra hörnradsindex.
- Egenskapen [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) specificerar den nedre högra hörnkolumnindex.

Följande exempel visar hur man lägger till ovala former i arbetsboken. Exemplet skapar två ovala former: en är fylld oval, den andra är en enkel cirkel.

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

## **Lägger till spinnerkontroll på arbetsboken**

En snurrfunktion är en textruta som är kopplad till en knapp (kallad en snurrknapp) som består av en uppåtpil och en nedåtpil som du klickar på för att successivt ändra värdet i textrutan. Genom att använda snurrfunktioner kan du se hur inmatningar i din finansiella modell kommer att påverka modellens utfall. Du kan koppla en snurrknapp till en specifik inmatningscell. När du klickar på uppåtpilen eller nedåtpilen på snurrknappen ökar eller minskar det heltalvärde som är kopplat till inmatningscellen. * Aspose.Cells * låter dig skapa snurrare i dina arbetsblad.

### **Använda Microsoft Excel**

För att placera en snurrkontroll i ditt arbetsblad:

- Se till att *Formulär * verktygsfält visas.
- Klicka på *Snurr* verktyget.
- I ditt arbetsbladsområde klicka och dra för att definiera rektangeln som kommer att hålla snurraren.
- När snurraren är placerad i arbetsbladet, högerklicka på kontrollen och klicka på *Formatkontroll* och ange maximala, minimala och inkrementella värden.
- I fältet *Cellänk* ange adressen för cellen till vilken denna snurrfunktion ska länkas.
- Klicka på *OK*.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod som heter [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), som används för att lägga till en snurrknapp till ett arbetsblad. Metoden returnerar ett [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) objekt. Klassen [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) representerar en snurrknapp. Det har några viktiga medlemmar:

- Egenskapen [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är kopplad till snurrknappen.
- Egenskapen [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) specificerar det maximala värdet för snurrknappsområdet.
- Egenskapen [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) specificerar det minimala värdet för snurrknappsområdet.
- Egenskapen [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) specificerar värdet för vilket en snurrare ökar med en linjebläddring.
- Egenskapen [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) indikerar om snurrknappen har 3D-skuggning.
- Egenskapen [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) specificerar det aktuella värdet för snurrknappen.

Följande exempel visar hur man lägger till en snurrknapp till arbetsbladet.

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

## **Lägger till rullningsfältkontroll till ett arbetsblad**

En rullningsfältkontroll används för att hjälpa till att välja data på ett arbetsblad på ett liknande sätt som en snurrknappkontroll. Genom att lägga till kontrollen till ett arbetsblad och koppla den till en cell är det möjligt att returnera ett numeriskt värde för den aktuella positionen för kontrollen.

### **Använda Microsoft Excel**

- För att lägga till ett rullningsfält i Excel 2003 och i tidigare versioner, klicka på *Rullningsfält* knappen på *Formulär* verktygsfältet, och skapa sedan ett rullningsfält som täcker cellerna B2:B6 i höjd och är ungefär en fjärdedel av bredden av kolumnen.
- För att lägga till ett rullningsfält i Excel 2007, klicka på *Utvecklar* fliken, klicka på *Infoga*, och klicka sedan på *Rullningsfält* i avsnittet Formulärkontroller.
- Högerklicka på rullningsfältet och klicka sedan på *Formatkontroll*.
- Skriv följande information och klicka på *OK*:
  - I rutan för *Aktuellt värde*, skriv 1.
  - I rutan för *Minsta värde*, skriv 1. Detta värde begränsar överkanten av rullningslisten till det första objektet i listan.
  - I rutan för *Högsta värde*, skriv 20. Detta nummer anger det maximala antalet poster i listan.
  - I rutan för *Inkrementellt värde*, skriv 1. Detta värde styr hur många nummer rullningslisten ökar det aktuella värdet med.
  - I rutan för *Sidändring*, skriv 5. Detta styrs hur mycket det aktuella värdet kommer att öka om du klickar inne i rullningslisten på någon av sidorna av skrollådan.
  - För att placera ett nummervärde i cell G1 (beroende på vilket objekt som är valt i listan), skriv G1 i rutan för *Cellkoppling*.
- Klicka på vilken cell som helst så att rullningslisten inte är vald.

När du klickar på upp- eller nedkontrollen på rullningslisten, uppdateras cellen G1 till ett nummer som indikerar det aktuella värdet för rullningslisten plus eller minus det inkrementella värdet för rullningslisten.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod med namnet [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), som används för att lägga till en rullningslistkontroll i kalkylarket. Metoden returnerar en [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) objekt. Klassen [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) representerar en rullningslist. Den har några viktiga medlemmar:

- Egenskapen [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) specificerar en cell som är kopplad till rullningslisten.
- Egenskapen [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) specificerar det maximala värdet för rullningslistintervallet.
- Egenskapen [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) specificerar det minsta värdet för rullningslistintervallet.
- Egenskapen [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) specificerar beloppet med vilket en rullningslist ökas en linjerullning.
- Egenskapen [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) indikerar om rullningslisten har 3D-skuggning.
- Egenskapen [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) specificerar det aktuella värdet för rullningslisten.
- Egenskapen [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) specificerar hur mycket det aktuella värdet kommer att öka om du klickar inne i rullningslisten på någon av sidorna av skrollådan.

Följande exempel visar hur du lägger till en rullningslist i kalkylarket.

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

## **Lägga till GroupBox-kontroll till gruppkontroller i ett kalkylblad**

Ibland måste du implementera alternativknappar eller andra kontroller som tillhör en viss grupp, du kan implementera genom att inkludera antingen en groupbox-kontroll eller en rektangelkontroll. Någon av dessa två objekt skulle fungera som avgränsare för gruppen. Efter att ha lagt till en av dessa former kan du sedan lägga till två eller fler alternativknappar eller andra gruppkontroller.

### **Använda Microsoft Excel**

För att placera en groupbox-kontroll i ditt kalkylblad och placera kontroller i den:

- För att starta en formulär, på huvudmenyn, klicka på *Visa*, följt av *Verktygsfält* och *Formulär*.
- På *Formulär* verktygsfält, klicka på *Group Box* och rita en rektangel på kalkylarket.
- Skriv en bildtext för rutan.
- På *Formulär* verktygsfält, klicka på *Alternativknapp* och klicka inne i *Group Box* strax under bildtexten.
- Från *Formulär* verktygsfältet igen, klicka på *Alternativknapp* och klicka inne i *Group Box* under den första alternativknappen.
- Ännu en gång på *Formulär* verktygsfält, klicka på *Alternativknapp* och klicka inne i *Group Box* under den föregående alternativknappen.

### **Använda Aspose.Cells**

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) tillhandahåller en metod med namnet [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), som används för att lägga till en group box-kontroll i kalkylarket. Metoden returnerar en [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) objekt. Dessutom grupperar [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) metoden av klassen [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) formerna, den tar en [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) array som parameter och returnerar en [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/) objekt. Klassen [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) representerar en group box. Den har några viktiga medlemmar:

- Egenskapen [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) specificerar en sträng för group box.
- Egenskapen [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) indikerar om group box har 3D-skuggning.

Följande exempel visar hur du ska lägga till en gruppbox och gruppera kontrollerna på arbetsbladet.

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

## **Fortsatta ämnen**
- [Lägg till ActiveX-kontroller med hjälp av Aspose.Cells](/cells/sv/cpp/add-activex-controls-using-aspose-cells/)
- [Ta bort ActiveX-kontroll](/cells/sv/cpp/remove-activex-control/)
- [Uppdatera ActiveX ComboBox Control](/cells/sv/cpp/update-activex-combobox-control/)
