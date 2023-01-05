---
title: Aspose.Cells for SharePoint Lisans Kurulumu
type: docs
weight: 10
url: /tr/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 kendinle mutlu olduktan sonra[değerlendirme](/cells/tr/sharepoint/evaluate-aspose-cells/), [lisans satın al](https://purchase.aspose.com/buy).

Satın almadan önce lisans abonelik koşullarını anladığınızdan ve kabul ettiğinizden emin olun.

{{% /alert %}}

Siparişin ödemesi yapıldığında lisans size e-posta ile gönderilir. Lisans, normal bir SharePoint çözüm paketini içeren bir ZIP arşividir.

ZIP lisansı şunları içerir:

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint çözüm paketi dosyası. Aspose.Cells for SharePoint lisansı, sunucu grubu genelinde dağıtımı ve geri çekmeyi kolaylaştırmak için bir SharePoint çözümü olarak paketlenmiştir.
- **beni oku.txt**– Lisans kurulum talimatları. Lisans kurulumu, sunucu konsolu üzerinden gerçekleştirilir.**stsadm.exe**. Lisans kurulumu için gerekli adımlar aşağıda verilmiştir.

#### **Lisansı Yükleme**

{{% alert color="primary" %}}

 Anlaşılır olması için yollar çıkarılmıştır. Gerçek yolu şuraya ekle:**stsadm.exe** ve/veya aşağıdaki adımları yürütürken çözüm dosyası.

{{% /alert %}}

1. Çözümü SharePoint çözüm deposuna eklemek için stsadm'yi çalıştırın:
 stsadm.exe -o addsolution -dosya adı Aspose.Cells.SharePoint.License.wsp
1. Çözümü gruptaki tüm sunuculara dağıtın:
 stsadm.exe -o dağıtma çözümü -adı Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Dağıtımı hemen tamamlamak için idari zamanlayıcı işlerini yürütün:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Windows SharePoint Services Yönetim hizmeti başlatılmamışsa, dağıtım adımını çalıştırırken bir uyarı alırsınız.**stsadm.exe**çözüm verilerini grup genelinde çoğaltmak için bu hizmete ve Windows SharePoint Zamanlayıcı Hizmeti'ne güvenir. Bu hizmetler sunucu grubunuzda çalışmıyorsa, lisansı her sunucuya ayrı ayrı dağıtmanız gerekebilir.

{{% /alert %}}
