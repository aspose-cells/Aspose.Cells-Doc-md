---
title: Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama
type: docs
weight: 130
url: /tr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, bir Excel dosyasından diğerine VBA projesini kopyalamanıza olanak tanır. VBA projesi belge, prosedürel, tasarımcı vb. çeşitli modüllerden oluşur. Tüm modüller basit bir kodla kopyalanabilir ancak Tasarımcı modül için erişilmesi veya kopyalanması gereken biraz ekstra veri olan Tasarımcı Depolama Alanı vardır. Aşağıdaki iki yöntem Tasarımcı Depolama Alanı ile ilgilenir.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**

Lütfen aşağıdaki örnek kodu inceleyin. [Taslak Excel dosyasından](50528345.xlsm) boş bir çalışbook'a VBA projesi kopyalar ve bunu [çıktı Excel dosyası](50528346.xlsm) olarak kaydeder. Eğer taslak Excel dosyasının içinde VBA projesini açarsanız aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, kendisi [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) ve [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage) yöntemleri kullanılarak kopyalanacaktır.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Aşağıdaki ekran görüntüsü, kopyalanan çıktı Excel dosyasını ve içeriğini göstermektedir. Düğme 1'e tıkladığınızda, VBA Kullanıcı Formunun içinde tıklama ile bir ileti kutusu gösterir.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Örnek Kod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
