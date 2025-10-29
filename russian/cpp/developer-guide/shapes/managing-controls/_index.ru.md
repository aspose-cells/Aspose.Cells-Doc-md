---
title: Управление элементами управления с C++
linktitle: Управление элементами управления
type: docs
weight: 150
url: /ru/cpp/managing-controls/
description: Узнайте, как добавлять и управлять различными элементами управления, такими как линии, прямоугольники, дуги, эллипсы, спиннеры, полосы прокрутки и групповые боксы в рабочих листах с помощью Aspose.Cells и C++.
---

## **Введение**

Разработчики могут добавлять различные объекты чертежа, такие как текстовые поля, чекбоксы, радиокнопки, выпадающие списки, метки, кнопки, линии, прямоугольники, дуги, эллипсы, спиннеры, полосы прокрутки, групповые боксы и др. Aspose.Cells предоставляет пространство имен `Aspose::Cells::Drawing`, которое содержит все объекты рисования. Однако некоторые объекты или фигуры еще не поддерживаются. Создайте эти объекты чертежа в проекте с помощью Microsoft Excel, а затем импортируйте их в Aspose.Cells. Aspose.Cells позволяет загружать эти объекты из проекта и сохранять их в сгенерированный файл.

## **Добавление элемента управления текстовым полем на лист**

Один из способов выделить важную информацию в отчете - это использование текстового поля. Например, добавьте текст для выделения названия компании или для указания географического региона с самыми высокими продажами и т. д. Aspose.Cells предоставляет класс [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/), используемый для добавления нового текстового поля в коллекцию. Есть еще один класс, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), который представляет текстовое поле, используемое для определения всех типов настроек. У него есть несколько важных членов:

- Свойство [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) определяет тип размещения.
- Свойство [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) определяет атрибуты шрифта.
- Метод [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) добавляет гиперссылку для текстового поля.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) возвращает объект [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/), используемый для установки формата заливки для текстового поля.
- Свойство [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) возвращает объект [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/), обычно используемый для стиля и толщины линии текстового поля.
- Свойство [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) определяет входной текст для текстового поля.

В следующем примере создаются два текстовых поля на первом листе книги. Первое текстовое поле хорошо оборудовано различными настройками формата. Второе является простым.

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

## **Манипулирование элементами управления текстовыми полями в электронных таблицах дизайнера**

Aspose.Cells также позволяет вам получать доступ к текстовым полям в электронных таблицах дизайнера и манипулировать ими. Используйте свойство [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/), чтобы получить коллекцию текстовых полей на листе.

В следующем примере используется файл Microsoft Excel, созданный в вышеприведенном примере. Он получает текстовые строки двух текстовых полей и изменяет текст второго текстового поля для сохранения файла.

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

## **Добавление элемента управления флажком на лист**

Флажки удобны, если вы хотите предоставить пользователю возможность выбрать между двумя вариантами, например, true или false; да или нет. Aspose.Cells позволяет использовать флажки на листах. Например, вы можете создать рабочую книгу с финансовым прогнозом, в которой нужно учесть определенное приобретение или нет. В этом случае вы можете разместить флажок наверху листа. Затем вы можете связать состояние этого флажка с другой ячейкой, чтобы, если флажок выбран, значение ячейки будет True; если он не выбран, значение ячейки будет False.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления флажком на вашем листе, выполните следующие шаги:

1. Убедитесь, что отображается панель инструментов Формы.
1. Нажмите на инструмент **Флажок** на панели инструментов Формы.
1. В области вашего листа нажмите и перетащите, чтобы определить прямоугольник, в котором будет размещен флажок и метка рядом с флажком.
1. После размещения флажка перейдите курсором мыши в область метки и измените метку.
1. В поле Cell Link укажите адрес ячейки, к которой должен быть привязан этот флажок.
1. Нажмите на **ОК**.

### **Использование Aspose.Cells**

Aspose.Cells предоставляет класс [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), который используется для добавления нового флажка в коллекцию. Еще один класс, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), представляет флажок. Он имеет некоторые важные члены:

- Cвойство [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) указывает ячейку, с которой связан флажок.
- Cвойство [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) указывает текстовую строку, связанную с флажком. Это метка флажка.
- Cвойство [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) указывает, отмечен ли флажок.

В следующем примере показано, как добавить флажок на лист.

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

## **Добавление элемента управления кнопкой радио на лист**

