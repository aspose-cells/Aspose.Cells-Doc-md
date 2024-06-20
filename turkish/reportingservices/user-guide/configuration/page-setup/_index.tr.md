---
title: Sayfa Ayarı
type: docs
weight: 80
url: /tr/reportingservices/page-setup/
---

Yapılandırma iki bölümü ve 8 çeşit Sayfa Ayarı özelliğini içerir. Bu özellikler arasında ad, index, FitToPagesTall, FitToPagesWide, ÜstKenarBoşluğu, AltbilgiKenarBoşluğu, BaşlıkKenarBoşluğu, AltKenarBoşluğu, SolKenarBoşluğu ve SağKenarBoşluğu bulunmaktadır.

- **ad** rapor adını temsil eder, ad boş olduğunda tüm raporu temsil eder.
- **index** dışa aktarılan Excel dosyasının çalışsayfa index'ini temsil eder.
- **FitToPagesTall** çalışsayfanın basıldığında ölçekleneceği dikey sayfa sayısını temsil eder.
- **FitToPagesWide** çalışsayfanın basıldığında ölçekleneceği yatay sayfa sayısını temsil eder.
- **FooterMargin**, ayırma ölçüsünü temsil eder, birim santimetre olarak.
- **HeaderMargin**, sayfanın üstünden başlığa olan uzaklığı, birim santimetre olarak temsil eder.
- **LeftMargin**, sol kenar boşluğunun boyutunu, birim santimetre olarak temsil eder.
- **RightMargin**, sağ kenar boşluğunun boyutunu, birim santimetre olarak temsil eder.
- **TopMargin**, üst kenar boşluğunun boyutunu, birim santimetre olarak temsil eder.
- **BottomMargin**, alt kenar boşluğunun boyutunu, birim santimetre olarak temsil eder.

PageSetup Yapılandırma Örneği:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
