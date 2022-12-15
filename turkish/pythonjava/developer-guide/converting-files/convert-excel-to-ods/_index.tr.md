---
title: Excel'i ODS'ye dönüştür
type: docs
weight: 40
url: /tr/python-java/convert-excel-to-ods/
---
## **Excel'i ODS'ye dönüştür**
ODS dosyaları, Apache OpenOffice Suite'in bir parçası olan Calc programı tarafından oluşturulur. ODS dosyaları, satırlar ve sütunlar halinde düzenlenmiş ve OASIS OpenDocument XML tabanlı standardı kullanılarak biçimlendirilmiş verileri depolar.

Aspose.Cells for Python via Java çalışan ODS dosyalarını destekler. Aşağıdaki örnekler, Excel'in bir ODS dosyasına dönüştürülmesini göstermektedir.
### **Doğrudan Dönüşüm**
Bir Excel dosyasını ODS'ye dönüştürmenin en basit yolu, çalışma kitabını yüklemek ve geçerek kaydetmektir.[SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) ikinci parametre olarak[çalışma kitabı.kaydet](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) yöntem.

Aşağıdaki kod parçacığı, Excel'in doğrudan ODS'ye dönüştürüldüğünü gösterdi

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **ODS belgesini ODF 1.1 veya 1.2 Spesifikasyonlarına kaydedin**
Aspose.Cells for Python via Java, ODS dosyalarını ODF 1.1 ve ODF 1.2 spesifikasyonlarında kaydetmeyi destekler. Bunun için API,[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) Emlak. Bu özellik şu şekilde ayarlanıyor:**doğru** dosyayı ODF 1.1 spesifikasyonu ile kaydedecektir. varsayılan değeri[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) dır-dir**yanlış**, böylece özel ayarlar olmadan kaydedilen ODS dosyası ODF 1.2 spesifikasyonu ile kaydedilir.

Aşağıdaki kod parçacığı, ODS dosyalarını ODF 1.1 ve 1.2 spesifikasyonlarıyla kaydetmeyi gösterdi.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
