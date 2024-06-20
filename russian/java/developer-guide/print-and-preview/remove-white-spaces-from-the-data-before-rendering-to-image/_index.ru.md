---
title: Удалите пробелы из данных перед их рендерингом в изображение
type: docs
weight: 270
url: /ru/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

Иногда вам нужно представить изображения листа в приложениях или веб-страницах. Например, вам может понадобиться вставить изображения в документ Word, файл PDF, презентацию PowerPoint или в другой документ. Фактически, вы хотите отобразить лист как изображение, чтобы его можно было вставить в другие приложения. API Aspose.Cells позволяет вам преобразовывать электронные таблицы Microsoft Excel в изображения.

{{% /alert %}}

Класс [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) способен преобразовывать лист в файл изображения с любыми указанными атрибутами, например, формат изображения, разбитые на страницы листы и т. д. Поддерживается несколько форматов изображений, включая BMP, GIF, JPG, TIFF и EMF.

При использовании функции конвертации листа в изображение выходное изображение имеет белое/пустое пространство, то есть рамку, вокруг себя по умолчанию. Можно убрать это. Установите верхние, левый, нижний и правый поля настройки страницы для исходного листа как 0 и укажите соответствующие атрибуты [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) соответственно.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
