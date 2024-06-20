---
title: Получение ширины и высоты бумаги из настройки страницы листа
type: docs
weight: 300
url: /ru/java/get-paper-width-and-height-from-pagesetup-of-worksheet/
---

## **Возможные сценарии использования**

Иногда вам может потребоваться узнать ширину и высоту бумаги, установленные в настройках страницы листа. Пожалуйста, используйте свойства [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) и [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight) для этой цели.

## **Получение ширины и высоты бумаги из настройки страницы листа**

В следующем образце кода объясняется использование свойств [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperWidth) и [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperHeight). Сначала изменяется размер бумаги на A2, затем находится ширина и высота бумаги, затем он меняется на A3, A4, Letter и находится ширина и высота бумаги соответственно.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-GetPaperWidthHeight-GetPaperWidthHeight.java" >}}

## **Вывод в консоль**

Вот вывод в консоль вышеуказанного образца кода.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11.0

{{< /highlight >}}
