---
title: Aspose.Cells for SharePointライセンスのアンインストール
type: docs
weight: 30
url: /ja/sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

Aspose.Cells for SharePointライセンスをアンインストールするには、以下の手順をサーバーコンソールから使用してください。 

{{% /alert %}} 

1. ファームからライセンスソリューションをリトラクトします：
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. リトラクションをすぐに完了するために、管理タイマージョブを実行します：
   stsadm.exe -o execadmsvcjobs
1. リトラクションの完了を待ちます。
   **Central Administration**に移動して、**Operations**、**Solution Management**を選択し、リトラクションが完了したかを確認できます。
1. SharePointソリューションストアからソリューションを削除します：
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp
