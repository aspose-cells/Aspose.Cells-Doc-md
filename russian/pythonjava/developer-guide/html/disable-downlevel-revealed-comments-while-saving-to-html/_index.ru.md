---
title: Отключить открытые комментарии нижнего уровня при сохранении в HTML
type: docs
weight: 20
url: /ru/python-java/disable-downlevel-revealed-comments-while-saving-to/
---
## **Отключить открытые комментарии нижнего уровня при сохранении в HTML**
Когда файл Excel преобразуется в HTML, Aspose.Cells добавляет в выходной файл HTML условные комментарии, отображаемые на более низком уровне. Эти условные комментарии в основном относятся к старым версиям Internet Explorer и не имеют отношения к современным браузерам. Для получения дополнительной информации об условных комментариях, раскрываемых Downlevel, перейдите по следующей ссылке.

[Условный комментарий — условный комментарий, отображаемый на нижнем уровне.](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Чтобы удалить условные комментарии, отображаемые на более низком уровне, Aspose.Cells предоставляет[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments)имущество. Настройка[HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) собственность на**Истинный**удалит условные комментарии, показанные Downlevel, в выходном файле HTML.

На следующем изображении показаны условные комментарии, показанные на уровне Downlevel, которые будут удалены в выходном файле HTML.

![дело:изображение_альтернативный_текст](Disable-Downlevel-Revealed-Comments.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
