---
title: Excel Elektronik Tablosunu PDF ye Dönüştür
type: docs
weight: 80
url: /tr/go-cpp/convert-excel-workbook-to-pdf/
---

## **Excel Çalışma Kitabını PDF'e Dönüştürme**

Aspose.Cells, Excel dosyalarını PDF'ye dönüştürmeyi destekler ve dönüşümde yüksek görsel sadakati korur.

{{% alert color="primary" %}}

Aspose.Cells, API ve Sürüm Numarası bilgilerini çıktı belgelerine doğrudan yazar. Örneğin, belge PDF'ye dönüştürülürken, Aspose.Cells for Go via C++ [Uygulama](https://reference.aspose.com/cells/go-cpp/workbook/) alanını 'Aspose.Cells' değeriyle doldurur ve [PDF Üretici](https://reference.aspose.com/cells/go-cpp/workbook/) alanını, örneğin, 'Aspose.Cells v24.12.0' ile doldurur.

Lütfen, Aspose.Cells for Go via C++'nin bu bilgileri çıktı Belgelerinden değiştirmesini veya kaldırmasını talimat veremeyeceğinizi unutmayın.

{{% /alert %}}

### **Doğrudan Dönüşüm**

Doğrudan Excel elektronik tablolarını PDF biçimine dönüştürmek için aşağıdaki adımları izleyin:

1. Boş yapıcıyı çağırarak [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfından bir nesne oluşturun.
1. Varolan bir şablon dosyasını açabilir/yükleyebilir veya çalışma kitabını sıfırdan oluşturuyorsanız bu adımı atlayabilirsiniz.
3. Aspose.Cells'in API'lerini kullanarak elektronik tabloda herhangi bir işlem yapın (giriş verileri, biçimlendirme uygulama, formüller belirleme, resimler veya diğer çizim nesneleri ekleme vb.).
1. Çalışma sayfası kodu tamamlandığında, çalışma sayfasını kaydetmek için [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) sınıfının [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) yöntemini çağırın.

Dosya formatı PDF olmalı, bu nedenle nihai PDF belgesini oluşturmak için `SaveFormat` enumerasyonundan ilgili `PDF` (önceden tanımlanmış değer) seçin.

Lütfen aşağıdaki örnek kodu, bunun [örnek Excel dosyası](67338368.xlsx) ve [çıktı PDF'si](67338369.pdf) ile inceleyin.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
