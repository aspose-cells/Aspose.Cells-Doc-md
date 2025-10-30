---
title: Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama
type: docs
weight: 130
url: /tr/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells for Python via .NET, bir VBA projesini bir Excel dosyasından diğerine kopyalamanıza olanak tanır. VBA projesi, Doküman, İşlemci, Tasarımcı vb. çeşitli modüllerden oluşur. Tüm modüller basit kodla kopyalanabilir, ancak Tasarımcı modülü için Ekstra veriler olan Tasarımcı Depolaması erişilmeli veya kopyalanmalı. Aşağıdaki iki yöntem Tasarımcı Depolaması ile ilgilidir.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**

Lütfen aşağıdaki örnek kodu inceleyin. [Taslak Excel dosyasından](50528345.xlsm) boş bir çalışbook'a VBA projesi kopyalar ve bunu [çıktı Excel dosyası](50528346.xlsm) olarak kaydeder. Eğer taslak Excel dosyasının içinde VBA projesini açarsanız aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, kendisi [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) ve [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage) yöntemleri kullanılarak kopyalanacaktır.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Aşağıdaki ekran görüntüsü, kopyalanan çıktı Excel dosyasını ve içeriğini göstermektedir. Düğme 1'e tıkladığınızda, VBA Kullanıcı Formunun içinde tıklama ile bir ileti kutusu gösterir.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Örnek Kod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
