---
title: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
linktitle: Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma
description: Node.js de C++ kullanarak hücre hizalamasını değiştirmek ve mevcut biçimlendirmeyi korumak için Aspose.Cells kütüphanesini kullanın
keywords: Aspose.Cells, Node.js via C++, hücre hizalaması, mevcut biçimlendirmeyi koru
type: docs
weight: 340
url: /tr/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/
---

## **Olası Kullanım Senaryoları**

Bazen, çoklu hücrelerin hizalamasını değiştirmek istersiniz ancak mevcut biçimlendirmeyi de korumak istersiniz. Aspose.Cells for Node.js via C++, bunu [**StyleFlag.setAlignments(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/#setAlignments-boolean-) metodunu kullanarak yapmanıza olanak tanır. Eğer **true** olarak ayarlarsanız, hizalamadaki değişiklikler gerçekleşir aksi takdirde gerçekleşmez. Lütfen not edin, [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesi, biçimlendirmeyi bir hücre aralığına uygulayan [**Range.applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/range/#applyStyle-style-styleflag-) metoduna parametre olarak geçirilir.

## **Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma**

Aşağıdaki örnek kod, [örnek Excel dosyasını](67338585.xlsx) yükler, aralık oluşturur ve yatay ve dikey olarak ortalayıp mevcut biçimlendirmeyi korur. Aşağıdaki ekran görüntüsü, örnek Excel dosyasını ve [çıktı Excel dosyasını](67338586.xlsx) karşılaştırır ve hücrelerin mevcut biçimlendirmesinin aynı olduğunu ancak hücrelerin şimdi yatay ve dikey olarak merkezlenmiş olduğunu gösterir.

![todo:image_alt_text](change-cells-alignment-and-keep-existing-formatting_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ChangeCellsAlignment.js" >}}
