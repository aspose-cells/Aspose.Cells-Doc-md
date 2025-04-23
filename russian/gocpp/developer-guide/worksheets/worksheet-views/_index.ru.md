---
title: Представления листа
type: docs
weight: 40
url: /ru/go-cpp/worksheet-views/
---

## **Предпросмотр разрывов страниц**

Все листы могут быть просмотрены в двух режимах:

- Обычный вид.
- Предварительный просмотр разрыва страницы.

Обычный вид является видом рабочего листа по умолчанию. Предварительный просмотр разрывов страниц - это режим редактирования, который отображает рабочий лист так, как он будет отпечатан. Предварительный просмотр разрывов страниц показывает, какие данные будут на каждой странице, чтобы можно было настроить область печати и разрывы страниц. С помощью Aspose.Cells разработчики могут включать обычный вид или режим предварительного просмотра разрывов страниц.

### **Управление режимами просмотра**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получать доступ к каждому листу в файле.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) содержит широкий набор методов для управления листами. Чтобы включить нормальный или режим предварительного просмотра разрывов страниц, используйте метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) возвращает булево значение, которое означает, что оно может принимать только значение **true** или **false**.

#### **Включение нормального режима**

Установите обычный вид листа, вызвав метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) и присвоив значение **false**.

#### **Включение предварительного просмотра разрывов страниц**

Установите любой лист в режим предварительного просмотра разрывов страниц, вызвав метод [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) и присвоив значение **true**. Это переключит лист из обычного режима в режим предварительного просмотра разрывов страниц.

Ниже приведен полный пример использования метода [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/), который включает режим предварительного просмотра разрывов страниц для первого листа файла Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Коэффициент масштабирования**

### **Использование Microsoft Excel**

Microsoft Excel предоставляет возможность установить коэффициент масштабирования листа. Эта функция помогает пользователям просматривать содержимое листа в уменьшенном или увеличенном виде. Пользователи могут установить коэффициент масштабирования на любое значение.

### **Aspose.Cells и коэффициент увеличения**

Aspose.Cells также позволяет разработчикам устанавливать масштаб листа. Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получать доступ к каждому листу файла.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) предоставляет широкий набор методов для управления листами. Для установки масштаба листа используйте метод [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Масштаб устанавливается путем присвоения числового (целого) значения методу [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

Ниже приведен полный пример использования метода [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/), показывающий, как установить масштаб первого листа файла Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Закрепить области**

### **Использование Microsoft Excel**

Закрепление области экрана - это функция, предоставляемая Microsoft Excel. Закрепление области экрана позволяет выбрать данные, которые останутся видимыми при прокрутке на листе.

### **Aspose.Cells и заморозка панелей**

Aspose.Cells также позволяет разработчикам применять закрепление панелей к листам во время выполнения. Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получать доступ к каждому листу файла.

Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) предоставляет широкий набор методов для управления листами. Для настройки закрепления панелей вызовите метод [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Метод [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) принимает следующие параметры:

- **Строка**, индекс строки, с которой начнется закрепление.
- **Столбец**, индекс столбца, с которого начнется закрепление.
- **Закрепленные строки**, количество видимых строк в верхней панели.
- **Закрепленные столбцы**, количество видимых столбцов в левой панели.

Ниже приведен полный пример, показывающий, как использовать метод [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) для закрепления строк и столбцов (начиная с C4, что соответствует 4-й строке и 3-му столбцу, нумерация начинается с 0) первого листа файла Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Разделение областей экрана**

Если вам нужно разделить экран для получения двух разных представлений на одном листе, используйте разделение областей экрана. Microsoft Excel предлагает очень удобную функцию, которая позволяет просматривать более одной копии вашего листа и прокручивать каждую область листа независимо: разделение областей экрана.

Разделы работают одновременно. Если вы внесете изменение в один, изменение одновременно появится в другом. Aspose.Cells предоставляет функцию разделения панелей для пользователей.

### **Применение и удаление разделенных панелей**

#### **Разделение панелей**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) предоставляет широкий спектр методов для управления файлом Excel. Для реализации разделенных видов используйте метод [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) класса [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Чтобы удалить разделенные панели, используйте метод [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

В примере мы используем простой шаблонный файл, который загружается, затем устанавливается функция разделенных панелей для ячейки на первом листе. Обновленный файл сохраняется.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Удаление панелей**

Удаление разделенных панелей с помощью метода [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
