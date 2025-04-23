---
title: Изменения в общедоступном API в Aspose.Cells 17.1.0
type: docs
weight: 380
url: /ru/java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells с версии 16.12.0 до 17.1.0, которые могут быть интересны для разработчиков модулей/приложений. Он включает не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но также описание любых изменений в поведении внутри Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка диаграмм Excel 2016**
API Aspose.Cells добавили поддержку нескольких диаграмм Excel 2016 путем расширения перечисления ChartType. Следующие новые поля были добавлены с выпуском Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: Серия представлена в виде ящика и усов.
- ChartType.FUNNEL: Серия представлена в виде воронки.
- ChartType.PARETO_LINE: Серия представлена в виде диаграммы Парето.
- ChartType.SUNBURST: Серия представлена в виде солнечной вспышки.
- ChartType.TREEMAP: Серия реализована в виде древовидной карты.
- ChartType.WATERFALL: Серия представлена в виде водопада.
- ChartType.HISTOGRAM: Серия представлена в виде гистограммы.

{{% alert color="primary" %}} 

Проверьте подробную статью по [чтению типов диаграмм Excel 2016](/cells/ru/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Добавлен сеттер для свойства LoadFilter.LoadDataFilterOptions**
Aspose.Cells 17.1.0 добавил сеттер для свойства LoadFilter.LoadDataFilterOptions для замены переменной экземпляра m_LoadDataFilterOptions. Пользователи могут изменять свойство LoadDataFilterOptions в собственной реализации класса LoadFilter, чтобы изменить поведение загрузки шаблонных файлов.

Вот простой сценарий использования.

{{% alert color="primary" %}} 

Проверьте подробную статью по [настраиваемой фильтрации шаблонов](/cells/ru/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Добавлено свойство CellsHelper.SignificantDigits**
Aspose.Cells 17.1.0 вывело свойство SignificantDigits из класса CellsHelper, которое позволяет устанавливать количество значащих цифр для числовых значений в электронной таблице. Значение по умолчанию свойства CellsHelper.SignificantDigits равно 17 и применимо только в случае, если результат должен быть сохранен в формате файла XLSX.

Вот простой сценарий для демонстрации использования свойства CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

Проверьте подробную статью по [установке количества значащих цифр](/cells/ru/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Добавлено свойство GlowEffect.Color**
Aspose.Cells 17.1.0 добавил свойство GlowEffect.Color, которое можно использовать для извлечения цвета свечения.

Следующий фрагмент использует свойство GlowEffect.Color.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Чтению цвета свечения формы](/cells/ru/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Добавлены свойства PageSetup.PaperWidth и PaperHeight.**
Aspose.Cells 17.1.0 добавил свойства PaperWidth и PaperHeight для класса PageSetup. Свойства PageSetup.PaperWidth и PageSetup.PaperHeight имеют тип double и представляют ширину и высоту бумаги в дюймах с учетом ориентации страницы.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Получению размера бумаги листа](/cells/ru/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Добавлено свойство WorkbookSettings.CheckCustomNumberFormat.**
Aspose.Cells 17.1.0 добавил свойство CheckCustomNumberFormat в класс WorkbookSettings. CheckCustomNumberFormat полезен для проверки, правильно ли установлено свойство Style.Custom или нет. Если свойство Style.Custom было неправильно установлено, т.е. значение не соответствует действительному шаблону, то API Aspose.Cells выдаст исключение CellsException с соответствующим сообщением.

{{% alert color="primary" %}} 

Проверьте подробную статью по [Проверке пользовательского формата](/cells/ru/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Добавлено поле DisplayUnitType.PERCENTAGE.**
Aspose.Cells 17.1.0 также добавил поле PERCENTAGE в перечисление DisplayUnitType. Поле DisplayUnitType.PERCENTAGE указывает, что значения на диаграмме должны быть разделены на 0.01.
## **Удалены API**
### **Экземплярная переменная m_LoadDataFilterOptions удалена.**
Этот релиз удалил экземплярную переменную m_LoadDataFilterOptions. Рекомендуется использовать свойство LoadFilter.LoadDataFilterOptions вместо нее.
{{< app/cells/assistant language="java" >}}
