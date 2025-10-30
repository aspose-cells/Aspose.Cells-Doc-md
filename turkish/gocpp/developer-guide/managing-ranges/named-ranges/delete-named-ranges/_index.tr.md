---
title: Golang ile C++ kullanarak Adlandırılmış Aralıkları Sil
linktitle: Adlandırılmış Aralıkları Sil
type: docs
weight: 90
url: /tr/go-cpp/delete-named-ranges/
description: Farklı isim veya adlandırılmış aralıkları Excel veya OpenOffice dosyalarından kaldırmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

## **Giriş**
Eğer Excel dosyalarında çok fazla tanımlanmış isim veya adlandırılmış aralık varsa, tekrar atıfta bulunulmadığından bazılarını temizlememiz gerekebilir.

## **MS Excel'de Adlandırılmış Aralığı Kaldır**

Excel'den adlandırılmış bir aralığı kaldırmak için şu adımları izleyebilirsiniz:
1. Microsoft Excel'i açın ve adlandırılmış aralığı içeren çalışma kitabını açın.
2. Excel kurdelesindeki "Formüller" sekmesine gidin.
3. "Tanımlı İsimler" grubundaki "Ad Yöneticisi" düğmesini tıklayın. Bu, Ad Yöneticisi iletişim kutusunu açacaktır.
4. Ad Yöneticisi iletişim kutusunda, kaldırmak istediğiniz adlandırılmış aralığı seçin.
5. "Sil" düğmesine tıklayın. İstenildiğinde silme işlemini onaylayın.
6. Ad Yöneticisi iletişim kutusunu kapatmak için "Kapat" düğmesine tıklayın.
7. Değişiklikleri korumak için çalışma kitabını kaydedin.

## **Aspose.Cells for C++ kullanarak Adlandırılmış Aralıkları Silme**
 Aspose.Cells for C++ ile liste içindeki isimlendirilmiş aralıkları veya tanımlı isimleri [metin](https://reference.aspose.com/cells/go-cpp/namecollection/remove_stringarray/) veya [indeks](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) kullanarak kaldırabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges.go" >}}
Not: Eğer tanımlanmış isim formüller tarafından referans gösteriliyorsa, kaldırılamaz. Sadece tanımlanmış ismin formülü kaldırabiliriz.

## **Bazı Adlandırılmış Aralıkları Kaldırma**
Bir tanımlı ismi kaldırdığımızda, dosyadaki tüm formüller tarafından kullanılıp kullanılmadığını kontrol etmeliyiz.
Adlandırılmış aralıkların kaldırılmasının performansını artırmak için bazılarını birlikte kaldırabiliriz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-1.go" >}}
## **Yinelenen Tanımlı İsimleri Kaldırma**
Bazı Excel dosyaları, aynı isimli tanımlanmış isimler nedeniyle bozulur. Bu yüzden bu yinelenen isimleri kaldırıp dosyayı onarabiliriz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteNamedRanges-2.go" >}}
