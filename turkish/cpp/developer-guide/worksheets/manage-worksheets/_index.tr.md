---
title: Çalışma Sayfalarını Yönet
type: docs
weight: 20
url: /tr/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Geliştiriciler, Microsoft Excel dosyalarındaki çalışma sayfalarını programlı olarak Aspose.Cells esnek API kullanarak kolayca oluşturabilir ve yönetebilir. Bu konuda, Microsoft Excel dosyalarına çalışma sayfası ekleme ve kaldırma yaklaşımları açıklanmaktadır.

{{% /alert %}} 

 Aspose.Cells bir sınıf sağlar[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) Bu bir Excel dosyasını temsil eder. bu[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf bir içerir[çalışma sayfaları](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon.

 Bir çalışma sayfası şununla temsil edilir:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) sınıf. bu[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar.
## **Çalışma Sayfalarını Yeni Bir Excel Dosyasına Ekleme**
Programlı olarak yeni bir Excel dosyası oluşturmak için:

1.  Şunun bir nesnesini oluşturun:[IÇalışma Sayfası](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)sınıf.
1.  Ara[Eklemek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) yöntemi[IÇalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) Toplamak. Excel dosyasına otomatik olarak boş bir çalışma sayfası eklenir. Yeni çalışma sayfasının sayfa dizini şuraya geçirilerek başvurulabilir:[IÇalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)Toplamak.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfaları üzerinde çalışma gerçekleştirin.
1.  Çağırarak yeni Excel dosyasını yeni çalışma sayfalarıyla kaydedin.[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) sınıf[Kayıt etmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **Sayfa Dizini Kullanarak Çalışma Sayfalarına Erişme**
Aşağıdaki örnek kod, dizinini belirterek herhangi bir çalışma sayfasına nasıl erişileceğini veya alınacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **Sayfa Dizini Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfalarını ada göre kaldırmak, çalışma sayfasının adı bilindiğinde işe yarar. Çalışma sayfasının adını bilmiyorsanız, aşırı yüklenmiş bir sürümünü kullanın.[KaldırAt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)çalışma sayfasının sayfa adı yerine sayfa dizinini alan yöntem.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
