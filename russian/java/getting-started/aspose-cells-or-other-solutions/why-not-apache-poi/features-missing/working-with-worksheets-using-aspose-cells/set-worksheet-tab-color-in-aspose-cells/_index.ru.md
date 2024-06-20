---
title: Настройка цвета вкладки листа в Aspose.Cells
type: docs
weight: 90
url: /ru/java/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Настройка цвета вкладки листа**
Aspose.Cells позволяет изменять цвет отдельных вкладок таблицы, чтобы выделить их из остальных. Например, вы можете сделать вкладку Expenses красной, Sales зеленой, Assets синей и т. д.
#### **Установка цвета вкладки таблицы в Microsoft Excel**
1. Щелкните правой кнопкой мыши на вкладке в листе внизу текущей таблицы.
1. Выберите **Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите **OK**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите страницу [Установить цвет вкладки таблицы](/java/set-worksheet-tab-color).

{{% /alert %}}
