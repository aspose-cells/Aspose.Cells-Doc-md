---
title: JSON u CSV ye dönüştür
type: docs
weight: 160
url: /tr/java/convert-json-to-csv/
---

Aspose.Cells, basit ve iç içe JSON'u CSV'ye dönüştürmeyi destekler. Bunun için API, [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) ve [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıfı, JSON düzeni için seçenekler sağlar, örneğin [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle) (dizi bir nesnenin özelliği ise başlığı yoksayar) veya [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable) (dizi bir tablo olarak işler). [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıfı, [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıfı tarafından belirlenen düzen seçeneklerini kullanarak JSON'u işler.

Aşağıdaki kod örneği, [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) ve [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıflarını yüklemek için kullanır, [kaynak JSON dosyası](ÖrnekJson.json) 'ı alır ve [çıktı CSV dosyasını](ÖrnekJson_out.csv) oluşturur.

## Örnek Kod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
