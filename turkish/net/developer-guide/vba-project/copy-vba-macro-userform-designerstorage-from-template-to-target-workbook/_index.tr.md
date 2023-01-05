---
title: VBA Macro UserForm DesignerStorage'ı Şablondan Hedef Çalışma Kitabına Kopyalayın
type: docs
weight: 130
url: /tr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Olası Kullanım Senaryoları**

Aspose.Cells, bir VBA projesini bir Excel dosyasından başka bir Excel dosyasına kopyalamanıza olanak tanır. VBA projesi, Document, Procedural, Designer, vb. gibi çeşitli modül türlerinden oluşur. Tüm modüller basit bir kodla kopyalanabilir ancak Designer modülü için, Designer Storage adı verilen, erişilmesi veya kopyalanması gereken bazı ekstra veriler vardır. Aşağıdaki iki yöntem Tasarımcı Depolaması ile ilgilidir.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **VBA Macro UserForm DesignerStorage'ı Şablondan Hedef Çalışma Kitabına Kopyalayın**

Lütfen aşağıdaki örnek koda bakın. VBA projesini kopyalar.[şablon excel dosyası](50528345.xlsm) boş bir çalışma kitabına kaydeder ve[çıktı excel dosyası](50528346.xlsm). Şablon Excel dosyası içinde VBA projesini açarsanız, aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Depolama Alanından oluşur, bu nedenle kullanılarak kopyalanacaktır.[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)ve[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)yöntemler.

**![todo:image_alt_text](şablondan-hedefe-çalışma kitabına kopyalama-vba-makro-kullanıcı formu-tasarımcı depolaması_1.png)**

Aşağıdaki ekran görüntüsü, şablon Excel dosyasından kopyalanan çıktı Excel dosyasını ve içeriğini gösterir. Düğme 1'e tıkladığınızda, tıklandığında bir mesaj kutusu gösteren bir komut düğmesine sahip olan VBA Kullanıcı Formunu açar.

**![todo:image_alt_text](template-to-hedef-workbook_2.png kopya-vba-makro-kullanıcı formu-tasarımcı depolaması)**

## **Basit kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
