---
title: Aspose.Cells for SharePointライセンスのインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}}

[評価](/cells/ja/sharepoint/evaluate-aspose-cells/)を完了してから、[ライセンスを購入](https://purchase.aspose.com/buy)してください。

購入前に、ライセンスサブスクリプション契約条件を理解し同意していることを確認してください。

{{% /alert %}}

注文が支払われた時点でライセンスがメールで送られます。ライセンスは通常のSharePointソリューションパッケージを含むZIPアーカイブです。

ライセンスZIPには次が含まれています：

- **Aspose.Cells.SharePoint.License.wsp** – SharePointソリューションパッケージファイル。Aspose.Cells for SharePointライセンスは、サーバーファーム全体に展開およびリトラクションするためにSharePointソリューションとしてパッケージ化されています。
- **readme.txt** – ライセンスのインストール手順。ライセンスのインストールはサーバーコンソールから**stsadm.exe**経由で行われます。ライセンスのインストールに必要な手順は以下に示されています。

#### **ライセンスのインストール**

{{% alert color="primary" %}}

理解しやすくするために、パスは省略されています。以下の手順を実行する際には、**stsadm.exe**やソリューションファイルの実際のパスを追加してください。

{{% /alert %}}

1. stsadmを実行して、SharePointソリューションストアにソリューションを追加します：
   stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. ソリューションをファーム内のすべてのサーバーに展開します：
   stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. 展開をすぐに完了するために、管理タイマージョブを実行します：
   stsadm.exe -o execadmsvcjobs

{{% alert color="primary" %}}

サーバーファームでWindows SharePoint Services Administrationサービスが起動していない場合、展開ステップを実行する際に警告が表示されます。**Stsadm.exe**はこのサービスとWindows SharePoint Timer Serviceに依存しており、これらのサービスがサーバーファームで実行されていない場合は、ライセンスを各サーバーに別々に展開する必要があります。

{{% /alert %}}
