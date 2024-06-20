---
title: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/python-java/disable-downlevel-revealed-comments-while-saving-to/
---

## **Отключить отображение устаревших комментариев при сохранении в HTML**
Когда файл Excel преобразуется в HTML, Aspose.Cells добавляет условные комментарии Downlevel-revealed в выходной файл HTML. Эти условные комментарии в основном относятся к старым версиям Internet Explorer и неактуальны в современных браузерах. Дополнительную информацию о Downlevel-revealed conditional comments можно найти по [следующей ссылке](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment).

[Условный комментарий - Downlevel-revealed conditional comment](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Для удаления условных комментариев Downlevel-revealed Aspose.Cells предоставляет свойство [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments). Установка свойства [HtmlSaveOptions.DisableDownlevelRevealedComments](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#DisableDownlevelRevealedComments) в **True** удалит условные комментарии Downlevel-revealed в выходном файле HTML.

Следующее изображение показывает условные комментарии Downlevel-revealed, которые будут удалены в итоговом файле HTML

![todo:image_alt_text](Disable-Downlevel-Revealed-Comments.png)
## **Образец кода**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
