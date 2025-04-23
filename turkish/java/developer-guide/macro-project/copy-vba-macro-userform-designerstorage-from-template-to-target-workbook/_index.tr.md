---
title: Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama
type: docs
weight: 60
url: /tr/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, bir Excel dosyasından VBA projeyi başka bir Excel dosyasına kopyalamanıza olanak tanır. VBA projesi, belge, prosedürel, tasarımcı vb. çeşitli modüllerden oluşur. Tüm modüller basit bir kodla kopyalanabilir ancak Tasarımcı modül için erişilmesi veya kopyalanması gereken Tasarımcı Deposu adında ekstra veri bulunmaktadır. Aşağıdaki iki yöntem, Tasarımcı Deposu ile ilgilidir.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [şablon Excel dosyasından](50528367.xlsm) boş bir çalışma kitabına VBA projesini kopyalar ve onu [çıktı Excel dosyası](50528366.xlsm) olarak kaydeder. Şablon Excel dosyasındaki VBA projesini açarsanız aşağıda gösterilen gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Deposu içerir, bu nedenle [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) ve [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-) yöntemleri kullanılarak kopyalanacaktır.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Aşağıdaki ekran görüntüsü, sonuç Excel dosyasını ve şablon Excel dosyasından kopyalanan içeriği göstermekte. Button 1'e tıkladığınızda, VBA Kullanıcı Formu'nun açıldığını ve kendisi üzerinde bir komut düğmesinin tıklanması durumunda bir ileti kutusunun gösterildiğini göreceksiniz.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
