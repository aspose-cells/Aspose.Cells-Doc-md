---
title: Çalışma Kitabının Otomatik Kurtarma özelliği nasıl ayarlanır?
type: docs
weight: 160
url: /tr/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Çalışma kitabının Otomatik Kurtarma özelliğini ayarlamak için Aspose.Cells'i kullanabilirsiniz. Bu özelliğin varsayılan değeri**doğru** . Ayarladığınızda**YANLIŞ** bir çalışma kitabında, Microsoft Excel, o Excel dosyasında Otomatik Kurtarma'yı (Otomatik kaydetme) devre dışı bırakır.

 Aspose.Cells sağlar[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) özelliği, bu seçeneği etkinleştirmek veya devre dışı bırakmak için.

{{% /alert %}}

## Çalışma Kitabının Otomatik Kurtarma özelliğini ayarlamak için Java kodu

 Aşağıdaki kod nasıl kullanılacağını açıklar[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) çalışma kitabının özelliği. Kod, önce bu özelliğin varsayılan değerini okur.**doğru** , ardından şu şekilde ayarlar:**YANLIŞ** ve çalışma kitabını kaydeder. Daha sonra çalışma kitabını tekrar okur ve bu özelliğin şu anda yanlış olan değerini okur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Örnek kod tarafından oluşturulan çıktı

İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
