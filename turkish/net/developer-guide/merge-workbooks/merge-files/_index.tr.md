---
title: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/net/merge-files/
---

## **Giriş**

Aspose.Cells, dosyaları birleştirmek için farklı yöntemler sunar. Basit veri, biçimlendirme ve formüller içeren dosyalar için, [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) yöntemi kullanılarak birkaç çalışma kitabı birleştirilebilir ve [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) yöntemi kullanılarak çalışsayfalar yeni bir çalışma kitabına kopyalanabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak birçok dosyayı birleştirmeniz gerekiyorsa, sistem kaynaklarının büyük bir bölümünü aldıklarını fark edebilirsiniz. Bunu önlemek için, daha verimli bir şekilde birden fazla dosyayı birleştirmek için [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) statik yöntemini kullanın.

## **Aspose.Cells Kullanarak Dosyaları Birleştirme**

Aşağıdaki örnek kod, [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) yöntemini kullanarak büyük dosyaları birleştirmenin nasıl yapılacağını göstermektedir. Basit ancak büyük verilere ve formüllere sahip Book1.xls ve Book2.xls adlı iki dosya alır.

{{% alert color="primary" %}}

Metod yalnızca veri, stiller, biçimlendirme ve formülleri birleştirmeyi destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi objeler, bu yöntemi kullanarak birleştirilmeyebilir. Ayrıca, işlem için geçici verileri saklamak için önbellek dosyası kullanılır.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
