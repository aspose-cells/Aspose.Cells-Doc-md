---
title: Применение стилей к GridWeb
type: docs
weight: 20
url: /ru/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, стиль, стили
description: В этой статье рассматривается способ применения или установки стиля в GridWeb.
---

{{% alert color="primary" %}} 

У Aspose.Cells.GridWeb есть свой собственный внешний вид, но возможно изменить его внешний вид. Aspose.Cells.GridWeb предоставляет несколько свойств, позволяющих разработчикам полностью контролировать его внешний вид. В этой теме обсуждаются некоторые из этих свойств.

{{% /alert %}} 
## **Применение предустановленных или пользовательских стилей к Aspose.Cells.GridWeb**
### **Предустановленные стили**
Для экономии усилий разработчиков Aspose.Cells.GridWeb предлагает несколько предустановленных стилей. Просто выберите стиль из списка, чтобы применить его.

|**Стили**|**Цветовая схема**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Когда выбран определенный стиль, меняется весь внешний вид элемента управления GridWeb. Разработчики могут выбрать Предустановленный стиль для применения на этапе проектирования GridWeb, но это задание также можно выполнить во время выполнения с использованием гибкого API Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Управление Aspose.Cells.GridWeb представлено классом GridWeb.

{{% /alert %}} 

Для выбора предустановленного стиля:

1. Добавьте управление Aspose.Cells.GridWeb на веб-форму.
1. Выберите предустановленный стиль, который будет применен к элементу управления.

Управление GridWeb предоставляет свойство PresetStyle, к которому разработчики могут назначить любой желаемый предустановленный стиль.

Результат выполнения нижеприведенного фрагмента кода показан ниже. 

**Управление GridWeb с примененным стилем Colorful1** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Стиль строки заголовка**
Если вы посмотрите на элемент управления GridWeb, вы заметите две строки заголовка. Одна для столбцов (то есть A, B, C, D и т. д.) и другая для строк (то есть 1, 2, 3, 4 и т. д.). Aspose.Cells.GridWeb позволяет разработчикам управлять внешним видом этих строк заголовка. Разработчики могут установить стиль строк заголовка как на этапе проектирования, так и во время выполнения.

{{% alert color="primary" %}} 

Управление GridWeb предоставляет свойство HeaderBarStyle, которое применяет стиль к обеим строкам заголовка элемента управления.

{{% /alert %}} 

Результат приведенного ниже примера кода показан здесь. 

**Измененный стиль строки заголовка** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Стиль панели вкладок**
Можно установить стиль панели вкладок. 

**Измененные стили активной и неактивной панелей вкладок** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

На приведенной выше фигуре лист4 является активной вкладкой, поэтому ее внешний вид отличается от других вкладок, как определено в приведенном ниже примере кода.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Файл повторно используемого настраиваемого стиля**
Aspose.Cells.GridWeb также поддерживает сохранение своего вида или настроек стиля в файле. Когда вы установили все свойства внешнего вида элемента управления GridWeb, вы можете сохранить эти свойства или настройки в файле на диске. Этот подход очень полезен для разработчиков, чтобы сэкономить время и усилия, повторно используя свои старые настройки стилей из файла стиля вместо установки всех свойств стиля (или вида) элемента управления по одному.
### **Сохранение файла стиля**
Как только вы закончили установку свойств стиля, вы можете сохранить свои настройки конфигурации стиля в виде файла XML (потому что файл стиля хранится как файл XML), вызвав метод SaveCustomStyleFile элемента управления GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Сохраненный файл стилей в формате XML, поэтому разработчики также могут редактировать этот файл с помощью любого текстового редактора, если это необходимо.

{{% /alert %}} 
### **Загрузка файла стилей**
Для применения настроек стиля из существующего файла стилей к элементу управления GridWeb, разработчики могут установить путь к файлу стилей в свойстве CustomStyleFileName элемента управления. Однако перед этим следует установить свойство PresetStyle элемента управления в значение Custom. Это необходимо, потому что файл стилей содержит информацию о пользовательском стиле, которая уже определена разработчиком.

{{% alert color="primary" %}} 

Также можно загружать или сохранять файл стилей с помощью инструмента Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

ВАЖНО: Загрузка файла стилей в элемент управления GridWeb не влияет на настройки форматирования ячеек элемента управления.

{{% /alert %}} 
### **Стандартный формат XML-шаблона стиля**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
