---
title: Управление элементами управления
type: docs
weight: 150
url: /ru/net/managing-controls/
---

## **Введение**

Разработчики могут добавлять различные графические объекты, такие как текстовые поля, флажки, переключатели, комбинированные поля выбора, ярлыки, кнопки, линии, прямоугольники, дуги, овалы, спиннеры, полосы прокрутки, групповые рамки и т. д. Aspose.Cells предоставляет пространство имен Aspose.Cells.Drawing, которое содержит все графические объекты. Однако есть несколько графических объектов или форм, которые пока не поддерживаются. Создайте эти графические объекты в электронной таблице дизайнера с помощью Microsoft Excel, а затем импортируйте электронную таблицу дизайнера в Aspose.Cells. Aspose.Cells позволяет загружать эти графические объекты из электронной таблицы дизайнера и записывать их в созданный файл.

## **Добавление элемента управления текстовым полем на лист**

Один из способов выделить важную информацию в отчете - это использование текстового поля. Например, добавьте текст для выделения названия компании или для указания географического региона с самыми высокими продажами и т. д. Aspose.Cells предоставляет класс [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection), используемый для добавления нового текстового поля в коллекцию. Есть еще один класс, [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), который представляет текстовое поле, используемое для определения всех типов настроек. У него есть несколько важных членов:

- Свойство [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) возвращает объект [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe), используемый для настройки содержимого текстового поля.
- Свойство [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) определяет тип размещения.
- Свойство [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) определяет атрибуты шрифта.
- Метод [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) добавляет гиперссылку для текстового поля.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) возвращает объект [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat), используемый для установки формата заливки для текстового поля.
- Свойство [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) возвращает объект [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat), обычно используемый для стиля и толщины линии текстового поля.
- Свойство [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) определяет входной текст для текстового поля.

В следующем примере создаются два текстовых поля на первом листе книги. Первое текстовое поле хорошо оборудовано различными настройками формата. Второе является простым.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Манипулирование элементами управления текстовыми полями в электронных таблицах дизайнера**

Aspose.Cells также позволяет вам получать доступ к текстовым полям в электронных таблицах дизайнера и манипулировать ими. Используйте свойство [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes), чтобы получить коллекцию текстовых полей на листе.

В следующем примере используется файл Microsoft Excel, созданный в вышеприведенном примере. Он получает текстовые строки двух текстовых полей и изменяет текст второго текстового поля для сохранения файла.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

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

Aspose.Cells предоставляет класс [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection), который используется для добавления нового флажка в коллекцию. Еще один класс, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), представляет флажок. Он имеет некоторые важные члены:

- Cвойство [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) указывает ячейку, с которой связан флажок.
- Cвойство [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) указывает текстовую строку, связанную с флажком. Это метка флажка.
- Cвойство [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) указывает, отмечен ли флажок.

В следующем примере показано, как добавить флажок на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

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

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton), который используется для добавления элемента управления кнопкой радио на лист. Метод возвращает объект [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton). Класс[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) представляет кнопку опции. Он имеет некоторые важные члены:

- Cвойство [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) указывает ячейку, с которой связана кнопка радио.
- Cвойство [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) указывает текстовую строку, связанную с кнопкой радио. Это метка кнопки радио.
- Cвойство [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) указывает, выбрана ли кнопка радио или нет.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) определяет формат заполнения переключателя.
- Свойство [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) определяет стили формата линии переключателя.

В следующем примере показано, как добавить переключатели на рабочий лист. Пример добавляет три радиокнопки, представляющие возрастные группы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox), который используется для добавления элемента управления 'Комбинированный список' на рабочий лист. Метод возвращает объект [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox). Класс [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) представляет комбинированный список. У него есть некоторые важные члены:

- Свойство [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) определяет ячейку, которая привязана к комбинированному списку.
- Свойство [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) определяет диапазон ячеек рабочего листа, используемых для заполнения комбинированного списка.
- Свойство [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) определяет количество строк списка, отображаемых в раскрывающейся части комбинированного списка.
- Свойство [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) указывает, имеет ли комбинированный список 3D-теневую окраску.

В следующем примере показано, как добавить комбинированный список на рабочий лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Добавление элемента управления 'Метка' на рабочий лист**

