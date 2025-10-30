---
title: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi
type: docs
weight: 80
url: /tr/python-net/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün boyunca değişiklik geçmişini sakla*** seçeneğini görebilirsiniz. Bu geçmişi koruma süresini gün cinsinden güncellemek için Aspose.Cells for Python via .NET'nin [**WorksheetCollection.revision_logs.days_preserving_history**](https://reference.aspose.com/cells/python-net/aspose.cells.revisions/revisionlogcollection/days_preserving_history) özelliğini kullanabilirsiniz.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur, sonra onu paylaşır ve revizyon günlüklerini koruyarak normalde 30 gün olan geçmişi 7 gün olarak günceller. Lütfen [Kod tarafından oluşturulan çıktı Excel dosyasına](60489773.xlsx) bir referans için bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
