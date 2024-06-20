---
title: Çalışma sayfası içindeki Şekil Önüne veya Arkasına Gönderme
type: docs
weight: 600
url: /tr/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Olası Kullanım Senaryoları**

Aynı konumda birden fazla şekil bulunduğunda, görünür olmaları şeklin Z-sıra konumlarına göre belirlenir. Aspose.Cells, şeklin Z-sıra konumunu değiştiren [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) metodunu sağlar. Şekli arka plana göndermek istiyorsanız, -1, -2, -3 vb. gibi negatif sayılar kullanacak ve şekli öne göndermek istiyorsanız, 1, 2, 3 vb. gibi pozitif sayılar kullanacaksınız.

## **Çalışma Sayfası İçinde Şekil Önüne veya Arkasına Gönderme**

Aşağıdaki örnek kod, [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack(int)) yönteminin kullanımını açıklar. Lütfen kod içinde kullanılan [örnek Excel dosyasını](50528362.xlsx) ve bunun tarafından oluşturulan [çıktı Excel dosyasını](50528361.xlsx) görün. Ekran görüntüsü, kodun örneğine olan etkiyi göstermektedir.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Örnek Kod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
