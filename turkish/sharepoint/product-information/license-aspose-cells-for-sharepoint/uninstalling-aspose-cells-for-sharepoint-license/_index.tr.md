---
title: Aspose.Cells for SharePoint Lisansının Kaldırılması
type: docs
weight: 30
url: /tr/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePoint lisansını kaldırmak için lütfen aşağıdaki adımları sunucu konsolundan uygulayın. 

{{% /alert %}} 

1. Lisans çözümünü çiftten geri alın:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Geri alma işlemini hemen tamamlamak için yönetici zamanlayıcı görevlerini çalıştırın:
   stsadm.exe -o execadmsvcjobs
1. Geri alma işleminin tamamlanmasını bekleyin:
   Geri çekmenin tamamlandığını kontrol etmek için **Merkezi Yönetim**, ardından **İşlemler** ve **Çözüm Yönetimi**'ne giderek Merkezi Yönetim'i kullanabilirsiniz.
1. Çözümü SharePoint çözüm deposundan kaldırın:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
