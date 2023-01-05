---
title: Отключить открытые комментарии нижнего уровня при сохранении в HTML
type: docs
weight: 20
url: /ru/net/disable-downlevel-revealed-comments-while-saving-to/
---
## **Возможные сценарии использования**

Когда вы сохраняете файл Excel по адресу HTML, тогда Aspose.Cells показывает условные комментарии более низкого уровня. Эти условные комментарии в основном относятся к более старым версиям Internet Explorer и не имеют отношения к современным веб-браузерам. Подробно о них можно прочитать по следующей ссылке.

- [Условный комментарий — условный комментарий, отображаемый на нижнем уровне.](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет устранить эти комментарии, обнаруженные на более низком уровне, путем установки параметра[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) собственность на**истинный**.

## **Отключить открытые комментарии нижнего уровня при сохранении в HTML**

В следующем примере кода показано использование[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/disabledownlevelrevealedcomments) имущество. На снимке экрана показан эффект этого свойства, когда для него не задано значение true. Пожалуйста, загрузите[образец файла Excel](50528257.xlsx) используется в этом коде и[вывод HTML](50528258.zip) созданный им для справки.

![дело:изображение_альтернативный_текст](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.cs" >}}
