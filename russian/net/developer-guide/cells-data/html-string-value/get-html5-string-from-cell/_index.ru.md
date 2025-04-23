---
title: Получить строку HTML5 из ячейки
type: docs
weight: 90
url: /ru/net/get-html5-string-from-cell/
description: Узнайте, как получить строку HTML5 из ячейки через API Aspose.Cells for .NET.
keywords: Получить строку HTML5 из ячейки, получить строку HTML5 из ячейки, управлять строкой HTML5 ячейки
---

## **Возможные сценарии использования**

Aspose.Cells возвращает строку HTML ячейки с использованием метода [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring), который принимает логический параметр. Если вы передадите **false** в качестве параметра, он вернет обычную HTML-строку, но если вы передадите **true** в качестве параметра, он вернет строку HTML5.

## **Получение строки HTML5 из ячейки**

В следующем образце кода создается объект книги и добавляется некоторый текст в ячейку A1 первого листа. Затем получается обычная HTML строка и HTML5 строка из ячейки A1, используя метод [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring), и выводится на консоль.

## **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Вывод в консоль**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
