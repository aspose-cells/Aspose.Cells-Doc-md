---
title: Çalışma Kitabı yüklenirken Tanımlı Adları Filtrele
type: docs
weight: 50
url: /tr/java/filter-defined-names-while-loading-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabında bulunan tanımlı adları filtrelemenize veya kaldırmanıza olanak tanır. Lütfen kullan[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)tanımlı adları yüklemek ve ~ kullanmak için[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)çalışma kitabını yüklerken bunları kaldırmak için. Lütfen unutmayın, tanımlı adları kaldırırsanız, çalışma kitabı içindeki formüller bozulabilir.

## **Çalışma Kitabı yüklenirken Tanımlı Adları Filtrele**

Aşağıdaki örnek kod,[örnek excel dosyası](61767873.xlsx)C1 hücresinde tanımlanmış adları içeren bir formüle sahip olan, yani*= TOPLA(Adım1, Adım2)*. Çünkü ~ kullanıyoruz[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)çalışma kitabını yüklerken tanımlı adları kaldırmak için C1 hücresindeki formül[çıktı excel dosyası](61767872.xlsx)kırılır ve görürsün*#NAME?*yerine. Lütfen kodun örnek Excel dosyası üzerindeki etkisini gösteren aşağıdaki ekran görüntüsüne bakın.

![yapılacaklar:resim_alternatif_metin](filter-defined-names-while-loading-workbook_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
