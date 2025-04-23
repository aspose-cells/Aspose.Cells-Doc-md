---
title: Настройка полей
type: docs
weight: 20
url: /ru/net/setting-margins/
description: В этой статье вы узнаете, как установить поля на листе Excel с использованием образца кода. Вы также узнаете, как программно установить поля для центрирования страницы, а также верхний и нижний колонтитулы параметров страницы с помощью API C# или .NET Library.
keywords: установить поля листа Excel по центру c#, установить верхний и нижний колонтитул листа c#
---

{{% alert color="primary" %}}

Aspose.Cells полностью поддерживает параметры настройки страниц Microsoft Excel. Разработчики могут настраивать параметры страницы для листов, чтобы контролировать процесс печати. В данном разделе рассматривается, как использовать Aspose.Cells для настройки полей страницы.

{{% /alert %}}

## **Установка полей**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), обеспечивающую доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет свойство [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), используемое для установки параметров настройки страницы для листа. Атрибут [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) является объектом класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), который позволяет разработчикам устанавливать различные параметры макета страницы для печатного листа. Класс [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) предоставляет различные свойства и методы, используемые для установки параметров настройки страницы.

### **Поля страницы**

Установите поля страницы (слева, справа, сверху, снизу), используя элементы класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). Ниже приведены несколько методов, используемых для указания полей страницы:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Центрирование на странице**

Можно центрировать что-либо на странице горизонтально и вертикально. Для этого есть несколько полезных элементов класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) и [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Поля верхнего и нижнего колонтитулов**

Установите поля верхнего и нижнего колонтитулов с помощью элементов класса [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), таких как [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) и [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
{{< app/cells/assistant language="csharp" >}}
