---
title: Расширение текста справа налево при экспорте файла Excel в HTML
type: docs
weight: 820
url: /ru/java/expanding-text-from-right-to-left-while-exporting-excel-file-to/
---

{{% alert color="primary" %}} 

Теперь Aspose.Cells поддерживает расширение текста справа налево при экспорте файла Excel в HTML. Эта функция была реализована с версии v8.9.0.0. Теперь, если ваш исходный файл Excel содержит текст, который расширяется справа налево, то Aspose.Cells экспортирует его в HTML правильно.

{{% /alert %}} 
## **Развертывание текста справа налево при экспорте файла Excel в HTML**
Следующий образец кода преобразует [образец файла Excel](5472562.xlsx) в формат HTML. На этом снимке экрана показано, как выглядит образец файла Excel в Microsoft Excel 2013.

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)

На этом снимке экрана показана [сгенерированная выходная HTML с более старой версией](5472570).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)

На этом снимке экрана показана [сгенерированная выходная HTML с новой версией](5472563).

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)

Как видно на снимках экрана, новая версия корректно разворачивает правосторонний текст влево, как и Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-ExpandTextFromRightToLeftWhileExportingExcelFileToHTML-.java" >}}
{{< app/cells/assistant language="java" >}}
