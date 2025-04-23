---
title: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 160
url: /tr/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak çalışma kitabının Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**. Eğer bir çalışma kitabında bunu **false** olarak ayarlarsanız, Microsoft Excel Otomatik Kurtarma (Oto Kaydet) özelliğini devre dışı bırakır.

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) özelliğini sağlar.

{{% /alert %}}

## Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak için Java Kodu

Aşağıdaki kod, çalışma kitabının [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) özelliğinin nasıl kullanılacağını açıklar. Kod önce bu özelliğin varsayılan değerini (**true**) okur, ardından onu **false** olarak ayarlar ve çalışma kitabını kaydeder. Sonra çalışma kitabını tekrar okur ve bu özelliğin o anda **false** olan değerini okur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Örnek Kod Tarafından Oluşturulan Çıkış

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
