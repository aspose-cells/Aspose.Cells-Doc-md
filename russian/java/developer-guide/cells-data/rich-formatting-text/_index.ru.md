---
title: Доступ и обновление частей форматированного текста ячейки
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 440
url: /ru/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет получить доступ и обновить части форматированного текста ячейки. Для этого можно использовать методы Cell.getCharacters() и Cell.setCharacters(). Эти методы возвращают и принимают массив объектов FontSetting, которые можно использовать для доступа к различным свойствам шрифта, таким как название шрифта, цвет шрифта, жирность и т. д.

{{% /alert %}} 
## **Доступ и обновление частей Rich Text ячейки**
Нижеприведенный код демонстрирует использование методов Cell.getCharacters() и Cell.setCharacters() с [исходным файлом Excel](5472937.xlsx), который можно загрузить по предоставленной ссылке. В исходном файле Excel есть форматированный текст в ячейке A1. Он состоит из 3 частей, и каждая имеет разный шрифт. Мы получим доступ к этим частям и обновим первую часть новым названием шрифта. Наконец, таблица сохраняется как [выходной файл Excel](5472930.xlsx). После его открытия вы увидите, что шрифт первой части текста был изменен на **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Вывод в консоль**
Вот вывод в консоль из приведенного выше образца кода с использованием [исходного файла Excel](5472937.xlsx).

{{< highlight java >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