Кнопка радио или кнопка опции — это элемент управления в форме круглого фрагмента, пользователь принимает решение, выбирая круглый фрагмент. Кнопка радио обычно, если не всегда, сопровождается другими. Такие кнопки радио отображаются и действуют как группа. Пользователь определяет, какая кнопка является действительной, выбирая только одну из них. При выборе одной кнопки она заполняется. Когда выбрана одна кнопка из группы, кнопки той же группы остаются пустыми.

### **Использование Microsoft Excel**

Для размещения элемента управления кнопкой радио на листе выполните следующие шаги:

1. Убедитесь, что панель **Формы** отображается.
1. Нажмите инструмент **Кнопка опции**.
1. На листе щелкните и перетащите для определения прямоугольника, который будет содержать кнопку опции и метку рядом с кнопкой опции.
1. После размещения кнопки радио на листе перейдите курсором мыши в область метки и измените метку.
1. В поле Cell Link укажите адрес ячейки, к которой должна быть привязана эта кнопка радио.
1. Нажмите **ОК**.

### **Использование Aspose.Cells**

Класс [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), который используется для добавления элемента управления радиокнопкой в рабочий лист. Метод возвращает объект [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/). Класс [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) представляет опциональную кнопку. Он содержит некоторые важные члены:

- Cвойство [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) указывает ячейку, с которой связана кнопка радио.
- Cвойство [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) указывает текстовую строку, связанную с кнопкой радио. Это метка кнопки радио.
- Cвойство [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) указывает, выбрана ли кнопка радио или нет.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) определяет формат заполнения переключателя.
- Свойство [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) определяет стили формата линии переключателя.

В следующем примере показано, как добавить переключатели на рабочий лист. Пример добавляет три радиокнопки, представляющие возрастные группы.

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

## **Добавление элемента управления 'Комбинированный список' на рабочий лист**

Для упрощения ввода данных или ограничения ввода определенных элементов, можно создать комбинированный список или раскрывающийся список допустимых записей, которые собраны из ячеек в другом месте рабочего листа. Когда вы создаете раскрывающийся список для ячейки, рядом с этой ячейкой отображается стрелка. Чтобы ввести информацию в эту ячейку, щелкните стрелку, а затем щелкните нужную запись.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления 'Комбинированный список' на рабочем листе, выполните следующие шаги:

1. Убедитесь, что панель **Формы** отображается.
1. Щелкните инструмент **Комбинированный список**.
1. В области рабочего листа нажмите и перетащите, чтобы определить прямоугольник, который будет содержать комбинированный список.
1. Как только комбинированный список размещен на рабочем листе, щелкните правой кнопкой мыши по элементу управления и выберите **Формат элемента управления**, чтобы указать диапазон ввода.
1. В поле **Связь с ячейкой** укажите адрес ячейки, к которой должен быть привязан этот комбинированный список.
1. Нажмите на **ОК**.

### **Использование Aspose.Cells**

Класс [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), который используется для добавления элемента управления 'Комбинированный список' на рабочий лист. Метод возвращает объект [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/). Класс [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) представляет комбинированный список. У него есть некоторые важные члены:

- Свойство [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) определяет ячейку, которая привязана к комбинированному списку.
- Свойство [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) определяет диапазон ячеек рабочего листа, используемых для заполнения комбинированного списка.
- Свойство [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) определяет количество строк списка, отображаемых в раскрывающейся части комбинированного списка.
- Свойство [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) указывает, имеет ли комбинированный список 3D-теневую окраску.

В следующем примере показано, как добавить комбинированный список на рабочий лист.

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

## **Добавление элемента управления 'Метка' на рабочий лист**

Метки - это средство предоставления пользователям информации о содержании таблицы. Aspose.Cells позволяет добавлять и управлять метками на рабочем листе. Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), используемый для добавления элемента управления 'Метка' на рабочий лист. Метод возвращает объект [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). Класс [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) представляет метку на рабочем листе. У него есть некоторые важные члены:

- Метод [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) указывает строку заголовка метки.
- Метод [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) указывает [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/) - способ прикрепления метки к ячейкам в листе.

В следующем примере показано, как добавить метку на лист.

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

## **Добавление элемента управления список на листе**

Элемен управления список создает элемент управления, который позволяет выбирать один или несколько элементов.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления список на листе:

