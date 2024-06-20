---
title: Bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında farklı yöntemler kullanarak otomatik uyarlama işlemlerini gerçekleştirir. Ekran görüntüsü, örnek kodun çalıştırılmasından sonra elde edilen sonuçları gösterir.
type: docs
weight: 120
url: /tr/python-net/autofit-rows-for-merged-cells/
description: Bu makale, Aspose.Cells for Python via .NET API si aracılığıyla birleştirilmiş hücreler için otomatik olarak satırları uyarlama yöntemini göstermektedir.
keywords: Python Excel Kütüphanesi, Python da Birleştirilmiş Hücreler için Satırları Otomatik Olarak Nasıl Kullanılır, Python da Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama.
---

{{% alert color="primary" %}}

Microsoft Excel, bir hücrenin içeriğine göre otomatik olarak hücre yüksekliğini ayarlamak için bir özellik sağlar. Bu özellik otomatik satırı uyarlama adını taşır. Microsoft Excel, birleştirilmiş hücrelerde otomatik sığdırma işlemini varsayılan olarak ayarlamaz. Bazen özellik, birleştirilmiş hücreler üzerinde otomatik satır uyarlama işlemi gerçekten uygulamak isteyen bir kullanıcı için önemli hale gelir.

{{% /alert %}}

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama Yöntemi**
Aspose.Cells for Python via .NET, bu özelliği [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API'sı aracılığıyla destekler. Bu API kullanılarak bir çalışma sayfasında, birleştirilmiş hücreler dahil olmak üzere satırları otomatik olarak uyarlama mümkün olmaktadır. İşte birleştirilmiş hücreleri otomatik olarak uyarlamanın tüm olası tiplerinin bir listesi:

- NONE
- FIRST_LINE
- LAST_LINE
- EACH_LINE

## **Birleştirilmiş Hücreler için Satırları Otomatik Olarak Ayarlama**

Lütfen aşağıdaki kodu görün, bir çalışma kitabı nesnesi oluşturur ve birden fazla çalışma sayfası ekler. Her çalışma sayfasında otomatik uyarlama işlemleri için farklı yöntemler kullanır. Ekran görüntüsü, örnek kodun yürütülmesinden sonra sonuçları göstermektedir.

<br>
<img src="result.png" width=80% />

## **C# Örnek Kodu**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
