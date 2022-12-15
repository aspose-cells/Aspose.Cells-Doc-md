---
title: Настройка параметров печати
type: docs
weight: 40
url: /ru/net/setting-print-options/
---
{{% alert color="primary" %}}

Microsoft Параметры настройки страницы Excel предоставляют несколько параметров печати (также называемых параметрами листа), которые позволяют пользователям управлять печатью страниц рабочего листа.

{{% /alert %}}

## **Настройка параметров печати**

Эти параметры печати позволяют пользователям:

- Выберите определенную область печати на листе.
- Печатайте заголовки.
- Распечатайте линии сетки.
- Печатать заголовки строк/столбцов.
- Добейтесь чернового качества.
- Печать комментариев.
- Вывести ошибки ячеек.
- Определите порядок страниц.

 Aspose.Cells поддерживает все параметры печати, предлагаемые Microsoft Excel, и разработчики могут легко настроить эти параметры для рабочих листов, используя свойства, предлагаемые[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)учебный класс. Использование этих свойств обсуждается ниже более подробно.

### **Установить область печати**

По умолчанию область печати включает все области рабочего листа, содержащие данные. Разработчики могут установить определенную область печати рабочего листа.

 Чтобы выбрать конкретную область печати, используйте кнопку[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) учебный класс'[**Область печати**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printarea)имущество. Назначьте этому свойству диапазон ячеек, определяющий область печати.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintArea-1.cs" >}}

### **Установить заголовки для печати**

 Aspose.Cells позволяет указать, что заголовки строк и столбцов будут повторяться на всех страницах печатного листа. Для этого используйте[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) учебный класс'[**PrintTitleColumns**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlecolumns) а также[**PrintTitleRows**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printtitlerows)характеристики.

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строк или столбцов. Например, строки определяются как $1:$2, а столбцы — как $A:$B.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintTitle-1.cs" >}}

### **Установите другие параметры печати**

[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class также предоставляет несколько других свойств для установки общих параметров печати следующим образом:

- [**ПринтСетка**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printgridlines)логическое свойство, определяющее, печатать линии сетки или нет.
- [**Печать заголовков**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printheadings): логическое свойство, определяющее, печатать заголовки строк и столбцов или нет.
- [**Черное и белое**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/blackandwhite): логическое свойство, определяющее, следует ли печатать рабочий лист в черно-белом режиме или нет.
- [**ПечатьКомментарии**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments): определяет, отображать ли комментарии печати на рабочем листе или в конце рабочего листа.
- [**ПечатьЧерновик**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printdraft): логическое свойство, определяющее, следует ли печатать лист без графики.
- [**Ошибки печати**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors): определяет, следует ли печатать ошибки ячеек как отображаемые, пустые, тире или Н/Д.

 Чтобы установить[**ПечатьКомментарии**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) а также[**Ошибки печати**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors) properties, Aspose.Cells также предоставляет два перечисления,[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype) , а также[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype) которые содержат предварительно определенные значения, которые должны быть присвоены[**ПечатьКомментарии**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printcomments) а также[**Ошибки печати**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printerrors)свойства соответственно.

 Предустановленные значения в[**PrintCommentsType**](https://reference.aspose.com/cells/net/aspose.cells/printcommentstype)перечислены ниже с их описанием.

|**Печать типов комментариев**|**Описание**|
|:- |:- |
|Печать на месте|Задает печать комментариев в том виде, в котором они отображаются на листе.|
|ПечатьБезКомментариев|Указывает, что комментарии не следует печатать.|
|ПринтлистЭнд|Указывает, что комментарии следует печатать в конце рабочего листа.|

 Предустановленные значения[**PrintErrorsType**](https://reference.aspose.com/cells/net/aspose.cells/printerrorstype)перечислены ниже с их описанием.



|**Типы ошибок печати**|**Описание**|
|:- |:- |
|PrintErrorsBlank|Указывает не печатать ошибки.|
|Принтеррорсдэш|Указывает печатать ошибки как "--".|
|PrintErrorsDisplayed|Задает печать ошибок в том виде, в котором они отображаются.|
|PrintErrorsNA|Указывает печатать ошибки как "#N/A".|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-OtherPrintOptions-1.cs" >}}

### **Установить порядок страниц**

[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) класс обеспечивает[**Заказ**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/order)свойство, которое используется для заказа печати нескольких страниц рабочего листа. Есть две возможности упорядочить страницы следующим образом.

- **Вниз, затем вверх:** печатает все страницы вниз перед печатью любых страниц справа.
- **Затем вниз:** печатает страницы слева направо перед печатью страниц ниже.

 Aspose.Cells предоставляет перечисление,[**ПринтОрдерТип**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)который содержит все предопределенные типы заказов.

 Предустановленные значения[**ПринтОрдерТип**](https://reference.aspose.com/cells/net/aspose.cells/printordertype)перечисление приведено ниже.

|**Типы заказов на печать**|**Описание**|
|:- |:- |
|ВнизЗатемОвер|Представляет порядок печати как вниз, так и вверх.|
|OverThenDown|Представляет порядок печати сверху вниз.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPageOrder-1.cs" >}}
