---
title: Добавление листов
type: docs
weight: 20
url: /ru/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: В данной статье описывается добавление листа (GridWorksheet) в GridWeb.
---

{{% alert color="primary" %}} 

Рабочие листы являются неотъемлемой частью Aspose.Cells.GridWeb. Вся информация управляется и хранится в виде рабочих листов. Aspose.Cells.GridWeb позволяет разработчикам добавлять один или несколько рабочих листов к элементу управления Aspose.Cells.GridWeb. В этой теме показаны простые подходы к добавлению рабочих листов в Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Добавление рабочего листа**
### **Без указания имени листа**
Самым простым способом добавления рабочего листа в Aspose.Cells.GridWeb является вызов метода Add коллекции GridWorksheetCollection в элементе управления GridWeb. Это создает рабочие листы с использованием имён по умолчанию (например, Лист1, Лист2, Лист3 и так далее) и добавляет их в элемент управления GridWeb.

**Результат: в элемент GridWeb добавлен рабочий лист с именем по умолчанию** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

Метод Add возвращает индекс нового рабочего листа, который можно использовать для доступа к экземпляру этого рабочего листа. Для получения более подробной информации о том, как получить доступ к рабочим листам, см. [Доступ к рабочим листам](/cells/ru/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **С указанным именем листа**
Для добавления рабочего листа с определенным именем в элемент управления GridWeb вместо использования схемы именования по умолчанию вызовите перегруженную версию метода Add, которая принимает указанное SheetName. Например, ниже приведен пример добавления рабочего листа с именем 'Счет'.

**Вывод: в GridWeb добавлен рабочий лист с указанным именем** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

Метод Add, принимающий имя рабочего листа в виде строки, возвращает экземпляр GridWorksheet.

{{% /alert %}}
