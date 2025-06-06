---
title: Как фильтровать пустые или непустые ячейки
type: docs
weight: 85
url: /ru/net/how-to-filter-blanks-and-non-blanks/
description: Узнать, как фильтровать пустые и непустые ячейки с использованием API Aspose.Cells for .NET.
keywords: Отфильтровать пустые, отфильтровать непустые, отфильтровать пустые в листе, отфильтровать непустые в листе, отфильтровать пустые в Excel, отфильтровать непустые в Excel, отфильтровать пустые и непустые в Excel
---

## **Возможные сценарии использования**
Фильтрация данных в Excel – это ценный инструмент, который улучшает анализ, исследование и презентацию данных, позволяя пользователям сосредоточиться на конкретных подмножествах данных в соответствии с их критериями, что делает общий процесс манипулирования данными и их интерпретации более эффективным и эффективным.

## **Как фильтровать пустые или непустые ячейки в Excel**
В Excel вы можете легко фильтровать пустые или непустые ячейки с помощью опций фильтрации. Вот как это можно сделать:

### **Как фильтровать пустые ячейки в Excel**
1. Выберите диапазон: Щелкните на букве заголовка столбца, чтобы выбрать весь столбец или выберите диапазон, в котором хотите отфильтровать пустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Отфильтруйте пустые ячейки: Щелкните на стрелке фильтра в столбце, который вы хотите отфильтровать пустыми. Снимите все параметры, кроме «Пустые», и нажмите OK. Это отобразит только пустые ячейки в этом столбце.
<br>
<image src="2.png" width="70%" />
1. Результат следующий:
<br>
<image src="3.png" width="70%" />

### **Как фильтровать непустые ячейки в Excel**
1. Выберите диапазон: нажмите на букву заголовка столбца, чтобы выбрать весь столбец, или выберите диапазон, в котором хотите отфильтровать непустые ячейки.
1. Откройте меню Фильтр: перейдите на вкладку "Данные" на ленте.
<br>
<image src="1.png" width="70%" />
1. Варианты фильтра: нажмите кнопку "Фильтр". Это добавит стрелки фильтрации к выбранному диапазону.
1. Фильтрация непустых ячеек: нажмите на стрелку фильтра в столбце, который хотите отфильтровать по непустоте. Снимите выбор со всех вариантов, кроме "Непустые" или "Пользовательский", и установите условия соответственно. Нажмите ОК. Это отобразит только ячейки, которые не пустые в этом столбце.
<br>
<image src="4.png" width="70%" />
1. Результат следующий:
<br>
<image src="5.png" width="70%" />

## **Как фильтровать пустые ячейки с помощью Aspose.Cells**
Если столбец содержит текст так, что несколько ячеек пустые, и требуется фильтр для выбора только тех строк, где присутствуют пустые ячейки, можно использовать функции [AutoFilter.MatchBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchblanks/) и [AutoFilter.AddFilter(int fieldIndex, string criteria)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/addfilter/), как показано ниже. 

Пожалуйста, ознакомьтесь с примерным кодом, загружающим [образец Excel-файла](sample.xlsx), который содержит некоторые фиктивные данные. Примерный код использует три метода для фильтрации пустот. Затем он сохраняет книгу как [выходной Excel-файл](FilteredBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-blanks.cs" >}}

## **Как фильтровать непустые ячейки с помощью Aspose.Cells**

Пожалуйста, посмотрите следующий образец кода, который загружает [образец Excel-файла](sample.xlsx), содержащий какие-то заглушечные данные. После загрузки файла вызовите функцию [AutoFilter.MatchNonBlanks(int fieldIndex)](https://reference.aspose.com/cells/net/aspose.cells/autofilter/matchnonblanks/) для фильтрации непустых данных, а затем сохраните книгу как [выходной Excel-файл](FilteredNonBlanks.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Filter-non-blanks.cs" >}}

{{< app/cells/assistant language="csharp" >}}
