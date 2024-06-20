---
title: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi
type: docs
weight: 90
url: /tr/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/
---

## **Olası Kullanım Senaryoları**

Çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün boyunca değişiklik geçmişini sakla*** seçeneğini alırsınız. Aspose.Cells ile bu tarihi koruma gün sayısını güncelleyebilirsiniz, [**WorksheetCollection.RevisionLogs.DaysPreservingHistory**](https://reference.aspose.com/cells/java/com.aspose.cells/revisionlogcollection#DaysPreservingHistory) özelliği ile.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod, boş bir çalışma kitabı oluşturur, ardından paylaşır ve genellikle 30 gün olan revizyon kayıtlarını koruma günlerini 7 gün olarak günceller. Bu kod tarafından oluşturulan [çıkış Excel dosyası](60489784.xlsx) referans için eklenmiştir.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.java" >}}
