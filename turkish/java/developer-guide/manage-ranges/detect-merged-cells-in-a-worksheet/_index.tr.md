---
title: Çalışma sayfasında birleştirilmiş hücreleri tespit et
type: docs
weight: 3000
url: /tr/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Microsoft Excel'de birkaç hücre birleştirilebilir. Bu genellikle karmaşık tablolar oluşturmak veya birden fazla sütunu kapsayan bir başlık hücresi oluşturmak için kullanılır.

Aspose.Cells, bir çalışma sayfasında birleştirilmiş hücre alanlarını tanımlamanıza olanak tanır. Onları tekrar ayırabilirsiniz. Bu makale, görevi Aspose.Cells kullanarak gerçekleştirmenin en basit kod satırlarını sağlar.

Bu makale, bir çalışma sayfasında birleştirilmiş hücreleri bulmanın ve ardından onları tekrar ayırmanın kompakt talimatlarını sağlar.

{{% /alert %}}

## **Demonstrasyon**

Bu örnek, **MergeTrial** adlı bir şablon Microsoft Excel dosyasını kullanır. Ayrıca Merge Trial olarak adlandırılan bir sayfada bazı birleştirilmiş hücre alanlarına sahiptir.

**Şablon dosya**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells, tüm birleşmiş hücreleri almak için kullanılan [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) metodunu sağlar.

Aşağıdaki kod çalıştırıldığında, dosyayı tekrar kaydetmeden önce sayfanın içeriğini temizler ve tüm hücre alanlarını tekrar birleştirir.

**Çıkış Dosyası**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Kod Örneği**

Lütfen bir çalışma sayfasında birleştirilmiş hücre alanlarını tanımlamanın ve onları tekrar ayırmanın örnek kodu için aşağıdaki örnek kodu inceleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **İlgili Makaleler**

- [Hücreleri birleştirme ve bölme](/cells/tr/java/merging-and-unmerging-cells/).
{{< app/cells/assistant language="java" >}}