Метки - это средство предоставления пользователям информации о содержании таблицы. Aspose.Cells позволяет добавлять и управлять метками на рабочем листе. Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel), используемый для добавления элемента управления 'Метка' на рабочий лист. Метод возвращает объект [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). Класс [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) представляет метку на рабочем листе. У него есть некоторые важные члены:

- Метод [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) указывает строку заголовка метки.
- Метод [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) указывает [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype) - способ прикрепления метки к ячейкам в листе.

В следующем примере показано, как добавить метку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox), который используется для добавления элемента управления списка на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox). Класс [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) представляет список. У него есть несколько важных членов:

- Метод [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) указывает ячейку, которая связана с элементом управления списка.
- Метод [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) указывает диапазон ячеек листа, использующихся для заполнения списка.
- Метод [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) указывает режим выбора элементов списка.
- Метод [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) указывает, имеет ли список 3D-затенение.

В следующем примере показано, как добавить список на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

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

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton), используемый для добавления элемента управления кнопкой на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button). Класс [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) представляет кнопку. У него есть некоторые важные члены:

- Свойство [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) определяет заголовок кнопки.
- Свойство [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) определяет атрибуты шрифта для подписи элемента управления кнопкой.
- Свойство [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ, которым кнопка присоединена к ячейкам на листе.
- Свойство [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) добавляет гиперссылку для элемента управления кнопкой. При нажатии на кнопку будет выполнено переход по связанному URL.

Приведенный ниже пример показывает, как добавить кнопку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Добавление линейного элемента управления на лист**

### **Использование Microsoft Excel**

1. На панели инструментов **Рисование** щелкните **Автофигуры**, наведите указатель на **Линии** и выберите стиль линии.
1. Перетащите для создания линии.
1. Выполните одно или оба из следующего:
   1. Для ограничения углов рисования линии под углом 15 градусов от начальной точки удерживайте клавишу SHIFT при перетаскивании.
   1. Чтобы удлинить линию в противоположных направлениях от первой конечной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline), который используется для добавления формы линии на лист. Метод возвращает объект [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape). Класс [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) представляет линию. У него есть некоторые важные члены:

- Метод [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) определяет формат линии.
- Метод [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ, которым линия присоединена к ячейкам на листе.

Следующий пример показывает, как добавить линии на лист. Создаются три линии с разными стилями.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Добавление стрелки к линии**

Aspose.Cells также позволяет вам рисовать стрелки. Возможно добавление стрелки к линии и форматирование линии. Например, вы можете изменить цвет линии или указать ее толщину и стиль.

Следующий пример показывает, как добавить стрелку к линии.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Добавление прямоугольного контроля на лист**

Aspose.Cells позволяет вам рисовать прямоугольные формы в ваших листах. Вы можете создать прямоугольник, квадрат и т. д. Вы также можете форматировать цвет заливки и цвет граничной линии контроля. Например, вы можете изменить цвет прямоугольника, задать цвет заливки, указать толщину и стиль прямоугольника по вашему усмотрению.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Прямоугольник**.
1. Перетащите, чтобы нарисовать прямоугольник.
1. Выполните одно или оба из следующего:
   1. Чтобы ограничить прямоугольник и нарисовать квадрат от его начальной точки, удерживайте клавишу SHIFT во время перетаскивания.
   1. Чтобы нарисовать прямоугольник из центральной точки, удерживайте клавишу CTRL во время перетаскивания.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle), который используется для добавления прямоугольной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape). Класс [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) представляет прямоугольник. У него есть несколько важных членов:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) указывает атрибуты форматирования линии прямоугольника.
- Свойство [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) указывает [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ, которым прямоугольник прикреплен к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) указывает стили форматирования заливки прямоугольника.

Следующий пример показывает, как добавить прямоугольник на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Добавление дугового контроля на лист**

