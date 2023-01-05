---
title: Применение стилей к GridWeb
type: docs
weight: 20
url: /ru/net/apply-styles-to-gridweb/
---
{{% alert color="primary" %}} 

Aspose.Cells. GridWeb имеет собственный внешний вид по умолчанию, но его внешний вид можно изменить. Aspose.Cells.GridWeb предоставляет несколько свойств, позволяющих разработчикам полностью контролировать его внешний вид. В этом разделе обсуждаются некоторые из этих свойств.

{{% /alert %}} 
## **Применение предустановленных или пользовательских стилей к Aspose.Cells.GridWeb**
### **Предустановленные стили**
Чтобы сэкономить усилия разработчиков, Aspose.Cells.GridWeb предлагает несколько предустановленных стилей. Просто выберите стиль из списка, чтобы применить стиль.

|**Стили**|**Цветовая схема**|
|:- |:- |
|Стандарт|Серебряный|
|Красочный1|Роза|
|Красочный2|Синий|
|Профессиональный1|Голубой|
|Профессиональный2|Снова голубой|
|Традиционный1|Темнота|
|Традиционный2|Серый|
|Обычай|Индивидуальные|
При выборе определенного стиля изменяется весь внешний вид элемента управления GridWeb. Разработчики могут выбрать предустановленный стиль для применения к Grid во время разработки, но эту задачу также можно выполнить во время выполнения с помощью гибкого API из Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Aspose.Cells. Элемент управления GridWeb представлен классом GridWeb.

{{% /alert %}} 

Чтобы выбрать предустановленный стиль:

1. Добавьте элемент управления Aspose.Cells.GridWeb в веб-форму.
1. Выберите предустановленный стиль, который будет применен к элементу управления.

Элемент управления GridWeb предоставляет свойство PresetStyle, которому разработчики могут назначать любой желаемый предустановленный стиль.

 Вывод приведенного ниже фрагмента кода показан ниже.

**Элемент управления GridWeb с примененным к нему стилем Colorful1** 

![дело:изображение_альтернативный_текст](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Стиль заголовка**
Если вы посмотрите на элемент управления GridWeb, вы заметите две полосы заголовка. Один для столбцов (то есть A, B, C, D и т. д.), а другой для строк (то есть 1, 2, 3, 4 и т. д.). Aspose.Cells.GridWeb позволяет разработчикам управлять внешним видом этих заголовков. Разработчики могут установить стиль заголовков либо во время разработки, либо во время выполнения.

{{% alert color="primary" %}} 

Элемент управления GridWeb предоставляет свойство HeaderBarStyle, которое применяет стиль к обеим полосам заголовков элемента управления.

{{% /alert %}} 

 Вывод приведенного ниже примера кода показан здесь.

**Измененный стиль панели заголовка** 

![дело:изображение_альтернативный_текст](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Стиль панели вкладок**
 Можно установить стиль панели вкладок.

**Изменены стили активных и неактивных панелей вкладок.** 

![дело:изображение_альтернативный_текст](apply-styles-to-gridweb_3.png)

На приведенном выше рисунке Лист4 является активной вкладкой, поэтому ее внешний вид отличается от других вкладок, как определено в приведенном ниже примере кода.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Многоразовый настраиваемый файл стиля**
Aspose.Cells.GridWeb также поддерживает сохранение параметров внешнего вида или стиля в файле. Когда вы установите все свойства внешнего вида элемента управления GridWeb, вы можете сохранить эти свойства или параметры в файле на диске. Этот подход очень полезен для разработчиков, так как позволяет сэкономить время и усилия, повторно используя свои старые конфигурации стилей из файла стилей вместо того, чтобы задавать все свойства стиля (или внешнего вида) элемента управления по одному.
### **Сохранение файла стиля**
После того, как вы закончите настройку свойств стиля, вы можете сохранить параметры конфигурации стиля в виде XML-файла (это связано с тем, что этот файл стиля хранится в виде XML-файла), вызвав метод SaveCustomStyleFile элемента управления GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Сохраненный файл стилей имеет формат XML, поэтому при желании разработчики могут редактировать этот файл в любом текстовом редакторе.

{{% /alert %}} 
### **Загрузка файла стиля**
Чтобы применить параметры стиля из существующего файла стиля к элементу управления GridWeb, разработчики могут указать путь к файлу стиля в свойстве CustomStyleFileName элемента управления. Но перед этим необходимо установить для свойства PresetStyle элемента управления значение Custom. Это связано с тем, что этот файл стиля содержит информацию о пользовательском стиле, которая уже определена разработчиком.

{{% alert color="primary" %}} 

Также можно загрузить или сохранить файл стиля с помощью Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО. Загрузка файла стиля в элемент управления GridWeb не влияет на параметры форматирования ячеек элемента управления.

{{% /alert %}} 
### **Стандартный формат шаблона стиля XML**
{{< highlight "java" >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
