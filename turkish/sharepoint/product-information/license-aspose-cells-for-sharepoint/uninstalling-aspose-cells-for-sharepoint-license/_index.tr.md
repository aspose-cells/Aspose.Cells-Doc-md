---
title: Aspose.Cells for SharePoint Lisansını Kaldırma
type: docs
weight: 30
url: /tr/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Aspose.Cells for SharePoint lisansını kaldırmak için lütfen sunucu konsolundan aşağıdaki adımları uygulayınız.

{{% /alert %}} 

1. Lisans çözümünü gruptan geri çekin:
 stsadm.exe -o retractsolution -adı Aspose.Cells.SharePoint.License.wsp -hemen
1. Geri çekmeyi hemen tamamlamak için idari zamanlayıcı işlerini yürütün:
 stsadm.exe -o execadmsvcjobs
1. Geri çekme işleminin tamamlanmasını bekleyin.
 Geri çekme işleminin tamamlanıp tamamlanmadığını kontrol etmek için Merkezi Yönetim'i şu adrese giderek kontrol edebilirsiniz:**Merkezi Yönetim** , sonra**Operasyonlar** ve**Çözüm Yönetimi**.
1. Çözümü SharePoint çözüm deposundan kaldırın:
 stsadm.exe -o deletesolution -adı Aspose.Cells.SharePoint.License.wsp
