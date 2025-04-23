---
title: Bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında farklı yöntemler kullanarak otomatik uyarlama işlemlerini gerçekleştirir. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonuçları gösterir.
type: docs
weight: 120
url: /tr/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel, bir hücrenin içeriğine göre otomatik olarak hücre yüksekliğini ayarlamak için bir özellik sağlar. Bu özellik otomatik satırı uyarlama adını taşır. Microsoft Excel, birleştirilmiş hücrelerde otomatik sığdırma işlemini varsayılan olarak ayarlamaz. Bazen özellik, birleştirilmiş hücreler üzerinde otomatik satır uyarlama işlemi gerçekten uygulamak isteyen bir kullanıcı için önemli hale gelir.

{{% /alert %}}

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama Yöntemi**
Aspose.Cells, [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/) API'si aracılığıyla bu özelliği destekler. Bu API'yi kullanarak, birleştirilmiş hücreler de dahil olmak üzere bir çalışma sayfasındaki satırları otomatik olarak uyarlama mümkün olmaktadır. İşte birleştirilmiş hücreleri otomatik olarak uyarlamanın tüm olası türlerinin bir listesi:

- Hiçbiri
- İlk Satır
- Son Satır
- HerSatir

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama**

Lütfen aşağıdaki kodu görün, bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında otomatik uyarlama işlemleri için farklı yöntemler kullanır. Ekran görüntüsü, örnek kodun yürütülmesinden sonra sonuçları göstermektedir.

<br>
<img src="result.png" width=80% />

## **C# Örnek Kodu**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
