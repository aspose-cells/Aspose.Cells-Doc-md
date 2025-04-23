---
title: Bir Çalışma Sayfasından Pivot Tablosunu Sil
type: docs
weight: 60
url: /tr/nodejs-cpp/delete-pivot-table-from-a-worksheet/
description: Excel Sayfalarına PivotTable Kaldırmak İçin Aspose.Cells for Node.js via C++ Kodu
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js kütüphanesi, çalışma sayfasından pivot tablo kaldırma, excel den pivot tablo kaldırma, Aspose.Cells for Node.js via C++ ile pivot tablo nasıl silinir, pivot tablo sil, excel den pivot tablo sil, pivot tablo sil, Aspose.Cells for Node.js via C++ pivot tablo kaldırma, pivot tablo kaldır, pivot tablo silme, pivot tablo nasıl silinir? 
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++, bir Çalışma Sayfasından Pivot Tablo silme veya kaldırma özelliği sağlar. Pivot tablo nesnesini veya pivot tablo konumunu kullanarak pivot tabloyu silebilirsiniz. Pivot tabloyu silmek için, pivot tablo nesnesi kullanılarak [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) yöntemini ve Pivot tablo koleksiyonundaki konum kullanılarak [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) yöntemini kullanın.

{{% /alert %}}

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Sayfasından Pivot Tablo nasıl silinir**

Aşağıdaki örnek kod, çalışma sayfasından iki pivot tablosunu siler. İlk önce [**Worksheet.getPivotTables().remove(pivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#remove-pivottable-) yöntemini kullanarak pivot tablosunu kaldırır, ardından [**Worksheet.getPivotTables().removeAt(index, keepData)**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#removeAt-number-boolean-) yöntemini kullanarak pivot tablosunu kaldırır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.js" >}}
