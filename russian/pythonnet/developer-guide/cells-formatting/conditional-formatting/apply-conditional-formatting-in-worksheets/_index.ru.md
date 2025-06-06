---
title: Применение условного форматирования в рабочих листах
description: Как использовать библиотеку Aspose.Cells для Python via .NET для применения условного форматирования в листах. Настройте эти критерии для получения большего контроля над внешним видом и отображением ячеек.
keywords: Aspose.Cells, Условное форматирование, Python, Лист, Форматирование
type: docs
weight: 130
url: /ru/python-net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Эта статья предназначена для подробного понимания того, как добавить условное форматирование к диапазону ячеек на рабочем листе.

Условное форматирование - это расширенная функция в Microsoft Excel, которая позволяет применять форматы к диапазону ячеек и менять этот формат в зависимости от значения ячейки или значения формулы. Например, фон ячейки может быть красным, чтобы выделить отрицательное значение, или цвет текста может быть зеленым для положительного значения. Когда значение ячейки соответствует условию форматирования, формат применяется. Если значение ячейки не соответствует условию форматирования, используется форматирование по умолчанию для ячейки.

Возможно применить условное форматирование с помощью автоматизации Microsoft Office, но это имеет свои недостатки. В этом участвует несколько причин и проблем: например, безопасность, стабильность, масштабируемость и скорость. Основной причиной поиска другого решения является то, что сама Microsoft настоятельно рекомендует не использовать автоматизацию Office для программных решений.

Эта статья показывает, как создать консольное приложение, добавить условное форматирование в ячейки с помощью нескольких простейших строк кода с использованием API Aspose.Cells.

{{% /alert %}}

## **Использование Aspose.Cells для применения условного форматирования на основе значения ячейки**

1. **Загрузите и установите Aspose.Cells**.
   1. Загрузите Aspose.Cells для Python via .NET.
1. Установите его на вашем компьютере для разработки.
   Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.
1. **Создайте проект**.
   Запустите Visual Studio.NET и создайте новое консольное приложение. Этот пример создает консольное приложение на Python, но вы можете использовать VB.NET тоже.
1. **Добавьте ссылки**.
   Добавьте ссылку на Aspose.Cells в свой проект.
1. *Применить условное форматирование на основе значения ячейки.
   Ниже приведен код, используемый для выполнения задачи. Я изменил условное форматирование ячейки.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingCellValue-1.py" >}}

При выполнении вышеуказанного кода условное форматирование применяется к ячейке “A1” в первом листе выходного файла (output.xls). Условное форматирование, примененное к A1, зависит от значения ячейки. Если значение ячейки A1 находится между 50 и 100, то цвет фона красный из-за примененного условного форматирования.

## **Использование Aspose.Cells для применения условного форматирования на основе формулы**

1. Применение условного форматирования в зависимости от формулы (Фрагмент кода)
   Ниже приведен код для выполнения задачи. Он применяет условное форматирование к B3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingFormula-1.py" >}}

При выполнении вышеуказанного кода условное форматирование применяется к ячейке “B3” в первом листе выходного файла (output.xls). Примененное условное форматирование зависит от формулы, которая вычисляет значение “B3” как сумму B1 и B2.

