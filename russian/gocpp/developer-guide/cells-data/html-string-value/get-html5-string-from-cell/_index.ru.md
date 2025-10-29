---
title: Получить строку HTML5 из ячейки с Golang через C++
linktitle: Получить HTML5 строку из ячейки
type: docs
weight: 90
url: /ru/go-cpp/get-html5-string-from-cell/
description: Узнайте, как получить HTML5 строку из ячейки с помощью API Aspose.Cells for C++.
keywords: Получить строку HTML5 из ячейки, получить строку HTML5 из ячейки, управлять строкой HTML5 ячейки
---

## **Возможные сценарии использования**

Aspose.Cells возвращает HTML-строку ячейки с помощью метода [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/), который принимает булевский параметр. Если передать **false**, он вернет обычный HTML, а если **true**, — HTML5.

## **Получить HTML5 строку из ячейки**

В следующем образце кода создается объект книги и добавляется некоторый текст в ячейку A1 первого листа. Затем получается обычная HTML строка и HTML5 строка из ячейки A1, используя метод [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/), и выводится на консоль.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Вывод в консоль**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
