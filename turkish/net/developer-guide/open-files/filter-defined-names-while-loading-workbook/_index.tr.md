---
title: Çalışma Kitabı yüklenirken Tanımlı Adları Filtrele
type: docs
weight: 50
url: /tr/net/filter-defined-names-while-loading-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabında bulunan tanımlı adları filtrelemenize veya kaldırmanıza olanak tanır. Lütfen kullan[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)tanımlı adları yüklemek ve ~ kullanmak için[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)çalışma kitabını yüklerken bunları kaldırmak için. Lütfen unutmayın, tanımlı adları kaldırırsanız, çalışma kitabı içindeki formüller bozulabilir.

## **Çalışma Kitabı yüklenirken Tanımlı Adları Filtrele**

 Aşağıdaki örnek kod,[örnek excel dosyası](61767860.xlsx) hücrede formülü olan**C1** tanımlı adları içeren örn.*= TOPLA(Adım1, Adım2)*. ~ kullandığımız için[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) çalışma kitabını yüklerken tanımlı adları kaldırmak için C1 hücresindeki formül[çıktı excel dosyası](61767861.xlsx) kırılır ve görürsün*#NAME?*yerine. Lütfen kodun örnek Excel dosyası üzerindeki etkisini gösteren aşağıdaki ekran görüntüsüne bakın.

![yapılacaklar:resim_alternatif_Metin](filter-defined-names-while-loading-workbook_1.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
