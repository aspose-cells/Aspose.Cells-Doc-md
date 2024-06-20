---
title: Удаление лицензии Aspose.Cells for SharePoint
type: docs
weight: 30
url: /ru/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Чтобы удалить лицензию Aspose.Cells for SharePoint, воспользуйтесь следующими шагами с консоли сервера. 

{{% /alert %}} 

1. Отозвать лицензионное решение из фермы:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Запустите административные таймер-задания для немедленного завершения отзыва:
   stsadm.exe -o execadmsvcjobs
1. Дождитесь завершения отзыва.
   Если вы хотите проверить, завершился ли отзыв с помощью Центральной администрации, перейдите в **Центральная администрация**, затем **Операции** и **Управление решениями**.
1. Удалите решение из хранилища решений SharePoint:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
