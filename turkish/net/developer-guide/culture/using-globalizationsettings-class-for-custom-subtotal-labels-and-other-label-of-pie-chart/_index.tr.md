---
title: Özel Ara Toplam Etiketleri ve Pasta Grafiğinin Diğer Etiketi için GlobalizationSettings Sınıfını Kullanma
type: docs
weight: 70
url: /tr/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Olası Kullanım Senaryoları**

 Aspose.Cells API'ler şu bilgileri açığa çıkardı:[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)kullanıcının bir e-tabloda Alt Toplamlar için özel etiketler kullanmak istediği senaryolarla başa çıkmak için sınıf. Ayrıca,[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)sınıf aynı zamanda değiştirmek için de kullanılabilir.**Başka** çalışma sayfasını veya grafiği işlerken Pasta grafiği için etiket.

## **GlobalizationSettings Sınıfına Giriş**

 bu[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) class şu anda, Alt Toplamlar için istenen etiketleri almak veya alt toplamlar için özel metin oluşturmak üzere özel bir sınıfta geçersiz kılınabilen aşağıdaki 3 yöntemi sunmaktadır.**Başka** Pasta grafiğin etiketi.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): Fonksiyonun toplam adını alır.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): Fonksiyonun genel toplam adını alır.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): Pasta grafikler için "Diğer" etiketlerinin adını alır.

### **Ara Toplamlar için Özel Etiketler**

 bu[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıfı geçersiz kılarak Ara Toplam etiketlerini özelleştirmek için kullanılabilir.[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)Yöntemler ileride gösterildiği gibi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 Özel etiketleri enjekte etmek için,[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) özelliğinin bir örneğine**Özel ayarlar**alt toplamları çalışma sayfasına eklemeden önce yukarıda tanımlanan sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 bu[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)class yalnızca yeni Ara Toplamlar eklemek için çalışır. Bir e-tablo zaten Ara Toplamlar içeriyorsa etiketleri değiştirilemez.

{{% /alert %}}

### **Pasta Grafiğinin Diğer Etiketi için Özel Metin**

 bu[**KüreselleşmeAyarları**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) sınıf teklifleri[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)Pasta grafiklerinin "Diğer" etiketine özel bir değer vermek için yararlı olan bir yöntem. Aşağıdaki kod parçacığı, özel bir sınıfı tanımlar ve[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)sistemin kültür tanımlayıcısına dayalı özel bir etiket alma yöntemi.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 Aşağıdaki kod parçacığı, bir Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve**Özel ayarlar**Yukarıda oluşturulan sınıf.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
