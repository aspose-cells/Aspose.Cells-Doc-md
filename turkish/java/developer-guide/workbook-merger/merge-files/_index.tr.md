---
title: Dosyaları Birleştirme
type: docs
weight: 10
url: /tr/java/merge-files/
---

## **Giriş**

Aspose.Cells, dosyaları birleştirmek için farklı yöntemler sağlar. Veriler, biçimlendirme ve formüller içeren basit dosyalar için [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine-com.aspose.cells.Workbook-) yöntemi, birkaç çalışma kitabını birleştirmek için kullanılabilir ve [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy-com.aspose.cells.Worksheet-) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak çok sayıda dosya birleştiriyorsanız, bunların sistem kaynaklarını çok kullanabileceğini fark edebilirsiniz. Bunu önlemek için, daha verimli bir yol olan CellsHelper.mergeFiles statik yöntemini kullanın.

## **Aspose.Cells Kullanarak Dosyaları Birleştirme**

Aşağıdaki örnek kod, CellsHelper.mergeFiles yöntemini kullanarak büyük dosyaları nasıl birleştirileceğini gösterir. MyBook1.xls ve MyBook2.xls adlı iki basit ama büyük dosyayı içerir. Dosyalar yalnızca biçimlendirilmiş veri ve formülleri içerir.

{{% alert color="primary" %}}

CellsHelper.mergeFiles yöntemi sadece veri, stiller, biçimlendirme ve formüllerin birleştirilmesini destekler. Bu yöntemle grafikler, resimler, açıklamalar veya diğer nesneler birleştirilmeyebilir. Ayrıca, geçici verileri depolamak için önbelleğe alınmış bir dosya bu işlem için kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
{{< app/cells/assistant language="java" >}}
