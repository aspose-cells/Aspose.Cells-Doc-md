---
title: Показывать и скрывать рабочие листы и вкладки
type: docs
weight: 10
url: /ru/python-net/show-and-hide-worksheets-and-tabs/
description: В этой статье приведен образец кода для использования API Aspose.Cells для Python via .NET для программного отображения и скрытия листа Excel. Кроме того, как показать и скрыть вкладки рабочей книги Excel.
keywords: Библиотека Python Excel, Показывает и скрывает лист Excel программно, Показывает и скрывает вкладки Python, Управление шириной панели вкладок в Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET позволяет пользователю показывать и скрывать элементы книги, включая листы и вкладки.

{{% /alert %}}

## **Показать и скрыть лист**

Файл Excel может содержать один или более одного листа. Когда мы создаем файл Excel, мы добавляем в него листы, на которых работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и оставить другие видимыми в Excel-файле по своему усмотрению. Итак, **Aspose.Cells для Python via .NET** позволяет разработчикам контролировать видимость листов в их Excel-файлах.

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получить доступ к каждому листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления рабочими листами. Для управления видимостью рабочего листа используйте свойство [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) является логическим свойством, что означает, что оно может хранить только значение **true** или **false**.

### **Сделать лист видимым**

Сделать рабочий лист видимым, установив свойство [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) в **true**

### **Скрыть лист**

Скрыть рабочий лист, установив свойство [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) в **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Показывать и скрывать вкладки**

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

Используя Aspose.Cells для Python via .NET, разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в Excel-файлах.

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы контролировать видимость вкладок в Excel-файле, разработчики могут использовать свойство [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) является логическим свойством, что означает, что в нем можно хранить только значение **true** или **false**.

### **Отображение вкладок**

Сделать вкладки видимыми с помощью свойства [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) в **true**.

### **Скрытие вкладок**

Скрыть вкладки в файле Excel, установив свойство [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) в false.

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки книги скрыты.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Управление Шириной Панели Вкладок**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
