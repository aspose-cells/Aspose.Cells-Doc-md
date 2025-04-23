---
title: Установить шрифт по умолчанию при преобразовании электронной таблицы в изображения
type: docs
weight: 840
url: /ru/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Пожалуйста, используйте свойство [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont), чтобы установить шрифт по умолчанию при отображении электронной таблицы в изображения. Это свойство будет действительным только в том случае, когда шрифт рабочей книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont), используется для всех этих ячеек, у которых недопустимые или отсутствующие шрифты.

{{% /alert %}} 
## **Установите шрифт по умолчанию при отображении электронной таблицы в изображения**
В следующем примере код создается рабочая книга, добавляется некоторый текст в ячейку A4 первого листа и устанавливается ее шрифт как недопустимый или отсутствующий шрифт. Затем создаются два изображения листа. Первое изображение создается с установкой свойства [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) *Courier New*, а второе изображение создается с установкой свойства [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) *Times New Roman*.

Это выходное изображение после установки свойства [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) на *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Это выходное изображение после установки свойства [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) на *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
