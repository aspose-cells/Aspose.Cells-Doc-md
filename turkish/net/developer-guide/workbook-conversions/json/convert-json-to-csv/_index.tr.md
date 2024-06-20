---
title: JSON u CSV ye dönüştür
type: docs
weight: 210
url: /tr/net/convert-json-to-csv/
---

## **JSON'ı CSV'ye dönüştür**

Aspose.Cells, basit ve iç içe JSON'u CSV'ye dönüştürmeyi destekler. Bunun için API, [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) sınıfı, JSON düzeni için seçenekler sağlar, örneğin [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) (diziyi bir nesnenin özelliği olarak yoksayar) veya [**ArrayAsTable**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable) (diziyi tablo olarak işler). [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıfı, JSON'u [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) sınıfı ile ayarlanan düzen seçenekleriyle işler.

Aşağıdaki kod örneği, [kaynak JSON dosyasını](104398869.json) yükleme ve [çıktı CSV dosyasını](104398870.csv) oluşturma için [**JsonLayoutOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions) ve [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) sınıflarının kullanımını göstermektedir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
