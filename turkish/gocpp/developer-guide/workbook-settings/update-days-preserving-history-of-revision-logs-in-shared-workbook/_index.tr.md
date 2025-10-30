---
title: Golang ile C++ kullanarak Paylaşılan Çalışma Kitabında Revizyon Günlüklerinin geçmişini koruyarak Günleri Güncelleyin
linktitle: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi
type: docs
weight: 80
url: /tr/go-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Golang ile C++ kullanarak Paylaşılan çalışma kitabında geçmişi koruma gün sayısını nasıl güncelleneceğini öğrenin
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün boyunca değişiklik geçmişini sakla*** seçeneğine sahip olursunuz. Aspose.Cells ile, değişiklik geçmişini koruma gün sayısını güncelleyebilirsiniz [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/go-cpp/revisionlogcollection/getdayspreservinghistory/) özelliğini kullanarak.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur, sonra onu paylaşır ve revizyon günlüklerini koruyarak normalde 30 gün olan geçmişi 7 gün olarak günceller. Lütfen [Kod tarafından oluşturulan çıktı Excel dosyasına](60489773.xlsx) bir referans için bakınız.

## **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UpdateDaysPreservingHistoryOfRevisionLogsInSharedWorkbook.go" >}}