Aspose.Cells позволяет вам рисовать дуговые формы на ваших листах. Вы можете создавать простые и заполненные дуги. Вы можете форматировать цвет заливки и цвет граничной линии контроля. Например, вы можете указать / изменить цвет дуги, установить цвет заливки, указать толщину и стиль формы по вашему усмотрению.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Дуга** в **Автофигуры**.
1. Перетащите, чтобы нарисовать дугу.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc), который используется для добавления формы дуги на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape). Класс [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) представляет дугу. У него есть некоторые важные члены:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) определяет атрибуты формата линии формы дуги.
- Свойство [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ, которым дуга присоединена к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) определяет стили формата заливки формы.
- Свойство [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) определяет индекс строки нижнего правого угла.
- Свойство [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить формы дуг на лист. Пример создает две формы дуги: одну заполненную, а другую простую.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Добавление овального элемента управления на лист**

Aspose.Cells позволяет вам рисовать овальные формы на листах. Создайте простые и закрашенные овальные формы и отформатируйте цвет заливки и цвет граничной линии элемента управления. Например, вы можете указать / изменить цвет овала, установить цвет закрашивания, указать вес и стиль формы.

### **Использование Microsoft Excel**

- На панели инструментов *Рисование* щелкните *Овал*.
- Перетащите, чтобы нарисовать овал.
- Выполните одно или оба следующих действия:
- Чтобы ограничить овал и нарисовать круг из его начальной точки, зажмите клавишу SHIFT при перетаскивании.
- Чтобы нарисовать овал из центральной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval), который используется для добавления овальной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval). Класс [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) представляет овальную форму. У него есть некоторые важные члены:

- Свойство [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) определяет атрибуты формата линии овальной формы.
- Свойство [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ, которым овал присоединен к ячейкам на листе.
- Свойство [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) определяет стили формата заливки формы.
- Свойство [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) определяет индекс строки нижнего правого угла.
- Свойство [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить овальные формы на лист. Пример создает две овальные формы: одна заполнена, а другая представляет собой просто кружок.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

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

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner), который используется для добавления элемента управления спинбокс на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner). Класс [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) представляет собой спинбокс. Он имеет некоторые важные члены:

- Свойство [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) указывает на ячейку, которая привязана к спинбоксу.
- Свойство [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) указывает максимальное значение для диапазона спинбокса.
- Свойство [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) указывает минимальное значение для диапазона спинбокса.
- Свойство [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) указывает значение инкремента для построчной прокрутки спиннера.
- Свойство [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) указывает, имеет ли спинбокс трехмерную тень.
- Свойство [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) указывает текущее значение спинбокса.

В следующем примере показано, как добавить спинбокс на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

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

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar), который используется для добавления элемента управления полосой прокрутки на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar). Класс [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) представляет полосу прокрутки. Он имеет некоторые важные члены:

- Свойство [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) указывает на ячейку, которая связана с полосой прокрутки.
- Свойство [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) устанавливает максимальное значение для диапазона полосы прокрутки.
- Свойство [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) устанавливает минимальное значение для диапазона полосы прокрутки.
- Свойство [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) указывает количество значений, на которое увеличится полоса прокрутки линейного прокрутки.
- Свойство [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) указывает, есть ли на полосе прокрутки 3D теневые эффекты.
- Свойство [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) устанавливает текущее значение полосы прокрутки.
- Свойство [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) указывает, насколько увеличится текущее значение, если вы щелкнете внутри полосы прокрутки с обеих сторон ползунка.

Приведенный пример показывает, как добавить полосу прокрутки на листе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

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

Класс [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox), который используется для добавления элемента управления GroupBox на лист. Метод возвращает объект [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox). Кроме того, метод [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) класса [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) группирует формы, он принимает массив [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) в качестве параметра и возвращает объект [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape). Класс [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) представляет элемент управления GroupBox. У него есть некоторые важные члены:

- Свойство [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) указывает строку заголовка элемента управления GroupBox.
- Свойство [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) указывает, имеет ли элемент управления GroupBox трехмерную затененность.

Приведенный пример показывает, как добавить элемент управления GroupBox и сгруппировать элементы управления на листе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Продвинутые темы**
- [Добавление элементов ActiveX в Aspose.Cells](/cells/ru/net/add-activex-controls-using-aspose-cells/)
- [Удалить элемент управления ActiveX](/cells/ru/net/remove-activex-control/)
- [Обновление элемента управления ComboBox ActiveX](/cells/ru/net/update-activex-combobox-control/)
{{< app/cells/assistant language="csharp" >}}
