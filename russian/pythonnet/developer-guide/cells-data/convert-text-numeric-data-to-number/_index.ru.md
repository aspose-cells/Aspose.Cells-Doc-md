---
title: Преобразовать текстовые числовые данные в число
type: docs
weight: 900
url: /ru/python-net/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовать числа, хранящиеся как текст в Excel, в числа с помощью API Aspose.Cells для Python via .NET.
keywords: python excel преобразовать текст в число, python excel преобразовать текст в число, python excel преобразовать текстовые числовые данные в число, python excel преобразовать текстовые числовые данные в число, python excel преобразовать числовой текст в число, python excel преобразовать числовой текст в число, преобразовать числовой текст в число в excel с помощью python, преобразовать числовой текст в число в excel с помощью python, преобразовать числовую строку в число в excel с помощью библиотеки python excel, python excel преобразовать текстовые числовые данные в число, python excel преобразовать числовую строку в число.
---

## **Возможные сценарии использования**
Иногда вам может понадобиться преобразовать числовые данные, введенные как текст, в числа. Вы можете ввести числа как текст в Microsoft Excel, поставив апостроф перед числом, например **'12345**. Затем Excel обрабатывает число как строку. Aspose.Cells для Python via .NET позволяет преобразовывать строки в числа.


## **Как преобразовать числа, хранящиеся как текст, в числа в Excel**
Вы можете преобразовать числа, хранящиеся как текст, в числа, следуя нескольким простым шагам.
1. Выберите любую одиночную ячейку или диапазон ячеек, у которых есть индикатор ошибки в верхнем левом углу.
1. Рядом с выбранной ячейкой или диапазоном ячеек нажмите кнопку ошибки, которая появляется. В меню щелкните Преобразовать в число. 
<br>
<img src="4.png" width=70% />
1. Если кнопка предупреждения недоступна, выберите столбец с этой проблемой. Если вы не хотите преобразовать весь столбец, вы можете выбрать одну или несколько ячеек. Убедитесь, что выбранные вами ячейки находятся в одном столбце, иначе этот процесс не сработает. Кнопка Текст в столбцах обычно используется для разделения столбца, но ее также можно использовать для преобразования одного столбца текста в числа. На вкладке Данные щелкните Текст в столбцах.
<br>
<img src="1.png" width=70% />
1. Щелкните кнопку Завершить во всплывающем окне.
<br>
<img src="2.png" width=70% />
1. Числа, сохраненные как текст, преобразуются в числа.
<br>
<img src="3.png" width=70% />

## **Как преобразовать числа, хранящиеся как текст, в числа с помощью библиотеки Aspose.Cells для Python Excel**
Aspose.Cells для Python via .NET предоставляет метод [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/), который можно использовать для преобразования всех строковых или текстовых числовых данных в числа.

На следующем снимке экрана показаны строковые числа в ячейках **A1:A17**. Строковые числа выровнены влево.
<br>
<img src="5.png" width=70% />

Эти строковые числа были преобразованы в числа с использованием [**Cells.convert_string_to_numeric_value()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/convert_string_to_numeric_value/) на следующем скриншоте. Как вы можете видеть, они теперь выровнены по правому краю.
<br>
<img src="6.png" width=70% />

## **Код Python для преобразования строковых числовых данных в фактические числа**

Следующий образец кода показывает, как преобразовать все строковые числовые данные в фактические числа во всех листах книги.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.py" >}}
