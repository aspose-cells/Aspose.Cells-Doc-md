---
title: Birden Fazla Konudaki Cell Değerlerini Aynı Anda Okumak
linktitle: Çoklu Konular
type: docs
weight: 1800
url: /tr/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Aspose.Cells for .NET API aracılığıyla Cell Birden Fazla Konudaki Değerleri Aynı anda nasıl okuyacağınızı öğrenin.
keywords: Read Cell Values in Multiple Threads Simultaneously, Aspose.Cells C# Multiple Threads, Read data in Multiple Threads
---
{{% alert color="primary" %}}

Aynı anda birden fazla iş parçacığında hücre değerlerinin okunmasının gerekliliği ortak bir gereksinimdir. Bu makalede, bu amaçla Aspose.Cells'in nasıl kullanılacağı açıklanmaktadır.

{{% /alert %}}

 Birden fazla iş parçacığında hücre değerlerini aynı anda okumak için[**Çalışma Sayfası.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading)*doğruya**. Bunu yapmazsanız yanlış hücre değerlerini alabilirsiniz.

Aşağıdaki kod:

1. Bir çalışma kitabı oluşturur.
1. Bir çalışma sayfası ekler.
1. Çalışma sayfasını dize değerleriyle doldurur.
1. Daha sonra rastgele hücrelerden değerleri aynı anda okuyan iki iş parçacığı oluşturur.
 Okunan değerler doğru ise hiçbir şey olmaz. Okunan değerler hatalıysa bir mesaj görüntülenir.

Bu satıra yorum yaparsanız:

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

ardından aşağıdaki mesaj görüntülenir:

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Aksi takdirde program herhangi bir mesaj vermeden çalışır, bu da hücrelerden okunan tüm değerlerin doğru olduğu anlamına gelir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
