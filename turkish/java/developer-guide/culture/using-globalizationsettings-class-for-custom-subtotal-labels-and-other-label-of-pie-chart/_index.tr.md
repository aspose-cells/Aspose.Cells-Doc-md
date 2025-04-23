---
title: Özel Alt Toplam Etiketleri ve Pasta Grafiği Diğer Etiketleri İçin GlobalizationSettings Sınıfını Kullanma
type: docs
weight: 50
url: /tr/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells API'leri, bir elektronik tabloda Alt Toplamlar için özel etiketler kullanmak isteyen kullanıcıların senaryolarıyla başa çıkmak için [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfını ortaya çıkardı. Dahası, [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfı, çalışma sayfası veya grafik oluştururken Pasta Grafiği için **Diğer** etiketini değiştirmek için de kullanılabilir.
## **GlobalizationSettings Sınıfı Tanıtımı**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfı şu anda istenen etiketleri almak için özelleştirilebilen 3 yöntem sunmaktadır veya Pasta grafiği için **Diğer** etiketi oluşturulabilir.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Fonksiyonun toplam adını alır.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Fonksiyonun genel toplam adını alır.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Pie grafikler için "Diğer" etiketlerinin adını alır.
### **Alt toplamlar için özel etiketler**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfı, [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) yöntemlerinin üzerine yazarak Alt toplam etiketlerini özelleştirmek için kullanılabilir, aşağıda gösterilmektedir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Özel Etiketlerin eklenmesi için, Özelleştirilmiş Alt Toplam kullanmadan önce **WorkbookSettings.GlobalizationSettings** özelliğini yukarıda tanımlanan *CustomSettings* sınıfının bir örneğine atamak gereklidir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfı sadece yeni Alt Toplam eklemek için çalışır. Eğer bir elektronik tablo zaten Alt Toplam içeriyorsa, onların etiketleri değiştirilemez.

{{% /alert %}} 
### **Pasta Grafiği için Diğer Etiket için Özel Metin**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) sınıfı, [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) yöntemiyle, Pie grafiklerin "Diğer" etiketi için özel bir değer vermenize olanak tanır. Aşağıdaki kod parçası, özelleştirilmiş bir sınıf tanımlar ve [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) yöntemini, JVM için varsayılan dil ayarlarına göre özel bir etiket almak üzere geçersiz kılar.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Aşağıdaki kod parçacığı, yukarıda oluşturulan *CustomSettings* sınıfını kullanarak bir Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve grafik bir resim olarak oluşturur.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Makine yerel ayarının Fransa olarak ayarlandığı durumda elde edilen resim aşağıdaki gibidir. Etiket "Diğer"nin *CustomSettings* sınıfında tanımlandığı gibi "Autre" olarak çevrildiğini görebilirsiniz.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
