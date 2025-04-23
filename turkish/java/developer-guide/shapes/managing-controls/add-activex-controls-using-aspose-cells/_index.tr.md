---
title: Aspose.Cells Kullanarak AktifX Kontrolleri Ekleme
type: docs
weight: 720
url: /tr/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells kullanarak ActiveX denetimleri ekleyebilirsiniz [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-) yöntemiyle. Bu yöntem, hangi tür ActiveX denetiminin eklenmesi gerektiğini belirten [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) parametresi alır. Aşağıdaki değerler vardır.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [DÖNDÜRME_DÜĞMESİ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [METİN_KUTUSU](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [ANAHTAR_DÜĞMESİ](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [BİLİNMEYEN](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

AktifX kontrolünü şekil koleksiyonuna ekledikten sonra, [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) özelliği üzerinden AktifX kontrol nesnesine erişebilir ve çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}} 
## **Aspose.Cells kullanarak Anahtar Düğmesi AktifX Kontrolü ekleme**
Aşağıdaki örnek kod, Aspose.Cells kullanarak Anahtar Düğmesi AktifX Kontrolü ekler. Bu kod ile oluşturulan [çıktı excel dosyasını](5473427.xlsx) referansınız için indirebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
