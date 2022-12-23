---
title: Dosyaları Birleştir
type: docs
weight: 10
url: /tr/java/merge-files/
---
## **Giriş**

 Aspose.Cells, dosyaları birleştirmek için farklı yollar sunar. Veriler, biçimlendirme ve formüller içeren basit dosyalar için,[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) yöntemi birkaç çalışma kitabını birleştirmek için kullanılabilir ve[**çalışma sayfası.kopya(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemlerin kullanımı kolay ve etkilidir, ancak birleştirilecek çok sayıda dosyanız varsa, çok fazla sistem kaynağı tükettiklerini görebilirsiniz. Bunu önlemek için, birkaç dosyayı birleştirmenin daha etkili bir yolu olan CellsHelper.mergeFiles statik yöntemini kullanın.

## **Aspose.Cells Kullanarak Dosyaları Birleştirin**

Aşağıdaki örnek kod, CellsHelper.mergeFiles yöntemi kullanılarak büyük dosyaların nasıl birleştirileceğini gösterir. İki basit ama büyük dosya gerektirir, MyBook1.xls ve MyBook2.xls. Dosyalar yalnızca biçimlendirilmiş verileri ve formülleri içerir.

{{% alert color="primary" %}}

CellsHelper.mergeFiles yöntemi yalnızca verilerin, stillerin, biçimlendirmenin ve formüllerin birleştirilmesini destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi nesneler bu yöntem kullanılarak birleştirilemez. Ayrıca, işlem için geçici verileri depolamak için önbelleğe alınmış bir dosya kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
