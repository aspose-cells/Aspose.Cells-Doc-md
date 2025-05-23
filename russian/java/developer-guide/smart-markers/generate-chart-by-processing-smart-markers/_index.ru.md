---
title: Генерация диаграммы путем обработки умных маркеров
type: docs
weight: 180
url: /ru/java/generate-chart-by-processing-smart-markers/
---

{{% alert color="primary" %}} 

API Aspose.Cells предоставляют класс WorkbookDesigner для работы с умными маркерами, где форматирование и формулы размещаются в таблицах дизайнера, а затем обрабатываются в соответствии с указанными источниками данных для заполнения данных в соответствии с умными маркерами. Также возможно создавать диаграммы Excel путем обработки умных маркеров, для этого требуются следующие шаги.

- Создание таблиц дизайнера
- Обработка таблиц дизайнера в соответствии с указанным источником данных
- Создание диаграммы на основе заполненных данных

{{% /alert %}} 
## **Создание таблиц дизайнера**
Таблица дизайнера - это простой файл Excel, созданный с помощью приложения Microsoft Excel или API Aspose.Cells, содержащий визуальное форматирование, формулы и умные маркеры, данные которых должны быть заполнены во время выполнения.

{{% alert color="primary" %}} 

Подробная информация о умных маркерах доступна [здесь](/cells/ru/java/smart-markers/).

{{% /alert %}} 

Для простоты мы будем создавать таблицу дизайнера с помощью API Aspose.Cells for Java, а затем обрабатываем ее в соответствии с динамически созданным источником данных для демонстрационных целей.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access the first (default) Worksheet from the collection

Worksheet dataSheet = book.getWorksheets().get(0);

//Name the first Worksheet for referencing

dataSheet.setName("ChartData");

//Access the CellsCollection of ChartData Worksheet

Cells cells = dataSheet.getCells();

//Place the markers in the Worksheet according to desired layout

cells.get("A1").putValue("&=$Headers(horizontal)");

cells.get("A2").putValue("&=$Year2000(horizontal)");

cells.get("A3").putValue("&=$Year2005(horizontal)");

cells.get("A4").putValue("&=$Year2010(horizontal)");

cells.get("A5").putValue("&=$Year2015(horizontal)");

{{< /highlight >}}

Если вы сохраните полученную таблицу в этой стадии, данные на листе будут выглядеть так.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_1.png)
## **Обработка таблицы дизайнера**
Для обработки таблицы дизайнера необходимо иметь источник данных, соответствующий используемым в таблице дизайнера умным маркерам. Например, мы создали запись умного маркера как **&=$Headers(horizontal)**, представляющую переменную по имени Headers, в то время как ключ **(horizontal)** подразумевает, что данные должны быть заполнены горизонтально.

Для демонстрации этого использования мы создадим источник данных с нуля и обработаем его в дизайнерской электронной таблице, созданной на предыдущем этапе. Однако в реальном времени данные могут уже быть доступны для дальнейшей обработки, поэтому вы можете пропустить создание источника данных, если данные уже доступны.

**Java**

{{< highlight csharp >}}

 //Create string arrays which will serve as data sources to the smart markers

String[] headers = new String[]{"", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10", "Item 11", "Item 12"};

String[] year2000 = new String[]{"2000", "310", "0", "110", "15", "20", "25", "30", "1222", "200", "421", "210", "133"};

String[] year2005 = new String[]{"2005", "508", "0", "170", "280", "190", "400", "105", "132", "303", "199", "120", "100"};

String[] year2010 = new String[]{"2010", "0", "210", "230", "1420", "1530", "160", "170", "110", "199", "129", "120", "230"};

String[] year2015 = new String[]{"2015", "2818", "320", "340", "260", "210", "310", "220", "0", "0", "0", "0", "122"};

{{< /highlight >}}

Обработка умных маркеров довольно проста, как показано ниже.

**Java**

{{< highlight csharp >}}

 //Create an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner();

//Set the Workbook property for the instance of WorkbookDesigner

designer.setWorkbook(book);

//Set data sources for smart markers

designer.setDataSource("Headers", headers);

designer.setDataSource("Year2000", year2000);

designer.setDataSource("Year2005", year2005);

designer.setDataSource("Year2010", year2010);

designer.setDataSource("Year2015", year2015);

//Process the designer spreadsheet against the provided data sources

designer.process();

{{< /highlight >}}

Если вы сохраните электронную таблицу на этом этапе, данные будут выглядеть следующим образом.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_2.png)

{{% alert color="primary" %}} 

Вышеприведенный фрагмент кода использует существующий экземпляр класса Workbook, созданный на первом этапе. Если у вас уже есть файл дизайнерской электронной таблицы на диске или в памяти, вы можете создать экземпляр класса Workbook, загрузив существующую дизайнерскую электронную таблицу.

{{% /alert %}} 
## **Создание диаграммы**
Как только данные на своем месте, все, что нам нужно сделать, - это создать диаграмму на основе источника данных. Чтобы сделать пример более простым, мы будем использовать метод Chart.setChartDataRange, чтобы нам не нужно было дополнительно настраивать диаграмму.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GenerateChartByProcessingSmartMarkers-GenerateChartByProcessingSmartMarkers.java" >}}





Окончательная диаграмма выглядит следующим образом.

![todo:image_alt_text](generate-chart-by-processing-smart-markers_3.png)
{{< app/cells/assistant language="java" >}}
