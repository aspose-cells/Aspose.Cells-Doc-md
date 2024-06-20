---
title: Установка Aspose.Cells for SharePoint лицензии
type: docs
weight: 10
url: /ru/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

Как только вы будете довольны своим [оценкой](/cells/ru/sharepoint/evaluate-aspose-cells/), [купите лицензию](https://purchase.aspose.com/buy).

Перед покупкой убедитесь, что вы понимаете и соглашаетесь с условиями лицензионной подписки.

{{% /alert %}}

Лицензия будет отправлена вам после оплаты заказа. Лицензия представляет собой ZIP-архив, содержащий обычный пакет решений SharePoint.

ZIP-архив лицензии содержит:

- **Aspose.Cells.SharePoint.License.wsp** – файл пакета решений SharePoint. Лицензия Aspose.Cells for SharePoint упакована в качестве пакета решений SharePoint для облегчения развертывания и отзыва по всей ферме серверов.
- **readme.txt** – Инструкции по установке лицензии. Установка лицензии выполняется с серверной консоли с помощью **stsadm.exe**. Ниже приведены необходимые шаги для установки лицензии.

#### **Установка лицензии**

{{% alert color="primary" %}}

Для ясности пути опущены. Добавьте фактический путь к **stsadm.exe** и/или файлу решения при выполнении указанных ниже шагов.

{{% /alert %}}

1. Запустите stsadm, чтобы добавить решение в хранилище решений SharePoint:
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Разверните решение на всех серверах фермы:
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Запустите административные таймер-задания для немедленного завершения развертывания:
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

При выполнении шага развертывания вы получите предупреждение, если служба администрирования Windows SharePoint Services не была запущена. **Stsadm.exe** зависит от этой службы и службы таймера Windows SharePoint для репликации данных решения по всей ферме. Если эти службы не запущены на вашей серверной ферме, вам может потребоваться отдельно развернуть лицензию на каждом сервере.

{{% /alert %}}
