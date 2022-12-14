---
title: Показать или скрыть вкладки в Aspose.Cells
type: docs
weight: 80
url: /ru/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Если вы внимательно посмотрите в конец файла Excel Microsoft, вы увидите ряд элементов управления. Это включает:

- Вкладки листа.
- Кнопки прокрутки вкладок.

Вкладки листов представляют рабочие листы в файле Excel. Щелкните любую вкладку, чтобы переключиться на этот рабочий лист. Чем больше рабочих листов в рабочей книге, тем больше вкладок листов. Если в файле Excel много рабочих листов, вам нужны кнопки для навигации по ним. Итак, Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки вкладок листа.

**Вкладки листов и кнопки прокрутки вкладок** 

![дело:изображение_альтернативный_текст](display-or-hide-tabs-in-aspose-cells_1.png)

Используя Aspose.Cells, разработчики могут контролировать видимость вкладок листа и кнопок прокрутки вкладок в файлах Excel.

{{% /alert %}} 

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls.

Вы можете видеть, что файл Book1.xls содержит вкладки на рисунке ниже. После выполнения кода примера вкладки скрыты, как видно из скриншота файла output.xls ниже.

**book1.xls: файл Excel до каких-либо изменений** 

![дело:изображение_альтернативный_текст](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: файл Excel после модификации** 

![дело:изображение_альтернативный_текст](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Управление шириной панели вкладок**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
