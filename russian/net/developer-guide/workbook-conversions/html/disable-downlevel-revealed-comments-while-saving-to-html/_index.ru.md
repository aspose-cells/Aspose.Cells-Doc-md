---
title: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Возможные сценарии использования**

Когда вы сохраняете свой файл Excel в формат HTML, то Aspose.Cells раскрывает Downlevel Conditional Comments. Эти условные комментарии в основном относятся к старым версиям Internet Explorer и не имеют отношения к современным веб-браузерам. Вы можете узнать о них подробнее по следующей ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет исключить эти Downlevel Revealed Comments, установив свойство [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) в **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments). На скриншоте показан эффект этого свойства, когда оно не установлено в true. Пожалуйста, загрузите [образец файла Excel](50528257.xlsx) используемый в этом коде и [выходной HTML](50528258.zip), сгенерированный им для справки.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
