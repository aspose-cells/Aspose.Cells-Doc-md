---
title: Установите цвет вкладки рабочего листа в Aspose.Cells
type: docs
weight: 20
url: /ru/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Установить цвет вкладки рабочего листа**
Aspose.Cells позволяет изменить цвет отдельных вкладок рабочего листа, чтобы они выделялись среди остальных. Например, вы можете сделать «Расходы» красным, «Продажи» — зеленым, «Активы» — синим и т. д.
### **Настройка цвета вкладки рабочего листа с помощью Microsoft Excel**
1. Щелкните правой кнопкой мыши вкладку на вкладке в нижней части текущего рабочего листа.
1. Выбирать**Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите**ХОРОШО**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Установить цвет вкладки рабочего листа** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Установить цвет вкладки рабочего листа](/cells/ru/net/set-worksheet-tab-color/).

{{% /alert %}}
