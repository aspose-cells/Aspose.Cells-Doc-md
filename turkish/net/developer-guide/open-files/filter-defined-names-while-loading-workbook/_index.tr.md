---
title: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/net/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, çalışma kitabı içinde bulunan tanımlı adları filtrelemenize veya kaldırmanıza izin verir. Lütfen çalışma kitabını yüklerken tanımlı adları yüklemek için [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) kullanın ve kaldırmak için ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) kullanın. Lütfen unutmayın, eğer tanımlı adları kaldırırsanız, çalışma kitabı içindeki formüller bozulabilir.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, tanımlı isimleri içeren formül içeren *C1* hücresinde bir [örnek Excel dosyası](61767860.xlsx) yükler. ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) kullanarak çalışma kitabını yüklerken tanımlı isimleri kaldırdığımızdan, [çıktı Excel dosyasında](61767861.xlsx) *C1* hücresindeki formül bozulur ve *#NAME?* görünür. Lütfen örnekteki etkiyi gösteren aşağıdaki ekran görüntüsüne bakınız.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
