---
title: Birleştirilmiş Satırları Otomatik Sığdır Cells
type: docs
weight: 120
url: /tr/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel, bir hücrenin yüksekliğini içeriğine göre otomatik olarak boyutlandırmanıza olanak tanıyan bir özellik sağlar. Bu özelliğe satırları otomatik sığdır adı verilir. Microsoft Excel, birleştirilmiş hücrelerde otomatik sığdırma işlemini yerel olarak ayarlamaz. Bazen bu özellik, satırları birleştirilmiş hücrelere de otomatik sığdırması gereken bir kullanıcı için hayati önem taşıyor.

{{% /alert %}}

##  **Satırları otomatik sığdırmak için AutoFitMergedCellsType nasıl kullanılır?**
 Aspose.Cells bu özelliği şu şekilde destekler:[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Bu API'i kullanarak, birleştirilmiş hücreler de dahil olmak üzere bir çalışma sayfasındaki satırları otomatik olarak sığdırmak mümkündür. Otomatik sığdırılan birleştirilmiş hücrelerin tüm olası türlerinin bir listesi:

- Hiçbiri
- İlk satır
- Son Satır
- Her çizgi

##  **Birleştirilmiş Satırları Otomatik Sığdır Cells**

Lütfen aşağıdaki koda bakın, bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında otomatik sığdırma işlemleri için farklı yöntemler kullanın. Ekran görüntüsü, örnek kodun yürütülmesinden sonraki sonuçları gösterir.

<br>
<img src="result.png" width=80% />

##  **C# Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
