---
title: Excel Elektronik Tablosunu PDF ye Dönüştür
type: docs
weight: 80
url: /tr/cpp/convert-excel-workbook-to-pdf/
---

## **Excel Çalışma Kitabını PDF'e Dönüştürme**
PDF dosyaları, kuruluşlar, devlet kurumları ve bireyler arasında belge değişiminde geniş ölçüde kullanılır. Standart bir belge biçimidir ve yazılım geliştiriciler genellikle Microsoft Excel dosyalarını PDF belgelerine dönüştürmek için bir yol bulmaları istenir.

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}} 

Aspose.Cells doğrudan API ve Sürüm Numarası hakkında bilgiyi çıktı belgelerine yazar. Örneğin, Belgeyi PDF'e dönüştürdüğünde, Aspose.Cells for C++ **Uygulama** alanını 'Aspose.Cells' değeriyle doldurur ve **PDF Üreticisi** alanını 'Aspose.Cells v18.5.0' gibi bir değerle doldurur.

{{% /alert %}} 
### **Doğrudan Dönüşüm**
Aspose.Cells, diğer yazılım bağımsız olarak elektronik tablolardan PDF'ye dönüşümü destekler. Basitçe, Excel dosyasını [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini kullanarak PDF'ye kaydedin. [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemi, yerel Excel dosyalarını PDF formatına dönüştüren [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırma üyesini sağlar.

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş yapıcıyı çağırarak [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının bir nesnesini örnekle.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
3. Aspose.Cells'in API'lerini kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Tablo kodu tamamlandığında, elektronik tabloyu kaydetmek için [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfının [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) yöntemini çağırın.

Dosya formatı PDF olmalı, bu nedenle son PDF belgesini oluşturmak için [SaveFormat](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) numaralandırmasından ilgili PDF (önceden tanımlanmış bir değer) seçin.

Lütfen, örnek kodunu, [örnek Excel dosyasını](67338368.xlsx) ve [çıktı PDF'sini](67338369.pdf) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
### **Gelişmiş Dönüşüm**
Dönüşüm için farklı özellikler belirlemek için ayrıca [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) sınıfını kullanabilirsiniz. **PdfSaveOptions** sınıfının farklı özelliklerini ayarlamak, çıktı PDF'inde yazdırma, yazı tipi, güvenlik ve sıkıştırma ayarları üzerinde kontrol sağlar. En önemli özellik, [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) olarak, Excel dosyalarını PDF/A uyumlu PDF dosyalarına kaydetmenizi sağlar.
#### **Çalışma Kitabını PDF/A Uyumlu Dosyalara Kaydetme**
Aşağıdaki kod parçası, Excel dosyalarını PDF/A uyumlu PDF formatına kaydetmek için **PdfSaveOptions** sınıfını nasıl kullanacağınızı gösterir.

Lütfen, örnek kodunu ve [çıktı PDF'sini](67338370.pdf) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
#### **PDF Oluşturma Saatini Ayarlayın**
**IPdfSaveOptions** sınıfı ile PDF oluşturma saati alabilir veya ayarlayabilirsiniz.

Lütfen, örnek kodunu ve [çıktı PDF'sini](67338371.pdf) inceleyin.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
