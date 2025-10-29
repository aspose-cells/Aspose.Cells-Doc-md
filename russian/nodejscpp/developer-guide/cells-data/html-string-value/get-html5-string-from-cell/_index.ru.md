---
title: Получить строку HTML5 из ячейки
type: docs
weight: 90
url: /ru/nodejs-cpp/get-html5-string-from-cell/
description: Узнайте, как получить HTML5 строку из ячейки через API Aspose.Cells for Node.js via C++.
keywords: Получить строку HTML5 из Ячейки Node.js через C++, Управлять строкой HTML5 ячейки Node.js через C++, Обрабатывать строку HTML5 ячейки Node.js через C++
---

## **Возможные сценарии использования**

Aspose.Cells возвращает строку HTML ячейки с использованием метода [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-), который принимает булевый параметр. Если передать **false** в качестве параметра, он вернёт обычный HTML, а если **true** — HTML5.

## **Получение строки HTML5 из ячейки**

Следующий пример создает объект книги и добавляет текст в ячейку A1 первого листа. Затем он получает строку Normal HTML и HTML5 из ячейки A1 с помощью метода [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) и выводит их в консоль.

## **Образец кода**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Вывод в консоль**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
