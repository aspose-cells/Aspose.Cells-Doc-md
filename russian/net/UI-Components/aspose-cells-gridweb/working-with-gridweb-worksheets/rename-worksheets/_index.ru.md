---
title: Переименование листов
type: docs
weight: 40
url: /ru/net/aspose-cells-gridweb/rename-worksheet/
keywords: GridWeb,переименование,переименовать лист,переименовать GridWorksheet
description: Эта статья представляет, как переименовать лист (GridWorksheet) в GridWeb.
---

{{% alert color="primary" %}} 

Переименование листа может быть очень полезным при работе с большим количеством листов в Aspose.Cells.GridWeb и принятии решения изменить их имена, чтобы они стали более содержательными. Например, лист, содержащий счет-фактуру, может быть переименован в Invoice вместо Sheet1. В этой теме описывается этот простой, но полезный функционал.

{{% /alert %}} 
## **Переименование листа**
Все листы содержат свойство Name, которое позволяет разработчикам получать доступ к именам листов или изменять их. Чтобы переименовать лист:

1. Получите доступ к листу из коллекции GridWorksheet.
2. Переименуйте выбранный лист.



{{% alert color="primary" %}} 

Для получения более подробной информации о том, как получить доступ к листам в Aspose.Cells.GridWeb, обратитесь к [Доступ к листам](/cells/ru/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 

Перед выполнением кода у листа есть имя по умолчанию, например, Sheet1.

**Входной файл: лист с именем по умолчанию Sheet1** 

![todo:image_alt_text](rename-worksheets_1.png)

После выполнения кода лист переименован в Students.

**Результат: лист переименован в Students** 

![todo:image_alt_text](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
