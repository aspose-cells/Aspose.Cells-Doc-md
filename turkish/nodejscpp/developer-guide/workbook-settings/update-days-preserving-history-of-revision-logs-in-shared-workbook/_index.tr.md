---  
title: Paylaşılan Çalışma Kitabında Revizyon Günlüklerini Korumak için Günleri Güncelleme ile Node.js ve C++ kullanma  
linktitle: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/  
description: Aspose.Cells for Node.js via C++ kullanarak paylaşılan çalışma kitaplarındaki revizyon günlüklerini koruma günlerini nasıl güncelleyeceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**

Çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün için değişiklik geçmişini sakla*** seçeneği bulunur. Aspose.Cells for Node.js via C++ kullanarak, [**WorksheetCollection.getDaysPreservingHistory()**](https://reference.aspose.com/cells/nodejs-cpp/revisionlogcollection/#getDaysPreservingHistory--) özelliği ile geçmişi koruma gün sayısını güncelleyebilirsiniz.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur, sonra onu paylaşır ve revizyon günlüklerini koruyarak normalde 30 gün olan geçmişi 7 gün olarak günceller. Lütfen [Kod tarafından oluşturulan çıktı Excel dosyasına](60489773.xlsx) bir referans için bakınız.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty workbook
const workbook = new AsposeCells.Workbook();

// Share the workbook
workbook.getSettings().setShared(true);

// Update DaysPreservingHistory of RevisionLogs
workbook.getWorksheets().getRevisionLogs().setDaysPreservingHistory(7);

// Save the workbook
workbook.save("outputShared_DaysPreservingHistory.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
