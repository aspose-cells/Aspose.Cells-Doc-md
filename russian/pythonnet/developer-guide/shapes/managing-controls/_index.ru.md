---
title: Управление элементами управления
type: docs
weight: 150
url: /ru/python-net/managing-controls/
---

## **Введение**

Разработчики могут добавлять различные объекты рисования, такие как текстовые поля, флажки, радиокнопки, комбобоксы, ярлыки, кнопки, линии, прямоугольники, дуги, овалы, спиннеры, ползунки, групповые рамки и др. Библиотека Aspose.Cells для Python via .NET содержит пространство имен Aspose.Cells.Drawing, которое включает все объекты рисования. Однако есть некоторые объекты или фигуры, которые пока не поддерживаются. Создайте эти объекты в проектной таблице с помощью Microsoft Excel, а затем импортируйте их в Aspose.Cells. Aspose.Cells для Python via .NET позволяет загружать эти объекты из проектной таблицы и сохранять их в сгенерированный файл.

## **Добавление элемента управления текстовым полем на лист**

Один из способов подчеркнуть важность информации в отчёте — использовать текстовое поле. Например, добавить текст для выделения названия компании или указания географического региона с самыми высокими продажами. Aspose.Cells для Python via .NET предоставляет класс [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection), который используется для добавления нового текстового поля в коллекцию. Также есть другой класс, [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox), представляющий текстовое поле, используемое для определения всех настроек. Он включает важные элементы:

- Свойство [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) возвращает объект [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe), используемый для настройки содержимого текстового поля.
- Свойство [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) определяет тип размещения.
- Свойство [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) определяет атрибуты шрифта.
- Метод [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) добавляет гиперссылку для текстового поля.
- Свойство [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) возвращает объект [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat), используемый для установки формата заливки для текстового поля.
- Свойство [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) возвращает объект [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat), обычно используемый для стиля и толщины линии текстового поля.
- Свойство [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) определяет входной текст для текстового поля.

В следующем примере создаются два текстовых поля на первом листе книги. Первое текстовое поле хорошо оборудовано различными настройками формата. Второе является простым.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Манипулирование элементами управления текстовыми полями в электронных таблицах дизайнера**

Aspose.Cells для Python via .NET также позволяет получать доступ к текстовым полям в дизайнерских листах и управлять ими. Используйте свойство [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes), чтобы получить коллекцию текстовых полей в листе.

В следующем примере используется файл Microsoft Excel, созданный в вышеприведенном примере. Он получает текстовые строки двух текстовых полей и изменяет текст второго текстового поля для сохранения файла.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Добавление элемента управления флажком на лист**

Флажки удобны, если нужно предоставить пользователю возможность выбрать между двумя вариантами, например, правда или ложь; да или нет. Aspose.Cells для Python via .NET позволяет использовать флажки в рабочих листах. Например, вы можете создать лист финансовых прогнозов, где можно либо учитывать конкретное приобретение, либо нет. В этом случае можно разместить флажок вверху листа. Его состояние можно связать с другой ячейкой: если флажок выбран — значение ячейки будет True, если нет — False.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления флажком на вашем листе, выполните следующие шаги:

1. Убедитесь, что отображается панель инструментов Формы.
1. Нажмите на инструмент **Флажок** на панели инструментов Формы.
1. В области вашего листа нажмите и перетащите, чтобы определить прямоугольник, в котором будет размещен флажок и метка рядом с флажком.
1. После размещения флажка перейдите курсором мыши в область метки и измените метку.
1. В поле Cell Link укажите адрес ячейки, к которой должен быть привязан этот флажок.
1. Нажмите на **ОК**.

### **Использование Aspose.Cells for Python via .NET**

Aspose.Cells для Python via .NET предоставляет класс [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection), который используется для добавления нового флажка в коллекцию. Есть также другой класс, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), который представляет флажок. Он имеет некоторые важные члены:

- Cвойство [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) указывает ячейку, с которой связан флажок.
- Cвойство [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) указывает текстовую строку, связанную с флажком. Это метка флажка.
- Cвойство [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) указывает, отмечен ли флажок.

