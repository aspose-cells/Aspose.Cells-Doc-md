---
title: Golang ve C++ kullanarak Dosyaları Birleştirme
linktitle: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/go-cpp/merge-files/
description: Aspose.Cells for C++ kullanarak Excel dosyalarını etkin bir şekilde nasıl birleştireceğinizi öğrenin.
---

## **Giriş**

Aspose.Cells, dosya birleştirme için farklı yollar sunar. Veri, biçimlendirme ve formüller içeren basit dosyalar için [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) yöntemi birkaç çalışma kitabını birleştirmek; ve [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak çok sayıda dosya birleştiriyorsanız, sistem kaynaklarınızın yoğun kullanıldığını fark edebilirsiniz. Bunu önlemek için, birkaç dosyayı birleştirmenin daha verimli yolu olan [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) statik yöntemini kullanın.

## **Aspose.Cells Kullanarak Dosyaları Birleştirme**

Aşağıdaki örnek kod, büyük dosyaları [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) yöntemi ile birleştirme yöntemini gösterir. İki basit ve büyük dosya olan Book1.xls ve Book2.xls kullanır. Dosyalar sadece biçimlendirilmiş veri ve formüller içerir.

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) yöntemi yalnızca veri, stiller, biçimlendirme ve formüllerin birleştirilmesini destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi nesneler bu yöntem kullanılarak birleştirilmeyebilir. Ayrıca, geçici verileri depolamak için önbelleğe alınmış bir dosya kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
