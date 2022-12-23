---
title: Dosyaları Birleştir
type: docs
weight: 20
url: /tr/net/merge-files/
---
## **Giriş**

 Aspose.Cells, dosyaları birleştirmek için farklı yollar sunar. Veriler, biçimlendirme ve formüller içeren basit dosyalar için,[**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) yöntem birkaç çalışma kitabını birleştirmek için kullanılabilir ve[**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)yöntem, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemlerin kullanımı kolay ve etkilidir, ancak birleştirilecek çok sayıda dosyanız varsa, çok fazla sistem kaynağı tükettiklerini görebilirsiniz. Bunu önlemek için,[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)statik yöntem, birkaç dosyayı birleştirmenin daha verimli bir yolu.

## **Aspose.Cells Kullanarak Dosyaları Birleştirin**

 Aşağıdaki örnek kod, büyük dosyaları kullanarak nasıl birleştirileceğini gösterir.[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)yöntem. Kitap1.xls ve Kitap2.xls olmak üzere iki basit ama büyük dosya gerektirir. Dosyalar yalnızca biçimlendirilmiş verileri ve formülleri içerir.

{{% alert color="primary" %}}

 bu[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) yöntem yalnızca verilerin, stillerin, biçimlendirmenin ve formüllerin birleştirilmesini destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi nesneler bu yöntem kullanılarak birleştirilemez. Ayrıca, işlem için geçici verileri depolamak için önbelleğe alınmış bir dosya kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
