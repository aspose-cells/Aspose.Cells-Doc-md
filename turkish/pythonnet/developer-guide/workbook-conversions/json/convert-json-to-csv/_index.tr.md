---
title: JSON u CSV ye dönüştür
type: docs
weight: 210
url: /tr/python-net/convert-json-to-csv/
description: Aspose.Cells for Python via .NET API ile json un csv dosyasına nasıl dönüştürüleceğini öğrenin.
keywords: Python da json ı csv ye dönüştürme, json ı csv ye dönüştürme Pyton via NET, json u csv ye dışa aktarma, json ı csv ye dönüştürme
---

## **JSON'ı CSV'ye dönüştür**

Aspose.Cells for Python via .NET, basit ve iç içe geçmiş JSON'un CSV'ye dönüştürülmesini destekler. Bunun için API, [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) sınıfı, JSON düzeni için seçenekleri sağlar like [**ignore_array_title**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/ignore_array_title/)(dizi bir nesnenin özelliği ise başlığı yok sayar) veya [**array_as_table**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions/array_as_table/)(diziyi bir tablo olarak işler). [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıfı, JSON'u [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) sınıfı ile ayarlanmış düzen seçenekleri kullanarak işler.

Aşağıdaki kod örneği, [kaynak JSON dosyasını](104398869.json) yükleme ve [çıktı CSV dosyasını](104398870.csv) oluşturma için [**JsonLayoutOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) sınıflarının kullanımını göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
