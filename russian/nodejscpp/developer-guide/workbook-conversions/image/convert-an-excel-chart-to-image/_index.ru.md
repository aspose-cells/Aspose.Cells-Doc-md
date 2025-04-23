---  
title: Преобразование графика Excel в изображение с помощью Node.js через C++  
linktitle: Конвертировать диаграмму Excel в изображение  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Узнайте, как конвертировать графики Excel в изображения, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Диаграммы наглядны и облегчают пользователю видеть сравнения, паттерны и тенденции в данных. Например, вместо анализа колонок чисел в таблице, диаграмма сразу показывает, уменьшаются ли продажи или растут, или сравнивает фактические продажи с плановыми. Людям часто приходится представлять статистическую и графическую информацию в легко понимаемой и легко поддерживаемой форме. Изображение помогает.  

Иногда в приложениях или веб-страницах требуются графики. Или может понадобиться для документа Word, файла PDF, презентации PowerPoint или другого приложения. В каждом случае вы хотите преобразовать график в изображение, чтобы использовать его в другом месте.  

{{% /alert %}}  

## **Конвертация диаграмм в изображения**  

В приведенных здесь примерах преобразуются круговая диаграмма и столбчатая диаграмма в изображения.  

### **Конвертация круговой диаграммы в файл изображения**  

Сначала создайте круговую диаграмму в Microsoft Excel, а затем преобразуйте ее в файл изображения с помощью Aspose.Cells for Node.js via C++. Этот пример кода создает изображение EMF на основе круговой диаграммы из шаблона файла Excel.  

|**Результат: изображение круговой диаграммы**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Создайте круговую диаграмму в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Введите некоторые данные в лист.  
   1. Создайте круговую диаграмму на основе данных.  
   1. Сохраните файл.  

|**Исходный файл.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Скачайте и установите Aspose.Cells:  
   1. [Скачайте Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Установите его на вашем компьютере для разработки.  

Все компоненты [Aspose](http://www.aspose.com/) работают в режиме оценки при первой установке. Режим оценки не имеет временных ограничений и вставляет в выходные документы только водяной знак.  

1. Создайте проект:  
   1. Запустите предпочитаемую IDE.  
   1. Создайте новое консольное приложение. В этом примере используется Node.js, но вы можете создать его в любой среде выполнения JavaScript.  
   1. Добавьте ссылку. В этом проекте используется Aspose.Cells, поэтому добавьте ссылку на Aspose.Cells for Node.js via C++.  
   1. Напишите код, который находит и конвертирует диаграмму. Приведен ниже код, используемый компонентом для выполнения задачи. Используется очень немного строк кода.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

### **Конвертация столбчатой диаграммы в файл изображения**  

Сначала создайте столбцовую диаграмму в Microsoft Excel и преобразуйте ее в файл изображения, как указано выше. После выполнения этого кода создается JPEG-файл на основе столбчатой диаграммы из шаблона файла Excel.  

|**Выходной файл: изображение столбчатой диаграммы.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Создайте столбчатую диаграмму в Microsoft Excel:  
   1. Откройте новую книгу в Microsoft Excel.  
   1. Введите некоторые данные в лист.  
   1. Создайте столбчатую диаграмму на основе данных.  
   1. Сохраните файл.  

|**Входной файл.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Создайте проект с ссылками, как описано выше.  
1. Динамически преобразуйте диаграмму в изображение. Ниже приведен используемый компонентом код для выполнения этой задачи. Код аналогичен предыдущему:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

