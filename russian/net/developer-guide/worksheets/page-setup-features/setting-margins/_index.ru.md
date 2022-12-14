---
title: Настройка полей
type: docs
weight: 20
url: /ru/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells полностью поддерживает параметры настройки страницы Microsoft Excel. Разработчикам может потребоваться настроить параметры страницы для рабочих листов, чтобы контролировать процесс печати. В этом разделе обсуждается, как использовать Aspose.Cells для настройки полей страницы.

{{% /alert %}}

## **Настройка полей**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , который представляет файл Excel.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)учебный класс.

[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)класс обеспечивает[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) свойство, используемое для установки параметров настройки страницы для рабочего листа.[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) атрибут является объектом[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) класс, который позволяет разработчикам устанавливать различные параметры макета страницы для печатного листа.[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)Класс предоставляет различные свойства и методы, используемые для установки параметров настройки страницы.

### **Поля страницы**

 Установите поля страницы (слева, справа, сверху, снизу) с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)члены класса. Ниже перечислены несколько методов, которые используются для указания полей страницы:

- [**Левое поле**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Правое поле**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Верхнее поле**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Нижнее поле**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Центрировать на странице**

Можно центрировать что-то на странице по горизонтали и по вертикали. Для этого есть несколько полезных членов[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) учебный класс,[**ЦентрГоризонтально**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) а также[**ЦентрВертикально**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Поля верхнего и нижнего колонтитула**

 Установите поля верхнего и нижнего колонтитула с помощью[**Настройка страницы**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) члены класса, такие как[**ЗаголовокМаргин**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) а также[**Нижний колонтитул**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
