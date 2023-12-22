---
title: Excel Çalışma Kitabını PDF'e dönüştürün
type: docs
weight: 80
url: /tr/cpp/convert-excel-workbook-to-pdf/
---
##  **Excel Çalışma Kitabını PDF'e dönüştürme**
PDF dosyaları kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde bulunmak için yaygın olarak kullanılır. Standart bir belge formatıdır ve yazılım geliştiricilerden sıklıkla Microsoft Excel dosyalarını PDF belgeye dönüştürmenin bir yolunu bulmaları istenir.

Aspose.Cells, Excel dosyalarının PDF'e dönüştürülmesini destekler ve dönüştürme sırasında yüksek görsel doğruluğu korur.

{{% alert color="primary" %}} 

 Aspose.Cells, çıktı belgelerine doğrudan API ve Sürüm Numarası hakkındaki bilgileri yazar. Örneğin, Belge PDF'e işlendiğinde, Aspose.Cells for C++ şunu doldurur:**Başvuru** 'Aspose.Cells' değerine sahip alan ve**PDF Üretici** değeri olan alan, örneğin 'Aspose.Cells v18.5.0'.

Lütfen Aspose.Cells for C++'e bu bilgiyi çıktı Belgelerinden değiştirmesi veya kaldırması talimatını veremeyeceğinizi unutmayın.

{{% /alert %}} 
###  **Doğrudan Dönüşüm**
Aspose.Cells, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'e dönüştürmeyi destekler. Bir Excel dosyasını kullanarak PDF'e kaydetmeniz yeterlidir.[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)sınıf'[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)yöntem.[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)yöntem şunları sağlar:[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)yerel Excel dosyalarını PDF biçimine dönüştüren numaralandırma üyesi.

Excel elektronik tablolarını doğrudan PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1.  Bir nesneyi somutlaştırın[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)boş yapıcısını çağırarak sınıfı.
1. Mevcut bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells' API'lerini kullanarak elektronik tablo üzerinde herhangi bir çalışma yapın (veri girişi, biçimlendirme uygulama, formül ayarlama, resim veya diğer çizim nesneleri ekleme vb.).
1.  Elektronik tablo kodu tamamlandığında,[Çalışma kitabı](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)sınıf'[Kaydetmek](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)Elektronik tabloyu kaydetme yöntemi.

Dosya formatı PDF olmalıdır, bu nedenle son PDF belgesini oluşturmak için SaveFormat numaralandırmasından ilgili PDF'i (önceden tanımlanmış bir değer) seçin

 Lütfen aşağıdaki örnek koda bakın;[örnek Excel dosyası](67338368.xlsx) Ve[çıkış PDF](67338369.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **Gelişmiş Dönüşüm**
Ayrıca şunları kullanmayı da tercih edebilirsiniz:[PdfKaydetmeSeçenekleri](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)Dönüşüm için farklı öznitelikler ayarlamak için sınıf. Farklı özelliklerin ayarlanması**PdfKaydetmeSeçenekleri** sınıfı, PDF çıktısının yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sahibi olmanızı sağlar. En önemli özellik,[Uyum Ayarla](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.
####  **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**
Aşağıdaki kod parçacığı, uygulamanın nasıl kullanılacağını gösterir.**PdfKaydetmeSeçenekleri**Excel dosyalarını PDF/A uyumlu PDF biçiminde kaydetmek için sınıf

 Lütfen aşağıdaki örnek koda ve onun[çıkış PDF](67338370.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **PDF Oluşturma Zamanını Ayarlayın**
İle**IPdfSaveSeçenekleri** sınıf, PDF oluşturma zamanını alabilir veya ayarlayabilirsiniz.

 Lütfen aşağıdaki örnek koda ve onun[çıkış PDF](67338371.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
