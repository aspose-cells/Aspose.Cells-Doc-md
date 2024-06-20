---
title: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/java/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabı içinde bulunan tanımlı adları filtrelemenize veya kaldırmanıza izin verir. Lütfen çalışma kitabını yüklerken tanımlı adları yüklemek için [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) kullanın ve kaldırmak için ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) kullanın. Lütfen unutmayın, eğer tanımlı adları kaldırırsanız, çalışma kitabı içindeki formüller bozulabilir.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, içinde MyName1 ve MyName2 isimli tanımlı adları olan [örnek Excel dosyasını](61767873.xlsx) yükler. Çalışma kitabını yüklerken tanımlı adları kaldırmak için ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES) kullandığımızdan, formül içeren C1 hücresindeki formül [çıktı Excel dosyasında](61767872.xlsx) bozulur ve *#NAME?* görürsünüz. Lütfen, örnek Excel dosyasındaki kodun etkisini gösteren aşağıdaki ekran görüntüsüne bakınız.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
