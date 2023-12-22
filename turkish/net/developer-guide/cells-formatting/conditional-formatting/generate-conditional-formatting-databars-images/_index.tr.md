---
title: Koşullu Biçimlendirme DataBars Görüntüleri Oluşturun
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Koşullu olarak biçimlendirilmiş veri çubuklarının ve görüntülerin oluşturulmasını destekleyerek kullanıcıların hücrelerin değerine göre elektronik tablonun görünümünü özelleştirmesine olanak tanır. Bu makale, koşullu olarak biçimlendirilmiş veri çubukları ve görüntüler oluşturmak için Aspose.Cells kitaplığının nasıl kullanılacağını tanıtacaktır.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /tr/net/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Bazen Koşullu Biçimlendirme DataBar'larının görüntülerini oluşturmanız gerekir. Aspose.Cells'i kullanabilirsiniz[**DataBar.ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage) Bu görüntüleri oluşturma yöntemi. Bu makalede Aspose.Cells kullanılarak DataBar görüntüsünün nasıl oluşturulacağı gösterilmektedir.

{{% /alert %}}

 Aşağıdaki örnek kod, C1 hücresinin DataBar görüntüsünü oluşturur. Öncelikle hücrenin format koşulu nesnesine erişir ve daha sonra bu nesneden[**Veri Çubuğu**](https://reference.aspose.com/cells/net/aspose.cells/databar) nesne ve onu kullanır[**ToImage()**](https://reference.aspose.com/cells/net/aspose.cells/databar/methods/toimage)Hücrenin görüntüsünü oluşturma yöntemi. Son olarak görüntüyü diske kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-GenerateDatabarImage-1.cs" >}}
