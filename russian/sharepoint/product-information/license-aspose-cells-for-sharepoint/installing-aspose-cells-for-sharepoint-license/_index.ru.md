---
title: Установка лицензии Aspose.Cells for SharePoint
type: docs
weight: 10
url: /ru/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

 Как только вы будете довольны своим[оценка](/cells/ru/sharepoint/evaluate-aspose-cells/), [купить лицензию](https://purchase.aspose.com/buy).

Перед покупкой убедитесь, что вы понимаете и согласны с условиями подписки на лицензию.

{{% /alert %}}

Лицензия высылается вам по электронной почте после оплаты заказа. Лицензия представляет собой ZIP-архив, содержащий обычный пакет решения SharePoint.

Лицензионный ZIP содержит:

- **Aspose.Cells.SharePoint.License.wsp** – Файл пакета решения SharePoint. Лицензия Aspose.Cells for SharePoint упакована как решение SharePoint для облегчения развертывания и отзыва на ферме серверов.
- **readme.txt** Инструкция по установке лицензии. Установка лицензии производится с консоли сервера через**stsadm.exe**. Шаги, необходимые для установки лицензии, приведены ниже.

#### **Установка лицензии**

{{% alert color="primary" %}}

 Пути опущены для ясности. Добавьте фактический путь к**stsadm.exe** и/или файл решения при выполнении следующих шагов.

{{% /alert %}}

1. Запустите stsadm, чтобы добавить решение в хранилище решений SharePoint:
 stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Разверните решение на всех серверах в ферме:
 stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Выполните административные задания таймера, чтобы немедленно завершить развертывание:
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Вы получите предупреждение при выполнении шага развертывания, если служба администрирования Windows SharePoint Services не запущена.**Stsadm.exe**использует эту службу и службу таймера SharePoint Windows для репликации данных решения по всей ферме. Если эти службы не работают на вашей ферме серверов, вам может потребоваться развернуть лицензию отдельно на каждом сервере.

{{% /alert %}}
