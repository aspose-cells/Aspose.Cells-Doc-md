---
title: Показать и скрыть рабочие листы и вкладки
type: docs
weight: 10
url: /ru/net/show-and-hide-worksheets-and-tabs/
---
{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю отображать и скрывать элементы книги, включая рабочие листы и вкладки.

{{% /alert %}}

## **Показать и скрыть рабочий лист**

 Файл Excel может иметь один или несколько рабочих листов. Всякий раз, когда мы создаем файл Excel, мы добавляем рабочие листы в файл Excel, в котором мы работаем. Каждый рабочий лист в файле Excel независим от другого рабочего листа, поскольку имеет свои собственные данные, настройки форматирования и т. д. Иногда разработчикам может потребоваться сделать несколько рабочих листов скрытыми, а другие видимыми в файле Excel для их собственных интересов. Так,**Aspose.Cells** позволяет разработчикам контролировать видимость рабочих листов в своих файлах Excel.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel.

 Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)Класс предоставляет широкий спектр свойств и методов для управления рабочими листами. Чтобы управлять видимостью рабочего листа, используйте[**Видимый**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) собственность[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Видимый**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ** ценность.

### **Делаем рабочий лист видимым**

 Сделайте рабочий лист видимым, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Видимый**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) собственность на**истинный**

### **Скрытие рабочего листа**

 Скройте рабочий лист, установив[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс'[**Видимый**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) собственность на**ЛОЖЬ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Показать и скрыть вкладки**

Если вы внимательно посмотрите в конец файла Excel Microsoft, вы увидите ряд элементов управления. Это включает:

- Вкладки листа.
- Кнопки прокрутки вкладок.

Вкладки листов представляют рабочие листы в файле Excel. Щелкните любую вкладку, чтобы переключиться на этот рабочий лист. Чем больше рабочих листов в рабочей книге, тем больше вкладок листов. Если в файле Excel много рабочих листов, вам нужны кнопки для навигации по ним. Итак, Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки вкладок листа.

Используя Aspose.Cells, разработчики могут контролировать видимость вкладок листа и кнопок прокрутки вкладок в файлах Excel.

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Класс предоставляет широкий спектр свойств и методов для управления файлом Excel. Чтобы контролировать видимость вкладок в файле Excel, разработчики могут использовать[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) имущество.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) является логическим свойством, что означает, что оно может хранить только**истинный** или же**ЛОЖЬ** ценность.

### **Делаем вкладки видимыми**

 Сделайте вкладки видимыми с помощью[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) собственность на**истинный**.

### **Скрытие вкладок**

 Скрыть вкладки в файле Excel, установив[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) учебный класс'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)свойство в false.

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки рабочей книги скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Управление шириной панели вкладок**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
