---
title: Удаление Aspose.Cells для лицензии SharePoint
type: docs
weight: 30
url: /ru/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

 Чтобы удалить лицензию Aspose.Cells для SharePoint, выполните следующие действия с консоли сервера.

{{% /alert %}} 

1. Отзовите лицензионное решение из фермы:
stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Выполните административные задания таймера, чтобы немедленно завершить отзыв:
 stsadm.exe -o execadmsvcjobs
1. Дождитесь завершения отвода.
 Вы можете использовать центр администрирования, чтобы проверить, завершен ли отзыв, перейдя к**Центральное управление** , тогда**Операции** а также**Управление решениями**.
1. Удалите решение из хранилища решений SharePoint:
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
