---
title: VBA Macro UserForm DesignerStorage'ı Şablondan Hedef Çalışma Kitabına Kopyalayın
type: docs
weight: 60
url: /tr/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, VBA projesini bir Excel dosyasından başka bir Excel dosyasına kopyalamanıza olanak tanır. VBA projesi, Belge, Prosedürel, Tasarımcı vb. gibi çeşitli modül türlerinden oluşur. Tüm modüller basit bir kodla kopyalanabilir ancak Tasarımcı modülü için, Tasarımcı Deposu adı verilen, erişilmesi veya kopyalanması gereken bazı ekstra veriler vardır. Aşağıdaki iki yöntem Tasarımcı Depolaması ile ilgilidir.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **VBA Macro UserForm DesignerStorage'ı Şablondan Hedef Çalışma Kitabına Kopyalayın**

Lütfen aşağıdaki örnek koda bakın. VBA projesini kopyalar.[şablon excel dosyası](50528367.xlsm)boş bir çalışma kitabına kaydeder ve[çıktı excel dosyası](50528366.xlsm). Şablon Excel dosyası içinde VBA projesini açarsanız, aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Depolama Alanından oluşur, bu nedenle kullanılarak kopyalanacaktır.[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) ve[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) yöntemler.

![yapılacaklar:resim_alternatif_Metin](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Aşağıdaki ekran görüntüsü, şablon Excel dosyasından kopyalanan çıktı Excel dosyasını ve içeriğini gösterir. Düğme 1'e tıkladığınızda, tıklandığında bir mesaj kutusu gösteren bir komut düğmesine sahip olan VBA Kullanıcı Formunu açar.

![yapılacaklar:resim_alternatif_Metin](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Basit kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
