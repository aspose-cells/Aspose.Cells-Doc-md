---
title: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 220
url: /tr/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak çalışbook'un AutoRecover özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bir çalışbook'ta bunu **false** olarak ayarladığınızda, Microsoft Excel o Excel dosyasında AutoRecover'ı (Otomatik Kaydetme) devre dışı bırakır.

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki kod, çalışbook'un [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) özelliğini nasıl kullanacağını açıklamaktadır. Kod ilk olarak bu özelliğin varsayılan değerini olan **true**'u okur, sonra onu **false** olarak ayarlar ve çalışbook'u kaydeder. Ardından çalışbook'u tekrar okur ve bu özelliğin bu zamanda **false** olan değerini okur.

## C# kodu ile Workbook'un AutoRecover özelliğinin ayarlanması

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Çıktı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
