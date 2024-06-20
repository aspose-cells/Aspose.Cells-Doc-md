---
title: Aspose.Cells for SharePoint Lisansının Yüklenmesi
type: docs
weight: 10
url: /tr/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

[Değerlendirme](/cells/tr/sharepoint/evaluate-aspose-cells/)den memnun kalırsanız, [bir lisans satın alın](https://satinalma.aspose.com/satin-al).

Satın almadan önce, lisans abonelik koşullarını anladığınızdan ve kabul ettiğinizden emin olun.

{{% /alert %}}

Lisans ödeme yapıldığında size e-posta ile gönderilir. Lisans, düzenli bir SharePoint çözüm paketi içeren bir ZIP arşividir.

Lisans ZIP şunları içerir:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint çözüm paketi dosyası. Aspose.Cells for SharePoint lisansı, sunucu çifti üzerinde dağıtım ve geri alma işlemlerini kolaylaştırmak üzere bir SharePoint çözümü olarak paketlenmiştir.
- **readme.txt** – Lisans kurulum talimatları. Lisans kurulumu **stsadm.exe** aracılığıyla sunucu konsolundan gerçekleştirilir. Lisansı kurmak için gereken adımlar aşağıda verilmiştir.

#### **Lisansın Yüklenmesi**

{{% alert color="primary" %}}

Netlik için yollar atlanmıştır. Aşağıdaki adımları uygularken, **stsadm.exe** ve/veya çözüm dosyasının gerçek yolunu ekleyin.

{{% /alert %}}

1. SharePoint çözüm deposuna çözümü eklemek için stsadm'yi çalıştırın:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Çözümü çiftteki tüm sunuculara dağıtın:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Dağıtımı hemen tamamlamak için yönetici zamanlayıcı görevlerini çalıştırın:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

Çiftinizde Windows SharePoint Services Yönetimi hizmetinin başlatılmadığına dair bir uyarı alırsınız. **Stsadm.exe**, bu hizmete ve sunucu çiftinde çözüm verilerini replike etmek için Windows SharePoint Zamanlayıcı Hizmetine güvenir. Bu hizmetler sunucu çiftinizde çalışmıyorsa, lisansı çiftinizde ayrı ayrı dağıtmanız gerekebilir.

{{% /alert %}}
