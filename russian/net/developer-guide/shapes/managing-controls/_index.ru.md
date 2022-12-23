---
title: Управление элементами управления
type: docs
weight: 150
url: /ru/net/managing-controls/
---
## **Вступление**

Разработчики могут добавлять различные объекты рисования, такие как текстовые поля, флажки, переключатели, поля со списком, метки, кнопки, линии, прямоугольники, дуги, овалы, счетчики, полосы прокрутки, групповые поля и т. д. Aspose.Cells предоставляет пространство имен Aspose.Cells.Drawing, которое содержит все объекты рисования. Однако есть несколько объектов рисования или фигур, которые пока не поддерживаются. Создайте эти объекты чертежа в электронной таблице дизайнера с помощью Microsoft Excel, а затем импортируйте электронную таблицу дизайнера в Aspose.Cells. Aspose.Cells позволяет загружать эти объекты чертежа из электронной таблицы дизайнера и записывать их в сгенерированный файл.

## **Добавление элемента управления текстовым полем на рабочий лист**

 Один из способов выделить важную информацию в отчете — использовать текстовое поле. Например, добавьте текст, чтобы выделить название компании или указать географический регион с самыми высокими продажами и т. д. Aspose.Cells обеспечивает[**ТекстбоксКоллекция**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) класс, используемый для добавления нового текстового поля в коллекцию. Есть еще класс,[**Текстовое окно**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)который представляет собой текстовое поле, используемое для определения всех типов настроек. В него входят несколько важных членов:

- [**Текстовый Фрейм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) свойство возвращает[**Мсотекстфрейм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) объект, используемый для настройки содержимого текстового поля.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) указывает тип размещения.
- [**Шрифт**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) свойство определяет атрибуты шрифта.
- [**Добавить гиперссылку**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) метод добавляет гиперссылку для текстового поля.
- [**ЗаполнитьФормат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) свойство возвращает[**Мсофиллформат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) объект, используемый для установки формата заполнения для текстового поля.
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) свойство возвращает[**Мсолинеформат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) объект, обычно используемый для стиля и веса строки текстового поля.
- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) Свойство указывает входной текст для текстового поля.

В следующем примере создаются два текстовых поля на первом листе книги. Первое текстовое поле хорошо оснащено различными настройками формата. Второй — простой.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Управление элементами управления текстовыми полями в электронных таблицах конструктора**

 Aspose.Cells также позволяет вам получать доступ к текстовым полям на листах конструктора и управлять ими. Использовать[**Рабочий лист.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) свойство, чтобы получить коллекцию текстовых полей на листе.

В следующем примере используется файл Excel Microsoft, который мы создали в приведенном выше примере. Он получает текстовые строки двух текстовых полей и изменяет текст второго текстового поля, чтобы сохранить файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Добавление элемента управления флажком на рабочий лист**

Флажки удобны, если вы хотите предоставить пользователю возможность выбора между двумя вариантами, например, true или false; Да или нет. Aspose.Cells позволяет использовать флажки на листах. Например, вы, возможно, разработали рабочий лист финансового прогноза, в котором вы можете либо учитывать конкретное приобретение, либо нет. В этом случае вы можете установить флажок в верхней части рабочего листа. Затем вы можете связать состояние этого флажка с другой ячейкой, чтобы, если флажок установлен, значением ячейки было True; если он не выбран, значение ячейки равно False.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления флажком на листе, выполните следующие действия.

1. Убедитесь, что панель инструментов «Формы» отображается.
1.  Нажмите на**Флажок** на панели инструментов «Формы».
1. В области рабочего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать флажок и метку рядом с флажком.
1. После установки флажка переместите курсор мыши в область метки и измените метку.
1.  в**Cell Ссылка**поле укажите адрес ячейки, к которой должен быть привязан этот флажок.
1.  Нажмите на**ХОРОШО**.

### **Использование Aspose.Cells**

 Aspose.Cells обеспечивает[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) класс, который используется для добавления нового флажка в коллекцию. Есть еще класс,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), который представляет собой флажок. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Свойство указывает ячейку, которая связана с флажком.
- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) Свойство указывает текстовую строку, связанную с флажком. Это метка флажка.
- [**Стоимость**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) Свойство указывает, установлен ли флажок или нет.

В следующем примере показано, как добавить флажок на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Добавление элемента управления Radio Button на рабочий лист**

Радиокнопка или опциональная кнопка — это элемент управления, состоящий из круглого прямоугольника. Пользователь принимает решение, выбирая круглое поле. Радиокнопка обычно, если не всегда, сопровождается другими. Такие переключатели отображаются и ведут себя как группа. Пользователь решает, какая кнопка действительна, выбирая только одну из них. Когда пользователь нажимает одну кнопку, она заполняется. Когда выбрана одна кнопка в группе, кнопки той же группы пусты.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления Radio Button на листе, выполните следующие действия.

1.  Убедитесь, что**Формы** отображается панель инструментов.
1.  Нажмите на**Кнопка выбора** инструмент.
1. На рабочем листе щелкните и перетащите, чтобы определить прямоугольник, который будет содержать кнопку выбора и метку рядом с кнопкой выбора.
1. Как только переключатель будет помещен на рабочий лист, переместите курсор мыши в область метки и измените метку.
1.  в**Cell Ссылка** поле укажите адрес ячейки, к которой должна быть привязана данная радиокнопка.
1.  Нажмите**ХОРОШО**.

### **Использование Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Аддрадиобуттон**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , который используется для добавления переключателя на рабочий лист. Метод возвращает[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) объект. Класс[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) представляет собой кнопку выбора. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Свойство указывает ячейку, которая связана с переключателем.
- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)Свойство указывает текстовую строку, связанную с переключателем. Это метка переключателя.
- [**Проверено**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) Свойство указывает, установлен ли переключатель или нет.
- [**ЗаполнитьФормат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) Свойство определяет формат заполнения переключателя.
- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) Свойство определяет стили формата строки переключателя.

В следующем примере показано, как добавить переключатели на лист. В примере добавлены три переключателя, представляющие возрастные группы.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

## **Добавление элемента управления Combo Box на рабочий лист**

Чтобы упростить ввод данных или ограничить записи определенными элементами, которые вы определяете, вы можете создать поле со списком или раскрывающийся список допустимых записей, который скомпилирован из ячеек в другом месте на рабочем листе. Когда вы создаете раскрывающийся список для ячейки, он отображает стрелку рядом с этой ячейкой. Чтобы ввести информацию в эту ячейку, щелкните стрелку и выберите нужную запись.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления полем со списком на листе, выполните следующие действия.

1.  Убедитесь, что**Формы** отображается панель инструментов.
1.  Нажать на**Поле со списком** инструмент.
1. В области рабочего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать поле со списком.
1.  Как только поле со списком будет помещено на рабочий лист, щелкните правой кнопкой мыши элемент управления, чтобы щелкнуть**Управление форматом** и укажите диапазон ввода.
1.  в**Cell Ссылка** поле укажите адрес ячейки, к которой должен быть привязан этот выпадающий список.
1.  Нажмите на**ХОРОШО**.

### **Использование Aspose.Cells**

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , который используется для добавления элемента управления полем со списком на лист. Метод возвращает[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) объект. Класс[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) представляет поле со списком. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Свойство указывает ячейку, которая связана с полем со списком.
- [**Диапазон ввода**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) Свойство указывает диапазон ячеек рабочего листа, используемый для заполнения поля со списком.
- [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) Свойство указывает количество строк списка, отображаемых в раскрывающейся части поля со списком.
- [**Тень**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) Свойство указывает, имеет ли поле со списком трехмерное затенение.

В следующем примере показано, как добавить поле со списком на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Добавление элемента управления метками на рабочий лист**

 Метки — это средство предоставления пользователям информации о содержимом электронной таблицы. Aspose.Cells позволяет добавлять метки и управлять ими на листе.[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , используемый для добавления элемента управления меткой на лист. Метод возвращает[**Этикетка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) объект. Класс[**Этикетка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) представляет метку на листе. В него входят несколько важных членов:

- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) Метод указывает строку заголовка метки.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) метод определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ прикрепления метки к ячейкам на листе.

