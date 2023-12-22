---
title: Kullanıcıların Excel Dosyasını Yazdırması Nasıl Engellenir
type: docs
weight: 600
url: /tr/net/how-to-prevent-printing-excel/
description: Aspose.Cells for .NET API numaralı telefondan kullanıcıların Excel yazdırmasını nasıl önleyeceğinizi öğrenin.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **Olası Kullanım Senaryoları**
Günlük işlerimizde excel dosyasında bazı önemli bilgiler bulunabilir, şirket içi dışarıya yayılan verileri korumak amacıyla bunların çıktısını almamıza izin vermeyecektir. Bu belgede başkalarının Excel dosyalarını yazdırmasını nasıl önleyeceğiniz anlatılacaktır.

##  **Kullanıcıların MS-Excel'de Dosya Yazdırması Nasıl Engellenir**
Yazdırılacak belirli dosyanızı korumak için aşağıdaki VBA kodunu uygulayabilirsiniz.
1. Başkalarının yazdırmasına izin vermediğiniz çalışma kitabınızı açın.
1. Excel şeridinde "Geliştirici" sekmesini seçin ve "Kontroller" bölümündeki "Kodu Görüntüle" düğmesine tıklayın. Alternatif olarak, Microsoft Visual Basic for Applications penceresini açmak için ALT + F11 tuşlarını basılı tutabilirsiniz.
<br>
<img src="1.png" width=70% />
1. Daha sonra soldaki Proje Gezgini'nde ThisWorkbook'a çift tıklayarak modülü açın ve bazı vba kodları ekleyin.
<br>
<img src="2.png" width=70% />
1. Daha sonra bu kodu kaydedip kapatın ve çalışma kitabına geri dönün; şimdi örnek dosyayı yazdırdığınızda bunların yazdırılmasına izin verilmeyecek ve aşağıdaki uyarı kutusunu alacaksınız:
<br>
<img src="3.png" width=70% />

##  **Kullanıcıların Aspose.Cells for .NET'i Kullanarak Excel Dosyasını Yazdırması Nasıl Engellenir?**

Aşağıdaki örnek kod, kullanıcıların excel dosyasını yazdırmasının nasıl önleneceğini gösterir:

1.  Yükle[örnek dosya](sample.xlsx).
1. Workbook'un VbaProject özelliğinden VbaModuleCollection nesnesini alın.
1. "ThisWorkbook" adı aracılığıyla VbaModule nesnesini alın.
1. VbaModule'un codes özelliğini ayarlayın.
1.  Örnek dosyayı şuraya kaydedin:[xlsm biçimi](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}