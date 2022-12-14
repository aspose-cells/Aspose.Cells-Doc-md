---
title: Общедоступный API Изменения в Aspose.Cells 16.11.0
type: docs
weight: 360
url: /ru/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

В этом документе описаны изменения в Aspose.Cells API с версии 16.10.0 до 16.11.0, которые могут представлять интерес для разработчиков модулей/приложений. Он включает в себя не только новые и обновленные общедоступные методы, добавленные и удаленные классы и т. д., но и описание любых изменений в поведении за кулисами в Aspose.Cells.

{{% /alert %}} 
## **Добавлены API**
### **Поддержка настроек глобализации**
Aspose.Cells 16.11.0 предоставил класс GlobalizationSettings вместе со свойством WorkbookSettings.GlobalizationSettings, чтобы заставить API Aspose.Cells использовать настраиваемые метки для промежуточных итогов. Класс GlobalizationSettings имеет следующие методы, которые можно переопределить в пользовательской реализации, чтобы дать нужные имена меткам.**Общий** & **Общий итог**.

- GlobalizationSettings.getTotalName: получает общее имя функции.
- GlobalizationSettings.getGrandTotalName: получает общее имя функции.

Вот простой пользовательский класс, который расширяет класс GlobalizationSettings и переопределяет его вышеупомянутые методы, чтобы возвращать пользовательские метки для функции консолидации Average.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

Следующий фрагмент загружает существующую электронную таблицу и добавляет промежуточный итог типа «Среднее» к данным, уже доступным на листе. Класс CustomSettings и его методы getTotalName и getGrandTotalName будут вызываться во время добавления промежуточного итога на рабочий лист.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

Класс GlobalizationSettings также предлагает метод getOtherName, который полезен для получения имени метки «Другое» для круговых диаграмм. Вот простой сценарий использования метода GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

Следующий фрагмент загружает существующую электронную таблицу, содержащую круговую диаграмму, и отображает диаграмму в изображение с использованием созданного выше класса CustomSettings.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Добавлен класс CellsFactory**
Aspose.Cells 16.11.0 предоставил класс CellsFactory, который в настоящее время имеет один метод, то есть; создатьСтиль. Метод CellsFactory.createStyle можно использовать для создания экземпляра класса Style без добавления его в пул стилей рабочей книги.

Вот простой сценарий использования метода CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Добавлено свойство Workbook.AbsolutePath**
Aspose.Cells 16.11.0 предоставило свойство Workbook.AbsolutePath, позволяющее получить или установить абсолютный путь к книге, хранящийся в файле workbook.xml. Это свойство полезно только при обновлении внешних ссылок.
### **Добавлен метод GridHyperlinkCollection.getHyperlink.**
Aspose.Cells.GridWeb 16.11.0 предоставил метод getHyperlink классу GridHyperlinkCollection, который позволяет получить экземпляр GridHyperlink либо путем передачи экземпляра GridCell, либо пары целых чисел, соответствующих индексам столбца строки.

{{% alert color="primary" %}} 

Если в указанной ячейке гиперссылка не найдена, метод getHyperlink вернет значение null.

{{% /alert %}} 

Вот простой сценарий использования метода getHyperlink.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **Устаревшие API**
### **Устаревший конструктор стилей**
В качестве альтернативы используйте метод cellFactory.createStyle.
## **Удаленные API**
### **Удален метод Cell.getConditionalStyle.**
Вместо этого используйте метод Cell.getConditionalFormattingResult.
### **Удален метод Cells.getMaxDataRowInColumn(int column)**
В качестве альтернативы используйте метод Cells.getLastDataRow(int).
### **Удаленное свойство PageSetup.Draft**
Вместо этого рекомендуется использовать свойство PageSetup.PrintDraft.
### **Удаленное свойство AutoFilter.FilterColumnCollection**
Пожалуйста, рассмотрите возможность использования свойства AutoFilter.FilterColumns для достижения той же цели.
### **Удалено свойство TickLabels.Rotation**
Вместо этого используйте свойство TickLabels.RotationAngle.
