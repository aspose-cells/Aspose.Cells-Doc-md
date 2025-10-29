---
title: Отключите просвечивающие комментарии при сохранении в HTML с помощью Golang через C++
linktitle: Отключить объяснительные комментарии следующего уровня
type: docs
weight: 20
url: /ru/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Устраните просвечивающие комментарии при сохранении файлов Excel в HTML с помощью Aspose.Cells и Golang через C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в HTML Aspose.Cells отображает условные комментарии следующего уровня. Эти условные комментарии в основном актуальны для старых версий Internet Explorer и не имеют значения для современных браузеров. Подробнее о них можно прочитать по следующей ссылке.

- [Условный комментарий - условный комментарий с раскрытием](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells позволяет устранить эти комментарии следующего уровня, установив свойство [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) в значение **true**.

## **Отключить отображение устаревших комментариев при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/). На снимке экрана видно, как влияет это свойство, когда оно не установлено в значение true. Для ознакомления скачайте [пример файла Excel](50528257.xlsx), использованный в этом коде, и [сгенерированный HTML](50528258.zip) для просмотра.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
