---
title: Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele
type: docs
weight: 50
url: /tr/python-net/filter-defined-names-while-loading-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET, çalışma kitabı içindeki tanımlı isimleri filtrelemenize veya kaldırmanıza izin verir. [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) kullanarak tanımlı isimleri yükleyebilir ve ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) kullanarak yüklerken kaldırabilirsiniz. Lütfen, tanımlı isimleri kaldırırsanız, çalışma kitabı içindeki formüller bozulabilir.

## **Çalışma Kitabını yüklerken Tanımlanmış Adları Filtrele**

Aşağıdaki örnek kod, tanımlı isimleri içeren formül içeren *C1* hücresinde bir [örnek Excel dosyası](61767860.xlsx) yükler. ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) kullanarak çalışma kitabını yüklerken tanımlı isimleri kaldırdığımızdan, [çıktı Excel dosyasında](61767861.xlsx) *C1* hücresindeki formül bozulur ve *#NAME?* görünür. Lütfen örnekteki etkiyi gösteren aşağıdaki ekran görüntüsüne bakınız.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
