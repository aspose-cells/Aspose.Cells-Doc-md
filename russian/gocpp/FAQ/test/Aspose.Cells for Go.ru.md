# Библиотека Go для форматов файлов Excel

![Версия 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Страница продукта](https://products.aspose.com/cells/go-cpp/) | [Документация](https://docs.aspose.com/cells/go-cpp/) | [Демонстрации](https://products.aspose.app/cells/family) | [Справочник API](https://reference.aspose.com/cells/go-cpp) | [Примеры](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Блог](https://blog.aspose.com/category/cells/) | [Релизы](https://releases.aspose.com/cells/go-cpp/) | [Бесплатная поддержка](https://forum.aspose.com/c/cells) | [Временная лицензия](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) — это нативная библиотека Go для создания, обработки, преобразования и работы с файлами Microsoft Excel без необходимости наличия Microsoft Office или автоматизации. API Excel для Go поддерживает Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML и другие форматы, такие как CSV, TSV и другие.

Позволяет разработчикам работать с строками, столбцами, данными, формулами, сводными таблицами, листами, таблицами, диаграммами и объектами рисования из своих собственных приложений на Go.

## Что такое Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ — это нативный API для локальной разработки на Go, предназначенный для интеграции функций создания, редактирования и преобразования таблиц в ваши приложения на Go. Он поддерживает работу с многими популярными форматами файлов электронных таблиц от Microsoft Excel (XLS, XLSX, XLSB, CSV и др.) и OpenOffice/LibreOffice (ODS).

Вы можете использовать Aspose.Cells for Go via C++ для разработки 64-битных приложений в любой среде разработки, поддерживающей Go, например, Microsoft Visual Studio. Aspose.Cells for Go via C++ — это нативная сборка, которую можно развернуть простым копированием. Вам не нужно беспокоиться о дополнительных сервисах или модулях.

Aspose.Cells for Go via C++ позволяет работать со встроенными и пользовательскими свойствами документа в Microsoft Excel. Поддерживается высококачественное преобразование рабочих книг Excel в файлы, совместимые с PDF/A. Работайте с формулами, сводными таблицами, листами, таблицами, диапазонами, диаграммами, объектами OLE и многим другим.

## Особенности обработки файлов Excel

- Открывайте файл электронной таблицы без участия Microsoft Excel.
- [Открыть файл Excel](https://docs.aspose.com/cells/go/different-ways-to-open-files/) по пути на локальном компьютере или с помощью потока.
- [Преобразовать лист](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) в различные форматы изображений.
- [Применить условное форматирование](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) по вашему выбору.
- [Манипулировать сводными таблицами](https://docs.aspose.com/cells/go/manipulate-pivot-table/) в ваших таблицах.
- [Преобразовать таблицу в диапазон](https://docs.aspose.com/cells/go/tables-and-ranges/) без потери форматирования.
- Получить название ячейки, указав индекс строки и столбца, аналогично [получить индекс строки и столбца по названию ячейки](https://docs.aspose.com/cells/go/names-and-indices/).
- Создать [пирамидальную диаграмму, линейную диаграмму, пузырьковую диаграмму](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), или собственную диаграмму.
- [Отрисовать](https://docs.aspose.com/cells/go/chart-rendering/) поддерживаемые типы диаграмм в изображения или PDF.
- [Вставить объект OLE в лист](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Получить все OLE-объекты, содержащиеся в листе, для [извлечения](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

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

Готовы попробовать Aspose.Cells for Go via C++? Просто выполните `go get -u github.com/aspose-cells/aspose-cells-go-cpp` и импортируйте `github.com/aspose-cells/aspose-cells-go-cpp` в ваш Go-файл. Если у вас уже есть Aspose.Cells for Go via C++ и вы хотите обновить версию, выполните `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0`, чтобы получить последнюю версию.

### Конвертация XLS в XLSX, XLSB и CSV с помощью Go

Попробуйте выполнить следующий пример, чтобы увидеть, как работает API в вашей среде, или ознакомьтесь с [репозиторием GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) для других сценариев использования.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Создайте пользовательскую диаграмму Excel с помощью Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Страница продукта](https://products.aspose.com/cells/go-cpp/) | [Документация](https://docs.aspose.com/cells/go-cpp/) | [Демонстрации](https://products.aspose.app/cells/family) | [Справочник API](https://reference.aspose.com/cells/go-cpp) | [Примеры](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Блог](https://blog.aspose.com/category/cells/) | [Релизы](https://releases.aspose.com/cells/go-cpp/) | [Бесплатная поддержка](https://forum.aspose.com/c/cells) | [Временная лицензия](https://purchase.aspose.com/temporary-license/)