В следующем примере показано, как добавить флажок на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

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

### **Использование Aspose.Cells for Python via .NET**

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button), который используется для добавления элемента управления кнопкой радио на лист. Метод возвращает объект [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton). Класс[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) представляет кнопку опции. Он имеет некоторые важные члены:

- Cвойство [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) указывает ячейку, с которой связана кнопка радио.
- Cвойство [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) указывает текстовую строку, связанную с кнопкой радио. Это метка кнопки радио.
- Cвойство [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) указывает, выбрана ли кнопка радио или нет.
- Свойство [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) определяет формат заполнения переключателя.
- Свойство [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) определяет стили формата линии переключателя.

В следующем примере показано, как добавить переключатели на рабочий лист. Пример добавляет три радиокнопки, представляющие возрастные группы.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **Использование Aspose.Cells for Python via .NET**

Класс [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box), который используется для добавления элемента управления 'Комбинированный список' на рабочий лист. Метод возвращает объект [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox). Класс [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) представляет комбинированный список. У него есть некоторые важные члены:

- Свойство [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) определяет ячейку, которая привязана к комбинированному списку.
- Свойство [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) определяет диапазон ячеек рабочего листа, используемых для заполнения комбинированного списка.
- Свойство [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) определяет количество строк списка, отображаемых в раскрывающейся части комбинированного списка.
- Свойство [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) указывает, имеет ли комбинированный список 3D-теневую окраску.

В следующем примере показано, как добавить комбинированный список на рабочий лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Добавление элемента управления 'Метка' на рабочий лист**

Метки являются средством информирования пользователей о содержимом таблицы. Aspose.Cells для Python via .NET позволяет добавлять и управлять метками в листе. Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label), используемый для добавления элемента управления метки в лист. Метод возвращает объект [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). Класс [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) представляет метку на листе. Он имеет некоторые важные члены:

- Метод [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) указывает строку заголовка метки.
- Метод [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) указывает [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype) - способ прикрепления метки к ячейкам в листе.

В следующем примере показано, как добавить метку на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box), который используется для добавления элемента управления списка на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox). Класс [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) представляет список. У него есть несколько важных членов:

- Метод [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) указывает ячейку, которая связана с элементом управления списка.
- Метод [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) указывает диапазон ячеек листа, использующихся для заполнения списка.
- Метод [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) указывает режим выбора элементов списка.
- Метод [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) указывает, имеет ли список 3D-затенение.

В следующем примере показано, как добавить список на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Добавление элемента управления кнопка на лист**

Кнопки полезны для выполнения некоторых действий. Иногда полезно назначить макрос VBA на кнопку или назначить гиперссылку для открытия веб-страницы.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления кнопка на вашем листе:

1. Убедитесь, что панель **Формы** отображается.
1. Щелкните инструмент **Кнопка**.
1. В области вашего листа щелкните и перетащите для определения прямоугольника, который будет содержать кнопку.
1. Как только список размещен на листе, щелкните правой кнопкой мыши на элементе управления и выберите **Формат управления**, затем укажите VBA-макрос и атрибуты, касающиеся шрифта, выравнивания, размера, полей и т. д.
1. Нажмите на **ОК**.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button), используемый для добавления элемента управления кнопкой на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button). Класс [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) представляет кнопку. У него есть некоторые важные члены:

- Свойство [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) определяет заголовок кнопки.
- Свойство [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) определяет атрибуты шрифта для подписи элемента управления кнопкой.
- Свойство [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), способ, которым кнопка присоединена к ячейкам на листе.
- Свойство [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) добавляет гиперссылку для элемента управления кнопкой. При нажатии на кнопку будет выполнено переход по связанному URL.

Приведенный ниже пример показывает, как добавить кнопку на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Добавление линейного элемента управления на лист**

### **Использование Microsoft Excel**

