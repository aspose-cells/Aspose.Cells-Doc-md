---
title: Получить строку HTML5 от Cell
type: docs
weight: 90
url: /ru/net/get-html5-string-from-cell/
---
## **Возможные сценарии использования**

Aspose.Cells возвращает строку HTML ячейки, используя[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) метод, который принимает логический параметр. Если вы пройдете**ЛОЖЬ**в качестве параметра он вернет обычный HTML, но если вы передадите**истинный** в качестве параметра он вернет строку HTML5.

## **Получить строку HTML5 от Cell**

В следующем примере кода создается объект книги и добавляется текст в ячейку A1 первого рабочего листа. Затем он получает обычную строку HTML и HTML5 из ячейки A1, используя[**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)метод и печатает их на консоли.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Консольный вывод**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
