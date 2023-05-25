---
title: Sayfa Yapısı Ölçeklendirme Faktörünü Hesapla
type: docs
weight: 300
url: /tr/net/calculate-page-setup-scaling-factor/
description: Bu makale, Excel çalışma sayfasının n sayfaya/sayfalara genişe m uzunluğa sığdır seçeneğini programlı olarak kullanarak Sayfa Yapısı ölçeklendirme faktörünü hesaplamak için C# API veya .NET kitaplığının nasıl kullanılacağını açıklayan örnek kod sağlar.
keywords: Fit to n page wide by m tall excel c#, calculate page setup scaling factor c#
---
{{% alert color="primary" %}}

 Sayfa Düzeni Ölçekleme'yi kullanarak ayarladığınızda**Genişliğe m uzunluğa n sayfaya sığdır** seçeneği, Microsoft Excel, Sayfa Yapısı Ölçeklendirme Faktörünü hesaplar. Aynı şeyi kullanarak hesaplayabilirsiniz.[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale)mülk. Bu özellik, yüzde değerine dönüştürülebilen bir çift değer döndürür. Örneğin, 0,5 döndürürse, ölçeklendirme faktörünün %50 olduğu anlamına gelir.

{{% /alert %}}

 Aşağıdaki örnek kod, kullanılarak sayfa düzeni ölçekleme faktörünün nasıl hesaplanacağını gösterir.[**SheetRender.PageScale**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/properties/pagescale) mülk.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CalculateScalingFactor-CalculatePageSetupScalingFactor.cs" >}}
