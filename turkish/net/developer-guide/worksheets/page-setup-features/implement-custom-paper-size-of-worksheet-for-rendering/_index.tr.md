---
title: Otomatik Olarak Çalışma Sayfası Kağıt Boyutunun Oluşturulması için Özelleştirilmiş Kağıt Boyutunun Uygulanması
type: docs
weight: 70
url: /tr/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Bu makale, Excel dosyasını PDF dosya biçimine programlı olarak dönüştürürken istediğiniz çalışma sayfalarının özel kağıt boyutunu ayarlamak için C# API veya .NET Kütüphane örnek kodunu nasıl kullanacağınızı açıklar.
keywords: c# ile excel i pdf olarak döndürürken özel kağıt boyutu ayarlama
---

## **Olası Kullanım Senaryoları**

MS Excel'de özel kağıt boyutları oluşturmak için doğrudan bir seçenek bulunmamaktadır, ancak Excel dosyasını PDF dosya biçimine dönüştürürken istediğiniz çalışma sayfasının özel kağıt boyutunu ayarlayabilirsiniz. Bu belge, Aspose.Cells API'larını kullanarak çalışma sayfasının özel kağıt boyutunu nasıl ayarlayacağınızı açıklar.

## **Otomatik Olarak Çalışma Sayfası için Özel Kağıt Boyutunun Uygulanması**

Aspose.Cells, çalışma sayfasının istediğiniz kağıt boyutunu uygulamanıza olanak tanır. İlk çalışma sayfası için özel bir sayfa boyutu belirtmek için [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) sınıfının [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) metodunu kullanabilirsiniz. Aşağıdaki örnek kod, çalışma kitabındaki ilk çalışma sayfası için özel bir kağıt boyutunu belirtmenin nasıl olduğunu açıklar. Lütfen ayrıca aşağıdaki kod ile oluşturulan [çıktı PDF](45056028.pdf) dosyasını referans için inceleyin.

## **Ekran Görüntüsü**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
{{< app/cells/assistant language="csharp" >}}
