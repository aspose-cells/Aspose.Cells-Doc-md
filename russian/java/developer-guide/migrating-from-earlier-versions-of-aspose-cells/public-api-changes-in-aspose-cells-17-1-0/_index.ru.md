---
title: Общедоступный API Изменения в Aspose.Cells 17.1.0
type: docs
weight: 380
url: /ru/java/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.12.0 до 17.1.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка диаграмм Excel 2016**
Aspose.Cells В API добавлена поддержка нескольких диаграмм Excel 2016 путем расширения перечисления ChartType. В выпуске Aspose.Cells 17.1.0 были добавлены следующие новые поля.

- ChartType.BOX_WHISKER: серия представлена в виде рамки и усов.
- ChartType.FUNNEL: серия представлена в виде воронки.
- ChartType.PARETO_LINE: серия представлена в виде линий Парето.
- ChartType.SUNBURST: серия представлена в виде солнечных лучей.
- ChartType.TREEMAP: серия представлена в виде древовидной карты.
- ChartType.WATERFALL: серия выложена в виде водопада.
- ChartType.HISTOGRAM: ряд представлен в виде гистограммы.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Чтение типов диаграмм Excel 2016](/cells/ru/java/read-and-manipulate-excel-2016-charts/)

{{% /alert %}} 
### **Добавлен установщик для свойства LoadFilter.LoadDataFilterOptions.**
Aspose.Cells В версии 17.1.0 добавлен установщик для свойства LoadFilter.LoadDataFilterOptions, заменяющий переменную экземпляра m_LoadDataFilterOptions. Пользователи могут изменить свойство LoadDataFilterOptions в собственной реализации класса LoadFilter, чтобы изменить поведение загрузки файлов шаблонов.

Вот простой сценарий использования.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Пользовательская фильтрация шаблонов](/cells/ru/java/filter-objects-while-loading-workbook-or-worksheet/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells 17.1.0 предоставил свойство SignificantDigits из класса CellsHelper, которое позволяет получить или установить количество значащих цифр для числовых значений в электронной таблице. Значение свойства CellsHelper.SignificantDigits по умолчанию равно 17, тогда как оно применимо, только если результат должен быть сохранен в формате файла XLSX.

Вот простой сценарий, демонстрирующий использование свойства CellsHelper.SignificantDigits.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Установка количества значащих цифр](/cells/ru/java/specifying-significant-digits-to-be-stored-in-excel-file/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Добавлено свойство GlowEffect.Color.**
Aspose.Cells В версии 17.1.0 добавлено свойство GlowEffect.Color, которое можно использовать для получения цвета эффекта свечения.

В следующем фрагменте используется свойство GlowEffect.Color.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Чтение цвета свечения фигуры](/cells/ru/java/read-color-of-the-shape-s-glow-effect/)
{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
Aspose.Cells 17.1.0 предоставляет свойства PaperWidth и PaperHeight для класса PageSetup. Свойства PageSetup.PaperWidth и PageSetup.PaperHeight имеют тип double, представляющий ширину и высоту бумаги в дюймах с учетом ориентации страницы.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Получение размера бумаги рабочего листа](/cells/ru/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)

{{% /alert %}} 
### **Добавлено свойство WorkbookSettings.CheckCustomNumberFormat.**
Aspose.Cells 17.1.0 добавило свойство CheckCustomNumberFormat в класс WorkbookSettings. CheckCustomNumberFormat полезен для проверки правильности установки свойства Style.Custom. В случае, если свойство Style.Custom установлено неправильно, т.е. значение не соответствует допустимому шаблону, тогда API-интерфейсы Aspose.Cells вызовут исключение CellsException с соответствующим сообщением.

{{% alert color="primary" %}} 

 Ознакомьтесь с подробной статьей о[Проверка пользовательской формы](/cells/ru/java/check-custom-number-format-when-setting-style-custom-property/)

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

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
### **Добавлено поле DisplayUnitType.PERCENTAGE**
Aspose.Cells 17.1.0 также предоставил поле PERCENTAGE для перечисления DisplayUnitType. Поле DisplayUnitType.PERCENTAGE указывает, что значения на графике должны быть разделены на 0,01.
## **Удаленные API**
### **Переменная экземпляра m_LoadDataFilterOptions удалена**
В этом выпуске удалена переменная экземпляра m_LoadDataFilterOptions. Вместо этого рекомендуется использовать свойство LoadFilter.LoadDataFilterOptions.
