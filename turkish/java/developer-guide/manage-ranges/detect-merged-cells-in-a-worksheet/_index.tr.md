---
title: Çalışma Sayfasında Birleştirilmiş Cells'i Algıla
type: docs
weight: 3000
url: /tr/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

Microsoft Excel'de birkaç hücre birleştirilebilir. Bu genellikle karmaşık tablolar oluşturmak veya birkaç sütuna yayılan bir başlığı tutan bir hücre oluşturmak için kullanılır.

Aspose.Cells, bir çalışma sayfasındaki birleştirilmiş hücre alanlarını belirlemenizi sağlar. Onları da ayırabilirsin. Bu makale, Aspose.Cells kullanarak görevi gerçekleştirmek için en basit kod satırlarını sağlar.

Bu makale, bir çalışma sayfasındaki birleştirilmiş hücrelerin nasıl bulunacağına ve daha sonra ayrıştırılacağına ilişkin kısa yönergeler sağlar.

{{% /alert %}}

## **Gösteri**

 Bu örnek, adlı bir şablon Microsoft Excel dosyası kullanır.**Birleştirme Denemesi**. Birleştirme Denemesi olarak da adlandırılan bir sayfada bazı birleştirilmiş hücre alanları vardır.

**şablon dosyası**

![yapılacaklar:resim_alternatif_metin](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells şunları sağlar:[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)birleştirilmiş hücre alanlarının ArrayList'ini almak için kullanılan yöntem.

Aşağıdaki kod yürütüldüğünde, sayfanın içeriğini temizler ve dosyayı yeniden kaydetmeden önce tüm hücre alanlarını ayırır.

**Çıktı Dosyası**

![yapılacaklar:resim_alternatif_metin](detect-merged-cells-in-a-worksheet_2.png)

## **Kod Örneği**

Bir çalışma sayfasındaki birleştirilmiş hücre alanlarını nasıl belirleyeceğinizi ve bunları nasıl ayıracağınızı öğrenmek için lütfen aşağıdaki örnek koda bakın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **İlgili Makaleler**

- [Hücreleri birleştirme ve bölme](/cells/tr/java/merging-and-unmerging-cells/).