1. Убедитесь, что панель **Формы** отображается.
1. Нажмите кнопку **Элемент управления список**.
1. В области вашего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать список.
1. Как только элемент управления списка размещен на листе, щелкните правой кнопкой мыши на элементе управления и щелкните **Форматировать элемент управления**, чтобы указать диапазон ввода.
1. В поле **Связь с ячейкой** укажите адрес ячейки, с которой должен быть связан этот список, и установите атрибут типа выбора (Одиночный, Множественный, Расширенный)
1. Нажмите **ОК**.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), который используется для добавления элемента управления списка на лист. Метод возвращает объект [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/). Класс [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) представляет список. У него есть несколько важных членов:

- Метод [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) указывает ячейку, которая связана с элементом управления списка.
- Метод [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) указывает диапазон ячеек листа, использующихся для заполнения списка.
- Метод [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) указывает режим выбора элементов списка.
- Метод [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) указывает, имеет ли список 3D-затенение.

В следующем примере показано, как добавить список на лист.

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

## **Добавление элемента управления кнопка на лист**

Кнопки полезны для выполнения некоторых действий. Иногда полезно назначить макрос VBA на кнопку или назначить гиперссылку для открытия веб-страницы.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления кнопка на вашем листе:

1. Убедитесь, что панель **Формы** отображается.
1. Щелкните инструмент **Кнопка**.
1. В области вашего листа щелкните и перетащите для определения прямоугольника, который будет содержать кнопку.
1. Как только список размещен на листе, щелкните правой кнопкой мыши на элементе управления и выберите **Формат управления**, затем укажите VBA-макрос и атрибуты, касающиеся шрифта, выравнивания, размера, полей и т. д.
1. Нажмите на **ОК**.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), используемый для добавления элемента управления кнопкой на лист. Метод возвращает объект [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/). Класс [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) представляет кнопку. У него есть некоторые важные члены:

- Свойство [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) определяет заголовок кнопки.
- Свойство [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) определяет атрибуты шрифта для подписи элемента управления кнопкой.
- Свойство [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) определяет [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), способ, которым кнопка присоединена к ячейкам на листе.
- Свойство [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) добавляет гиперссылку для элемента управления кнопкой. При нажатии на кнопку будет выполнено переход по связанному URL.

Приведенный ниже пример показывает, как добавить кнопку на лист.

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

## **Добавление линейного элемента управления на лист**

### **Использование Microsoft Excel**

1. На панели инструментов **Рисование** щелкните **Автофигуры**, наведите указатель на **Линии** и выберите стиль линии.
1. Перетащите для создания линии.
1. Выполните одно или оба из следующего:
   1. Для ограничения углов рисования линии под углом 15 градусов от начальной точки удерживайте клавишу SHIFT при перетаскивании.
   1. Чтобы удлинить линию в противоположных направлениях от первой конечной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), который используется для добавления линии в рабочий лист. Метод возвращает объект [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/). Класс [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) представляет линию. Он содержит некоторые важные члены:

- Метод [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) определяет формат линии.
- Метод [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) определяет [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), способ, которым линия присоединена к ячейкам на листе.

Следующий пример показывает, как добавить линии на лист. Создаются три линии с разными стилями.

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

### **Добавление стрелки к линии**

Aspose.Cells также позволяет вам рисовать стрелки. Возможно добавление стрелки к линии и форматирование линии. Например, вы можете изменить цвет линии или указать ее толщину и стиль.

Следующий пример показывает, как добавить стрелку к линии.

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

## **Добавление прямоугольного контроля на лист**

Aspose.Cells позволяет вам рисовать прямоугольные формы в ваших листах. Вы можете создать прямоугольник, квадрат и т. д. Вы также можете форматировать цвет заливки и цвет граничной линии контроля. Например, вы можете изменить цвет прямоугольника, задать цвет заливки, указать толщину и стиль прямоугольника по вашему усмотрению.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Прямоугольник**.
1. Перетащите, чтобы нарисовать прямоугольник.
1. Выполните одно или оба из следующего:
   1. Чтобы ограничить прямоугольник и нарисовать квадрат от его начальной точки, удерживайте клавишу SHIFT во время перетаскивания.
   1. Чтобы нарисовать прямоугольник из центральной точки, удерживайте клавишу CTRL во время перетаскивания.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), который используется для добавления прямоугольной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/). Класс [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) представляет прямоугольник. У него есть несколько важных членов:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) указывает атрибуты форматирования линии прямоугольника.
- Свойство [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) указывает [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), способ, которым прямоугольник прикреплен к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) указывает стили форматирования заливки прямоугольника.

Следующий пример показывает, как добавить прямоугольник на лист.

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

