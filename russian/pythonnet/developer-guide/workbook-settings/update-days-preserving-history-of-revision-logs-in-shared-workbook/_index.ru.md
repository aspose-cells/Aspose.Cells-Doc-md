---
title: Обновление дней, сохраняющих историю журналов версий в общей книге
type: docs
weight: 80
url: /ru/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Возможные сценарии использования**

При обмене рабочими книгами появляется опция ***Сохранять историю изменений N дней***, как показано на следующем скриншоте. Вы можете обновить количество дней для сохранения истории с помощью свойства [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history) API Aspose.Cells для Python via .NET.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Обновление дней, сохраняющих историю журналов версий в общей книге**

В следующем образце кода создается пустая книга, затем ее делят и обновляются журналы ревизии для сохранения истории на 7 дней, что обычно составляет 30 дней. Пожалуйста, обратитесь к [выходному файлу Excel](60489773.xlsx), созданному кодом в качестве справки.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

