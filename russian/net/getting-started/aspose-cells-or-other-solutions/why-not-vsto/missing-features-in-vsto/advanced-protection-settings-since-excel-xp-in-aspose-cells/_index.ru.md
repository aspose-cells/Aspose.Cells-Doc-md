---
title: Дополнительные параметры защиты начиная с Excel XP в Aspose.Cells
type: docs
weight: 20
url: /ru/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Удалить строки или столбцы.
- Редактируйте содержимое, объекты или сценарии.
- Отформатируйте ячейки, строки или столбцы.
- Вставьте строки, столбцы или гиперссылки.
- Выберите заблокированные или разблокированные ячейки.
- Используйте сводные таблицы и многое другое.

Aspose.Cells поддерживает все параметры расширенной защиты, предлагаемые в Excel XP или более поздних версиях.

{{% /alert %}}

## **Параметры дополнительной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть параметры защиты, доступные в Excel XP:

1.  От**Инструменты** меню, выберите**Защита** с последующим**Защитить лист**.
 Отображается диалоговое окно.

   **Диалоговое окно для отображения параметров защиты в Excel XP**

![дело:изображение_альтернативный_текст](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Разрешить или ограничить функции рабочих листов или применить пароль.

### **Параметры дополнительной защиты с использованием Aspose.Cells**

Aspose.Cells поддерживают все расширенные настройки защиты.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.

[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс обеспечивает[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)свойство, которое используется для применения этих дополнительных параметров защиты.[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) Собственность фактически является объектом[**Защита**](https://reference.aspose.com/cells/net/aspose.cells/protection) класс, который инкапсулирует несколько логических свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство дополнительных параметров защиты, поддерживаемых Excel XP и более поздних версиях.

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
