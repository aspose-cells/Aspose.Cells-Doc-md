---
title: Отключите CSS при сохранении в HTML с помощью Golang через C++
linktitle: Отключить CSS при сохранении в HTML
type: docs
weight: 320
url: /ru/go-cpp/disable-css-while-saving-to-html/
description: Узнайте, как отключить CSS при сохранении файлов Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

При сохранении файла Excel в одностраничный HTML, CSS-элементы обычно внедряются в HTML-файл и располагаются в разделе HEAD. Если вы прикрепите этот файл как содержимое/тело электронной почты, большинство почтовых клиентов удалит CSS-элементы, что приведет к неправильному отображению. В версии Aspose.Cells 24.12 появилась возможность опционально отключить CSS, позволяя применять стили непосредственно внутри HTML-элементов. Если вы хотите установить HTML как содержимое/тело письма, используйте свойство [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) и установите его в значение **true**.

## **Отключить CSS при сохранении в HTML**

Следующий пример кода показывает использование свойства [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/).

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
