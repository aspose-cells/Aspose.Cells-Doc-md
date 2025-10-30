---
title: Golang ile C++ kullanarak Yerleşik Stilleri Kullanma
linktitle: Dahili Stiller Kullanma
type: docs
weight: 80
url: /tr/go-cpp/using-built-in-styles/
description: C++ kodu ile Excel in yerleşik stillerini Aspose.Cells for C++ API kullanarak kullanma
keywords: c++ ile Excel yerleşik stillerini kullanma, C++ ile çalışma kitabında programlı stil uygulama, programlı stil uygulama, c++ ile Excel de yerleşik stilleri uygulama, c++ ile çalışma kitabında yerleşik stilleri uygulama, c++ kodu ile çalışma kitabına yerleşik stil uygulama, c++ kodu ile Excel çalışma kitabına yerleşik stil uygulama
---

{{% alert color="primary" %}}

Aspose.Cells, bir elektronik tablo belgesinde bir hücreyi biçimlendirmek için tekrar kullanılabilir stillerin geniş bir koleksiyonunu sağlar. Kitabımızda dahili stilleri kullanabilir ve ayrıca özel stiller oluşturabiliriz.

{{% /alert %}}

## **Dahili Stilleri Nasıl Kullanılır**

[**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/go-cpp/workbook/createbuiltinstyle/) yöntemi ve [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) numaralı numaralaması yerleşik stilleri kullanmayı kolaylaştırır. İşte tüm olası yerleşik stiller listesi:

- YİRMİ_YÜZDE_GENEL_1
- YİRMİ_YÜZDE_GENEL_2
- YİRMİ_YÜZDE_GENEL_3
- YİRMİ_YÜZDE_GENEL_4
- YİRMİ_YÜZDE_GENEL_5
- YİRMİ_YÜZDE_GENEL_6
- KIRK_YÜZDE_GENEL_1
- KIRK_YÜZDE_GENEL_2
- KIRK_YÜZDE_GENEL_3
- KIRK_YÜZDE_GENEL_4
- KIRK_YÜZDE_GENEL_5
- KIRK_YÜZDE_GENEL_6
- ALTMIS_YÜZDE_GENEL_1
- ALTMIS_YÜZDE_GENEL_2
- ALTMIS_YÜZDE_GENEL_3
- ALTMIS_YÜZDE_GENEL_4
- ALTMIS_YÜZDE_GENEL_5
- ALTMIS_YÜZDE_GENEL_6
- VURGU_1
- VURGU_2
- VURGU_3
- VURGU_4
- VURGU_5
- VURGU_6
- KÖTÜ
- HESAPLAMA
- HÜCRE_KONTROLÜ
- VİRGÜL
- VIRGÜL_1
- PARA_BİRİMİ
- PARA_BİRİMİ_1
- AÇIKLAYICI_METİN
- İYİ
- BAŞLIK_1
- BAŞLIK_2
- BAŞLIK_3
- BAŞLIK_4
- HYPERLINK
- TAKİP_EDİLEN_HİPERBAĞLANTI
- GİRİŞ
- BAĞLI_HÜCRE
- TARAFSIZ
- NORMAL
- NOT
- ÇIKIŞ
- YÜZDE
- BAŞLIK
- TOPLAM
- UYARI_METNİ
- SATIR_SEVİYESİ
- SÜTUN_SEVİYESİ

## C++ ile yerleşik stilleri kullanmak için kod

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingBuiltInStyles.go" >}}
