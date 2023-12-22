---
title: Получить и установить стиль для ячеек
description: Узнайте, как форматировать и стилизовать данные в Aspose.Cells for .NET, включая форматирование текста, форматирование чисел, форматирование даты и другие параметры стилизации. Наше руководство поможет вам создать профессионально выглядящие таблицы с привлекательным форматированием.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Стили
type: docs
weight: 50
url: /ru/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET В версии 4.4.2 представлены два новых метода форматирования ячеек: Cell.GetStyle и Cell.SetStyle. В этой статье рассматривается подход Cell.GetStyle/SetStyle, который поможет вам решить, какой метод подходит вам лучше всего.

{{% /alert %}} 
##  **Форматирование Cells**
Существует два способа форматирования ячейки, как показано ниже.
###  **Использование GetStyle()**
С помощью следующего фрагмента кода объект Style инициируется для каждой ячейки при ее форматировании. Если форматируется много ячеек, потребляется большой объем памяти, поскольку объект Style является большим объектом. Эти объекты Style не будут освобождены до тех пор, пока не будет вызван метод Workbook.Save.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **Использование SetStyle()**
Первый подход прост и понятен, так почему же мы добавили второй подход?

Мы добавили второй подход для оптимизации использования памяти. После использования метода Cell.GetStyle для получения объекта Style измените его и используйте метод Cell.SetStyle, чтобы вернуть его в эту ячейку. Этот объект Style не будет сохранен, и .NET GC соберет его, если на него нет ссылки.

При вызове метода Cell.SetStyle объект Style не сохраняется для каждой ячейки. Вместо этого мы сравниваем этот объект Style с внутренним пулом объектов Style, чтобы увидеть, можно ли его повторно использовать. Для каждого объекта Workbook сохраняются только объекты Style, отличающиеся от существующих. Это означает, что для каждого файла Excel существует всего несколько сотен объектов Style, а не тысячи. Для каждой ячейки сохраняется только индекс пула объектов Style.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **Предварительные темы**
- [Создайте объект Style, используя класс CellsFactory.](/cells/ru/net/create-style-object-using-cellsfactory-class/)
- [Изменить существующий стиль](/cells/ru/net/modify-an-existing-style/)
- [Повторное использование объектов стиля](/cells/ru/net/reusing-style-objects/)
- [Использование встроенных стилей](/cells/ru/net/using-built-in-styles/)


