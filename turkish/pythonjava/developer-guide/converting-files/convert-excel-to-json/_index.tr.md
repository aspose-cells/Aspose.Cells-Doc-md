---
title: Excel i JSON a Dönüştür
type: docs
weight: 300
url: /tr/python-java/convert-excel-to-json/
description: Aspose.Cells for Python via Java ile excel dosyasını json a dönüştürme konusunu öğrenin.
keywords: Ofis 2013, ofis 2016, ofis 2019 ve ofis 365 olmadan çalışma kitabını json olarak dışa aktarma
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java, Dosya Json(JavaScript Object Notation) 'a dönüştürmeyi destekler.

{{% /alert %}}

## **Excel Çalışma Kitabını JSON'a Dönüştür**

Excel Çalışma Kitabı'nı JSON'a dönüştürmek için Aspose.Cells for Python via Java kütüphanesinin en iyi kararı olduğundan emin olmak zorunda değilsiniz. Aspose.Cells for Python via Java API'si, elektronik tabloları JSON biçimine dönüştürmeyi destekler. Çalışma kitabını JSON'a dışa aktarmak için, [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)) metodunun ikinci parametresi olarak [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat)'ü geçirin. Elektronik tabloyu JSON biçimine dışa aktarmak için ek ayarları belirtmek için [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) sınıfını da kullanabilirsiniz.

Aşağıdaki kod örneği, Excel Çalışma Kitabı'nın Json olarak dışa aktarılmasını gösterir. Referans için, kod tarafından oluşturulan Json dosyası için [örnek dosyayı](sample.xlsx) dönüştürme koduna bakın.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

Aşağıdaki kod örneği, ek ayarları belirtmek için JsonSaveOptions sınıfını kullanan Excel Workbook'ünü Json olarak dışa aktarmanın bir örneğini göstermektedir. Referans için kodu görmek için [kaynak dosyayı](sample.xlsx) kodla üretilen Json dosyası ile birlikte inceleyin.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
