---
title: Çalışma Kitabının Otomatik Kurtarma özelliği nasıl ayarlanır?
type: docs
weight: 220
url: /tr/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Çalışma kitabının Otomatik Kurtarma özelliğini ayarlamak için Aspose.Cells'i kullanabilirsiniz. Bu özelliğin varsayılan değeri**doğru** . Ayarladığınızda**YANLIŞ** bir çalışma kitabında, Microsoft Excel, o Excel dosyasında Otomatik Kurtarma'yı (Otomatik kaydetme) devre dışı bırakır.

 Aspose.Cells sağlar[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) özelliği, bu seçeneği etkinleştirmek veya devre dışı bırakmak için.

{{% /alert %}}

 Aşağıdaki kod nasıl kullanılacağını açıklar[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) çalışma kitabının özelliği. Kod, önce bu özelliğin varsayılan değerini okur.**doğru** , ardından şu şekilde ayarlar:**YANLIŞ** ve çalışma kitabını kaydeder. Daha sonra çalışma kitabını tekrar okur ve bu özelliğin değerini okur.**YANLIŞ** şu anda.

## Çalışma Kitabının Otomatik Kurtarma özelliğini ayarlamak için C# kodu

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Çıktı**

İşte yukarıdaki örnek kodun konsol çıktısı.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
