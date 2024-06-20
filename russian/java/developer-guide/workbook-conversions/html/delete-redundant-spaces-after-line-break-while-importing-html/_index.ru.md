---
title: Удаление избыточных пробелов после переноса строки при импорте HTML
type: docs
weight: 620
url: /ru/java/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}} 

Используйте свойство [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces) и установите его в **true**, чтобы удалять все избыточные пробелы после тега переноса строки. По умолчанию это свойство **false**, и избыточные пробелы сохраняются в выходных файлах Excel.

{{% /alert %}} 
## **Эффект установки свойства HtmlLoadOptions.DeleteRedundantSpaces в значения false и true**
На следующем скриншоте показан эффект установки этого свойства в **false** и **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)
## **Удаление избыточных пробелов после переноса строки при импорте HTML**
Приведенный ниже код показывает использование свойства [HtmlLoadOptions.DeleteRedundantSpaces](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#DeleteRedundantSpaces). Пожалуйста, установите его в **true** или **false**, чтобы получить выходные данные, как показано на выше скриншоте.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-DeleteRedundantSpacesFromHtml-1.java" >}}