## **Добавление дугового контроля на лист**

Aspose.Cells позволяет вам рисовать дуговые формы на ваших листах. Вы можете создавать простые и заполненные дуги. Вы можете форматировать цвет заливки и цвет граничной линии контроля. Например, вы можете указать / изменить цвет дуги, установить цвет заливки, указать толщину и стиль формы по вашему усмотрению.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Дуга** в **Автофигуры**.
1. Перетащите, чтобы нарисовать дугу.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), который используется для добавления формы дуги на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/). Класс [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) представляет дугу. У него есть некоторые важные члены:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) определяет атрибуты формата линии формы дуги.
- Свойство [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) определяет [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), способ, которым дуга присоединена к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) определяет стили формата заливки формы.
- Свойство [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) определяет индекс строки нижнего правого угла.
- Свойство [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить формы дуг на лист. Пример создает две формы дуги: одну заполненную, а другую простую.

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

## **Добавление овального элемента управления на лист**

Aspose.Cells позволяет вам рисовать овальные формы на листах. Создайте простые и закрашенные овальные формы и отформатируйте цвет заливки и цвет граничной линии элемента управления. Например, вы можете указать / изменить цвет овала, установить цвет закрашивания, указать вес и стиль формы.

### **Использование Microsoft Excel**

- На панели инструментов *Рисование* щелкните *Овал*.
- Перетащите, чтобы нарисовать овал.
- Выполните одно или оба следующих действия:
- Чтобы ограничить овал и нарисовать круг из его начальной точки, зажмите клавишу SHIFT при перетаскивании.
- Чтобы нарисовать овал из центральной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), который используется для добавления овальной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/). Класс [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) представляет овальную форму. У него есть некоторые важные члены:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) определяет атрибуты формата линии овальной формы.
- Свойство [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) определяет [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), способ, которым овал присоединен к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) определяет стили формата заливки формы.
- Свойство [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) определяет индекс строки нижнего правого угла.
- Свойство [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить овальные формы на лист. Пример создает две овальные формы: одна заполнена, а другая представляет собой просто кружок.

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

## **Добавление элемента управления спинбокс на лист**

Спинбокс - это текстовое поле, присоединенное к кнопке (называемой спинкнопка), состоящей из стрелки вверх и стрелки вниз, по которой вы щелкаете для пошагового изменения значения в текстовом поле. Используя спинбоксы, вы можете видеть, как изменения ввода влияют на модель вывода в вашей финансовой модели. Вы можете присоединить спинкнопку к определенной ячейке ввода. Когда вы нажимаете на стрелку вверх или вниз на спинкнопке, целочисленное значение в целевой ячейке ввода увеличивается или уменьшается. *Aspose.Cells* позволяет вам создавать спинбоксы на ваших листах.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления спинбокс на листе:

- Убедитесь, что отображается *панель инструментов Формы*.
- Щелкните инструмент *Спиннер*.
- В области вашего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать спиннер.
- Как только спиннер размещен на листе, щелкните правой кнопкой мыши по элементу управления и выберите *Форматировать элемент управления* и укажите максимальное, минимальное и инкрементальное значения.
- В поле *Связь с ячейкой* укажите адрес ячейки, к которой должен быть привязан этот спинбокс.
- Щелкните *OK*.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), который используется для добавления элемента управления спинбокс на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/). Класс [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) представляет собой спинбокс. Он имеет некоторые важные члены:

- Свойство [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) указывает на ячейку, которая привязана к спинбоксу.
- Свойство [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) указывает максимальное значение для диапазона спинбокса.
- Свойство [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) указывает минимальное значение для диапазона спинбокса.
- Свойство [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) указывает значение инкремента для построчной прокрутки спиннера.
- Свойство [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) указывает, имеет ли спинбокс трехмерную тень.
- Свойство [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) указывает текущее значение спинбокса.

В следующем примере показано, как добавить спинбокс на лист.

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

## **Добавление полосы прокрутки на лист**

Элемент управления полосой прокрутки используется для выбора данных на листе аналогичным образом спинбоксу. Добавляя элемент управления к листу и привязывая его к ячейке, можно вернуть числовое значение текущего положения элемента управления.

### **Использование Microsoft Excel**

