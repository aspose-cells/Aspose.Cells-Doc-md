---
title: Настройка цвета вкладки листа в Aspose.Cells
type: docs
weight: 20
url: /ru/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Настройка цвета вкладки листа**
Aspose.Cells позволяет изменять цвет отдельных вкладок таблицы, чтобы выделить их из остальных. Например, вы можете сделать вкладку Expenses красной, Sales зеленой, Assets синей и т. д.
### **Установка цвета вкладки таблицы в Microsoft Excel**
1. Щелкните правой кнопкой мыши на вкладке в листе внизу текущей таблицы.
1. Выберите **Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите **OK**.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Настройка цвета вкладки листа** с любого из указанных ниже сайтов социального программирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Дополнительные сведения см. в разделе [Настройка цвета вкладки листа](/cells/ru/net/set-worksheet-tab-color/).

{{% /alert %}}
