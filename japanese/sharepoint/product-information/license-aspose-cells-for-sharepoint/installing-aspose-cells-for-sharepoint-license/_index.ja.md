---
title: Aspose.Cells for SharePoint ライセンスのインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-cells-for-sharepoint-license/
---
{{% alert color="primary" %}}

あなたがあなたに満足したら[評価](/cells/ja/sharepoint/evaluate-aspose-cells/), [ライセンスを購入する](https://purchase.aspose.com/buy).

購入する前に、ライセンス サブスクリプションの条件を理解し、同意していることを確認してください。

{{% /alert %}}

注文の支払いが完了すると、ライセンスが電子メールで送信されます。ライセンスは、通常の SharePoint ソリューション パッケージを含む ZIP アーカイブです。

ライセンス ZIP には次が含まれます。

- **Aspose.Cells.SharePoint.License.wsp** – SharePoint ソリューション パッケージ ファイル。 Aspose.Cells for SharePoint ライセンスは、SharePoint ソリューションとしてパッケージ化されており、サーバー ファーム全体での展開と撤回を容易にします。
- **readme.txt**– ライセンスのインストール手順。ライセンスのインストールは、サーバー コンソールから**stsadm.exe**.ライセンスのインストールに必要な手順を以下に示します。

#### **ライセンスのインストール**

{{% alert color="primary" %}}

わかりやすくするために、パスは省略されています。実際のパスを追加します**stsadm.exe**および/または以下の手順を実行する際のソリューション ファイル。

{{% /alert %}}

1. stsadm を実行して、ソリューションを SharePoint ソリューション ストアに追加します。
 stsadm.exe -o addsolution -ファイル名 Aspose.Cells.SharePoint.License.wsp
1. ファーム内のすべてのサーバーにソリューションを展開します。
 stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. 管理タイマー ジョブを実行して、展開をすぐに完了します。
 stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

 Windows SharePoint サービス管理サービスが開始されていない場合、展開手順を実行すると警告が表示されます。**Stsadm.exe**は、このサービスと Windows SharePoint Timer Service に依存して、ファーム全体にソリューション データをレプリケートします。これらのサービスがサーバー ファームで実行されていない場合は、ライセンスを各サーバーに個別に展開する必要がある場合があります。

{{% /alert %}}
