---
title: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 220
url: /tr/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET kullanarak çalışma kitabının Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bir çalışma kitabında bunu **false** olarak ayarladığınızda, Microsoft Excel bu Excel dosyasında Otomatik Kurtarma (Otomasave) özelliğini devre dışı bırakır.

Aspose.Cells for Python via .NET, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) özelliği sağlar.

{{% /alert %}}

Aşağıdaki kod, çalışma kitabının [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) özelliğinin nasıl kullanılacağını açıklar. Kod önce bu özelliğin varsayılan değeri olan **true**'yu okur, sonra onu **false** olarak ayarlar ve çalışma kitabını kaydeder. Ardından tekrar okur ve bu özelliğin şu anda **false** olduğunu gösterir.

## C# kodu ile Workbook'un AutoRecover özelliğinin ayarlanması

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Çıktı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
