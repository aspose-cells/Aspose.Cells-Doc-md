---
title: Her Excel Çalışma Sayfası İçin Bir PDF Sayfası Render Etme  Excel den PDF ye Dönüşüm ile Golang
type: docs
weight: 100
url: /tr/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Aspose.Cells kullanarak Golang ile C++ üzerinden Excel çalışma sayfalarını her biri bir sayfa olacak şekilde PDF biçimine dönüştürün.
---

{{% alert color="primary" %}} 

Büyük Microsoft Excel dosyalarıyla çalışırken (örneğin, birçok sayfası olan ve her sayfasında 50 kolon ve 300 veya daha fazla satır verisi bulunan çalışma kitabı), PDF çıktısının her çalışma sayfası için bir sayfa gösterdiğinden emin olmak isteyebilirsiniz, sayfanın boyutu büyük farklılıklar gösterebilir. Bu durum, her sayfanın çok farklı sayfa boyutlarına sahip olmasına neden olur. Bu, Aspose.Cells for C++ kullanılarak gerçekleştirilebilir.

{{% /alert %}} 

Lütfen birden çok çalışsayfasına sahip bir Excel dosyasını PDF'ye dönüştüren aşağıdaki örnek kodu inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Eğer [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) seçeneği **true** olarak ayarlanmışsa, tüm sayfa içeriği tek bir PDF sayfasına işlenecektir.

{{% /alert %}} {{% alert color="primary" %}} 

Eğer dosyanız formüller içeriyorsa, PDF'ye dönüştürmeden hemen önce [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) çağrısı yapmak en iyisidir. Bu, formüle bağlı değerlerin yeniden hesaplanmasını sağlar ve PDF'de doğru değerler gösterilir.

{{% /alert %}}
