---
title: JSON'i CSV'e dönüştür
type: docs
weight: 210
url: /tr/net/convert-json-to-csv/
---
## **JSON'i CSV'e dönüştür**

Aspose.Cells, basit ve yuvalanmış JSON'in CSV'e dönüştürülmesini destekler. Bunun için API şunları sağlar:**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** ve**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** sınıflar. bu**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**class, JSON düzeni için aşağıdaki gibi seçenekler sunar**[IgnoreArrayTitle](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(dizi bir nesnenin özelliğiyse başlığı yok sayar) veya**[ArrayAsTable](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(diziyi tablo olarak işler). bu**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**class, JSON ile ayarlanan düzen seçeneklerini kullanarak işler.**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**sınıf.

Aşağıdaki kod örneği, kullanımını gösterir**[JsonLayoutOptions](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**ve**[JsonUtility](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** yüklemek için sınıflar[kaynak JSON dosyası](104398869.json) ve oluşturur[çıktı CSV dosyası](104398870.csv).

### **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
