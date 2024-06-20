---
title: Добавить ячейку с формулами
type: docs
weight: 30
url: /ru/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb, формула
description: В этой статье описано, как добавить формулу в ячейку сетки GridWeb.
---

{{% alert color="primary" %}} 

Самая ценная функция, предлагаемая Aspose.Cells.GridWeb, - это поддержка формул или функций. У Aspose.Cells.GridWeb есть свой собственный Движок формул, который вычисляет формулы в рабочих книгах. Aspose.Cells.GridWeb поддерживает как встроенные, так и определяемые пользователем функции или формулы. В этой теме подробно рассматривается добавление формул в ячейки с использованием API Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Добавление формул в ячейки**
### **Как добавить и вычислить формулу?**
Можно добавлять, получать доступ и изменять формулы в ячейках, используя свойство Formula ячейки. Aspose.Cells.GridWeb поддерживает пользовательские формулы от простых до сложных. Однако с большим количеством встроенных функций или формул (аналогично Microsoft Excel) также поставляется Aspose.Cells.GridWeb. Для просмотра полного списка встроенных функций обратитесь к этому [списку поддерживаемых функций.](/cells/ru/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

Синтаксис формулы должен быть совместим с синтаксисом Microsoft Excel. Например, все формулы должны начинаться с знака равенства (=).

Чтобы добавить формулу динамически, Aspose.Cells.GridWeb распознает ее как формулу даже если вы не используете знак **=**, но если конечные пользователи работают в графическом интерфейсе, они должны использовать знак "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Формула добавлена в ячейку B3, но не вычислена GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

На снимке экрана выше вы можете видеть, что формула была добавлена в B3, но ее еще не вычислили. Чтобы вычислить все формулы, вызовите метод CalculateFormula GridWorksheetCollection GridWeb control после добавления формул в рабочие книги, как показано ниже.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Пользователи также могут вычислять формулы, нажимая кнопку **Отправить**.

**Нажатие кнопки «Отправить» GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**ВАЖНО**: Если пользователь нажимает кнопки **Сохранить** или **Отменить**, или вкладки листов, все формулы автоматически вычисляются GridWeb.

**Результат формулы после вычисления** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Ссылка на ячейки из других рабочих книг**
С помощью Aspose.Cells.GridWeb можно ссылаться на значения, хранящиеся в разных рабочих книгах в их формулах, создавая сложные формулы.

Синтаксис для ссылки на значение ячейки из другой рабочей книги: НазваниеЛиста!ИмяЯчейки.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
