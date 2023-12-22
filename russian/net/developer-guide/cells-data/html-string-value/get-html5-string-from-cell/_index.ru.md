---
title: Получите строку HTML5 с номера Cell.
type: docs
weight: 90
url: /ru/net/get-html5-string-from-cell/
description: Узнайте, как получить строку HTML5 от Cell до Aspose.Cells for .NET API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **Возможные сценарии использования**

Aspose.Cells возвращает строку HTML ячейки, используя[**ПолучитьHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) метод, который принимает логический параметр. Если ты пройдешь**ЛОЖЬ** в качестве параметра он вернет Normal HTML, но если вы передадите**истинный** в качестве параметра он вернет строку HTML5.

##  **Получите строку HTML5 с номера Cell.**

В следующем примере кода создается объект книги и добавляется текст в ячейку A1 первого листа. Затем он получает строку Normal HTML и HTML5 из ячейки A1, используя[**ПолучитьHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)метод и печатает их на консоли.

##  **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **Консольный вывод**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
