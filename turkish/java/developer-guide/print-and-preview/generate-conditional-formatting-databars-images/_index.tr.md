---
title: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
type: docs
weight: 170
url: /tr/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod, hücre C1'in DataBar görüntüsünü oluşturur. İlk olarak, hücrenin biçim koşulu nesnesine erişir, ardından bu nesneden DataBar nesnesine erişir ve hücrenin görüntüsünü oluşturmak için [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) yöntemini kullanır. Son olarak, görüntüyü diske kaydeder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
