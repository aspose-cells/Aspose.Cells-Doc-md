---
title: Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Okuma
linktitle: Çoklu İş Parçacıkları
type: docs
weight: 1800
url: /tr/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for .NET API si aracılığıyla Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Okumayı Öğrenin.
keywords: Aynı Anda Birden Fazla İş Parçacığından Hücre Değerlerini Oku, Aspose.Cells C# Çoklu İş Parçacıkları, Birden Fazla İş Parçacığında Veri Okuma
---

{{% alert color="primary" %}}

Aynı Anda Birden Fazla İş Parçacığında hücre değerlerini okuma ihtiyacı yaygın bir gereksinimdir. Bu makale bu amaçla Aspose.Cells'in nasıl kullanılacağını açıklar.

{{% /alert %}}

Daha fazla bir iş parçacığında hücre değerlerini okumak için [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) değerini **true** olarak ayarlayın. Aksi takdirde yanlış hücre değerlerini alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Sonra rastgele hücrelerden aynı anda değer okuyan iki iş parçacığı oluşturur.
   Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler yanlışsa bir mesaj görüntülenir.

Eğer bu satırı yorumlarsanız:

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

o zaman aşağıdaki mesaj görüntülenir:

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde, program herhangi bir mesaj göstermeden çalışır, bu da demek olur ki tüm hücrelerden okunan değerler doğrudur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
