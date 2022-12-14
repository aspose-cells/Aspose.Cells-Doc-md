---
title: Получить строку HTML5 от Cell
type: docs
weight: 40
url: /ru/python-java/get-html5-string-from-cell/
---
## **Получить строку HTML5 от Cell**
Используя Aspose.Cells для Python через Java, вы можете получить строку HTML из ячейки. Это может быть достигнуто с помощью[getHtmlString (логическое значение html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) метод, предоставленный API. Если вы пройдете**ЛОЖЬ**в качестве параметра он вернет вам обычный HTML, но если вы передадите**истинный**в качестве параметра он вернет строку HTML5.

В следующем примере кода создается объект книги и добавляется текст в ячейку A1 первого рабочего листа. Затем он получает обычную строку HTML и HTML5 из ячейки A1, используя[getHtmlString (логическое значение html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) метод и печатает их.
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Ниже приведен вывод, созданный приведенным выше фрагментом кода.
## **Выход**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
