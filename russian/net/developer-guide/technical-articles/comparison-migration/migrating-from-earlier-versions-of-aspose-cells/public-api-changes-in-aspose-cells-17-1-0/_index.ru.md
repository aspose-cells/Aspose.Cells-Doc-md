---
title: Общедоступный API Изменения в Aspose.Cells 17.1.0
type: docs
weight: 370
url: /ru/net/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.12.0 до 17.1.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка диаграмм Excel 2016**
Aspose.Cells В API добавлена поддержка нескольких диаграмм Excel 2016 путем расширения перечисления ChartType. В выпуске Aspose.Cells 17.1.0 были добавлены следующие новые поля.

- ChartType.BoxWhisker: серия представлена в виде прямоугольника и усов.
- ChartType.Funnel: серия представлена в виде воронки.
- ChartType.ParetoLine: серия представлена в виде линий Парето.
- ChartType.Sunburst: серия представлена в виде солнечных лучей.
- ChartType.Treemap: серия представлена в виде древовидной карты.
- ChartType.Waterfall: Серия построена в виде водопада.
- ChartType.Histogram: ряд представлен в виде гистограммы.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Чтение типов диаграмм Excel 2016](/cells/ru/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Добавлен установщик для свойства LoadFilter.LoadDataFilterOptions.**
Aspose.Cells В версии 17.1.0 добавлен установщик для свойства LoadFilter.LoadDataFilterOptions, заменяющий переменную экземпляра m_LoadDataFilterOptions. Пользователи могут изменить свойство LoadDataFilterOptions в собственной реализации класса LoadFilter, чтобы изменить поведение загрузки файлов шаблонов.

Вот простой сценарий использования.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Пользовательская фильтрация шаблонов](/cells/ru/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            this.LoadDataFilterOptions = LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            this.LoadDataFilterOptions = LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}


### **Добавлено свойство CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 предоставил свойство SignificantDigits из класса CellsHelper, которое позволяет получить или установить количество значащих цифр для числовых значений в электронной таблице. Значение свойства CellsHelper.SignificantDigits по умолчанию равно 17, тогда как оно применимо только в том случае, если результат должен быть сохранен в формате файла XLSX.

Вот простой сценарий, демонстрирующий использование свойства CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Установка количества значащих цифр](/cells/ru/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Добавлено свойство GlowEffect.Color.**
Aspose.Cells В версии 17.1.0 добавлено свойство GlowEffect.Color, которое можно использовать для получения цвета эффекта свечения.

В следующем фрагменте используется свойство GlowEffect.Color.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Чтение цвета свечения фигуры](/cells/ru/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Read the source excel file

var book = new Workbook(dir + "sample.xlsx");

// Access first worksheet

var sheet = book.Worksheets[0];

// Access the first shape

var shape = sheet.Shapes[0];

// Read the glow effect color

var glow = shape.Glow;

var color = glow.Color;

{{< /highlight >}}


### **Добавлены свойства PageSetup.PaperWidth и PaperHeight.**
Aspose.Cells 17.1.0 предоставляет свойства PaperWidth и PaperHeight для класса PageSetup. Свойства PageSetup.PaperWidth и PageSetup.PaperHeight имеют тип double, представляющий ширину и высоту бумаги в дюймах с учетом ориентации страницы.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Получение размера бумаги рабочего листа](/cells/ru/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Добавлено свойство WorkbookSettings.CheckCustomNumberFormat.**
Aspose.Cells 17.1.0 добавило свойство CheckCustomNumberFormat в класс WorkbookSettings. CheckCustomNumberFormat полезен для проверки правильности установки свойства Style.Custom. В случае, если свойство Style.Custom установлено неправильно, т.е. значение не соответствует допустимому шаблону, тогда API-интерфейсы Aspose.Cells вызовут исключение CellsException с соответствующим сообщением.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Проверка пользовательского формата](/cells/ru/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 // Create an instance of Workbook

var book = new Workbook();

// Set CheckCustomNumberFormat property to true

book.Settings.CheckCustomNumberFormat = true;

// Access first worksheet

var sheet = book.Worksheets[0];

// Access a cell

var cell = sheet.Cells["B5"];

// Insert a value to the cell

cell.PutValue(2347);

// Access cell's style

Style style = cell.GetStyle();



// Set Custom property to an invalid pattern

style.Custom = "ggg @ fff";

// Set the modified style to the cell

cell.SetStyle(style);

{{< /highlight >}}


### **Добавлено поле DisplayUnitType.Percentage**
Aspose.Cells 17.1.0 также предоставляет поле Percentage перечислению DisplayUnitType. Поле DisplayUnitType.Percentage указывает, что значения на графике должны быть разделены на 0,01.
## **Удаленные API**
### **Переменная экземпляра m_LoadDataFilterOptions удалена**
В этом выпуске удалена переменная экземпляра m_LoadDataFilterOptions. Вместо этого рекомендуется использовать свойство LoadFilter.LoadDataFilterOptions.
