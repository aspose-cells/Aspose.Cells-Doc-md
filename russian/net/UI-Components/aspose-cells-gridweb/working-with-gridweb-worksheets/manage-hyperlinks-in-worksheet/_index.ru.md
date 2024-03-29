﻿---
title: Управление гиперссылками на листе
type: docs
weight: 100
url: /ru/net/manage-hyperlinks-in-worksheet/
---
{{% alert color="primary" %}} 

В этом разделе обсуждается, какие типы гиперссылок поддерживаются в Aspose.Cells.GridWeb и как управлять ими программно. Гиперссылки можно использовать либо для создания ссылок на веб-URL-адреса, либо для выполнения обратной передачи на сервер.

{{% /alert %}} 
## **Работа с гиперссылками**
### **Типы гиперссылок**
Как правило, Aspose.Cells.GridWeb поддерживает следующие гиперссылки:

- [URL-гиперссылки](/cells/ru/net/manage-hyperlinks-in-worksheet/), гиперссылки, которые могут быть связаны с веб-URL.
- [Текстовые гиперссылки](/cells/ru/net/manage-hyperlinks-in-worksheet/), гиперссылки URL применяются к тексту.
- [Гиперссылки на изображения](/cells/ru/net/manage-hyperlinks-in-worksheet/), гиперссылки URL применяются к изображениям.
- [Cell командные гиперссылки](/cells/ru/net/manage-hyperlinks-in-worksheet/), гиперссылки, которые отправляют данные на сервер. Такие гиперссылки больше похожи на кнопку, которая при нажатии запускает событие на стороне сервера.

В следующих разделах подробно описывается использование всех типов гиперссылок. Также обсуждается, как получить доступ или удалить ссылки.
### **Добавление гиперссылок**

#### **URL гиперссылки**
Гиперссылки URL больше похожи на простые гиперссылки, которые вы обычно видите на веб-сайтах. Гиперссылка URL работает как якорь в ячейке. Всякий раз, когда на него нажимают, он переходит на веб-страницу или открывает новое окно браузера.

Существуют различные типы URL-гиперссылок:

- Текстовые гиперссылки.
- Гиперссылки на изображения.

Разработчики могут указать изображение для гиперссылки. Если изображение не указано, создается текстовая гиперссылка; в противном случае создается гиперссылка на изображение.


##### **Текстовые гиперссылки**
Чтобы добавить текстовую гиперссылку на лист:

1. Добавьте элемент управления Aspose.Cells.GridWeb в свою веб-форму.
1. Доступ к рабочему листу.
1. Добавьте гиперссылку в ячейку на листе.
1. Установите текст, который будет отображаться в ячейке.
1. Установите URL-адрес гиперссылки.
1. Установите цель гиперссылки, если это необходимо.
1. При желании установите подсказку инструмента.

{{% alert color="primary" %}} 

 ПРИМЕЧАНИЕ. Цель гиперссылки может быть установлена на_ себя,_top или _parent для открытия URL-адресов в новом, текущем или верхнем окне соответственно.

{{% /alert %}} 

В приведенном ниже примере на рабочий лист добавляются две гиперссылки. У одного нет цели, а для другого установлено значение _parent.

**Вывод: текстовые гиперссылки добавлены на лист.** 

![дело:изображение_альтернативный_текст](manage-hyperlinks-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddTextHyperlinks.cs" >}}


##### **Гиперссылки изображений**
Чтобы добавить гиперссылку на изображение:

1. Добавьте элемент управления Aspose.Cells.GridWeb в свою веб-форму.
1. Доступ к рабочему листу.
1. Добавьте гиперссылку в ячейку.
1. Установите URL-адрес изображения, которое будет отображаться в виде гиперссылки.
1. Установите URL-адрес гиперссылки.
1. При желании установите подсказку инструмента.
1. При необходимости задайте текст гиперссылки.

**Вывод: гиперссылки изображений добавлены на лист.** 

![дело:изображение_альтернативный_текст](manage-hyperlinks-in-worksheet_2.png)

{{% alert color="primary" %}} 

 Установка AltText гиперссылки изображения выполняет ту же функцию, что и установка<ALT> тег в HTML. Текст отображается только в том случае, если гиперссылка на изображение не отображается. (Например, если изображение не находится в указанном месте.) Если изображение второй гиперссылки не найдено, вывод приведенного ниже фрагмента кода будет выглядеть следующим образом.

**Не удалось найти изображение для URL-адреса изображения** 

![дело:изображение_альтернативный_текст](manage-hyperlinks-in-worksheet_3.png)

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddImageHyperlinks.cs" >}}


#### **Cell Командные гиперссылки**
Гиперссылка команды ячейки — это особый тип гиперссылки, которая запускает событие на стороне сервера вместо открытия веб-страницы. Разработчики могут добавлять код к событию на стороне сервера и выполнять любую задачу при нажатии на гиперссылку. Эта функция позволяет разработчикам создавать более интерактивные приложения.

Чтобы добавить гиперссылку команды ячейки:

1. Добавьте элемент управления Aspose.Cells.GridWeb в свою веб-форму.
1. Доступ к рабочему листу.
1. Добавьте гиперссылку в ячейку.
1. Задайте для команды гиперссылки любое желаемое значение.
 Значение используется обработчиком событий гиперссылки для его распознавания.
1. При желании установите подсказку инструмента.
1. Установите URL-адрес изображения, которое будет отображаться в виде гиперссылки.

**На рабочий лист добавлена гиперссылка команды ячейки.** 

![дело:изображение_альтернативный_текст](manage-hyperlinks-in-worksheet_4.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-AddCellCommandHyperlinks.cs" >}}
##### **Обработка событий командных гиперссылок Cell**
Разработчикам необходимо создать обработчик событий для события CellCommand элемента управления GridWeb, чтобы выполнять определенные задачи при щелчке гиперссылки на конкретную команду ячейки. Обработчик событий CellCommand предоставляет объект типа CellEventArgs, который предлагает свойство Argument. Используйте свойство Argument, чтобы определить конкретную гиперссылку, сравнив ее значение CellCommand.

В приведенном ниже примере создается обработчик событий для гиперссылки команды ячейки, созданной в приведенном выше коде. CellCommand гиперссылки был установлен на Click. Итак, в обработчике события сначала проверьте его, а затем добавьте код, который отображает сообщение в ячейке A6.

Обработчик событий вызывается при нажатии гиперссылки.

**Вывод: текст добавляется в ячейку A6 при нажатии на гиперссылку** 

![дело:изображение_альтернативный_текст](manage-hyperlinks-in-worksheet_5.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddHyperlinks.aspx-HandleCellCommandHyperlinkEvent.cs" >}}
### **Доступ к гиперссылкам**
Чтобы получить доступ к существующей гиперссылке:

1. Получите доступ к ячейке, которая его содержит.
1. Получить ссылку на ячейку.
1. Передайте ссылку в метод GetHyperlink коллекции Hyperlinks, чтобы получить доступ к гиперссылке.
1. Измените свойства гиперссылки.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-AccessHyperlinks.cs" >}}
### **Удаление гиперссылок**
Чтобы удалить гиперссылку:

1. Доступ к активному рабочему листу.
1. Удалите гиперссылку с помощью метода Remove коллекции Hyperlinks.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageHyperlinks.aspx-RemoveHyperlink.cs" >}}
