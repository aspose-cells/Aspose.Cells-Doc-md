---
title: Sayfa ayarı
type: docs
weight: 80
url: /tr/reportingservices/page-setup/
---
Yapılandırma, iki bölüm ve 8 tür Sayfa Yapısı özelliği içerir. Bu özellikler arasında name, index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin ve RightMargin bulunur.

- **isim** rapor adını temsil eder, ad boş bırakıldığında tüm raporu temsil eder.
- **dizin** dışa aktarılan Excel dosyasının çalışma sayfası dizinini temsil eder.
- **Sayfalara SığdırUzun** yazdırıldığında çalışma sayfasının ölçekleneceği uzun sayfa sayısını temsil eder.
- **Sayfalara SığdırGeniş** çalışma sayfasının yazdırıldığında ölçekleneceği genişlikteki sayfa sayısını temsil eder.
- **Altbilgi Kenar Boşluğu**sayfanın altından altbilgiye olan mesafeyi santimetre biriminde temsil eder.
- **Başlık Marjı** sayfanın üstünden başlığa olan mesafeyi santimetre biriminde temsil eder.
- **sol kenar boşluğu** sol kenar boşluğunun boyutunu santimetre biriminde temsil eder.
- **sağ kenar boşluğu** sağ kenar boşluğunun boyutunu santimetre biriminde temsil eder.
- **Üst boşluk** üst kenar boşluğunun boyutunu santimetre biriminde temsil eder.
- **Alt Marj** alt kenar boşluğunun boyutunu santimetre biriminde temsil eder.

Sayfa Kurulumu Yapılandırma Örneği:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