- Чтобы добавить полосу прокрутки в Excel 2003 и более ранних версиях, щелкните кнопку *Полоса Прокрутки* на панели *Формы* и затем создайте полосу прокрутки, которая занимает ячейки B2:B6 по высоте и примерно четверть ширины столбца.
- Чтобы добавить полосу прокрутки в Excel 2007, щелкните вкладку *Разработчик*, затем *Вставка* и выберите *Полоса Прокрутки* в разделе Элементы управления формы.
- Щелкните правой кнопкой мыши на полосе прокрутки, затем выберите *Формат управления*.
- Введите следующую информацию и нажмите *OK*:
  - В поле *Текущее значение* введите 1.
  - В поле *Минимальное значение* введите 1. Это значение ограничивает верхнюю границу полосы прокрутки первым элементом в списке.
  - В поле *Максимальное значение* введите 20. Это число указывает максимальное количество записей в списке.
  - В поле *Инкрементное изменение* введите 1. Это значение управляет количеством чисел, на которое элемент управления полосой прокрутки приращивает текущее значение.
  - В поле *Изменение страницы* введите 5. Эта запись управляет тем, насколько увеличится текущее значение при щелчке внутри полосы прокрутки с обеих сторон ползунка.
  - Чтобы поместить числовое значение в ячейку G1 (в зависимости от выбранного элемента в списке), введите G1 в поле *Ссылка на ячейку*.
- Щелкните на любой ячейке, чтобы полоса прокрутки не была выбрана.

Когда вы щелкаете на управление вверх или вниз на полосе прокрутки, ячейка G1 обновляется числом, указывающим текущее значение полосы прокрутки плюс или минус инкрементальное изменение полосы прокрутки.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), который используется для добавления элемента управления полосой прокрутки на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/). Класс [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) представляет полосу прокрутки. Он имеет некоторые важные члены:

- Свойство [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) указывает на ячейку, которая связана с полосой прокрутки.
- Свойство [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) устанавливает максимальное значение для диапазона полосы прокрутки.
- Свойство [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) устанавливает минимальное значение для диапазона полосы прокрутки.
- Свойство [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) указывает количество значений, на которое увеличится полоса прокрутки линейного прокрутки.
- Свойство [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) указывает, есть ли на полосе прокрутки 3D теневые эффекты.
- Свойство [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) устанавливает текущее значение полосы прокрутки.
- Свойство [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) указывает, насколько увеличится текущее значение, если вы щелкнете внутри полосы прокрутки с обеих сторон ползунка.

Приведенный пример показывает, как добавить полосу прокрутки на листе.

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

## **Добавление элемента управления GroupBox в элементы управления на листе**

Иногда вам необходимо реализовать радиокнопки или другие элементы управления, которые принадлежат определенной группе, это можно сделать, включив в группу элемент управления GroupBox или прямоугольник. Любой из этих двух объектов будет служить разделителем группы. После добавления одной из этих форм, можно добавить две или более радиокнопок или других объектов группы.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления GroupBox на листе и разместить в нем элементы управления:

- Чтобы запустить форму, на главной панели меню щелкните *Просмотр*, а затем *Панели инструментов* и *Формы*.
- На панели инструментов *Формы* щелкните *GroupBox* и нарисуйте прямоугольник на листе.
- Введите строку заголовка для рамки.
- На панели инструментов *Формы* щелкните *Option Button* и щелкните внутри элемента *GroupBox* прямо под строкой заголовка.
- Снова на панели инструментов *Формы* щелкните *Option Button* и щелкните внутри *Group Box* под первой радиокнопкой.
- Еще раз на панели инструментов *Формы* щелкните *Option Button* и щелкните внутри *Group Box* под предыдущей радиокнопкой.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) предоставляет метод с именем [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), который используется для добавления элемента управления GroupBox на лист. Метод возвращает объект [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/). Кроме того, метод [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) класса [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) группирует формы, он принимает массив [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) в качестве параметра и возвращает объект [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/). Класс [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) представляет элемент управления GroupBox. У него есть некоторые важные члены:

- Свойство [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) указывает строку заголовка элемента управления GroupBox.
- Свойство [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) указывает, имеет ли элемент управления GroupBox трехмерную затененность.

Приведенный пример показывает, как добавить элемент управления GroupBox и сгруппировать элементы управления на листе.

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

## **Продвинутые темы**
- [Добавление элементов ActiveX в Aspose.Cells](/cells/ru/cpp/add-activex-controls-using-aspose-cells/)
- [Удалить элемент управления ActiveX](/cells/ru/cpp/remove-activex-control/)
- [Обновление элемента управления ComboBox ActiveX](/cells/ru/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
