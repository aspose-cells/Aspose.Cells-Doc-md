---
title: Lisansın Başarıyla Yüklendiğini Belirleme
type: docs
weight: 260
url: /tr/net/determining-if-the-license-is-loaded-successfully/
description: Lisansın başarıyla yüklendiğini Aspose.Cells for NET API leri üzerinden nasıl algılayacağınızı öğrenin.
keywords: C# da Lisansın Başarıyla Yüklendiğini Nasıl Algılayacağınız, C# kullanarak Lisansın Başarıyla Yüklendiğini Belirleme, C# ile Lisansın Başarıyla Yüklendiğini Kontrol Etme, Lisansın Durumunu Kontrol Etme.
---

{{% alert color="primary" %}}

Aspose.Cells, lisansın başarıyla yüklendiğini belirlemek için [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) özelliğini sağlar. Bu özelliği lisansı ayarlamadan önce erişirseniz **false** döndürecek, lisansı ayarladıktan sonra ise başarıyla yüklendiğini belirten **true** döndürecektir.

{{% /alert %}}

## Lisansın Başarıyla Yüklendiğini Belirleme için C# kodu

Aşağıdaki kod, bir lisansı ayarlamadan önce [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) özelliğine erişir ve **false** döndürür. Ardından lisansı yükler ve tekrar özelliğe erişir, bu kez **true** döner.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol (hata ayıklama) çıktısı şöyle

{{< highlight java >}}

False

True

{{< /highlight >}}