1. На панели инструментов **Рисование** щелкните **Автофигуры**, наведите указатель на **Линии** и выберите стиль линии.
1. Перетащите для создания линии.
1. Выполните одно или оба из следующего:
   1. Для ограничения углов рисования линии под углом 15 градусов от начальной точки удерживайте клавишу SHIFT при перетаскивании.
   1. Чтобы удлинить линию в противоположных направлениях от первой конечной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line), который используется для добавления формы линии на лист. Метод возвращает объект [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape). Класс [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) представляет линию. У него есть некоторые важные члены:

- Метод [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) определяет формат линии.
- Метод [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), способ, которым линия присоединена к ячейкам на листе.

Следующий пример показывает, как добавить линии на лист. Создаются три линии с разными стилями.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Добавление стрелки к линии**

Aspose.Cells для Python via .NET также позволяет рисовать стрелки. Можно добавить наконечник стрелки к линии и форматировать линию. Например, можно изменить цвет линии или указать толщину и стиль линии.

Следующий пример показывает, как добавить стрелку к линии.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Добавление прямоугольного контроля на лист**

Aspose.Cells для Python via .NET позволяет рисовать прямоугольные фигуры в листах. Можно создать прямоугольник, квадрат и т. д. Также разрешается задавать цвет заливки и границы фигуры. Например, можно изменить цвет прямоугольника, установить цвет заливки, указать толщину и стиль фигуры по необходимости.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Прямоугольник**.
1. Перетащите, чтобы нарисовать прямоугольник.
1. Выполните одно или оба из следующего:
   1. Чтобы ограничить прямоугольник и нарисовать квадрат от его начальной точки, удерживайте клавишу SHIFT во время перетаскивания.
   1. Чтобы нарисовать прямоугольник из центральной точки, удерживайте клавишу CTRL во время перетаскивания.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle), который используется для добавления прямоугольной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape). Класс [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) представляет прямоугольник. У него есть несколько важных членов:

- Свойство [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) указывает атрибуты форматирования линии прямоугольника.
- Свойство [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) указывает [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), способ, которым прямоугольник прикреплен к ячейкам на листе.
- Свойство [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) указывает стили форматирования заливки прямоугольника.

Следующий пример показывает, как добавить прямоугольник на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Добавление дугового контроля на лист**

Aspose.Cells для Python via .NET позволяет рисовать дуги в листах. Можно создавать простые и заполненные дуги. Также разрешается задавать цвет заливки и цвет границы фигуры. Например, можно указать/изменить цвет дуги, установить цвет затенения, определить толщину и стиль фигуры по необходимости.

### **Использование Microsoft Excel**

1. На панели **Рисование** щелкните **Дуга** в **Автофигуры**.
1. Перетащите, чтобы нарисовать дугу.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc), который используется для добавления формы дуги на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape). Класс [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) представляет дугу. У него есть некоторые важные члены:

- Свойство [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) определяет атрибуты формата линии формы дуги.
- Свойство [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), способ, которым дуга присоединена к ячейкам на листе.
- Свойство [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) определяет стили формата заливки формы.
- Свойство [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) определяет индекс строки нижнего правого угла.
- Свойство [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить формы дуг на лист. Пример создает две формы дуги: одну заполненную, а другую простую.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Добавление овального элемента управления на лист**

Aspose.Cells для Python via .NET позволяет рисовать эллиптические фигуры в листах. Можно создавать простые и залитые эллипсы и настраивать цвет заливки и цвет границы фигуры. Например, можно указать/изменить цвет эллипса, установить цвет затенения, определить толщину и стиль фигуры.

### **Использование Microsoft Excel**

- На панели инструментов *Рисование* щелкните *Овал*.
- Перетащите, чтобы нарисовать овал.
- Выполните одно или оба следующих действия:
- Чтобы ограничить овал и нарисовать круг из его начальной точки, зажмите клавишу SHIFT при перетаскивании.
- Чтобы нарисовать овал из центральной точки, удерживайте клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval), который используется для добавления овальной формы на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval). Класс [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) представляет овальную форму. У него есть некоторые важные члены:

- Свойство [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) определяет атрибуты формата линии овальной формы.
- Свойство [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) определяет [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), способ, которым овал присоединен к ячейкам на листе.
- Свойство [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) определяет стили формата заливки формы.
- Свойство [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) определяет индекс строки нижнего правого угла.
- Свойство [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) определяет индекс столбца нижнего правого угла.

