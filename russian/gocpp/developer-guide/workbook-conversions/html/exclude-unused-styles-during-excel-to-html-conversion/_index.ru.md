---
title: Исключите неиспользуемые стили при преобразовании Excel в HTML с помощью Golang через C++
linktitle: Исключить неиспользуемые стили
type: docs
weight: 30
url: /ru/go-cpp/exclude-unused-styles-during-excel-to-html-conversion/
description: Узнайте, как исключить неиспользуемые стили при преобразовании Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Файлы Microsoft Excel могут содержать множество неиспользуемых стилей. При экспорте файла Excel в формат HTML экспортируются эти неиспользуемые стили, что может увеличить размер HTML. Вы можете исключить неиспользуемые стили при преобразовании файла Excel в HTML, установив свойство [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) в **true**. На следующем скриншоте показан пример неиспользуемого стиля внутри итогового HTML.

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **Исключить неиспользуемые стили во время преобразования Excel в HTML**

Следующий пример создает рабочую книгу и также добавляет неиспользуемый именованный стиль. Поскольку свойство [**HtmlSaveOptions.GetExcludeUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexcludeunusedstyles/) установлено в **true**, этот неиспользуемый стиль не будет экспортирован в [итоговый HTML](61767778.zip). Если установить его в **false**, то этот неиспользуемый стиль появится в итоговом HTML, что видно в разметке HTML, как показано выше.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExcludeUnusedStylesDuringExcelToHtmlConversion.go" >}}
