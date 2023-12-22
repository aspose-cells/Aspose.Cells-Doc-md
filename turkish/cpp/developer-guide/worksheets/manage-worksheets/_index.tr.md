---
title: Çalışma Sayfalarını Yönet
type: docs
weight: 20
url: /tr/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

Geliştiriciler, Aspose.Cells esnek API'i kullanarak Microsoft Excel dosyalarındaki çalışma sayfalarını programlı olarak kolayca oluşturabilir ve yönetebilir. Bu konu, Microsoft Excel dosyalarındaki çalışma sayfalarını ekleme ve kaldırma yaklaşımlarını açıklamaktadır.

{{% /alert %}} 

 Aspose.Cells bir sınıf sağlıyor[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) bu bir Excel dosyasını temsil eder.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf bir içerir[Çalışma sayfaları](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon.

Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)class, çalışma sayfalarını yönetmek için çok çeşitli yöntemler sağlar.
##  **Yeni Bir Excel Dosyasına Çalışma Sayfaları Ekleme**
Programlı olarak yeni bir Excel dosyası oluşturmak için:

1.  Bir nesne oluşturun[Çalışma kağıdı](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)sınıf.
1.  Ara[Eklemek](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) yöntemi[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) Toplamak. Excel dosyasına otomatik olarak boş bir çalışma sayfası eklenir. Yeni çalışma sayfasının sayfa dizinini ileterek başvurulabilir.[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)Toplamak.
1. Bir çalışma sayfası referansı edinin.
1. Çalışma sayfalarında çalışma yapın.
1. Yeni Excel dosyasını yeni çalışma sayfalarıyla birlikte arayarak kaydedin.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıf[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)yöntem.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **Sayfa Dizinini Kullanarak Çalışma Sayfalarına Erişme**
Aşağıdaki örnek kod, herhangi bir çalışma sayfasına, dizinini belirterek nasıl erişileceğini veya bu sayfanın nasıl alınacağını gösterir.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **Sayfa Dizinini Kullanarak Çalışma Sayfalarını Kaldırma**
 Çalışma sayfalarını ada göre kaldırmak, çalışma sayfasının adı bilindiğinde işe yarar. Çalışma sayfasının adını bilmiyorsanız, aşırı yüklenmiş bir sürümünü kullanın.[KaldırAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)çalışma sayfasının sayfa adı yerine sayfa dizinini alan yöntem.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
