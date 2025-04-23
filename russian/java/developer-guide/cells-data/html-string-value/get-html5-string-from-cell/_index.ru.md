---
title: Получить строку HTML5 из ячейки
type: docs
weight: 90
url: /ru/java/get-html5-string-from-cell/
---

## **Возможные сценарии использования**

Aspose.Cells возвращает HTML-строку ячейки, используя метод [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString). Если вы передадите **false** в качестве параметра, он вернет вам обычный HTML, но если вы передадите **true**, он вернет HTML5 строку.

## **Получение строки HTML5 из ячейки**

Нижеприведенный образец кода создает объект книги и добавляет некоторый текст в ячейку A1 первого листа. Затем он получает обычную HTML-строку и HTML5-строку из ячейки A1, используя метод [**getHtmlString(boolean html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString), и выводит их в консоли.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Вывод в консоль**

{{< highlight java >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