В следующем примере показано, как добавить метку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

## **Добавление элемента управления «Список» на рабочий лист**

Элемент управления "список" создает элемент управления "список", который позволяет выбирать один или несколько элементов.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления списком на листе:

1.  Убедитесь, что**Формы** отображается панель инструментов.
1.  Нажать на**Список** инструмент.
1. В области рабочего листа щелкните и перетащите, чтобы определить прямоугольник, который будет содержать поле со списком.
1.  После того, как поле списка будет помещено на лист, щелкните правой кнопкой мыши элемент управления, чтобы щелкнуть**Управление форматом** и укажите диапазон ввода.
1.  в**Cell Ссылка**поле, укажите адрес ячейки, к которой этот список должен быть привязан, и установите атрибут типа выбора (Одиночный, Несколько, Расширить)
1.  Нажмите**ХОРОШО**.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Аддлистбокс**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , который используется для добавления элемента управления списком на лист. Метод возвращает[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) объект. Класс[**СписокБокс**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) представляет собой список. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) метод указывает ячейку, которая связана со списком.
- [**Диапазон ввода**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) Метод указывает диапазон ячеек рабочего листа, используемый для заполнения списка.
- [**Тип Выбора**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)метод определяет режим выбора списка.
- [**Тень**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) Метод указывает, имеет ли поле списка трехмерное затенение.

В следующем примере показано, как добавить список на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

## **Добавление элемента управления «Кнопка» на рабочий лист**

Кнопки полезны для выполнения некоторых действий. Иногда полезно назначить макрос VBA для кнопки или назначить гиперссылку для открытия веб-страницы.

### **Использование Microsoft Excel**

Чтобы поместить элемент управления «Кнопка» на лист:

1.  Убедитесь, что**Формы** отображается панель инструментов.
1.  Нажать на**Кнопка** инструмент.
1. В области рабочего листа щелкните и перетащите, чтобы определить прямоугольник, который будет удерживать кнопку.
1.  Как только поле со списком будет помещено на лист, щелкните правой кнопкой мыши элемент управления и выберите**Управление форматом**, затем укажите макрос VBA и атрибуты, относящиеся к шрифту, выравниванию, размеру, полям и т. д.
1.  Нажмите на**ХОРОШО**.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьКнопку**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , используемый для добавления кнопки на рабочий лист. Метод возвращает[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) объект. Класс[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) представляет собой кнопку. В него входят несколько важных членов:

- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) свойство указывает заголовок кнопки.
- [**Шрифт**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) Свойство указывает атрибуты шрифта для метки элемента управления кнопки.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) свойство определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ прикрепления кнопки к ячейкам на листе.
- [**Добавить гиперссылку**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) Свойство добавляет гиперссылку для кнопки. Нажав на кнопку, вы перейдете к соответствующему URL-адресу.

В следующем примере показано, как добавить кнопку на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Добавление элемента управления линией на рабочий лист**

### **Использование Microsoft Excel**

1.  На**Рисунок** панель инструментов, нажмите**Автофигуры** , указать на**Линии**и выберите нужный стиль линии.
1. Перетащите, чтобы нарисовать линию.
1. Выполните одно или оба из следующих действий:
 1. Чтобы линия рисовалась под углом 15 градусов от начальной точки, удерживайте нажатой клавишу SHIFT при перетаскивании.
 1. Чтобы удлинить линию в противоположных направлениях от первой конечной точки, удерживайте нажатой клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , который используется для добавления формы линии на лист. Метод возвращает[**Линейная форма**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) объект. Класс[**Линейная форма**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) представляет собой линию. В него входят несколько важных членов:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) метод определяет формат строки.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) метод определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)способ прикрепления линии к ячейкам на листе.

В следующем примере показано, как добавить строки на лист. Он создает три линии с разными стилями.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Добавление стрелки к линии**

