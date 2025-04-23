---
title: Özel Alt Toplam Etiketleri ve Pasta Grafiği Diğer Etiketleri İçin GlobalizationSettings Sınıfını Kullanma
type: docs
weight: 70
url: /tr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, kullanıcının elektronik tabloda Özel Alt Toplam etiketleri kullanmak istediği senaryolarla başa çıkmak için [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfını açığa çıkarmıştır. Ayrıca, [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı, çalışma sayfasını veya çizimi render ederken **Diğer** etiketi için özel metni değiştirmek için kullanılabilir.

## **GlobalizationSettings Sınıfı Tanıtımı**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı şu anda istenen toplam etiketleri almak için özelleştirilmiş bir sınıfta geçersiz kılınabilen aşağıdaki 3 yöntemi sunmaktadır veya bir Pasta grafiğinin **Diğer** etiketi için özel metni oluşturmak için.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Fonksiyonun toplam ismini alır.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Fonksiyonun genel toplam ismini alır.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Pie grafikleri için "Diğer" etiketlerin adını alır.

### **Alt toplamlar için özel etiketler**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı, alt toplam etiketlerini özelleştirmek için önümüzdeki gibi [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) ve [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) yöntemlerini geçersiz kılma amacıyla kullanılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

Özel etiketler enjekte etmek için, Alt toplamları çalışma sayfasına eklemek öncesinde yukarıda tanımlanan **CustomSettings** sınıfına bir örnek atamak gereklidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı yalnızca yeni Alt toplamları eklemek için çalışır. Bir elektronik tablo zaten Alt toplamlar içeriyorsa, etiketleri değiştirilemez.

{{% /alert %}}

### **Pasta Grafiği için Diğer Etiket için Özel Metin**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı, Pasta grafiklerinin "Diğer" etiketine özel bir değer vermek için yararlı olan [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) yöntemi sunar. Aşağıdaki kesit, bir özel sınıfı tanımlar ve sistem kültür tanımlayıcısına dayalı bir özel etiket almak için [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) yöntemini geçersiz kılar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

Aşağıdaki kesit, yukarıda oluşturulan **CustomSettings** sınıfını kullanarak bir Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve grafiği resim olarak oluşturur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