В следующем примере показано, как добавить овальные формы на лист. Пример создает две овальные формы: одна заполнена, а другая представляет собой просто кружок.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Добавление элемента управления спинбокс на лист**

Переключатель — это текстовое поле, прикрепленное к кнопке (называемой кнопкой переклѐчателя), которая состоит из стрелки вверх и стрелки вниз, нажатие которых позволяет поэтапно изменять значение в текстовом поле. Используя переключатели, вы можете видеть, как изменение входных данных модели повлияет на результаты модели. Можно прикрепить кнопку переключателя к определенной входной ячейке. При нажатии на стрелку вверх или вниз значение целого числа в целевой ячейке увеличивается или уменьшается. *Aspose.Cells для Python via .NET* позволяет создавать переключатели в ваших листах.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления спинбокс на листе:

- Убедитесь, что отображается *панель инструментов Формы*.
- Щелкните инструмент *Спиннер*.
- В области вашего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать спиннер.
- Как только спиннер размещен на листе, щелкните правой кнопкой мыши по элементу управления и выберите *Форматировать элемент управления* и укажите максимальное, минимальное и инкрементальное значения.
- В поле *Связь с ячейкой* укажите адрес ячейки, к которой должен быть привязан этот спинбокс.
- Щелкните *OK*.

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner), который используется для добавления элемента управления спинбокс на лист. Метод возвращает объект [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner). Класс [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) представляет собой спинбокс. Он имеет некоторые важные члены:

- Свойство [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) указывает на ячейку, которая привязана к спинбоксу.
- Свойство [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) указывает максимальное значение для диапазона спинбокса.
- Свойство [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) указывает минимальное значение для диапазона спинбокса.
- Свойство [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) указывает значение инкремента для построчной прокрутки спиннера.
- Свойство [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) указывает, имеет ли спинбокс трехмерную тень.
- Свойство [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) указывает текущее значение спинбокса.

В следующем примере показано, как добавить спинбокс на лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

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

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar), который используется для добавления элемента управления полосой прокрутки на лист. Метод возвращает объект [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar). Класс [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) представляет полосу прокрутки. Он имеет некоторые важные члены:

- Свойство [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) указывает на ячейку, которая связана с полосой прокрутки.
- Свойство [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) устанавливает максимальное значение для диапазона полосы прокрутки.
- Свойство [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) устанавливает минимальное значение для диапазона полосы прокрутки.
- Свойство [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) указывает количество значений, на которое увеличится полоса прокрутки линейного прокрутки.
- Свойство [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) указывает, есть ли на полосе прокрутки 3D теневые эффекты.
- Свойство [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) устанавливает текущее значение полосы прокрутки.
- Свойство [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) указывает, насколько увеличится текущее значение, если вы щелкнете внутри полосы прокрутки с обеих сторон ползунка.

Приведенный пример показывает, как добавить полосу прокрутки на листе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

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

### **Использование Aspose.Cells for Python via .NET**

Класс [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) предоставляет метод с именем [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box), который используется для добавления элемента управления GroupBox на лист. Метод возвращает объект [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox). Кроме того, метод [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) класса [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) группирует формы, он принимает массив [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) в качестве параметра и возвращает объект [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape). Класс [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) представляет элемент управления GroupBox. У него есть некоторые важные члены:

- Свойство [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) указывает строку заголовка элемента управления GroupBox.
- Свойство [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) указывает, имеет ли элемент управления GroupBox трехмерную затененность.

Приведенный пример показывает, как добавить элемент управления GroupBox и сгруппировать элементы управления на листе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Продвинутые темы**
- [Добавить элементы ActiveX](/cells/ru/python-net/add-activex-controls-using-aspose-cells/)
- [Удалить элемент управления ActiveX](/cells/ru/python-net/remove-activex-control/)
- [Обновление элемента управления ComboBox ActiveX](/cells/ru/python-net/update-activex-combobox-control/)
{{< app/cells/assistant language="python-net" >}}
