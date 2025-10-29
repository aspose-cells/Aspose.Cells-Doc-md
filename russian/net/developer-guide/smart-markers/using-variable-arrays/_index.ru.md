---
title: Умное импортирование переменных массивов в Excel с помощью умных маркеров
type: docs
weight: 30
url: /ru/net/how-to-import-variable-arrays-with-smart-markers/
---

## **Почему использовать переменные массивы для умных маркеров**
Variable arrays (e.g., <<products[0].name>> or <<foreach item in cart>>) enable dynamic handling of repeated data structures in templates. They solve limitations of flat/nested objects when dealing with lists, tables, or collections.

1. Динамическое повторение без жесткого кодирования: статические маркеры не работают с данными переменной длины (например, позиции заказа, разрешения пользователей). Массивы итерируются динамически. 
2. Упрощенная агрегация: вычисляйте суммы, средние значения или фильтры напрямую. Избегайте ручной логики JavaScript/C# в шаблонах.
3. Представление данных в таблицах/списках: естественное соответствие: таблицы, сетки и списки по умолчанию отображаются в массивах.
4. Эффективность использования памяти: массивы уменьшают сложность шаблонов и накладные расходы на привязку данных.
5. Интеграция с API/источниками данных: соответствует данным, ориентированным на JSON/массивы (например, REST API).

## **Как импортировать переменные массивы с умными маркерами**
Приведенный ниже пример кода показывает, как использовать переменные массивы в умных маркерах. Мы размещаем маркер переменного массива в ячейке A1 первого листа рабочей книги динамически, который содержит строку значений, которые мы устанавливаем для маркера, обрабатываем маркеры для заполнения данных в ячейках по маркерам. Наконец, мы сохраняем файл Excel.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingVariableArray-1.cs" >}}

## **Как импортировать свойства HTML с умными маркерами**
The following sample code explains the use of HTML property of the Smart Markers. When it will be processed, it will show "World" in "Hello World" as bold because of HTML <b> tag.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingHTMLProperty-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
