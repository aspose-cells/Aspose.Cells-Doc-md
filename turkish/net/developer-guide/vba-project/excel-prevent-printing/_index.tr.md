---
title: Excel Dosyasının Yazdırılmasını Nasıl Engelleriz
type: docs
weight: 600
url: /tr/net/how-to-prevent-printing-excel/
description: Aspose.Cells for .NET API si aracılığıyla excel dosyasının yazdırılmasını nasıl engelleyeceğinizi öğrenin.
keywords: excel yazdırma, excel yazdırmayı engelleme, kullanıcıların excel i yazdırmaması nasıl engellenir, excel yazdırma engelleme, çalışma kitabının yazdırılmasını engelleme, Kullanıcıların VBA ile tam çalışma kitabını yazdırmalarını engelleyin. 
---

## **Olası Kullanım Senaryoları**
Günlük çalışmamızda, excel dosyasında önemli bilgiler olabilir, iç verilerin yayılmasını korumak için şirket bize bunları yazdırmamamızı istemeyebilir. Bu belge size diğerlerinin Excel dosyalarını yazdırmalarını nasıl engelleyeceğinizi gösterecektir.

## **MS-Excel'de Kullanıcıların Dosyayı Yazdırmasını Nasıl Engelleriz**
Belirli dosyanızın yazdırılmasını korumak için aşağıdaki VBA kodunu uygulayabilirsiniz.
1. Başkalarına yazdırmalarına izin vermediğiniz çalışma kitabınızı açın.
1. Excel menüsünde 'Geliştirici' sekmesini seçin ve 'Kontroller' bölümünde 'Kod Görüntüle' düğmesine tıklayın. Alternatif olarak, Microsoft Visual Basic for Applications penceresini açmak için ALT + F11 tuşlarına basılı tutabilirsiniz.
<br>
<img src="1.png" width=70% />
1. Ardından sol tarafta bulunan Proje Gezgini'nde ThisWorkbook'a çift tıklayarak modülü açın ve bazı vba kodları ekleyin.
<br>
<img src="2.png" width=70% />
1. Sonra bu kodu kaydedin ve kapatın, çalışma kitabına geri dönün ve şimdi örnek dosyayı yazdırdığınızda yazdırılmasına izin verilmeyecektir ve aşağıdaki uyarı kutusunu alacaksınız:
<br>
<img src="3.png" width=70% />

## **Aspose.Cells for .NET kullanarak Excel Dosyasının Yazdırılmasını Nasıl Engelleriz**

Aşağıdaki örnek kod, kullanıcıların excel dosyasını yazdırmalarını engellemek için nasıl kullanılacağını göstermektedir:

1. [Örnek dosyayı](örnek.xlsx) yükleyin.
1. Workbook'ün VbaProject özelliği üzerinden VbaModuleCollection nesnesini alın.
1. Workbok'un VbaProject özelliği üzerinden "ThisWorkbook" adıyla VbaModule nesnesini alın.
1. VbaModule'nin kodları özelliğini ayarlayın.
1. Örnek dosyayı [xlsm biçimine](out.xlsm) kaydedin.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
