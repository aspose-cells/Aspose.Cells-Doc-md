---
title: Özel Ara Toplam Etiketleri ve Pasta Grafiğinin Diğer Etiketi için GlobalizationSettings Sınıfını Kullanma
type: docs
weight: 50
url: /tr/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Olası Kullanım Senaryoları**
 Aspose.Cells API'ler şu bilgileri açığa çıkardı:[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) kullanıcının bir e-tabloda Alt Toplamlar için özel etiketler kullanmak istediği senaryolarla başa çıkmak için sınıf. Ayrıca,[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıf aynı zamanda değiştirmek için de kullanılabilir.**Diğer** çalışma sayfasını veya grafiği işlerken Pasta grafiği için etiket.
## **GlobalizationSettings Sınıfına Giriş**
 bu[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class şu anda, Alt Toplamlar için istenen etiketleri almak veya alt toplamlar için özel metin oluşturmak üzere özel bir sınıfta geçersiz kılınabilen aşağıdaki 3 yöntemi sunmaktadır.**Diğer** Pasta grafiğin etiketi.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Fonksiyonun toplam adını alır.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Fonksiyonun genel toplam adını alır.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Pasta grafikler için "Diğer" etiketlerinin adını alır.
### **Ara Toplamlar için Özel Etiketler**
 bu[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)sınıfı geçersiz kılarak Ara Toplam etiketlerini özelleştirmek için kullanılabilir.[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) yöntemler aşağıda gösterildiği gibi.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Özel etiketleri enjekte etmek için,[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) özelliğinin bir örneğine*Özel ayarlar*alt toplamları çalışma sayfasına eklemeden önce yukarıda tanımlanan sınıf.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 bu[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)class yalnızca yeni Ara Toplamlar eklemek için çalışır. Bir e-tablo zaten Ara Toplamlar içeriyorsa etiketleri değiştirilemez.

{{% /alert %}} 
### **Pasta Grafiğinin Diğer Etiketi için Özel Metin**
 bu[KüreselleşmeAyarları](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıf şunları sunar:[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) Pasta grafiklerinin "Diğer" etiketine özel bir değer vermek için yararlı olan yöntem. Aşağıdaki kod parçacığı, özel bir sınıfı tanımlar ve[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) yöntemi, JVM için varsayılan dil ayarını temel alan özel bir etiket alma yöntemidir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Aşağıdaki kod parçacığı, bir Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve*Özel ayarlar*Yukarıda oluşturulan sınıf.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Aşağıdaki, makinenin yerel ayarı Fransa olarak ayarlandığında ortaya çıkan görüntüdür. Gördüğünüz gibi "Diğer" etiketi, içinde tanımlandığı gibi "Yazar" olarak çevrilmiştir.*Özel ayarlar*sınıf.

![yapılacaklar:resim_alternatif_metin](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