Aspose.Cells также позволяет рисовать линии со стрелками. К строке можно добавить стрелку и отформатировать строку. Например, вы можете изменить цвет линии или указать толщину и стиль линии.

В следующем примере показано, как добавить стрелку к линии.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Добавление элемента управления «Прямоугольник» на рабочий лист**

Aspose.Cells позволяет рисовать прямоугольные формы на ваших листах. Вы можете создать прямоугольник, квадрат и т. д. Вам также разрешено форматировать цвет заливки и цвет линии границы элемента управления. Например, вы можете изменить цвет прямоугольника, установить цвет заливки, указать вес и стиль прямоугольника для ваших нужд.

### **Использование Microsoft Excel**

1.  На**Рисунок** панель инструментов, нажмите**Прямоугольник**.
1. Перетащите, чтобы нарисовать прямоугольник.
1. Выполните одно или оба из следующих действий:
 1. Чтобы заставить прямоугольник рисовать квадрат из начальной точки, удерживайте нажатой клавишу SHIFT при перетаскивании.
 1. Чтобы нарисовать прямоугольник из центральной точки, удерживайте нажатой клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьПрямоугольник**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , который используется для добавления прямоугольной формы на лист. Метод возвращает[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) объект. Класс[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) представляет собой прямоугольник. В него входят несколько важных членов:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) определяет атрибуты формата линии прямоугольника.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) свойство определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ прикрепления прямоугольника к ячейкам на листе.
- [**ЗаполнитьФормат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) определяет стили формата заливки прямоугольника.

В следующем примере показано, как добавить прямоугольник на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Добавление управления дугой на рабочий лист**

Aspose.Cells позволяет рисовать дуги на рабочих листах. Вы можете создавать простые и заполненные дуги. Вы можете форматировать цвет заливки и цвет границы элемента управления. Например, вы можете указать/изменить цвет дуги, установить цвет штриховки, указать вес и стиль формы для ваших нужд.

### **Использование Microsoft Excel**

1.  На**Рисунок** панель инструментов, нажмите**Дуга** в**Автофигуры**.
1. Перетащите, чтобы нарисовать дугу.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**аддарк**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , который используется для добавления формы дуги на рабочий лист. Метод возвращает[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) объект. Класс[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) представляет собой дугу. В него входят несколько важных членов:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) Свойство задает атрибуты формата линии формы дуги.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) свойство определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ прикрепления дуги к ячейкам рабочего листа.
- [**ЗаполнитьФормат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)определяет стили формата заливки фигуры.
- [**нижняя правая строка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) Свойство указывает индекс строки в правом нижнем углу.
- [**Нижняя правая колонка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) Свойство указывает индекс столбца в правом нижнем углу.

В следующем примере показано, как добавить дуги на рабочий лист. В примере создаются две формы дуги: одна заполненная, а другая простая.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Добавление овального элемента управления на рабочий лист**

Aspose.Cells позволяет рисовать овалы на рабочих листах. Создавайте простые овальные формы с заливкой и форматируйте цвет заливки и цвет линии границы элемента управления. Например, вы можете указать/изменить цвет овала, задать цвет штриховки, указать вес и стиль фигуры.

### **Использование Microsoft Excel**

-  На*Рисунок* панель инструментов, нажмите*Овал*.
- Перетащите, чтобы нарисовать овал.
- Выполните одно или оба из следующих действий:
- Чтобы заставить овал рисовать окружность из начальной точки, удерживайте нажатой клавишу SHIFT при перетаскивании.
- Чтобы нарисовать овал из центральной точки, удерживайте нажатой клавишу CTRL при перетаскивании.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьОвал**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , который используется для добавления овальной формы на лист. Метод возвращает[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) объект. Класс[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) представляет собой овальную форму. В него входят несколько важных членов:

