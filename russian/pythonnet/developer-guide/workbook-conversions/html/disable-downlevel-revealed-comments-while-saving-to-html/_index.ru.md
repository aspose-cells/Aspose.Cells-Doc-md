---
title: Отключить отображение комментариев уровня Downlevel при сохранении в HTML
type: docs
weight: 20
url: /ru/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML, API Aspose.Cells for Python via .NET показывает условные комментарии уровней ниже. Эти условные комментарии в основном актуальны для старых версий Internet Explorer и не важны для современных веб-браузеров. Подробнее о них можно прочитать по следующей ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells for Python via .NET позволяет устранить эти раскрываемые условные комментарии, установив свойство [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) в значение **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments). На скриншоте показан эффект этого свойства, когда оно не установлено в true. Пожалуйста, загрузите [образец файла Excel](50528257.xlsx) используемый в этом коде и [выходной HTML](50528258.zip), сгенерированный им для справки.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
{{< app/cells/assistant language="python-net" >}}
