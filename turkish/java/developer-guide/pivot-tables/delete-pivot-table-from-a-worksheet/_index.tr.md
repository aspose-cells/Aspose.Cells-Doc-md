---
title: Bir Çalışma Sayfasından Pivot Tablosunu Sil
type: docs
weight: 50
url: /tr/java/delete-pivot-table-from-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells, bir Pivot Tablosunu bir Çalışma Sayfasından silme veya kaldırma özelliği sağlar. Pivot tablosunu pivot tablo nesnesini veya konumunu kullanarak silebilirsiniz. Lütfen pivot tablosunu silmek için [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) yöntemini kullanın ve konumu içinde pivot tablosu nesnesini silmek için [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) yöntemini kullanın.

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod, çalışma sayfasından iki pivot tablosunu siler. İlk olarak, pivot tablosunu [**Worksheet.getPivotTables().remove()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#remove-com.aspose.cells.PivotTable-) yöntemini kullanarak kaldırır ve ardından pivot tablosunu konumu kullanarak [**Worksheet.getPivotTables().removeAt()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#removeAt-int-) yöntemini kullanarak kaldırır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DeletePivotTableFromWorksheet-DeletePivotTableFromWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