- [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) Свойство задает атрибуты формата линии овальной формы.
- [**Размещение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) свойство определяет[**Тип размещения**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), способ прикрепления овала к ячейкам на рабочем листе.
- [**ЗаполнитьФормат**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)определяет стили формата заливки фигуры.
- [**нижняя правая строка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) Свойство указывает индекс строки в правом нижнем углу.
- [**Нижняя правая колонка**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) Свойство указывает индекс столбца в правом нижнем углу.

В следующем примере показано, как добавить на лист овальные фигуры. В примере создаются две овальные формы: одна заполнена овалом, другая представляет собой простой круг.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Добавление элемента управления Spinner на рабочий лист**

 Поле прокрутки — это текстовое поле, прикрепленное к кнопке (называемой кнопкой прокрутки), состоящее из стрелок вверх и стрелок вниз, которые вы нажимаете для постепенного изменения значения в текстовом поле. Используя счетчики, вы можете увидеть, как изменения входных данных в вашей финансовой модели повлияют на выходные данные модели. Вы можете прикрепить кнопку прокрутки к определенной ячейке ввода. Пока вы нажимаете стрелку вверх или стрелку вниз на кнопке прокрутки, целочисленное значение в целевой ячейке ввода увеличивается или уменьшается.*Aspose.Cells* позволяет создавать счетчики на ваших листах.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления счетчиком на листе:

-  Убедитесь, что*Формы* отображается панель инструментов.
-  Нажмите на*Спиннер* инструмент.
- В области рабочего листа щелкните и перетащите, чтобы определить прямоугольник, который будет удерживать счетчик.
-  Как только счетчик будет помещен на рабочий лист, щелкните элемент управления правой кнопкой мыши и выберите*Управление форматом* и укажите максимальное, минимальное и возрастающее значения.
-  в*Cell Ссылка* поле укажите адрес ячейки, к которой этот счетчик должен быть привязан.
-  Нажмите на*ХОРОШО*.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**ДобавитьSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) который используется для добавления элемента управления счетчиком на рабочий лист. Метод возвращает[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) объект. Класс[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) представляет собой спин-бокс. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Свойство указывает ячейку, которая связана с полем счетчика.
- [**Максимум**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) Свойство задает максимальное значение диапазона счетчика.
- [**Мин.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) Свойство задает минимальное значение диапазона счетчика.
- [**Инкрементальное изменение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) Свойство указывает величину значения, на которую счетчик увеличивается при прокрутке строки.
- [**Тень**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) Свойство указывает, имеет ли счетчик трехмерное затенение.
- [**Текущая стоимость**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) свойство указывает текущее значение счетчика.

В следующем примере показано, как добавить счетчик на рабочий лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Добавление полосы прокрутки на рабочий лист**

Элемент управления полосы прокрутки используется для выбора данных на листе аналогично элементу управления счетчиком. Добавляя элемент управления на рабочий лист и связывая его с ячейкой, можно вернуть числовое значение для текущей позиции элемента управления.

### **Использование Microsoft Excel**

- Чтобы добавить полосу прокрутки в Excel 2003 и более ранних версиях, щелкните значок*Полоса прокрутки* кнопка на*Формы* панели инструментов, а затем создайте полосу прокрутки, которая покрывает ячейки B2:B6 по высоте и составляет примерно одну четвертую ширины столбца.
-  Чтобы добавить полосу прокрутки в Excel 2007, щелкните значок*Разработчик* вкладка, нажмите*Вставлять* , а затем щелкните*Полоса прокрутки* в разделе «Управление формой».
-  Щелкните правой кнопкой мыши полосу прокрутки и выберите*Управление форматом*.
-  Введите следующую информацию и нажмите*ХОРОШО*:
 - В*Текущая стоимость* коробка, тип 1.
 - В*Минимальное значение* поле, введите 1. Это значение ограничивает верхнюю часть полосы прокрутки первым элементом в списке.
 - В*Максимальное значение* введите 20. Это число указывает максимальное количество записей в списке.
 - В*Постепенное изменение* поле, введите 1. Это значение определяет, на сколько чисел элемент управления полосы прокрутки увеличивает текущее значение.
 - В*Смена страницы* поле, введите 5. Эта запись определяет, насколько будет увеличиваться текущее значение, если вы щелкнете внутри полосы прокрутки с любой стороны полосы прокрутки.
 Чтобы поместить числовое значение в ячейку G1 (в зависимости от того, какой элемент выбран в списке), введите G1 в поле*Cell ссылка* коробка.
