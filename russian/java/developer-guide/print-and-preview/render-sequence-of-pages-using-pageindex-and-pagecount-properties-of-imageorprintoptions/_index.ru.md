---
title: Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions
type: docs
weight: 100
url: /ru/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/
---

## **Возможные сценарии использования**

Вы можете отображать последовательность страниц вашего файла Excel в формате изображений с помощью Aspose.Cells используя свойства [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) и [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Эти свойства полезны, когда в вашей таблице так много например тысячи страниц, но вы хотите отобразить только некоторые из них. Это не только сэкономит время обработки, но и снизит память, используемую процессом рендеринга.

## **Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions**

В следующем образце кода загружается [образец Excel-файла](55541812.xlsx) и рендерятся только страницы 4, 5, 6 и 7 с использованием свойств [**ImageOrPrintOptions.PageIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageIndex) и [**ImageOrPrintOptions.PageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#PageCount). Вот сгенерированные кодом отображенные страницы.

|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_1.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_2.png)|
| :- | :- |
|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_3.png)|![todo:image_alt_text](render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions_4.png)|

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderLimitedNoOfSequentialPages-1.java" >}}
{{< app/cells/assistant language="java" >}}
