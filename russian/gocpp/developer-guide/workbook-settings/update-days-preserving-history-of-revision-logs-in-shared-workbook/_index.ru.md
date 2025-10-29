---
title: Обновление дней с сохранением истории журналов изменений в общем рабочем листе с помощью Golang через C++
linktitle: Обновление дней, сохраняющих историю журналов версий в общей книге
type: docs
weight: 80
url: /ru/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Узнайте, как обновлять число дней для сохранения истории в общем рабочем листе с помощью Aspose.Cells и Golang через C++
---

## **Возможные сценарии использования**

Если вы делитесь книгой, у вас есть опция ***Сохранять историю изменений на протяжении N дней***, как показано на следующем скриншоте. Вы можете обновить количество дней для сохранения истории с помощью Aspose.Cells с [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/) свойством.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Обновление дней, сохраняющих историю журналов версий в общей книге**

В следующем образце кода создается пустая книга, затем ее делят и обновляются журналы ревизии для сохранения истории на 7 дней, что обычно составляет 30 дней. Пожалуйста, обратитесь к [выходному файлу Excel](60489773.xlsx), созданному кодом в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
