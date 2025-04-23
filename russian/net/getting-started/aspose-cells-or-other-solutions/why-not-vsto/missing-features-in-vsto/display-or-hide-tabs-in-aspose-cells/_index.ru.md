---
title: Показ или Скрытие Вкладок в Aspose.Cells
type: docs
weight: 80
url: /ru/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

**Вкладки листов и кнопки прокрутки вкладок** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel. 

{{% /alert %}} 

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл с именем output.xls.

Вы можете увидеть, что файл Book1.xls содержит вкладки на рисунке ниже. После выполнения примерного кода вкладки скрыты, как видно на скриншоте файла output.xls ниже.

**book1.xls: Файл Excel перед любыми модификациями** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Файл Excel после изменений** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Управление Шириной Панели Вкладок**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
