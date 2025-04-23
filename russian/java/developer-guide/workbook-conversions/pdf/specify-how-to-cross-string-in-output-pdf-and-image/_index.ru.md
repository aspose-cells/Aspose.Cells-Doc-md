---
title: Указание того, как пересекать строку в выходном PDF и изображении
type: docs
weight: 110
url: /ru/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Возможные сценарии использования**

Когда ячейка содержит текст или строку, но она больше ширины ячейки, то строка переполняется, если следующая ячейка в следующем столбце пуста или пуста. При сохранении вашего файла Excel в формат PDF/изображение вы можете контролировать этот переполнение, указав тип пересечения с использованием перечисления [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). У него следующие значения

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Отображение как MS Excel, зависит от следующей ячейки. Если следующая ячейка пуста, строка будет перечеркнута или обрезана.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-KEEP): Отображение строки как при экспорте PDF/изображения MS Excel

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS-OVERRIDE): Отображение всего текста, пересекая другие ячейки и перезаписывая текст пересекаемых ячеек

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT-IN-CELL): Отображение только строки в пределах ширины ячейки.

## **Указание того, как пересекать строку в выходном PDF/изображении с использованием TextCrossType**

В следующем примере кода загружается образец файла Excel и сохраняется в формат PDF/изображение, указав разные [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Образец файла Excel и выходные файлы можно скачать по следующим ссылкам:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}
{{< app/cells/assistant language="java" >}}
