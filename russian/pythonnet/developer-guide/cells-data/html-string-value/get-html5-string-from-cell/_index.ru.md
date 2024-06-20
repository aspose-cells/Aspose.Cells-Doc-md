---
title: Получить строку HTML5 из ячейки
type: docs
weight: 90
url: /ru/python-net/get-html5-string-from-cell/
description: Узнайте, как получить строку HTML5 из ячейки с помощью Aspose.Cells для Python via .NET API.
keywords: Библиотека для Python Excel, Получить HTML5 строку из ячейки Python, Получить HTML5 строку из ячейки с помощью Python, Управление HTML5 строкой ячейки в Python.
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET возвращает HTML строку ячейки, используя метод [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool), который принимает булевый параметр. Если вы передаете **false** в качестве параметра, он вернет обычный HTML, но если вы передадите **true** в качестве параметра, он вернет HTML5 строку.

## **Получение строки HTML5 из ячейки**

В следующем образце кода создается объект книги и добавляется некоторый текст в ячейку A1 первого листа. Затем получается обычная HTML строка и HTML5 строка из ячейки A1, используя метод [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool), и выводится на консоль.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Вывод в консоль**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
