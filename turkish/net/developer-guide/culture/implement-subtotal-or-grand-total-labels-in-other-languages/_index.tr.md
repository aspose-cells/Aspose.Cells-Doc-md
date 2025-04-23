---
title: Diğer dillerde Alt Toplam veya Genel Toplam etiketlerini uygulayın
type: docs
weight: 50
url: /tr/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **Olası Kullanım Senaryoları**

Bazen, Çin, Japon, Arap, Hint vb. gibi İngilizce olmayan dillerde, ara toplam ve genel toplam etiketlerini göstermek isteyebilirsiniz. Aspose.Cells, bu kullanmanıza izin verir [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfını ve [**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) özelliğini kullanarak. Lütfen [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfını nasıl kullanacağınızın bu makalesine bakınız.

- [Özel Ara Toplamların Kullanımı ve Pasta Grafiği Etiketleri İçin GlobalizationSettings Sınıfını Kullanma](/cells/tr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **Diğer dillerde Alt Toplam veya Genel Toplam etiketlerini uygulayın**

Aşağıdaki örnek kod, [örnek excel dosyasını](5115151.xlsx) yüklüyor ve Çince dilinde ara toplam ve genel toplam adlarını uygulamaktadır. Bu kodun oluşturduğu [çıktı Excel dosyasını](5115152.xlsx) referans için kontrol edin. Öncelikle [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfını oluşturuyoruz ve ardından kodumuzda kullanıyoruz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

Şimdi yukarıda oluşturulan sınıfı aşağıdaki gibi kodda kullanın:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
