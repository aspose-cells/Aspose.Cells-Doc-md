---
title: Преобразование текстовых числовых данных в число
type: docs
weight: 150
url: /ru/java/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовать числа, хранящиеся в виде текста, в числа с помощью Aspose.Cells for Java API.
keywords: excel convert text to number, excel convert text to number java, excel convert text numeric data to number, excel convert text numeric data to number java, excel convert numeric text to number, excel convert numeric text to number java, excel convert numeric text to number with java, convert numeric text to number in excel with java, convert numeric text to number in excel with java, convert numeric string to number in excel with java, excel convert text numeric data to number java, excel convert numeric string to number java
---
##  **Возможные сценарии использования**
Иногда вам нужно преобразовать числовые данные, введенные в виде текста, в числа. Вы можете вводить числа в виде текста в Excel Microsoft, поставив апостроф перед числом, например *'12345**. Затем Excel обрабатывает число как строку. Aspose.Cells позволяет конвертировать строки в числа.


## Преобразование чисел, хранящихся в виде текста, в числа в Excel
Вы можете преобразовать числа, хранящиеся в виде текста, в числа, выполнив несколько простых шагов.
1. Выберите любую ячейку или диапазон ячеек, у которых есть индикатор ошибки в верхнем левом углу.
1.  Рядом с выбранной ячейкой или диапазоном ячеек нажмите появившуюся кнопку ошибки. В меню нажмите «Преобразовать в число».
<br>
<img src="4.png" width=70% />
1. Если кнопка оповещения недоступна, выберите столбец с этой проблемой. Если вы не хотите конвертировать весь столбец, вместо этого вы можете выбрать одну или несколько ячеек. Просто убедитесь, что выбранные вами ячейки находятся в одном столбце, иначе этот процесс не сработает. Кнопка «Текст в столбцы» обычно используется для разделения столбца, но ее также можно использовать для преобразования одного столбца текста в числа. На вкладке «Данные» нажмите «Текст по столбцам».
<br>
<img src="1.png" width=70% />
1. Нажмите кнопку «Готово» во всплывающем окне.
<br>
<img src="2.png" width=70% />
1. Числа, хранящиеся в виде текста, преобразуются в числа.
<br>
<img src="3.png" width=70% />

##  Преобразуйте числа, хранящиеся в виде текста, в числа, используя Aspose.Cells для JAVA.
Aspose.Cells for Java API обеспечивает[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) метод, который можно использовать для преобразования всех строковых или текстовых числовых данных в числа.

На следующем снимке экрана показаны номера строк в ячейках *A1:A17**. Номера строк выравниваются по левому краю.
<br>
<img src="5.png" width=70% />

 Эти строковые числа были преобразованы в числа с помощью[**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue()) на следующем снимке экрана. Как видите, теперь они выровнены по правому краю.
<br>
<img src="6.png" width=70% />

##  Java код для преобразования строковых числовых данных в фактические числа.
В следующем примере кода показано, как преобразовать все строковые числовые данные в фактические числа на всех листах.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
