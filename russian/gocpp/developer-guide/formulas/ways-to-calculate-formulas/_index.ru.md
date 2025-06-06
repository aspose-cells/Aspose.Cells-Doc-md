---
title: Способы вычисления формул
type: docs
weight: 30
url: /ru/go-cpp/ways-to-calculate-formulas/
---

## **Введение**

У Aspose.Cells есть встроенный движок вычисления формул. Он может не только пересчитывать формулы, импортированные из шаблонов дизайнера, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

## **Добавление формул и вычисление результатов**

Aspose.Cells поддерживает большинство формул или функций, которые составляют часть Microsoft Excel. их можно использовать через API или с помощью дизайнерских электронных таблиц. Aspose.Cells поддерживает огромный набор математических, строковых, логических, дата/время, статистических, поисковых и ссылочных формул.

Используйте метод Cell.SetFormula для добавления формулы в ячейку. При применении формулы к ячейке всегда начинайте строку с знака равенства (=), как это делается при создании формулы в Microsoft Excel. Используйте запятую (,) для разделения параметров функции.

Для вычисления результатов формул вызовите метод Workbook.CalculateFormula(), который обрабатывает все формулы, встроенные в файл Excel. Пожалуйста, ознакомьтесь с примером кода ниже, добавляющим формулу и вычисляющим ее результаты. Пожалуйста, проверьте [выходной файл Excel](38109185.xlsx), созданный с помощью этого кода.

**Пример кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingFormulasAndCalculatingResults.go" >}}

## **Вычисление формул один раз**

Когда Workbook.CalculateFormula() вызывается для вычисления значений формул в шаблоне книги, Aspose.Cells создает цепочку вычислений. Это увеличивает производительность при вычислении формул для второго или третьего раза.

Однако, если шаблон содержит много формул, первый раз вычисления формулы может занять много времени процессора и памяти.

Aspose.Cells позволяет отключить создание цепочки вычислений, что полезно, когда вы хотите вычислить формулы только один раз.

Пожалуйста, вызовите Workbook.GetISettings().SetCreateCalcChain() с параметром false. Вы можете использовать [предоставленный файл Excel](38109186.xlsx) для тестирования этого кода.

**Пример кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CalculatingFormulasOnceOnly.go" >}}
