---
title: Paylaşılan Çalışma Kitabında Revision Günlükleriyle Geçmişi Korumak İçin Günleri Güncelleyin C++ ile
linktitle: Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Koruyan Günlük Günlerini Güncelleme Yöntemi
type: docs
weight: 80
url: /tr/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Aspose.Cells kullanarak C++ ile paylaşılan bir çalışma kitabında geçmişi koruma gün sayısını nasıl güncelleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Bir çalışma kitabını paylaştığınızda, aşağıdaki ekran görüntüsünde gösterildiği gibi ***N gün boyunca değişiklik geçmişini sakla*** seçeneğine sahip olursunuz. Aspose.Cells ile, değişiklik geçmişini koruma gün sayısını güncelleyebilirsiniz [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/) özelliğini kullanarak.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Paylaşılan Çalışma Kitabındaki Revizyon Günlüğü Tarihini Güncelleme**

Aşağıdaki örnek kod boş bir çalışma kitabı oluşturur, sonra onu paylaşır ve revizyon günlüklerini koruyarak normalde 30 gün olan geçmişi 7 gün olarak günceller. Lütfen [Kod tarafından oluşturulan çıktı Excel dosyasına](60489773.xlsx) bir referans için bakınız.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
