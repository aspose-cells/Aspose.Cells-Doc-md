# C++ библиотека для форматов файлов Excel

![Версия 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![баннер](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Страница продукта](https://products.aspose.com/cells/cpp/) | [Документация](https://docs.aspose.com/cells/cpp/) | [Демо](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Примеры](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Блог](https://blog.aspose.com/category/cells/) | [Релизы](https://releases.aspose.com/cells/cpp/) | [Бесплатная поддержка](https://forum.aspose.com/c/cells) | [Временная лицензия](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) - это нативная библиотека C++, предназначенная для создания, обработки, обработки и преобразования файлов Microsoft Excel? без необходимости использования Microsoft Office? или Automation. 

Он позволяет разработчикам работать со строками, столбцами таблицы, данными, формулами, сводными таблицами, рабочими листами, таблицами, диаграммами и объектами рисования из своих собственных приложений C++.

## Что такое Aspose.Cells for C++?

Aspose.Cells for C++ - это нативный API C++ для интеграции функций создания, обработки и преобразования электронных таблиц в ваши приложения C++. Он поддерживает работу с многими популярными форматами файлов электронных таблиц из Microsoft Excel (XLS, XLSX, XLSB, CSV и др.) и OpenOffice/LibreOffice (ODS).

Вы можете использовать Aspose.Cells for C++ для разработки 64-разрядных приложений в любой среде разработки, поддерживающей C++, такой как Microsoft Visual Studio. Aspose.Cells for C++ является нативной сборкой, которую можно развернуть, просто скопировав ее. Вам не нужно беспокоиться о других службах или модулях.

Aspose.Cells for C++ позволяет работать со встроенными и настраиваемыми свойствами документов в Microsoft Excel. Поддерживает качественное преобразование книг Excel в файлы, соответствующие стандарту PDF/A. Работайте с формулами, сводными таблицами, рабочими листами, таблицами, диапазонами, диаграммами, объектами OLE и многое другое.

## Особенности обработки файлов Excel

- Открывайте файл электронной таблицы без участия Microsoft Excel.
- [Открывайте файл Excel](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) через путь на локальном компьютере или с помощью потока.
- [Конвертировать рабочий лист](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) в различные форматы изображений.
- [Применить условное форматирование](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) по вашему выбору.
- [Управлять сводными таблицами](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) в ваших электронных таблицах.
- [Преобразовать таблицу в диапазон](https://docs.aspose.com/cells/cpp/tables-and-ranges/) без потери форматирования.
- Получить имя ячейки, указав индекс строки и столбца, а также [получить индекс строки и столбца ячейки](https://docs.aspose.com/cells/cpp/names-and-indices/) по ее имени.
- Создать [пирамидальную диаграмму, линейную диаграмму, пузырьковую диаграмму](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/) или пользовательскую диаграмму.
- [Отрисовать](https://docs.aspose.com/cells/cpp/chart-rendering/) поддерживаемые типы диаграмм в изображения или PDF.
- [Вставить объект OLE в рабочий лист](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Получить доступ ко всем объектам OLE, содержащимся в рабочем листе, для [извлечения](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Поддерживаемые форматы чтения и записи

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Другие:** HTML, MHTML

## Сохранить документы электронных таблиц

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Portable Document Format:** PDF, XPS
**Text:** CSV, TSV, TabDelimited\
**Изображения:** SVG, JPEG, PNG, BMP, GIF
**Web:** HTML, MHTML\
**Метафайл:** EMF\
**Другое** DIF

## Начало работы

Вы готовы попробовать Aspose.Cells for C++? Просто выполните `Install-Package Aspose.Cells.Cpp` из консоли менеджера пакетов в Visual Studio, чтобы получить пакет NuGet. Если у вас уже есть Aspose.Cells for C++ и вы хотите обновить версию, выполните `Update-Package Aspose.Cells.Cpp`, чтобы получить последнюю версию.

### Конвертация XLS в XLSX, XLSB & CSV с помощью C++

Попробуйте выполнить нижеприведенный отрывок кода, чтобы увидеть, как работает API в вашей среде, или проверьте [Репозиторий GitHub](https://github.com/aspose-cells/Aspose.Cells-for-C) для других типичных сценариев использования.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Создание пользовательской диаграммы Excel с помощью C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Страница продукта](https://products.aspose.com/cells/cpp/) | [Документация](https://docs.aspose.com/cells/cpp/) | [Демо](https://products.aspose.app/cells/family) | [API Reference](https://reference.aspose.com/cells/cpp) | [Примеры](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Блог](https://blog.aspose.com/category/cells/) | [Релизы](https://releases.aspose.com/cells/cpp/) | [Бесплатная поддержка](https://forum.aspose.com/c/cells) | [Временная лицензия](https://purchase.aspose.com/temporary-license/)
