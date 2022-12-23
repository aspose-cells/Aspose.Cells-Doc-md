---
title: Отключить открытые комментарии нижнего уровня при сохранении в HTML
type: docs
weight: 20
url: /ru/java/disable-downlevel-revealed-comments-while-saving-to-html/
---
## **Возможные сценарии использования**

Когда вы сохраняете файл Excel по адресу HTML, тогда Aspose.Cells показывает условные комментарии более низкого уровня. Эти условные комментарии в основном относятся к старым версиям Internet Explorer и не имеют отношения к современным веб-браузерам. Подробно о них можно прочитать по следующей ссылке.

- [Условный комментарий — условный комментарий, отображаемый на нижнем уровне.](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет устранить эти комментарии, обнаруженные на более низком уровне, путем установки параметра[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)собственность на**истинный**.

## **Отключить открытые комментарии нижнего уровня при сохранении в HTML**

В следующем примере кода показано использование[**HtmlSaveOptions.DisableDownlevelRevealedComments**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DisableDownlevelRevealedComments)имущество. На снимке экрана показан эффект этого свойства, когда для него не установлено значение**истинный**. Пожалуйста, загрузите[образец файла Excel](50528267.xlsx)используется в этом коде и[вывод HTML](50528266.zip)файл, созданный им для справки.

![дело:изображение_альтернативный_текст](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DisableDownlevelRevealedCommentsWhileSavingToHTML.java" >}}
