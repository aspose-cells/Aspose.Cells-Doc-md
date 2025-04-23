---
title: Çalışsayfaları Yönet
type: docs
weight: 20
url: /tr/go-cpp/manage-worksheets/
---

{{% alert color="primary" %}}

Geliştiriciler, Aspose.Cells esnek API'sını kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları oluşturabilir ve yönetebilir. Bu konu, Microsoft Excel dosyalarında çalışma sayfaları eklemek ve kaldırmak için yaklaşımları açıklar.

{{% /alert %}}

Aspose.Cells, Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını sağlar. Bu [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfı, Excel dosyasındaki her sayfa öğesine erişim sağlayan [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunu içerir.

Bir sayfa öğesi [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfı, sayfa öğelerini yönetmek için çok çeşitli yöntemler sağlar.

## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**

Programlı olarak yeni bir Excel dosyası oluşturmak için:

1. [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sınıfından bir nesne oluşturun.
1. [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) yöntemini çağırın. Boş bir sayfa öğesi otomatik olarak Excel dosyasına eklenir. Yeni sayfa öğesinin sayfa indeksini kullanarak [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) koleksiyonunda referans alınabilir.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfalarında çalışma yapın.
1. [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfını kullanarak yeni sayfa öğeleriyle yeni Excel dosyasını kaydedin [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) yöntemiyle.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingWorksheetsToNewExcelFile.go" >}}

## **Sayfa İndeksini Kullanarak Eşleşmelere Erişme**

Aşağıdaki örnek kod, indeksini belirterek herhangi bir eşleşmeye erişmeyi veya almayı gösterir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessingWorksheetsUsingSheetIndex.go" >}}

## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**

Sayfa adına göre sayfa öğelerini kaldırmak iyi çalışır, sayfa adını bilmiyorsanız, sayfa adını yerine sayfa indeksini alan [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) yönteminin aşırı yüklenmiş bir sürümünü kullanın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingWorksheetsUsingSheetIndex.go" >}}
