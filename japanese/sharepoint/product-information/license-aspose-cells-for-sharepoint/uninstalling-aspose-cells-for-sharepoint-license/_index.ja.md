---
title: Aspose.Cells for SharePoint ライセンスのアンインストール
type: docs
weight: 30
url: /ja/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}} 

Aspose.Cells for SharePoint ライセンスをアンインストールするには、サーバー コンソールから次の手順を実行してください。

{{% /alert %}} 

1. ライセンス ソリューションをファームから撤回します。
 stsadm.exe -o 撤回ソリューション -name Aspose.Cells.SharePoint.License.wsp -immediate
1. 管理タイマー ジョブを実行して、撤回をすぐに完了します。
 stsadm.exe -o execadmsvcjobs
1. 撤回が完了するまで待ちます。
サーバーの全体管理を使用して、撤回が完了したかどうかを確認できます。**集中管理**、 それから**操作**と**ソリューション管理**.
1. SharePoint ソリューション ストアからソリューションを削除します。
 stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
