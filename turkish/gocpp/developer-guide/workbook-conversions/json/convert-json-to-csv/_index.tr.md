---
title: JSON u CSV ye Dönüştür, Golang ve C++ ile
linktitle: JSON u CSV ye dönüştür
type: docs
weight: 210
url: /tr/go-cpp/convert-json-to-csv/
description: Aspose.Cells for C++ kullanarak basit ve iç içe JSON örnekleri ile JSON dan CSV ye nasıl dönüştürüleceğini öğrenin.
---

## **JSON'ı CSV'ye dönüştür**

Aspose.Cells, basit ve iç içe JSON'u CSV'ye dönüştürmeyi destekler. Bunun için API [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını sağlar. [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) sınıfı, [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (diziyi bir nesnenin özelliği ise başlığı yoksayar) veya [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (diziyi tablo olarak işler) gibi JSON düzeni seçenekleri sunar. [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıfı, JSON'u [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) sınıfı ile ayarlanmış düzen seçeneklerini kullanarak işler.

Aşağıdaki kod örneği, [kaynak JSON dosyasını](104398869.json) yüklemek ve [çıktı CSV dosyasını](104398870.csv) oluşturmak için [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) ve [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) sınıflarını kullanmayı gösterir.

### **Örnek Kod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
