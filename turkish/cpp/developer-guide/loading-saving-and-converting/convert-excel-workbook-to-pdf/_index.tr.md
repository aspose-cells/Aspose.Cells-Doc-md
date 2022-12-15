---
title: Excel Çalışma Kitabını PDF'ye Dönüştür
type: docs
weight: 80
url: /tr/cpp/convert-excel-workbook-to-pdf/
---
## **Excel Çalışma Kitabını PDF'ye Dönüştürme**
PDF dosyaları, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinde bulunmak için yaygın olarak kullanılır. Standart bir belge biçimidir ve yazılım geliştiricilerden genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmenin bir yolunu bulmaları istenir.

Aspose.Cells, Excel dosyalarının PDF'ye dönüştürülmesini destekler ve dönüştürmede yüksek görsel doğruluğu korur.

{{% alert color="primary" %}} 

 Aspose.Cells, API ve Sürüm Numarası ile ilgili bilgileri doğrudan çıktı belgelerine yazar. Örneğin, Belgeyi PDF'ye dönüştürürken Aspose.Cells for C++,**Başvuru** 'Aspose.Cells' değerine sahip alan ve**PDF Yapımcısı** değeri olan alan, örneğin 'Aspose.Cells v18.5.0'.

Lütfen Aspose.Cells for C++'e bu bilgileri çıktı Belgelerinden değiştirme veya kaldırma talimatı veremeyeceğinizi unutmayın.

{{% /alert %}} 
### **Doğrudan Dönüşüm**
Aspose.Cells, diğer yazılımlardan bağımsız olarak elektronik tablolardan PDF'ye dönüştürmeyi destekler. kullanarak bir Excel dosyasını PDF'e kaydetmeniz yeterlidir.[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)sınıf'[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)yöntem. bu[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)yöntemi sağlar[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)yerel Excel dosyalarını PDF biçimine dönüştüren numaralandırma üyesi.

Excel elektronik tablolarını doğrudan PDF formatına dönüştürmek için aşağıdaki adımları izleyin:

1.  nesnesinin örneğini oluşturun[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)boş kurucusunu çağırarak sınıf.
1. Mevcut bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
1. Aspose.Cells' API'lerini kullanarak elektronik tablo üzerinde herhangi bir iş yapın (verileri girin, biçimlendirmeyi uygulayın, formülleri ayarlayın, resimler veya başka çizim nesneleri ekleyin, vb.).
1.  Elektronik tablo kodu tamamlandığında,[IÇalışma Kitabı](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)sınıf'[Kaydetmek](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)elektronik tabloyu kaydetme yöntemi.

Dosya formatı PDF olmalıdır, bu nedenle son PDF belgesini oluşturmak için SaveFormat numaralandırmasından ilgili PDF'yi (önceden tanımlanmış bir değer) seçin.

 Lütfen aşağıdaki örnek koda bakın,[örnek excel dosyası](67338368.xlsx) ve[çıktı PDF](67338369.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **Gelişmiş Dönüşüm**
kullanmayı da tercih edebilirsiniz.[IPdfSaveSeçenekleri](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)dönüşüm için farklı öznitelikler ayarlamak için sınıf. Farklı özelliklerin ayarlanması**IPdfSaveSeçenekleri** class çıktı PDF için yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özelliği[Uyum Ayarla](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.
#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**
Aşağıdaki kod parçacığı, nasıl kullanılacağını gösterir.**IPdfSaveSeçenekleri**Excel dosyalarını PDF/A uyumlu PDF biçiminde kaydetmek için sınıf

 Lütfen aşağıdaki örnek koda ve onun[çıktı PDF](67338370.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **PDF Oluşturma Zamanını Ayarlayın**
İle**IPdfSaveSeçenekleri** sınıf, PDF oluşturma süresini alabilir veya ayarlayabilirsiniz.

 Lütfen aşağıdaki örnek koda ve onun[çıktı PDF](67338371.pdf) senin referansın için.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
