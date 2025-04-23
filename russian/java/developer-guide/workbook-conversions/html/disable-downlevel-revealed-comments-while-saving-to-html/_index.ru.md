---
title: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/java/disable-downlevel-revealed-comments-while-saving-to-html/
---

## **Возможные сценарии использования**

Когда вы сохраняете свой файл Excel в HTML, то Aspose.Cells показывает Downlevel Conditional Comments. Эти условные комментарии в основном относятся к старым версиям Internet Explorer и не имеют отношения к современным веб-браузерам. Вы можете подробнее прочитать об этом по следующей ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет убрать эти Downlevel Revealed Comments, установив свойство [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) в **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Приведенный ниже код показывает использование [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments) свойства. На скриншоте показан эффект этого свойства, когда оно не установлено в **true**. Пожалуйста, скачайте [пример файла Excel](50528267.xlsx), используемый в этом коде, и сгенерированный им [файл HTML](50528266.zip) для справки.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