- Щелкните любую ячейку, чтобы полоса прокрутки не была выбрана.

Когда вы щелкаете элемент управления вверх или вниз на полосе прокрутки, ячейка G1 обновляется до числа, которое указывает текущее значение полосы прокрутки плюс или минус постепенное изменение полосы прокрутки.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Добавить полосу прокрутки**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , который используется для добавления полосы прокрутки на рабочий лист. Метод возвращает[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) объект. Класс[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) представляет полосу прокрутки. В него входят несколько важных членов:

- [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) Свойство указывает ячейку, которая связана с полосой прокрутки.
- [**Максимум**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) Свойство задает максимальное значение диапазона полосы прокрутки.
- [**Мин.**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) Свойство задает минимальное значение диапазона полосы прокрутки.
- [**Инкрементальное изменение**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) Свойство указывает величину значения, на которое полоса прокрутки увеличивается на прокрутку строки.
- [**Тень**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) Свойство указывает, имеет ли полоса прокрутки трехмерное затенение.
- [**Текущая стоимость**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) Свойство указывает текущее значение полосы прокрутки.
- [**Изменение страницы**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)Свойство указывает, насколько будет увеличено текущее значение, если щелкнуть внутри полосы прокрутки с любой стороны поля прокрутки.

В следующем примере показано, как добавить полосу прокрутки на лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Добавление элемента управления GroupBox к элементам управления группы на рабочем листе**

Иногда вам нужно реализовать переключатели или другие элементы управления, принадлежащие к определенной группе, которые вы можете реализовать, включив либо групповое поле, либо элемент управления прямоугольником. Любой из этих двух объектов будет служить разделителем группы. После добавления одной из этих фигур вы можете добавить два или более переключателя или другие групповые объекты.

### **Использование Microsoft Excel**

Чтобы разместить элемент управления групповым полем на листе и поместить в него элементы управления:

-  Чтобы запустить форму, в главном меню нажмите*Вид* , с последующим*Панели инструментов* и*Формы*.
-  На*Формы* панели инструментов, нажмите кнопку*Групповой ящик* и нарисуйте прямоугольник на рабочем листе.
- Введите строку заголовка для поля.
-  На*Формы* панель инструментов, нажмите*Кнопка выбора* и щелкните внутри*Групповой ящик* прямо под строкой заголовка.
-  От*Формы* снова нажмите на панель инструментов*Кнопка выбора* и щелкните внутри*Групповой ящик*под первой радиокнопкой.
-  Еще раз на*Формы* панель инструментов, нажмите*Кнопка выбора* и щелкните внутри*Групповой ящик* под предыдущим переключателем.

### **Использование Aspose.Cells**

[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс предоставляет метод с именем[**Аддгруппбокс**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , который используется для добавления элемента управления групповым полем на лист. Метод возвращает[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) объект. Более того,[**Группа**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) метод[**Коллекция форм**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) класс группирует формы, требуется[**Форма**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) массив в качестве параметра и возвращает[**Групшейп**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) объект. Класс[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) представляет собой групповое поле. В него входят несколько важных членов:

- [**Текст**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) Свойство указывает строку заголовка группового поля.
- [**Тень**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) Свойство указывает, имеет ли поле группы трехмерное затенение.

В следующем примере показано, как добавить поле группы и сгруппировать элементы управления на листе.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Предварительные темы**
- [Добавьте элементы управления ActiveX, используя Aspose.Cells.](/cells/ru/net/add-activex-controls-using-aspose-cells/)
- [Удалить элемент управления ActiveX](/cells/ru/net/remove-activex-control/)
- [Обновите элемент управления ActiveX ComboBox](/cells/ru/net/update-activex-combobox-control/)
