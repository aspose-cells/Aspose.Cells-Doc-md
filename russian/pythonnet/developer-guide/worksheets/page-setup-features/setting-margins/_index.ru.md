---
title: Настройка полей
type: docs
weight: 20
url: /ru/python-net/setting-margins/
description: В этой статье вы узнаете, как установить поля листа Excel с помощью примерного кода. Вы также узнаете, как программно установить поля для центра страницы, полей заголовка и нижнего колонтитула настроек страницы с использованием API Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, установка полей листа Excel в центре с помощью Python, установка полей заголовка и нижнего колонтитула листа с помощью Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET полностью поддерживает опции настройки страницы Microsoft Excel. Разработчикам может потребоваться настроить настройки страницы для листов, чтобы контролировать процесс печати. В этой теме рассматривается, как использовать Aspose.Cells для Python via .NET для настройки полей страниц.

{{% /alert %}}

## **Как установить поля**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет собой файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет свойство [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), используемое для установки параметров настройки страницы для листа. Атрибут [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) является объектом класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), который позволяет разработчикам устанавливать различные параметры макета страницы для печатного листа. Класс [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) предоставляет различные свойства и методы, используемые для установки параметров настройки страницы.

## **Как установить поля страницы**

Установите поля страницы (слева, справа, сверху, снизу), используя элементы класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). Ниже приведены несколько методов, используемых для указания полей страницы:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Как центрировать на странице**

Можно центрировать что-либо на странице горизонтально и вертикально. Для этого есть несколько полезных элементов класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) и [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Как установить поля верхнего и нижнего колонтитулов**

Установите поля верхнего и нижнего колонтитулов с помощью элементов класса [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), таких как [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) и [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
