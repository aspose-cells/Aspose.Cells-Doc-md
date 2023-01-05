---
title: Установить цвет вкладки рабочего листа в xlsx4j
type: docs
weight: 60
url: /ru/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - Установить цвет вкладки рабочего листа**
Aspose.Cells позволяет изменить цвет отдельных вкладок рабочего листа, чтобы они выделялись среди остальных. Например, вы можете сделать «Расходы» красным, «Продажи» — зеленым, «Активы» — синим и т. д.
### **Настройка цвета вкладки рабочего листа с помощью Microsoft Excel**
1. Щелкните правой кнопкой мыши вкладку на вкладке в нижней части текущего рабочего листа.
1. Выбирать**Цвет вкладки**.
1. Выберите цвет из палитры.
1. Нажмите**ХОРОШО**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Установить цвет вкладки рабочего листа](/java/set-worksheet-tab-color).

{{% /alert %}}
