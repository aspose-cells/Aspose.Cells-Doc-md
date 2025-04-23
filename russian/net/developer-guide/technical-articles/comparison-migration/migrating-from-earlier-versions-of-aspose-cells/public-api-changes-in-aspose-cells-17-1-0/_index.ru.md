---
title: Изменения в общедоступном API в Aspose.Cells 17.1.0
type: docs
weight: 370
url: /ru/net/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 16.12.0 до 17.1.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка диаграмм Excel 2016**
API Aspose.Cells добавили поддержку нескольких диаграмм Excel 2016 путем расширения перечисления ChartType. Следующие новые поля были добавлены с выпуском Aspose.Cells 17.1.0.

- ChartType.BoxWhisker: Серия представлена в виде ящика и усов.
- ChartType.Funnel: Серия представлена в виде воронки.
- ChartType.ParetoLine: Серия представлена в виде кривых Парето.
- ChartType.Sunburst: Серия представлена в виде sunburst.
- ChartType.Treemap: Серия представлена в виде дерева.
- ChartType.Waterfall: Серия представлена в виде водопада.
- ChartType.Histogram: Серия представлена в виде гистограммы.

{{% alert color="primary" %}} 

Проверьте подробную статью по [чтению типов диаграмм Excel 2016](/cells/ru/net/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Добавлен сеттер для свойства LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 добавил сеттер для свойства LoadFilter.LoadDataFilterOptions для замены переменной экземпляра m_LoadDataFilterOptions. Пользователи могут изменять свойство LoadDataFilterOptions в собственной реализации класса LoadFilter, чтобы изменить поведение загрузки шаблонных файлов.

Вот простой сценарий использования.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Custom Template Filtering](/cells/ru/net/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 17.1.0 вывело свойство SignificantDigits из класса CellsHelper, которое позволяет устанавливать количество значащих цифр для числовых значений в электронной таблице. Значение по умолчанию свойства CellsHelper.SignificantDigits равно 17 и применимо только в случае, если результат должен быть сохранен в формате файла XLSX.

Вот простой сценарий для демонстрации использования свойства CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Setting Number of Significant Digits](/cells/ru/net/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

 // Specify the number of significant digits

CellsHelper.SignificantDigits = 15;

{{< /highlight >}}


### **Добавлено свойство GlowEffect.Color**
Aspose.Cells 17.1.0 добавил свойство GlowEffect.Color, которое можно использовать для извлечения цвета свечения.

Следующий фрагмент использует свойство GlowEffect.Color.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Reading the Shape's Glow Color](/cells/ru/net/read-color-of-shape-s-glow-effect/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 17.1.0 добавил свойства PaperWidth и PaperHeight для класса PageSetup. Свойства PageSetup.PaperWidth и PageSetup.PaperHeight имеют тип double и представляют ширину и высоту бумаги в дюймах с учетом ориентации страницы.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Retrieving Worksheet's Paper Size](/cells/ru/net/get-paper-width-and-height-of-page-setup-of-worksheet/)

{{% /alert %}} 
### **Добавлено свойство WorkbookSettings.CheckCustomNumberFormat.**
Aspose.Cells 17.1.0 добавил свойство CheckCustomNumberFormat в класс WorkbookSettings. CheckCustomNumberFormat полезен для проверки, правильно ли установлено свойство Style.Custom или нет. Если свойство Style.Custom было неправильно установлено, т.е. значение не соответствует действительному шаблону, то API Aspose.Cells выдаст исключение CellsException с соответствующим сообщением.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Verifying Custom Format](/cells/ru/net/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**C#**

{{< highlight csharp >}}

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
Aspose.Cells 17.1.0 также добавил поле Percentage в перечисление DisplayUnitType. Поле DisplayUnitType.Percentage указывает, что значения на диаграмме будут делиться на 0.01.
## **Удалены API**
### **Экземплярная переменная m_LoadDataFilterOptions удалена.**
Этот релиз удалил экземплярную переменную m_LoadDataFilterOptions. Рекомендуется использовать свойство LoadFilter.LoadDataFilterOptions вместо нее.
{{< app/cells/assistant language="csharp" >}}
