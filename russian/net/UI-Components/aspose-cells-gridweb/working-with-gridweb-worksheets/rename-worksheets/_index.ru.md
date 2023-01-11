﻿---
title: Переименовать рабочие листы
type: docs
weight: 40
url: /ru/net/rename-worksheets/
---
{{% alert color="primary" %}} 

Переименование рабочего листа может быть очень полезным при работе с большим количеством рабочих листов в Aspose.Cells.GridWeb и решении изменить их имена, чтобы сделать их более значимыми. Например, рабочий лист, содержащий счет-фактуру, можно переименовать в «Счет-фактура» вместо «Лист1». В этом разделе описывается эта простая, но полезная функция.

{{% /alert %}} 
## **Переименование рабочего листа**
Все рабочие листы содержат свойство Name, которое позволяет разработчикам получать доступ к именам рабочих листов или изменять их. Чтобы переименовать рабочий лист:

1. Получите доступ к рабочему листу из коллекции GridWorksheetCollection.
1. Переименуйте выбранный рабочий лист.



{{% alert color="primary" %}} 

 Дополнительные сведения о том, как получить доступ к рабочим листам в Aspose.Cells.GridWeb, см.[Доступ к рабочим листам](/cells/ru/net/access-worksheets/).

{{% /alert %}} 

Перед выполнением кода рабочему листу присваивается имя по умолчанию, например Sheet1.

**Входной файл: рабочий лист с именем по умолчанию Sheet1** 

![дело:изображение_альтернативный_текст](rename-worksheets_1.png)

После запуска кода рабочий лист переименовывается в Student.

**Вывод: рабочий лист переименован в «Студенты».** 

![дело:изображение_альтернативный_текст](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}