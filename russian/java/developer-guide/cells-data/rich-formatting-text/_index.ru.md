---
title: Доступ и обновление частей форматированного текста Cell
linktitle: Расширенное форматирование текста
type: docs
weight: 440
url: /ru/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells позволяет вам получать доступ и обновлять части расширенного текста ячейки. Для этого вы можете использовать методы Cell.getCharacters() и Cell.setCharacters(). Эти методы будут возвращать и принимать массив объектов FontSetting, которые вы можете использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, жирность и т. д.

{{% /alert %}} 
## **Доступ и обновление частей форматированного текста Cell**
 Следующий код демонстрирует использование методов Cell.getCharacters() и Cell.setCharacters() с использованием[исходный файл excel](5472937.xlsx) который вы можете скачать по предоставленной ссылке. Исходный файл Excel содержит форматированный текст в ячейке A1. Он состоит из 3 частей, и каждая часть имеет свой шрифт. Мы получим доступ к этим частям и обновим первую часть новым именем шрифта. Наконец, он сохраняет книгу как[выходной файл excel](5472930.xlsx) . Когда вы откроете его, вы обнаружите, что шрифт первой части текста изменился на**"Ариал"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Консольный вывод**
 Вот вывод консоли приведенного выше примера кода с использованием[исходный файл excel](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
