---
title: Excel i ODS ye Dönüştür
type: docs
weight: 40
url: /tr/python-java/convert-excel-to-ods/
---

## **Excel'i ODS'ye Dönüştür**
ODS dosyaları, Apache OpenOffice Suite'in bir parçası olan Calc programı tarafından oluşturulur. ODS dosyaları, satır ve sütunlar şeklinde düzenlenmiş verileri depolar ve OASIS OpenDocument XML tabanlı standart kullanılarak biçimlendirilir.

Aspose.Cells for Python via Java, ODS dosyaları üzerinde çalışmayı destekler. Aşağıdaki örnekler, Excel'in ODS dosyasına dönüştürülmesini göstermektedir.
### **Doğrudan Dönüşüm**
Bir Excel dosyasını ODS'ye dönüştürmenin en basit yolu, çalışma kitabını yüklemek ve ikinci parametre olarak [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) 'i [Workbook.kaydet](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) metoduna geçirerek kaydetmektir.

Aşağıdaki kod örneği, Excel'in doğrudan ODS'ye dönüştürülmesini göstermektedir

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **ODS belgesini ODF 1.1 veya 1.2 Teknik Şartnamesine kaydet**
Aspose.Cells for Python via Java, ODF 1.1 ve ODF 1.2 teknik şartnamelerine göre ODS dosyalarını kaydetmeyi destekler. Bunun için API, [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) özelliğini sağlar. Bu özelliği **true** olarak ayarlamak, dosyanın ODF 1.1 şartnamesi ile kaydedilmesini sağlar. [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) 'ın varsayılan değeri **false** olduğundan, özel ayarlar olmadan kaydedilen ODS dosyası ODF 1.2 şartnamesi ile kaydedilir.

Aşağıdaki kod örneği, ODF 1.1 ve 1.2 şartnamelerine göre ODS dosyalarının kaydedilmesini göstermektedir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
