---
title: Получить строку HTML5 от Cell
type: docs
weight: 90
url: /ru/java/get-html5-string-from-cell/
---
## **Возможные сценарии использования**

Aspose.Cells возвращает строку HTML ячейки, используя[**getHtmlString (логическое значение html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)метод. Если вы пройдете**ЛОЖЬ**в качестве параметра он вернет вам обычный HTML, но если вы передадите**истинный**в качестве параметра он вернет строку HTML5.

## **Получить строку HTML5 от Cell**

В следующем примере кода создается объект книги и добавляется текст в ячейку A1 первого рабочего листа. Затем он получает обычную строку HTML и HTML5 из ячейки A1, используя[**getHtmlString (логическое значение html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)метод и печатает их на консоли.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Консольный вывод**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
