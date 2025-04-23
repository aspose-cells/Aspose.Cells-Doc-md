---
title: Показывать и скрывать рабочие листы и вкладки
type: docs
weight: 10
url: /ru/net/show-and-hide-worksheets-and-tabs/
description: Эта статья предоставляет образец кода для использования API C# или .NET Library для программного отображения и скрытия рабочего листа Excel. Кроме того, как показать и скрыть вкладки книги Excel.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю показывать и скрывать элементы книги, включая рабочие листы и вкладки.

{{% /alert %}}

## **Показать и скрыть лист**

Файл Excel может содержать один или более листов. Всякий раз, когда мы создаем файл Excel, мы добавляем листы в файл Excel, в котором работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и сделать другие видимыми в файле Excel по своему усмотрению. Таким образом, **Aspose.Cells** позволяет разработчикам контролировать видимость листов в их файлах Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), которая позволяет получить доступ к каждому рабочему листу в файле Excel.

Рабочий лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления рабочими листами. Для управления видимостью рабочего листа используйте свойство [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) является логическим свойством, что означает, что оно может хранить только значение **true** или **false**.

### **Сделать лист видимым**

Сделать рабочий лист видимым, установив свойство [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в **true**

### **Скрыть лист**

Скрыть рабочий лист, установив свойство [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) в **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Показывать и скрывать вкладки**

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы контролировать видимость вкладок в файле Excel, разработчики могут использовать свойство [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) является логическим свойством, что означает, что оно может хранить только значение **true** или **false**.

### **Отображение вкладок**

Сделать вкладки видимыми с помощью свойства [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) в **true**.

### **Скрытие вкладок**

Скрыть вкладки в файле Excel, установив свойство [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) класса [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) в false.

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки книги скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Управление Шириной Панели Вкладок**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
