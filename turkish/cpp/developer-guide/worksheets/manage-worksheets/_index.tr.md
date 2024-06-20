---
title: Çalışsayfaları Yönet
type: docs
weight: 20
url: /tr/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

Geliştiriciler, Aspose.Cells esnek API'sını kullanarak Microsoft Excel dosyalarında programlı olarak çalışma sayfaları oluşturabilir ve yönetebilir. Bu konu, Microsoft Excel dosyalarında çalışma sayfaları eklemek ve kaldırmak için yaklaşımları açıklar.

{{% /alert %}} 

Aspose.Cells, bir Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonu içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı, çalışma sayfalarını yönetmek için geniş bir yöntem yelpazesi sağlar.
## **Yeni bir Excel Dosyasına Çalışsayfalar Ekleme**
Programlı olarak yeni bir Excel dosyası oluşturmak için:

1. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfının bir örneğini oluşturun.
1. [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunun [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) yöntemini çağırın. Boş bir çalışma sayfası otomatik olarak Excel dosyasına eklenir. Yeni çalışma sayfasının çalışma kitabının sayfa dizinine geçirilmesiyle [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonuna başvurulabilir.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfalarında çalışma yapın.
1. Yeni Eşleşme Tabloları ile yeni Excel dosyasını kaydedin, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) metodu çağrılarak.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **Sayfa İndeksini Kullanarak Eşleşmelere Erişme**
Aşağıdaki örnek kod, indeksini belirterek herhangi bir eşleşmeye erişmeyi veya almayı gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**
Eşleşme adının bilindiği durumda eşleşmelerin kaldırılması iyi çalışır. Eğer eşleşme adını bilmiyorsanız, eşleştirmenin adı yerine sayfa indeksini alan [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) metodu için aşırı yüklenmiş bir versiyonunu kullanın.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
