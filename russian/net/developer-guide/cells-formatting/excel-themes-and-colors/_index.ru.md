---
title: Темы и цвета Excel
type: docs
weight: 100
url: /ru/net/excel-themes-and-colors/
description: Код C#, чтобы использовать цветовую схему Excel с API Aspose.Cells for .NET
keywords: C#, чтобы создавать и применять цветовые схемы, C# программно создавать свою собственную цветовую схему, программно применять пользовательскую цветовую схему, C# как использовать цветовую схему в Excel
---

## **Как применить и создать цветовую схему в Excel**
Темы документов позволяют легко координировать цвета, шрифты и графические эффекты форматирования документов Excel и быстро обновлять их. 
Темы предоставляют единообразный вид с именованными стилями, графическими эффектами и другими объектами, используемыми в рабочей книге. Например, стиль Accent1 в темах Office и Apex выглядит по-разному. Часто вы применяете тему документа, а затем изменяете ее в соответствии с вашими запросами.

### **Как применить цветовую схему в Excel**
1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.
1. Нажмите кнопку "Цвета" в разделе "Темы".
<br>
<img src="color.png" width=70% />
1. Выберите цветовую палитру, которая соответствует вашим требованиям, или наведите курсор на схему, чтобы увидеть предварительный просмотр.

### **Как создать пользовательскую цветовую схему в Excel**
Вы можете создать собственный набор цветов, чтобы придать вашему документу свежий, уникальный вид или соответствовать корпоративному стилю вашей организации.

1. Откройте Excel и перейдите на вкладку "Разметка страницы" на ленте Excel.
1. Нажмите кнопку "Цвета" в разделе "Темы".
1. Нажмите кнопку "Настроить цвета...".
<br>
<img src="color2.png" width=70% />

1. В диалоговом окне "Создание новых тем цветов" вы можете выбрать цвета для каждого элемента, нажав на выпадающие списки цветов рядом с ними. Вы можете выбрать цвета из палитры или определить пользовательские цвета, используя опцию "Другие цвета".
<br>
<img src="color3.png" width=70% />
1. После выбора всех желаемых цветов укажите имя для вашей пользовательской цветовой схемы в поле "Имя".

1. Нажмите кнопку "Сохранить", чтобы сохранить вашу пользовательскую цветовую схему. Ваша пользовательская цветовая схема теперь будет доступна в раскрывающемся меню "Цвета" для последующего использования.

## **Как создать и применить цветовую схему в Aspose.Cells**
Aspose.Cells предоставляет возможности настройки тем и цветов.

### **Как создать пользовательскую цветовую тему в Aspose.Cells**
Если цвета темы используются в файле, нам не нужно изменять каждую ячейку индивидуально, мы просто должны изменить цвета в теме.

Приведенный ниже пример показывает, как применить пользовательские темы с желаемыми цветами. Мы используем образец файла шаблона, созданный вручную в Microsoft Excel 2007.

Приведенный ниже пример загружает шаблонный файл XLSX, определяет цвета для различных типов цвета темы, применяет пользовательские цвета и сохраняет файл Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **Как применить цвета темы в Aspose.Cells**

Приведенный ниже пример применяет передний план ячейки и цвета шрифта на основе цветов темы по умолчанию (рабочей книги). Он также сохраняет файл Excel на диск.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **Как получить и установить цвета темы в Aspose.Cells**
 Ниже приведены несколько методов и свойств, реализующих цвета темы.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Используется для установки цвета переднего плана.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Используется для установки цвета фона.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Используется для установки цвета шрифта.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Используется для получения цвета темы.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Используется для установки цвета темы.

В следующем примере показано, как получить и установить цвета темы.

В следующем примере используется шаблонный файл XLSX, получаются цвета для различных типов цветов темы, изменяются цвета и сохраняется файл Microsoft Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Продвинутые темы**
- [Извлечение данных о теме из файла Excel](/cells/ru/net/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="csharp" >}}
