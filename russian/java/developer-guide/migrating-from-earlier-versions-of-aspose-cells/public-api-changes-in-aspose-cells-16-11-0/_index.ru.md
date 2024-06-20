---
title: Изменения в открытом API в Aspose.Cells 16.11.0
type: docs
weight: 360
url: /ru/java/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Этот документ описывает изменения в API Aspose.Cells от версии 16.10.0 до 16.11.0, которые могут быть интересны модульным/программным разработчикам. Он включает не только новые и обновленные публичные методы, добавленные и удаленные классы и т. д., но также описывает любые изменения в поведении за кадром в Aspose.Cells.

{{% /alert %}} 
## **Добавленные API**
### **Поддержка настроек глобализации**
Aspose.Cells 16.11.0 предоставляет класс GlobalizationSettings вместе со свойством WorkbookSettings.GlobalizationSettings для принудительного использования пользовательских меток для Промежуточных и Итоговых итогов в API Aspose.Cells. В классе GlobalizationSettings есть следующие методы, которые могут быть переопределены в пользовательской реализации, чтобы дать желаемые имена меткам **Промежуточный** и **Итоговый**.

- GlobalizationSettings.getTotalName: Получает имя промежуточного итога.
- GlobalizationSettings.getGrandTotalName: Получает имя итогового итога.

Вот простой пользовательский класс, который расширяет класс GlobalizationSettings и переопределяет упомянутые выше методы для возврата пользовательских меток для функции объединения Среднее.

**Java**

{{< highlight csharp >}}

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

Следующий фрагмент загружает существующую электронную таблицу и добавляет Промежуточный итог типа Среднее к данным, уже доступным в листе. Класс CustomSettings и его методы getTotalName и getGrandTotalName будут вызваны во время добавления Промежуточного итога в лист.

**Java**

{{< highlight csharp >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

Класс GlobalizationSettings также предлагает метод getOtherName, который полезен для получения имен меток "Другие" для круговых графиков. Вот простой сценарий использования метода GlobalizationSettings.getOtherName.

**Java**

{{< highlight csharp >}}

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

Следующий фрагмент загружает существующую электронную таблицу с круговой диаграммой и рендерит диаграмму в изображение, используя созданный выше класс CustomSettings.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells 16.11.0 предоставляет класс CellsFactory, который в настоящее время имеет один метод, а именно: createStyle. Метод createStyle класса CellsFactory может быть использован для создания экземпляра класса Style без добавления его в пул стилей книги.

Вот простой сценарий использования метода createStyle класса CellsFactory.

**Java**

{{< highlight csharp >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Добавлено свойство AbsolutePath книги**
Aspose.Cells 16.11.0 предоставляет свойство AbsolutePath для книги, которое позволяет получить или установить абсолютный путь книги, сохраненный в файле workbook.xml. Это свойство полезно только при обновлении внешних ссылок.
### **Добавлен метод getHyperlink класса GridHyperlinkCollection**
Aspose.Cells.GridWeb 16.11.0 предоставляет метод getHyperlink класса GridHyperlinkCollection, который позволяет получить экземпляр GridHyperlink путем передачи экземпляра GridCell или пары целых чисел, соответствующих индексам строки и столбца.

{{% alert color="primary" %}} 

В случае, если на указанной ячейке не найдена гиперссылка, метод getHyperlink вернет null.

{{% /alert %}} 

Вот простой сценарий использования метода getHyperlink.

**Java**

{{< highlight csharp >}}

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
### **Устаревший конструктор Style**
Пожалуйста, используйте метод cellsFactory.createStyle в качестве альтернативы.
## **Удаленные API**
### **Удален метод getConditionalStyle класса Cell**
Пожалуйста, используйте метод getConditionalFormattingResult класса Cell вместо.
### **Удален метод getMaxDataRowInColumn(int column) класса Cells**
Пожалуйста, используйте метод getLastDataRow(int) в качестве альтернативы.
### **Удален свойство Draft класса PageSetup**
Рекомендуется использовать свойство PrintDraft класса PageSetup вместо.
### **Удалено свойство FilterColumnCollection класса AutoFilter**
Пожалуйста, рассмотрите возможность использования свойства AutoFilter.FilterColumns для достижения той же цели.
### **Свойство Deleted TickLabels.Rotation**
Пожалуйста, используйте свойство TickLabels.RotationAngle вместо.
