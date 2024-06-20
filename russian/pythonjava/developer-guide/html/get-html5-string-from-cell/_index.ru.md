---
title: Получить строку HTML5 из ячейки
type: docs
weight: 40
url: /ru/python-java/get-html5-string-from-cell/
---

## **Получение строки HTML5 из ячейки**
С помощью Aspose.Cells для Python via Java можно получить HTML-строку из ячейки. Это можно достичь с помощью метода getHtmlString(boolean html5), предоставляемого API. Если передать false в качестве параметра, он вернет вам обычную HTML-строку, но если передать true, то вернет HTML5-строку.

В следующем образце кода создается объект книги и добавляется некоторый текст в ячейку A1 первого листа.Затем получается обычная HTML-строка и HTML5-строка из ячейки A1 с помощью метода getHtmlString(boolean html5) и выводятся.
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Ниже приведенный вывод, сгенерированный вышеуказанным образцом кода.
## **Вывод**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
